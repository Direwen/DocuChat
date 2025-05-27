<template>
    <div class="min-h-screen flex items-center justify-center bg-gray-50">
      <div class="max-w-md w-full p-6 bg-white rounded shadow">
        <h2 class="text-2xl font-bold mb-4">Login</h2>
        <form @submit.prevent="login">
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700">Email</label>
            <input type="email" v-model="email" class="w-full px-3 py-2 border rounded" required />
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700">Password</label>
            <input type="password" v-model="password" class="w-full px-3 py-2 border rounded" required />
          </div>
          <button type="submit" class="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700">
            Sign In
          </button>
        </form>
        <p class="mt-4 text-center">
          Don't have an account?
          <NuxtLink to="/auth/register" class="text-blue-600 underline">Register</NuxtLink>
        </p>
      </div>
    </div>
  </template>
  
  <script setup>
  const email = ref('')
  const password = ref('')
  
  function login() {
    // Mock login logic
    alert('Logged in as ' + email.value)
  }
  </script>