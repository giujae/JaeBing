<template>
  <div class="comment-container">
    <form v-on:submit.prevent="createComment">
      <div class="row">
        <div class="col-2 d-flex align-items-center m-0">
          <label for="content" class="m-0">댓글달기: </label>
        </div>
        <div class="col-6 position-relative">
          <input type="text" class="form-control" id="content" v-model="content" />
        </div>
        <div class="col-4 d-flex align-items-center">
          <button type="submit" class="comment-create-btn">등록</button>
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

<style>
.comment-container {
  width: 100%;
  max-width: 500px;
  margin: 0 auto;
}

.comment-container .row {
  display: flex;
  align-items: flex-end;
}

.comment-container .col-2,
.comment-container .col-6,
.comment-container .col-4 {
  flex: 1;
}

.comment-container .col-2 label {
  white-space: normal;
  overflow: visible;
  text-overflow: ellipsis;
  display: inline-block;
  width: 100%;
}

.comment-container .col-6 input[type="text"] {
  width: 100%;
  position: absolute;
  bottom: 0;
}

.comment-container .col-4 {
  display: flex;
  align-items: flex-end;
}
</style>
