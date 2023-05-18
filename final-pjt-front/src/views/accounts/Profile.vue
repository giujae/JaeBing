<template>
  <div>
    <h1 class="font-do my-3">프로필</h1>
    <div v-if="profile">
      <p><strong>회원코드:</strong> {{ profile.id }}</p>
      <p><strong>아이디:</strong> {{ profile.username }}</p>
      <p><strong>가입일:</strong> {{ formatDate(profile.date_joined) }}</p>
      <p><strong>생일:</strong> {{ profile.date_of_birth }}</p>
      <p><strong>이메일:</strong> {{ profile.email }}</p>
      <p><strong>등급:</strong> {{ isAdmin ? '관리자' : '일반회원' }}</p>
    </div>
    <p v-else>Loading...</p>
  </div>
</template>

<script>
import axios from 'axios';

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: 'Profile',
  data() {
    return {
      profile: null,
      isAdmin: false,
    };
  },
  methods: {
    formatDate(date) {
      return this.$moment(date).format('YYYY-MM-DD');
    },
  },
  created() {
    const username = this.$route.params.username;
    axios
      .get(`${SERVER_URL}/accounts/profile/${username}/`)
      .then((res) => {
        this.profile = res.data;
        this.isAdmin = res.data.is_superuser;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&family=Jua&family=Poor+Story&family=Slabo+27px&display=swap');
</style>
