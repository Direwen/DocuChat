<template>
  <div class="h-full flex items-center justify-center">
    <div class="max-w-md w-full p-6 rounded shadow">
      <h2 class="text-2xl font-bold mb-4">Register</h2>
      <form @submit.prevent="register">
        <div class="mb-4">
          <label class="block text-sm font-medium mb-1">Username</label>
          <InputsText v-model="username" placeholder="E.g. Alex" />
        </div>
        <div class="mb-4">
          <label class="block text-sm font-medium mb-1">Emai</label>
          <InputsEmail v-model="email" />
        </div>
        <div class="mb-4">
          <label class="block text-sm font-medium mb-1">Password</label>
          <InputsPassword v-model="password" />
        </div>
        <button
          type="submit"
          class="btn btn-block btn-primary"
        >
          Register
        </button>
      </form>
      <p class="mt-4 text-center text-accent flex justify-between items-center">
        <span>Already have an account?</span>
        <NuxtLink to="/auth/login" class="underline underline-offset-3">Login</NuxtLink>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const username = ref('');
const password = ref('');
const email = ref('');

function register() {
  // Mock registration logic
  alert('Registered with username: ' + username.value);
}

definePageMeta({
  layout: 'guest',
});
</script>