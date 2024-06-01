<script setup>
import SalesYear from './SalesYear.vue'
</script>

<template>
  <div class="container">
    <div class="box"><SalesYear></SalesYear></div>
    <div class="boxText">
      <p>
        Pelo gráfico ao lado, percebe-se que o mercado de videogames teve um enorme salto a partir
        dos anos 2000. Nessa década, consoles como PlayStation 2, Xbox e Nintendo GameCube lideraram
        as vendas, visto que ofereceram qualidades técnicas inovadoras e uma variedade de jogos para
        todas as idades. Franquias de sucesso, como "Grand Theft Auto" e "Halo", surgiram nessa
        época. Os anos de 2008 (677.69 milhões de vendas globais) e de 2009 (662.7 milhões de vendas
        globais) se destacaram como os mais fortes para a indústria, com o lançamento de consoles
        populares como o PlayStation 3, Xbox 360 e Nintendo Wii.
      </p>
    </div>
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
  height: 600px;
  background-color: #fff;
  border: 1px solid #ccc;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10px;
  color: black;
}

.boxText {
  width: 45%;
  height: 600px;
  background-color: #fff;
  border: 1px solid #ccc;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: large;
  padding: 40px;
  color: black;
}
</style>
