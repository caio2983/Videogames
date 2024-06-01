<script setup>
import GenresGrafico from './GenresGrafico.vue'
</script>

<template>
  <div class="container">
    <div class="box"><GenresGrafico></GenresGrafico></div>
    <div class="boxText">
      Pelo gráfico, os gêneros de jogos que mais venderam foram 1-Esportes(1330 milhões de vendas
      globais),2-Tiro (1032 milhões de vendas globais),3-Role-Playing(926 milhões de vendas
      globais).Os jogos de esportes alcançaram tamanho sucesso pois capitalizam na popularidade de
      competições reais como futebol e basquete, enquanto os shooters cativam os jogadores com
      narrativas envolventes e ação intensa. Exemplos notáveis de sucesso incluem títulos como "FIFA
      09", "Call of Duty: World at War" e "Fallout 3" lançados nos anos de 2008 e 2009,
      respectivamente. Por outro lado, gêneros como quebra-cabeça (puzzle), estratégia (strategy) e
      simulação (simulation) tendem a ter vendas mais modestas devido à sua natureza mais específica
      e à menor atratividade para o público em geral devido à maior complexidade que os títulos
      desse gênero apresentam.
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
