<template>
  <div class="container">
    <form v-on:submit.prevent="createComment">
      <div class="row">
        <div class="col-2 d-flex align-items-center">
          <label for="content" class="font-1-5em">댓글달기: </label>
        </div>
        <div class="col-6 d-flex align-items-center">
          <input type="text" class="form-control" id="content" v-model="content" />
        </div>
        <div class="col-4 d-flex align-items-center">
          <button type="submit" class="btn btn-pink font-1-2em">등록</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
import axios from 'axios';

export default {
  name: 'CommentForm',
  data: function () {
    return {
      content: '',
    };
  },
  props: {
    post: [Object, String],
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
    createComment: function () {
      const config = this.setToken();

      const commentItem = {
        content: this.content,
      };
      const postId = this.post.id;
      axios
        .post(`${SERVER_URL}/community/${postId}/comment_create/`, commentItem, config)
        .then((res) => {
          this.$store.state.comments.unshift(res.data);
          this.content = '';
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created: function () {
    console.log('post타입은?' + typeof this.post);
    console.log(this.post);
  },
};
</script>

<style></style>
