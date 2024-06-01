<script setup>
import X360_Top5Grafico from './X360_Top5Grafico.vue'
import PS3_Top5Grafico from './PS3_Top5Grafico.vue'
</script>

<template>
  <div class="container">
    <div class="box"><X360_Top5Grafico /></div>
    <div class="box"><PS3_Top5Grafico /></div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  justify-content: space-around;
  align-items: center;
  margin: 20px;
  padding: 20px;
  background-color: #f0f0f0;
  border-radius: 10px;
}

.box {
  width: 45%;
  height: 600px; /* Ajuste a altura conforme necessário */
  background-color: #fff;
  border: 1px solid #ccc;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10px;
}
</style>
