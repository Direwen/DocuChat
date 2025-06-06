<template>
    <NuxtLayout name="authenticated">
        <!-- This is the header passed to layout's #header slot -->
        <template #header>
            <DocumentsHeader />
        </template>

        <!-- Main content passed to layout's default slot -->
        <div class="container mx-auto py-8 px-4 sm:px-6 lg:px-8">
            <div class="card bg-base-100 shadow-lg">
                <div class="card-body p-0">
                    <table class="table w-full">
                        <!-- Table Header -->
                        <thead>
                            <tr class="bg-base-200">
                                <th class="px-6 py-4 text-sm font-semibold text-base-content/80">File Name</th>
                                <th class="px-6 py-4 text-sm font-semibold text-base-content/80">Uploaded Date</th>
                                <th class="px-6 py-4 text-sm font-semibold text-base-content/80 text-right">Actions</th>
                            </tr>
                        </thead>
                        <!-- Table Body -->
                        <tbody>
                            <tr v-for="(document, index) in documents" :key="index"
                                class="border-b border-base-200 hover:bg-base-200/50 transition-colors">
                                <td class="px-6 py-4 text-base-content">{{ document.fileName }}</td>
                                <td class="px-6 py-4 text-base-content/70">{{ document.uploadedDate }}</td>
                                <td class="px-6 py-4 flex justify-end items-center gap-3">
                                    <button class="btn btn-ghost btn-sm rounded-full"
                                        aria-label="Create chat for document" @click="createChat(document)">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none"
                                            viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                                        </svg>
                                    </button>
                                    <div class="dropdown dropdown-end">
                                        <button tabindex="0" class="btn btn-ghost btn-sm rounded-full"
                                            aria-label="Delete document">
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="currentColor"
                                                viewBox="0 0 20 20">
                                                <path
                                                    d="M6 10a2 2 0 11-4 0 2 2 0 014 0zm6 0a2 2 0 11-4 0 2 2 0 014 0zm6 0a2 2 0 11-4 0 2 2 0 014 0z" />
                                            </svg>

                                        </button>
                                        <ul tabindex="0"
                                            class="dropdown-content menu bg-base-100 rounded-box z-10 w-48 p-2 shadow-lg">
                                            <li>
                                                <button class="text-error hover:bg-error hover:text-error-content"
                                                    @click="deleteDocument(document)">
                                                    Delete Document
                                                </button>
                                            </li>
                                        </ul>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </NuxtLayout>
</template>

<script setup>
definePageMeta({ 
  layout: false 
})

// Dummy data for documents
const documents = [
    {
        fileName: "Project_Proposal.pdf",
        uploadedDate: "2025-06-01",
    },
    {
        fileName: "Meeting_Notes.docx",
        uploadedDate: "2025-05-28",
    },
    {
        fileName: "Research_Paper.pdf",
        uploadedDate: "2025-05-20",
    },
]

// Placeholder functions for button actions
const createChat = (document) => {
    console.log(`Creating chat for ${document.fileName}`)
    // Add logic to initiate a chat session for the document
}

const deleteDocument = (document) => {
    console.log(`Deleting ${document.fileName}`)
    // Add logic to delete the document
}
</script>
