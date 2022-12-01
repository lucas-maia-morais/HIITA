<template>
  <div class="home content">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <h2>Home Page</h2>
    <p>Welcome back, {{ username }}!</p>
    <!-- Criar componente aqui de treinos Header disponiveis -->
    <!-- Usar props para passar informações de cada treino a serem mostradas -->
    <!-- No clique abre a pagina de treino refernte a aquele componente -->
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  components: {
  },
  data() {
    return {
      username: 'Neymar',
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
};
</script>

<style scoped>
h2 {
  color: white
}
</style>
