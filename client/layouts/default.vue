<template>
  <div>

    <div class="drawer lg:drawer-open">
      <input id="my-drawer-2" type="checkbox" class="drawer-toggle" />
      <div class="drawer-content flex flex-col items-center">
        
        <!-- navbar -->
        <div class="lg:hidden navbar bg-base-100 shadow-sm">
          <label for="my-drawer-2"  class="btn btn-primary drawer-button lg:hidden">
            Open drawer
          </label>
          <a class="btn btn-ghost text-xl">daisyUI</a>
        </div>
        
        <!-- Page content here -->
        <slot name="header"></slot>
        <div class="divider"></div>

        <slot></slot>

      </div>
      <div class="drawer-side">
        <label for="my-drawer-2" aria-label="close sidebar" class="drawer-overlay"></label>
        <ul class="menu bg-base-200 text-base-content min-h-full w-80 p-4">
          <!-- Sidebar content here -->
          <li><a>Conversation</a></li>
          <li><a>Documents</a></li>
          <li><a>Help & Support</a></li>
        </ul>
      </div>
    </div>

  </div>
</template>