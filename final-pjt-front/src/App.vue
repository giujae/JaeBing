<template>
  <div id="app">
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
      integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2"
      crossorigin="anonymous"
    />

    <div id="nav" class="main-nav" v-if="this.$route.path !== '/'">
      <b-navbar toggleable="lg">
      <b-navbar-toggle target="navbar-nav-collapse"></b-navbar-toggle>

    <b-navbar-brand href="/movies" class="font-weight-bold">Home</b-navbar-brand>

    <b-collapse id="navbar-nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item-dropdown text="Community">
          <b-dropdown-item>
            <router-link :to="{ name: 'Post' }">Post</router-link>
          </b-dropdown-item>
          <b-dropdown-item>ES</b-dropdown-item>
        </b-nav-item-dropdown>

        <b-nav-item-dropdown text="My Page">
          <b-dropdown-item>
            <router-link :to="{ name: 'Profile', params: { username: username } }">Profile</router-link>
          </b-dropdown-item>
          <b-dropdown-item>Settings</b-dropdown-item>
        </b-nav-item-dropdown>

        <template v-if="is_admin">
          <b-nav-item>
            <router-link :to="{ name: 'ManageMovie' }" class="nav-margin">
              <span class="badge badge-pill badge-warning">영화관리</span>
            </router-link>
          </b-nav-item>

          <b-nav-item>
            <router-link :to="{ name: 'AdminManagement' }" class="nav-margin">
              <span class="badge badge-pill badge-warning">회원관리</span>
            </router-link>
          </b-nav-item>
        </template>
      </b-navbar-nav>

      <b-navbar-nav class="ml-auto">
        <template v-if="$store.state.login">
          <b-nav-item>
            <button @click="triggerSearch" class="font-weight-bold font-do search-btn">검색</button>
          </b-nav-item>

            <p class="user font-weight-bold text-truncate">해윙 {{ username }}!</p>

          <b-nav-item>
            <router-link @click.native="logout" to="#" class="nav-margin">
              <button class="font-weight-bold">Logout</button>
            </router-link>
          </b-nav-item>
        </template>

        <template v-else>
          <b-nav-item>
            <router-link :to="{ name: 'Signup' }" class="nav-margin">
              <button class="font-weight-bold">Signup</button>
            </router-link>
          </b-nav-item>

          <b-nav-item>
            <router-link :to="{ name: 'Login' }" class="nav-margin">
              <button class="font-weight-bold">Login</button>
            </router-link>
          </b-nav-item>
        </template>

        </b-navbar-nav>
      </b-collapse>
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
      hideAdd: true,
    };
  },
  methods: {
    logout: function () {
      localStorage.removeItem('jwt');
      localStorage.removeItem('username');
      localStorage.removeItem('login_user');
      this.login = false;
      this.$store.state.login = false;
      this.$store.state.is_admin = false;
      this.$store.state.login_user = '';
      this.$store.state.username = null;
      this.$router.push({
        name: 'Main',
      });
    },
    triggerSearch: function () {
      this.$router.push({ name: 'MovieSearch' });
    },
  },
  created: function () {
    // 로그인
    const token = localStorage.getItem('jwt');

    if (this.$route.path !== '/') {
      console.log('입구컷');
      if (token) {
        this.login = true;
      }
      console.log('1번 발동');
      this.$store.dispatch('getMovie');
      if (this.$store.state.ordered_movie_list.length == 0) {
        // 영화 목록이 비어있는 경우에만 getMovie 액션 호출
        console.log('비었는데요?');
      }
      if (this.$route.path !== '/movies') {
        console.log('2번 발동');
        this.$router.push({ name: 'MovieList' });
      }
    }
  },

  computed: {
    ...mapState(['is_admin', 'username']),
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&family=Jua&family=Nanum+Gothic&family=Poor+Story&family=Slabo+27px&display=swap');

#app {
  font-family: 'Salbo 27px', 'Nanum Gothic', Helvetica, Arial, sans-serif;
  /* Do Hyeon Jua Poor Story */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  background: #101130;
  /* background-color: #0F2648; */
  width: 100%;
  min-height: 100vh;
}


#nav a {
  font-weight: bold;
  color: #e8d1d9;
  text-decoration-line: none;
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
  padding: 0px;
}

/* 네브바 토글 속성 */
.collapse {
  color: #e8d1d9;
  border-color: #e8d1d9;
}

/* 네브바 클릭시 나오는 item 속성 */
.drop-item {
  color: #3c537f;
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
  margin: -5px;
}

.logout {
  border-color: #0f264800;
  background-color: #0f264800;
  padding: 8px;
}

.user {
  color: #e8d1d9;
  padding: 8px;
  margin-top: 10px;
}

.appear {
  display: none;
}

.jumbotron {
  background: linear-gradient(360deg, #e8d1d9, #3c537f, #101130);
}
</style>
