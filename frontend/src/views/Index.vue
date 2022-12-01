<template>
    <div>
        <LoginRegister v-if="!loggedin" />
        <Home :username="username" :loggedin="loggedin" v-else />
    </div>
</template>

<script>
import LoginRegister from '@/views/LoginRegister.vue';
import Home from '@/views/Home.vue';

export default {
  components: {
    LoginRegister,
    Home,
  },
  data() {
    return {
      loggedin: false,
      username: 'neymar',
    };
  },
  created() {
    const path = 'http://localhost:5000/HIITA/loggedin';

    const req = fetch(path, {
      method: 'GET',
    });
    console.log(req);
    const res = req.json();
    this.loggedin = res.loggedin;
    console.log(this.loggedin);
  },
};
</script>
