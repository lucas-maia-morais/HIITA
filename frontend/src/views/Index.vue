<template>
    <div>
      <h1>Login</h1>
      <div class="links">
        <a @click="showLogin=true">Login</a>
        <a @click="showLogin=false">Register</a>
      </div>
      <Login v-if="showLogin" />
      <Register v-else />
    </div>
</template>

<script>
import Login from '@/components/Login.vue';
import Register from '@/components/Register.vue';

export default {
  components: {
    Login,
    Register,
  },
  data() {
    return {
      showLogin: false,
    };
  },
};
</script>
