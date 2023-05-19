<template>
  <div id="app">
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
      integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2"
      crossorigin="anonymous"
    />

    <div id="nav" class="p-2 main-nav">
      <b-navbar toggleable="lg" type="dark" id="navbar">
        <b-navbar-brand :style="{ 'font-size': '40px' }" class="nav-margin">
          <!-- <img :src="images.logo" width="80" alt="logo" /> -->
          <router-link :to="{ name: 'MovieList' }" id="logo" class="font-weight-bold"></router-link>
        </b-navbar-brand>

        <b-navbar-nav>
          <b-nav-item>
            <router-link :to="{ name: 'MovieList' }" id="logo" class="font-weight-bold"> Home </router-link>
          </b-nav-item>

          <!-- Navbar dropdowns -->
          <b-nav-item-dropdown text="Community" right>
            <b-dropdown-item class="drop-item">
              <router-link :to="{ name: 'Post' }" class="nav-margin">Post</router-link>
            </b-dropdown-item>
            <b-dropdown-item class="drop-item">ES</b-dropdown-item>
          </b-nav-item-dropdown>

          <b-nav-item-dropdown text="My Page" right>
            <b-dropdown-item class="drop-item">
              <router-link :to="{ name: 'Profile', params: { username: username } }">Profile</router-link>
            </b-dropdown-item>
            <b-dropdown-item class="drop-item">Settings</b-dropdown-item>
          </b-nav-item-dropdown>

          <b-navbar-nav>
            <div v-if="login">
              <p class="mr-3">해윙 {{ username }} !</p>
            </div>

            <div v-if="is_admin">
              <router-link :to="{ name: 'ManageMovie' }" class="nav-margin">
                <span class="badge badge-pill badge-warning">영화관리</span></router-link
              >
              <router-link :to="{ name: 'AdminManagement' }" class="nav-margin">
                <span class="badge badge-pill badge-warning">회원관리</span></router-link
              >
            </div>

            <div v-if="login">
              <router-link @click.native="logout" to="#" class="nav-margin">
                <span class="badge badge-pill badge-info">Logout</span></router-link
              >
            </div>

            <div v-else>
              <router-link :to="{ name: 'Signup' }" class="nav-margin">
                <button class="font-weight-bold">Signup</button>
              </router-link>
              <router-link :to="{ name: 'Login' }" class="nav-margin">
                <button class="font-weight-bold">Login</button>
              </router-link>
            </div>
          </b-navbar-nav>
        </b-navbar-nav>
      </b-navbar>
    </div>

    <router-view @login="login = true" />

    <div class="jumbotron font-poor mt-5" id="footerjumbo">
      <div class="container">
        <div class="row">
          <div class="col-3">
            <!-- <img :src="images.logo" width="190" alt="logo" /> -->
          </div>
          <div class="col-9"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// const SERVER_URL = process.env.VUE_APP_SERVER_URL

import { mapState } from 'vuex';
// import axios from 'axios'

export default {
  name: 'App',
  data: function () {
    return {
      login: false,
      images: {
        logo: require('@/assets/images/logo.png'),
        flamingo: require('@/assets/images/flamingo.png'),
      },
    };
  },
  methods: {
    logout: function () {
      localStorage.removeItem('jwt');
      this.login = false;
      this.$store.state.login = false;
      this.$store.state.is_admin = false;
      this.$store.state.login_user = '';
      this.$store.state.username = null;
      this.$router.push({
        name: 'Login',
      });
    },
  },
  created: function () {
    // 로그인

    const token = localStorage.getItem('jwt');

    if (token) {
      this.login = true;
    }
    this.$store.dispatch('getMovie');

    this.$router.push({ name: 'MovieList' });
  },
  computed: {
    ...mapState(['is_admin', 'username']),
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&family=Jua&family=Nanum+Gothic&family=Poor+Story&family=Slabo+27px&display=swap');
@import './assets/css/mycss.css';

#app {
  font-family: 'Salbo 27px', 'Nanum Gothic', Helvetica, Arial, sans-serif;
  /* Do Hyeon Jua Poor Story */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
  background: #0f2648;
  /* background-color: #0F2648; */
  width: 100%;
  min-height: 100vh;
}

#nav a {
  font-weight: bold;
  /* background: linear-gradient(45deg, #E8D1D9, #3C537F, #0f2648); */
  /* color: #2c3e50; */
}

#nav a.router-link-exact-active {
  /* color: #D44C7F; */
  color: #e8d1d9;
}

#logo {
  /* color: #de5078 !important; */
}

#footerjumbo {
  /* background-color: #de5078; */
  height: 250px;
  margin-bottom: 0rem;
}

/* 추가 */

/* community Mypage 네브바 속성 */
span {
  color: #e8d1d9;
}

/* 네브바 속성 */
.navbar {
  background-color: #0f2648;
}

/* 네브바 클릭시 나오는 item 속성 */
.drop-item {
  color: #e8d1d9;
}

/* signup login 속성 */
button {
  color: #e8d1d9;
  background-color: #0f2648;
  border-color: #0f264800;
  padding: 8px;
}

.dropdown-toggle::after {
  color: #e8d1d9;
}
</style>
