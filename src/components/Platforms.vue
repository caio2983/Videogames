<script setup>
import PlatformsGrafico from './PlatformsGrafico.vue'
</script>

<template>
  <div class="container">
    <div class="box"><PlatformsGrafico></PlatformsGrafico></div>
    <div class="boxText"></div>
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
  width: 90%;
  height: 600px;
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
zzs
