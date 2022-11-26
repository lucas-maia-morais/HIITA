<template>
    <div>
        <nav class="navtop">
            <div>
                <h1>{{ alt }}</h1>
                <router-link to="/" id="logo-url">
                    <img :src="logo" :alt ="alt" id="logo" />
                </router-link>
                <router-link to="/"><i class="fas fa-home"></i>Home</router-link>
                <router-link to="/Profile"><i class="fas fa-user-circle"></i>Profile</router-link>
                <router-link to="/Logout"><i class="fas fa-sign-out-alt"></i>Logout</router-link>
                <!-- <a href=""><i class="fas fa-home"></i>Home</a>
                <a href=""><i class="fas fa-user-circle"></i>Profile</a>
                <a href=""><i class="fas fa-sign-out-alt"></i>Logout</a> -->
            </div>
        </nav>
    </div>
</template>

<script>
export default {
  name: 'Navbar',
  props: ['logo', 'alt'],
};
</script>

<style scoped>
    #logo {
        width: 80px;
        height: 40px;
    }
</style>
