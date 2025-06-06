<template>

  <p>
    {{ authStore.user }}
  </p>

</template>

<script setup>
import { useAuthStore } from '@/stores/authStore';

const authStore = useAuthStore();

definePageMeta({
  layout: 'guest'
})

</script>