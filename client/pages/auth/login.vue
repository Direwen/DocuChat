<template>
  <div class="h-full flex items-center justify-center">
    <div class="max-w-md w-full p-6 rounded shadow">
      <h2 class="text-2xl font-bold mb-4">Login</h2>
      <form @submit.prevent="login">
        <div class="mb-4">
          <label class="block text-sm font-medium mb-1">Username</label>
          <InputsText v-model="username" placeholder="E.g. Alex" />
        </div>
        <div class="mb-4">
          <label class="block text-sm font-medium mb-1">Password</label>
          <InputsPassword v-model="password" />
        </div>
        <button
          type="submit"
          class="btn btn-block btn-primary"
        >
          Sign In
        </button>
      </form>
      <p class="mt-4 text-center text-accent flex justify-between items-center">
        <span>Don't have an account?</span>
        <NuxtLink to="/auth/register" class="underline underline-offset-3">Register</NuxtLink>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const username = ref('');
const password = ref('');
const authStore = useAuthStore();

function login() {
  // Mock login logic
  // alert('Logged in as ' + username.value + 'with password: ' + password.value);
  authStore.login({username: username.value, password: password.value});

}

definePageMeta({
  layout: 'guest',
})
</script>