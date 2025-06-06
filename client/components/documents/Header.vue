<template>
  <header class="w-full bg-base-100 shadow-lg py-4 px-4 sm:px-6 lg:px-8">
    <div class="container mx-auto flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 sm:gap-6">
      <!-- Left Section: Title and Description -->
      <section class="flex flex-col items-start">
        <h1 class="text-xl sm:text-2xl lg:text-3xl font-bold text-primary">
          Documents
        </h1>
        <p class="text-xs sm:text-xs lg:text-sm text-base-content/40 mt-1 max-w-md">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Asperiores vitae neque ipsa, ab perferendis soluta!
        </p>
      </section>

      <!-- Right Section: Action Button -->
      <div class="w-full sm:w-auto">
        <InputsBaseModal buttonText="New Document" title="Greetings!" content="Click outside or press ESC to close"
          modalId="my_modal_2" buttonClass="btn btn-primary w-full sm:w-auto text-sm sm:text-base" />
      </div>
    </div>
  </header>
</template>