<template>
    <div class="p-6">
      <h1 class="text-3xl font-bold mb-4">Details for Item {{ itemId }}</h1>
      <p>This is a mock detail page for item ID: {{ itemId }}</p>
      <NuxtLink to="/" class="text-blue-600 underline mt-4 inline-block">
        ← Back to Home
      </NuxtLink>
    </div>
  </template>
  
  <script setup>
  const route = useRoute()
  const itemId = computed(() => route.params.id)
  </script>