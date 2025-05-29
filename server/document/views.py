from django.shortcuts import render
from django.db import transaction
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Document, DocumentChunk
from .serializers import DocumentSerializer, DocumentChunkSerializer
from .utils.text_extractor import TextExtractor
from .utils.text_splitter import get_text_splitter
from .utils.vector_operations import add_documents, remove_documents, get_similar_docs, delete_collection
from .utils.vector_store import get_embedding_dimension
import traceback


class DocumentViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        try:
            serializer.is_valid(raise_exception=True)
            uploaded_file = self.request.FILES.get('file')
            with transaction.atomic():
                document = serializer.save(user=self.request.user)
                #Create vector collection name based on document ID
                collection_name = str(document.id) 
                #Extract Texts form Uploaded File
                extracted_text = TextExtractor(uploaded_file).extract_text()
                #Chunk Texts
                chunked_texts = get_text_splitter().split_text(extracted_text)
                #Create & Store Embeddings
                embeddings_ids = add_documents(
                    collection_name=collection_name,
                    texts=chunked_texts,
                    metadata={
                        "document_id": str(collection_name), 
                        "user_id": str(self.request.user.id),
                        "document_name": document.name
                    }
                )
                #Get Embedding Dimension
                embedding_dim = get_embedding_dimension()
                #Create Document Chunks Records with these Embeddings IDS, its respective order index and Document ID
                DocumentChunk.objects.bulk_create([
                    DocumentChunk(
                        document=document,
                        content=chunked_texts[index],
                        chunk_index=index,
                        embedding_id=embedding_id,
                        embedding_dim=embedding_dim
                    )
                    for index, embedding_id in enumerate(embeddings_ids)
                ])
        except Exception as e:
            try:
                delete_collection(collection_name)
            except Exception as e:
                print(f"An error occured during deleting collection: {e}")
            # Raise a generic API exception so DRF handles it
            raise ValidationError({
                "error": "An error occurred while processing your document.",
                "details": str(e),
                "trace": traceback.format_exc()
            })