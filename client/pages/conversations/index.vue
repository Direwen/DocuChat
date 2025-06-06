<template>
  <NuxtLayout name="authenticated">
    <!-- Conversations Header -->
    <template #header>
      <ConversationsHeader />
    </template>

    <!-- Conversations List -->
    <div class="container mx-auto py-6 px-4 sm:px-6 lg:px-8">
      <div class="space-y-6">
        <!-- Past 7 days -->
        <div>
            <ConversationsDateDisplay />
        
            <ConversationsList />
        </div>

      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>

definePageMeta({ 
  layout: false 
})

// Placeholder functions for button actions
const deleteConversation = (name) => {
  console.log(`Deleting conversation: ${name}`)
  // Add logic to delete the conversation
}
</script>