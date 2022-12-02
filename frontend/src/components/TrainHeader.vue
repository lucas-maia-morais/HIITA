<template>
    <tr class="trainheader">
        <td>{{treino.title}}</td>
        <td>{{treino.descricao}}</td>
        <td><button @click="$emit('showTrain', treino.id)">
          <i class="fas fa-check"></i></button></td>
    </tr>
</template>

<script>
export default {
  props: {
    treino: Object,
  },
};
</script>

<style scoped>
.trainheader {
    background-color: #2c3e50;
    color: white;
}
</style>
