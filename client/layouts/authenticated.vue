<template>
  <div>

    <div class="drawer lg:drawer-open">
      <input id="my-drawer-2" type="checkbox" class="drawer-toggle" />
      <div class="drawer-content flex flex-col items-center">

        <!-- navbar -->
        <div class="lg:hidden navbar bg-base-100 shadow-sm">
          <label for="my-drawer-2" class="btn btn-primary drawer-button lg:hidden">
            Open drawer
          </label>
          <a class="btn btn-ghost text-xl">daisyUI</a>
        </div>

        <!-- Page content here -->
        <slot name="header"></slot>
        <slot></slot>

      </div>

      <!-- sidebar -->
      <div class="drawer-side">
        <label for="my-drawer-2" aria-label="close sidebar" class="drawer-overlay"></label>
        <ul class="menu bg-base-200 text-base-content w-80 p-6 min-h-screen relative">
          <!-- Logo Section -->
          <div class="mb-8 flex gap-2">
            <UtilsThemeController2 />
            <h1
              class="text-3xl font-bold text-primary bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">
              DocuChat
            </h1>
          </div>

          <!-- Navigation Links -->
          <li class="space-y-2">
            <NuxtLink to="/conversations"
              class="flex items-center gap-4 p-3 rounded-lg hover:bg-base-300 transition-colors"
              :class="{ 'bg-primary text-primary-content hover:bg-primary/70': $route.path === '/conversations' }">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                stroke="currentColor" class="size-6">
                <path stroke-linecap="round" stroke-linejoin="round"
                  d="M7.5 8.25h9m-9 3H12m-9.75 1.51c0 1.6 1.123 2.994 2.707 3.227 1.129.166 2.27.293 3.423.379.35.026.67.21.865.501L12 21l2.755-4.133a1.14 1.14 0 0 1 .865-.501 48.172 48.172 0 0 0 3.423-.379c1.584-.233 2.707-1.626 2.707-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0 0 12 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018Z" />
              </svg>
              <span>Conversations</span>
            </NuxtLink>

            <NuxtLink to="/documents" class="flex items-center gap-4 p-3 rounded-lg hover:bg-base-300 transition-colors"
              :class="{ 'bg-primary text-primary-content hover:bg-primary/70': $route.path === '/documents' }">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                stroke="currentColor" class="size-6">
                <path stroke-linecap="round" stroke-linejoin="round"
                  d="M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m2.25 0H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z" />
              </svg>
              <span>Documents</span>
            </NuxtLink>

            <NuxtLink to="/" class="flex items-center gap-4 p-3 rounded-lg hover:bg-base-300 transition-colors"
              :class="{ 'bg-primary text-primary-content hover:bg-primary/70': $route.path === '/' }">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                stroke="currentColor" class="size-6">
                <path stroke-linecap="round" stroke-linejoin="round"
                  d="M9.879 7.519c1.171-1.025 3.071-1.025 4.242 0 1.172 1.025 1.172 2.687 0 3.712-.203.179-.43.326-.67.442-.745.361-1.45.999-1.45 1.827v.75M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9 5.25h.008v.008H12v-.008Z" />
              </svg>
              <span>Help & Support</span>
            </NuxtLink>
          </li>

          <!-- bottom section -->
          <li class="absolute bottom-0.5 left-0 w-full p-4">

            <UtilsAccountSetting />
          </li>
        </ul>
      </div>
    </div>

  </div>
</template>