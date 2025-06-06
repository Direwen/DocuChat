<template>
  <!-- Trigger Button with Custom Class -->
  <button class="btn" :class="buttonClass" @click="openModal">{{ buttonText }}</button>

  <!-- Modal Dialog -->
  <dialog :id="modalId" class="modal modal-bottom sm:modal-middle" ref="modalRef">
    <div class="modal-box">
      <h3 class="text-lg font-bold">{{ title }}</h3>
      <p class="py-4">{{ content }}</p>
      <div class="modal-action">
        <!-- Content slot for custom actions -->
        <slot name="actions"></slot>
        <!-- Cancel Button -->
        <form method="dialog">
          <button class="btn">Cancel</button>
        </form>
      </div>
    </div>
    <!-- Backdrop for outside click closure -->
    <form method="dialog" class="modal-backdrop" @click="closeModal">
      <button hidden>close</button>
    </form>
  </dialog>
</template>

<script setup>
import { ref } from 'vue'

// Props definition
const props = defineProps({
  buttonText: {
    type: String,
    default: 'Open Modal',
  },
  title: {
    type: String,
    default: 'Hello!',
  },
  content: {
    type: String,
    default: 'Press ESC key or click outside to close',
  },
  modalId: {
    type: String,
    default: 'my_modal',
  },
  buttonClass: {
    type: String,
    default: '',
  },
})

// Refs
const modalRef = ref(null)

// Methods
const openModal = () => {
  if (modalRef.value) {
    modalRef.value.showModal()
  }
}

const closeModal = () => {
  if (modalRef.value) {
    modalRef.value.close()
  }
}
</script>
