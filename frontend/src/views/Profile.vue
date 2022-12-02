<template>
<div class="loggedin content">
  <h2>Profile Page</h2>
  <div>
      <p>Your account details are below:</p>
      <table>
          <tr>
              <td>Username:</td>
              <td>{{ account['username'] }}</td>
          </tr>
          <tr>
              <td>Password:</td>
              <td>{{ account['password'] }}</td>
          </tr>
          <tr>
              <td>Email:</td>
              <td>{{ account['email'] }}</td>
          </tr>
      </table>
      <h1>Table of training performed</h1>
    <table class="trainheadertable">
      <tr>
        <th>Data</th>
        <th>Hora</th>
        <th>Treino</th>
      </tr>
      <TrainExecuted v-for="(treino, index) in treinos" :key="index" :treino="treino"/>
    </table>
  </div>
  <!-- Colocar aqui componente com treinos realizados pelo usuário -->
</div>
</template>

<script>
import TrainExecuted from '../components/TrainExecuted.vue';

export default {
  components: { TrainExecuted },
  data() {
    return {
      account: {
        username: 'neymarjr',
        email: 'neymarjr@gmail.com',
        password: 'hexa',
      },
      treinos: [{ data: '21/11/2022', hora: '12:30', title: 'Peito' },
        { data: '22/11/2022', hora: '7:30', title: 'costas' }],
    };
  },
};
</script>

<style scoped>
.trainheadertable {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

.trainheadertable td, .trainheadertable th {
  border: 1px solid #ddd;
  padding: 8px;
}

.trainheadertable tr:nth-child(even){
  background-color: #f2f2f2;
  color: #2c3e50;
}

.trainheadertable tr:hover tr:nth-child(odd){background-color: #ddd;}

.trainheadertable th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
