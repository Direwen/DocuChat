<template>
    <div class="p-6">
      <h1 class="text-3xl font-bold mb-6">Welcome to the Home Page</h1>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <!-- Dummy Cards -->
        <div v-for="item in items" :key="item.id" class="border p-4 rounded shadow">
          <h2 class="text-xl font-semibold">{{ item.title }}</h2>
          <p>{{ item.description }}</p>
          <NuxtLink :to="`/documents/${item.id}`" class="text-blue-600 underline mt-2 inline-block">
            <el-button type="primary">View Document</el-button>
          </NuxtLink>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  const items = [
    { id: 1, title: 'Item One', description: 'This is the first item.' },
    { id: 2, title: 'Item Two', description: 'This is the second item.' },
    { id: 3, title: 'Item Three', description: 'This is the third item.' }
  ]
  </script>