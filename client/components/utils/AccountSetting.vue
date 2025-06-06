<template>
    <div class="flex items-center justify-between gap-4 p-3 rounded-lg hover:bg-transparent">
      <!-- Avatar -->
      <div class="w-10 h-10 rounded-full bg-gradient-to-br from-primary to-secondary flex items-center justify-center">
        <span class="text-sm font-semibold text-primary-content/80">D</span>
      </div>
      <!-- Name -->
      <span class="grow text-base font-medium text-base-content">Direwen</span>
      <!-- Dropdown Menu -->
      <div class="dropdown dropdown-end dropdown-top">
        <button tabindex="0" role="button" class="btn btn-ghost btn-sm">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="size-6"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M6.75 12a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0ZM12.75 12a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0ZM18.75 12a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Z"
            />
          </svg>
        </button>
        <ul
          tabindex="0"
          class="dropdown-content menu bg-base-100 rounded-box z-10 w-48 p-2 shadow-lg mt-2"
        >
          <li>
            <button class="hover:bg-base-200 transition-colors">Profile</button>
          </li>
          <li>
            <button class="hover:bg-base-200 transition-colors">Logout</button>
          </li>
        </ul>
      </div>
    </div>
  </template>