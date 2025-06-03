<template>
    <label class="w-full input validator flex items-center gap-2 border rounded px-3 py-2">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="h-[1em] opacity-50">
            <rect x="3" y="11" width="18" height="11" rx="2" ry="2" stroke="currentColor" fill="none" stroke-width="2">
            </rect>
            <path d="M7 11V7a5 5 0 0 1 10 0v4" stroke="currentColor" stroke-width="2" fill="none"></path>
        </svg>

        <input type="password" :value="modelValue" @input="$emit('update:modelValue', $event.target.value)"
            placeholder="Password" class="outline-none flex-1 bg-transparent" />
    </label>
    <div class="validator-hint hidden">Enter password</div>
</template>

<script setup>
defineProps({
    modelValue: {
        type: String,
        required: true,
    },
});
defineEmits(['update:modelValue']);
</script>
