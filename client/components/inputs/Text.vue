<template>
    <label class="w-full input validator flex items-center gap-2 border rounded px-3 py-2">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="h-[1em] opacity-50">
            <path stroke="currentColor" stroke-width="2" fill="none" d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2">
            </path>
            <circle cx="12" cy="7" r="4" stroke="currentColor" stroke-width="2" fill="none"></circle>
        </svg>

        <input type="text" :value="modelValue" @input="$emit('update:modelValue', $event.target.value)"
            :placeholder="placeholder" class="outline-none flex-1 bg-transparent" />
    </label>
    <div class="validator-hint hidden">Enter a valid username</div>
</template>

<script setup>
defineProps({
    modelValue: {
        type: String,
        required: true,
    },
    placeholder: {
        type: String,
        required: false,
    }
});
defineEmits(['update:modelValue']);
</script>