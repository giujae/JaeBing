<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-6">
          <h1 class="m-3">안농 :) 어서와!</h1>
          <h2>로그인 할래yo?</h2>
        </div>
      </div>

      <div class="row">
        <div class="col-6 d-flex justify-content-center" id="rightline">
          <div class="mb-3 mt-5" style="max-width: 18rem">
            <div class="card-body">
              <div class="input-group-lg">
                <h4>아이디</h4>
                <input
                  type="text"
                  placeholder="아이디 입력해!"
                  id="username"
                  class="form-control"
                  v-model="credentials.username"
                />
              </div>
              <br />
              <br />
              <div class="input-group-lg">
                <h4>비밀번호</h4>
                <input
                  placeholder="비밀번호 입력해!"
                  type="password"
                  id="password"
                  class="form-control"
                  v-model="credentials.password"
                  @keypress.enter="login"
                />
              </div>
              <br />
              <button @click="login" class="login-btn btn mt-3 font-1-5em btn-block">웅! 자 드가자</button>
            </div>
          </div>
        </div>

        <div class="col-6 d-flex align-items-center justify-content-center">
          <div>
            <h3 class="signup-ment">이걸 아직도 가입 안 했어?!</h3>
            <div class="emptydiv"></div>
            <router-link class="signup-a" :to="{ name: 'Signup' }">당장 가입 해.</router-link>
            <div class="emptydiv"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      },
    };
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt');

      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        },
      };
      return config;
    },

    login: function () {
      axios
        .post(`${SERVER_URL}/accounts/api-token-auth/`, this.credentials)
        .then((res) => {
          // console.log(res)
          localStorage.setItem('jwt', res.data.token);
          this.$emit('login');
          this.$store.state.login = true;

          // console.log(res)
          const config = this.setToken();
          axios
            .get(`${SERVER_URL}/accounts/user/`, config)
            .then((res) => {
              // console.log(res.data)
              const id = res.data;
              this.$store.state.login_user = id;
              this.$store.state.username = this.credentials.username;
              localStorage.setItem('username', this.credentials.username);
              localStorage.setItem('login_user', id);
              this.$store.dispatch('recommendMovie', id);
              this.$store.dispatch('getMovie');
              // console.log(this.$store.state.login_user)
            })
            .catch((err) => {
              console.log(err);
            });

          axios
            .post(`${SERVER_URL}/accounts/is-admin/`, this.credentials)
            .then((res) => {
              this.$store.dispatch('isAdmin', res.data);
              localStorage.setItem('is_admin', res.data);
            })
            .catch((err) => {
              console.log(err);
            });
          this.$store.state.username = this.credentials.username;
          if (this.flag) {
            this.$router.push({
              name: 'AdminManagement',
            });
          } else {
            this.$router.push({
              name: 'MovieList',
            });
          }
        })
        .catch((err) => {
          console.log(err);
          alert('로그인 정보가 일치하지 않습니다.');
        });
    },
  },
  mounted() {
    window.scrollTo(0, 0);
    const token = localStorage.getItem('jwt');
    if (token) {
      const config = this.setToken();

      // 토큰 검증 및 사용자 정보 요청
      axios
        .get(`${SERVER_URL}/accounts/user/`, config)
        .then((res) => {
          const id = res.data;
          this.$store.state.login_user = id;
          this.$store.state.username = this.credentials.username;
          localStorage.setItem('username', this.credentials.username);
          localStorage.setItem('login_user', id);
          this.$store.dispatch('recommendMovie', id);

          // 로그인 상태를 설정
          this.$store.state.login = true;
        })
        .catch((err) => {
          console.log(err);

          // 토큰 검증 실패 시 로그인 상태를 false로 설정
          this.$store.state.login = false;
        });
    } else {
      // 토큰이 없는 경우 로그인 상태를 false로 설정
      this.$store.state.login = false;
    }
  },
};
</script>

<style scoped>
/* 로그인 멘트 */
.container {
  color: #e8d1d9;
  min-height: 80vh;
  background-image: url('https://st2.depositphotos.com/14548252/47970/v/600/depositphotos_479708850-stock-illustration-evening-landscape-with-bright-fireworks.jpg');
  background-size: cover;
  background-position: center;
}

/* 로그인 카드 속성 */

/* 로그인 인풋 속성 */
.form-control {
  background-color: #e8d1d900;
}

/* 중간 점선 */
#rightline {
  border-right: dashed #e8d1d969;
}

.emptydiv {
  height: 50px;
}

/* 회원가입 멘트 속성 */
.signup-ment {
  text-decoration: none;
}

/* 회원가입 버튼 속성 */
.signup-a {
  color: #e8d1d9;
  text-decoration: none;
  font-size: 20px;
}

/* 로그인 버튼 속성 */
.login-btn {
  color: #e8d1d9;
  font-size: 20px;
}

html {
  /* background-color: #0F2648; */
  /* background: red !important; */
}

<<<<<<< HEAD
.card-body {
  background-image: url(./pngwing.png);
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
}
=======


>>>>>>> 0bce9d4d89afa62f14037f5485c953d66bd67ade
</style>
