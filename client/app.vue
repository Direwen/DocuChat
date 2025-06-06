<template>
  <div>
    <NuxtRouteAnnouncer />
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<script setup>
import { useAuthStore } from '@/stores/authStore';

const authStore = useAuthStore();

if (import.meta.client) {
  const token = localStorage.getItem('token');
  if (token && !authStore.isAuthenticated) {
    authStore.getUser();
  }
}

useHead({
  htmlAttrs: {
    'data-theme': 'autumn',
  },
});
</script>

