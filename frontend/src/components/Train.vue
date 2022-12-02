<template>
  <div>
    <button @click="$emit('closeTrain')"><i class="fas fa-times-circle-o">Close</i></button>
    <button @click="$emit('saveTrain')"><i class="fas fa-times-circle-o">Save</i></button>
    <h1>{{train.title}}</h1>
      <p v-for="exercise in exercises" :key="exercise.id" >
        <a>{{exercise.name}}</a>
        <a>    </a>
        <a>{{exercise.descricao}}</a>
      </p>
  </div>
</template>

<script>
export default {
  props: {
    train: Object,
    exercises: Array,
  },
};
</script>
