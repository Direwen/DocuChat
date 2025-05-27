<template>
    <header class="bg-white shadow">
        <div class="container mx-auto px-4 py-4 flex justify-between items-center">
            <h1 class="text-xl font-bold">My Nuxt App</h1>
            <nav class="space-x-4">
                <NuxtLink 
                    v-for="link in links" 
                    :key="link.path" 
                    :to="link.path"
                    class="px-3 py-2 rounded-md text-sm font-medium transition-colors duration-200"
                    :class="$route.path === link.path ? 'bg-blue-100 text-blue-700' : 'text-gray-700 hover:bg-gray-100'"
                >
                    {{ link.name }}
                </NuxtLink>
            </nav>
        </div>
    </header>
</template>

<script setup>
const links = [
    { name: 'Home', path: '/' },
    { name: 'Login', path: '/auth/login' },
    { name: 'Register', path: '/auth/register' }
]
</script>