<template>
    <div>
        <form @click="login()" method="post">
            <label for="username">
                <i class="fas fa-user"></i>
            </label>
            <input type="text" name="username" placeholder="Username" id="username" required>
            <label for="password">
                <i class="fas fa-lock"></i>
            </label>
            <input type="password" name="password" placeholder="Password" id="password" required>
            <div class="msg">{{ msg }}</div>
            <input type="submit" value="Login">
        </form>
    </div>
</template>

<script>
export default {
  name: 'Login',
  methods: {
    async login() {
      console.log('login');
    },
    async register() {
      console.log('register');
    },
  },
};
</script>
