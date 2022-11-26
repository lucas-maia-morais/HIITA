<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <h2>Home Page</h2>
    <p>Welcome back, {{ username }}!</p>
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
};
</script>

<style scoped>
p, h2 {
  color: white
}
</style>
