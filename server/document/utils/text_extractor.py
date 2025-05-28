import pymupdf
from docx import Document
import io

class TextExtractor:
    def __init__(self, file):
        self.file = file
        self.file_type = file.name.split(".")[-1].lower()

    def extract_text(self):
        if self.file_type == 'pdf':
            return self.__extract_text_from_pdf()
        elif self.file_type == 'docx':
            return self.__extract_text_from_docx()
        elif self.file_type == 'txt':
            return self.__extract_text_from_txt()
        else:
            raise ValueError(f"Unsupported file type: {self.file_type}")

    def __extract_text_from_pdf(self):
        # resets the file pointer to the beginning of the file 
        self.file.seek(0)
        reader = pymupdf.open(stream=self.file.read(), filetype="pdf")
        extracted_content = ""
        for page_num in range(len(reader)):
            page = reader.load_page(page_num)
            extracted_content += page.get_text().strip() + "\n"
        return extracted_content

    def __extract_text_from_docx(self):
        # resets the file pointer to the beginning of the file 
        self.file.seek(0)
        file_stream = io.BytesIO(self.file.read())
        doc = Document(file_stream)
        full_text = [para.text for para in doc.paragraphs]
        return '\n'.join(full_text)

    def __extract_text_from_txt(self):
        # resets the file pointer to the beginning of the file 
        self.file.seek(0)
        return self.file.read().decode('utf-8')