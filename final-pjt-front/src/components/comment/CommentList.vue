<template>
  <div>
    <h2 class="mt-5 font-do">댓글 목록</h2>

    <div v-for="(comment, idx) in comments" :key="idx" class="media mt-3">
      <div class="media-body">
        <h3 class="mt-0">[{{ comment.user.username }}] {{ comment.content }}</h3>
        <p>작성: {{ $moment(comment.created_at).format('YYYY-MM-DD hh:mm:ss') }} |</p>
        <p>수정: {{ $moment(comment.created_at).format('YYYY-MM-DD hh:mm:ss') }}</p>

        <div v-if="updateTrigger === comment.id">
          <UpdateForm :updateCommentItem="updateCommentItem" :post="post" @trigger="changeTrigger" />
        </div>
        <div>
          <!--작성자와 접속자가 같다면, 수정/삭제 버튼 활성화-->
          <!--단, 관리자의 경우 삭제 버튼 활성화 -->
          <button
            class="btn btn-pink mr-1"
            v-if="comment.user.id === login_user && updateTrigger === false"
            @click="updatePostForm(comment)">
            댓글 수정
          </button>

          <button
            class="btn btn-secondary font-jua mr-1"
            v-if="is_admin && updateTrigger === false"
            @click="deleteComment(comment)">
            댓글 삭제
          </button>

          <button
            class="btn btn-secondary font-jua mr-1"
            v-else-if="comment.user.id === login_user && updateTrigger === false"
            @click="deleteComment(comment)">
            댓글 삭제
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
import axios from 'axios';
import UpdateForm from '@/components/comment/UpdateForm';

import { mapState } from 'vuex';

export default {
  name: 'CommentList',
  components: {
    UpdateForm,
  },
  data: function () {
    return {
      updateTrigger: false,
      updateCommentItem: '',
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

    deleteComment: function (comment) {
      const config = this.setToken();
      axios
        .delete(`${SERVER_URL}/community/${this.post.id}/comment/${comment.id}/`, config)
        .then((res) => {
          const targetCommentIdx = this.comments.findIndex((comment) => {
            return comment.id === res.data.id;
          });
          this.$store.state.comments.splice(targetCommentIdx, 1);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    updatePostForm: function (comment) {
      this.updateTrigger = comment.id;
      this.updateCommentItem = comment;
    },
    changeTrigger: function () {
      this.updateTrigger = false;
    },
  },
  created: function () {
    // if (login) {
    //   this.username = this.$store.state.username
    //   this.login = this.$store.state.login
    // }
  },
  computed: {
    ...mapState(['login', 'login_user', 'username', 'is_admin', 'comments']),
  },
};
</script>

<style scoped>
div > p {
  display: inline;
  margin: 10px 5px;
}
</style>
