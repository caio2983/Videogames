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
  background-color: var(--color-background);
  padding: 20px;
  color: var(--color-heading);
  text-align: center;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border-bottom: 1px solid var(--color-border);
}

header h1 {
  margin: 0;
  font-size: 36px;
  font-weight: bold;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

header h2 {
  margin: 0;
  font-size: 20px;
  font-weight: normal;
  margin-top: 10px;
}

header a {
  color: var(--color-heading);
  text-decoration: none;
}

header a:hover {
  text-decoration: underline;
}

main {
  padding: 20px;
}
</style>
