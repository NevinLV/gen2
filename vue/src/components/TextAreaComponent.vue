<script setup lang="ts">
import {ref} from 'vue'

interface Props {
  value?: string;
}

const props = withDefaults(defineProps<Props>(), {
  value: "",
});

const emit = defineEmits<{
  changeValue: [value: string];
}>();

const input_value = ref<string>(props.value);

/**
 * Изменение значения
 */
function changeValue() {
  if (input_value.value !== null) emit("changeValue", input_value.value);
}
</script>

<template>
<textarea class="task-input" style="width: 100%; height: 370px; z-index: 99;" v-model="input_value" @input="changeValue">
</textarea>
</template>
