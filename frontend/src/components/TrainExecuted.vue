<template>
    <tr class="trainexecuted">
        <td>{{treino.data}}</td>
        <td>{{treino.hora}}</td>
        <td>{{treino.title}}</td>
    </tr>
</template>

<script>
export default {
  props: {
    treino: Object,
  },
};
</script>
