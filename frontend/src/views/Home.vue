<template>
  <div class="home content">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <h2>Home Page</h2>
    <Message v-if="showMessage" :message=message :error=false />
    <Train :train="choosedTrain" :exercises="exercises" v-if="isTrainingVisible"
      @saveTrain="saveTrain" @closeTrain="closeTrain"/>
    <table class="trainheadertable">
      <tr>
        <th>Ficha</th>
        <th>Descricao</th>
        <th>Escolher</th>
      </tr>
      <TrainHeader v-for="(treino, index) in treinos" :key="index" :treino="treino"
        @showTrain="showTrain"/>
    </table>
    <!-- Criar componente aqui de treinos Header disponiveis -->
    <!-- Usar props para passar informações de cada treino a serem mostradas -->
    <!-- No clique abre a pagina de treino refernte a aquele componente -->
  </div>
</template>

<script>
// @ is an alias to /src
import TrainHeader from '../components/TrainHeader.vue';
import Train from '../components/Train.vue';
import Message from '../components/Message.vue';

export default {
  name: 'Home',
  components: {
    TrainHeader,
    Train,
    Message,
  },
  data() {
    return {
      username: 'Neymar',
      treinos: [{ id: '1', title: 'peito', descricao: 'treino de peito' },
        { id: '2', title: 'costas', descricao: 'treino de costas' }],
      isTrainingVisible: false,
      choosedTrain: {},
      exercises: [],
      showMessage: false,
      message: '',
    };
  },
  async created() {
    const path = 'http://localhost:5000/HIITA/loggedin';

    const req = await fetch(path, {
      method: 'GET',
      headers: new Headers(),
    });
    // console.log(req);
    const res = await req.json();
    this.loggedin = res.loggedin;
    console.log(this.loggedin);
  },
  methods: {
    showTrain(tid) {
      this.isTrainingVisible = true;
      const trainId = tid;
      this.choosedTrain = this.treinos.find((el) => el.id === trainId);
      this.exercises = [{ id: '1', title: 'supino', descricao: '3x10' },
        { id: '2', title: 'barra', descricao: '4x10' }];
    },
    saveTrain() {
      this.message = 'Treino salvo';
      this.showMessage = true;
      setTimeout(() => {
        this.showMessage = false;
        this.message = '';
      }, 3000);
    },
    closeTrain() {
      this.isTrainingVisible = false;
      this.choosedTrain = '';
    },
  },
};
</script>

<style scoped>
h2 {
  color: white
}

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

.trainheadertable tr:hover {background-color: #ddd;}

.trainheadertable th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
