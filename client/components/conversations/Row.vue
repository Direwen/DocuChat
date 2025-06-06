<template>

    <div class="flex gap-5 p-2 rounded-lg">

        <!-- Icon -->
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
            class="size-6 mt-1">
            <path stroke-linecap="round" stroke-linejoin="round"
                d="M7.5 8.25h9m-9 3H12m-9.75 1.51c0 1.6 1.123 2.994 2.707 3.227 1.129.166 2.27.293 3.423.379.35.026.67.21.865.501L12 21l2.755-4.133a1.14 1.14 0 0 1 .865-.501 48.172 48.172 0 0 0 3.423-.379c1.584-.233 2.707-1.626 2.707-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0 0 12 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018Z" />
        </svg>

        <!-- Content -->
        <section class="grow border-b border-base-300 flex justify-between items-center pb-4">
            <div>
                <p class="text-base-content">British United College BSc Computer Science Top-Up Program Overview</p>
                <span class="text-sm text-base-content/70">Tuesday, June 3 at 9:37 AM</span>
            </div>
            <div class="dropdown dropdown-end">
                <button tabindex="0" class="btn btn-ghost btn-sm">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                        stroke="currentColor" class="size-6">
                        <path stroke-linecap="round" stroke-linejoin="round"
                            d="M6.75 12a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0ZM12.75 12a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0ZM18.75 12a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Z" />
                    </svg>
                </button>
                <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-10 w-48 p-2 shadow-lg">
                    <li><button class="text-error hover:bg-error hover:text-error-content">Delete</button></li>
                </ul>
            </div>
        </section>
    </div>
</template>