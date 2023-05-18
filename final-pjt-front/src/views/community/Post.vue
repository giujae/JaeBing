<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-3">
          <h1 class="font-do my-3">게시판</h1>
        </div>
        <div class="col-9 align-middle">
          <button v-if="this.$store.state.login" @click="createPost()" class="btn font-1-5em my-4">
            글 작성하기
          </button>
          <p v-else class="my-4 float-right">게시글을 작성하려면 로그인이 필요합니다.</p>
        </div>
      </div>
      <div class="row">
        <table class="table table-hover">
          <tr>
            <th>No</th>
            <th>제목</th>
            <th>작성자</th>
            <th>작성일</th>
          </tr>
          <tr v-for="(post, idx) in posts" :key="idx">
            <th>{{ post.id }}</th>
            <th @click="postDetail(post)">{{ post.title }}</th>
            <th>{{ post.user.username }}</th>
            <th>{{ $moment(post.created_at).format('YYYY-MM-DD hh:mm:ss') }}</th>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
import axios from 'axios';

export default {
  name: 'Post',
  data: function () {
    return {
      posts: [],
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
    createPost: function () {
      this.$router.push({
        name: 'CreatePost',
        params: {
          purpose: 'create',
        },
      });
    },
    postDetail: function (post) {
      this.$router.push({
        name: 'PostDetail',
        params: {
          id: post.id,
        },
      });
    },
  },
  created: function () {
    const config = this.setToken();
    axios
      .get(`${SERVER_URL}/community/`, config)
      .then((res) => {
        this.posts = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
  mounted() {
    window.scrollTo(0, 0);
  },
};
</script>

<style></style>
