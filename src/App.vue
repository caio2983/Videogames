<script setup>
import VgSalesYear from './components/VgSalesYear.vue'
import X360_PS3 from './components/X360_PS3.vue'
import Genres from './components/Genres.vue'
import Platforms from './components/Platforms.vue'
</script>

<template>
  <header>
    <h1>Relatório de Vendas de Video Games</h1>
    <h2>
      Dados retirados de
      <a
        href="https://www.kaggle.com/datasets/gregorut/videogamesales"
        target="_blank"
        rel="noopener noreferrer"
      >
        https://www.kaggle.com/datasets/gregorut/videogamesales
      </a>
    </h2>
  </header>

  <main>
    <VgSalesYear></VgSalesYear>
    <X360_PS3></X360_PS3>
    <Genres></Genres>
    <Platforms></Platforms>
  </main>
</template>

<style scoped>
header {
  background-color: #4caf50; /* Cor de fundo verde */
  padding: 20px; /* Espaçamento interno */
  color: white; /* Cor da fonte */
  text-align: center; /* Centralizar o texto */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Sombra leve */
}

header h1 {
  margin: 0;
  font-size: 28px; /* Tamanho da fonte do título */
}

header h2 {
  margin: 0;
  font-size: 18px; /* Tamanho da fonte do subtítulo */
  font-weight: normal; /* Peso da fonte do subtítulo */
  margin-top: 10px; /* Espaço entre título e subtítulo */
}

main {
  padding: 20px; /* Espaçamento interno */
}
</style>
