<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
  name: "Header"
})
</script>

<template>
  <header style="width: 100vw;">
    <div class="row px-5">
      <div class="col d-flex logo">
        GEN<span class="accent">ED</span>IS
      </div>
      <div class="col-auto dark-panel">
        <button class="me-2">Войти</button>
        <button  class="me-2">Зарегистрироваться</button>
      </div>
    </div>
  </header>
</template>

<style scoped>

</style>