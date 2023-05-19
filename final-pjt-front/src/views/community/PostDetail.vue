<template>
  <div>
    <div class="container">
      <div class="row">
        <h1 class="font-do my-5">글 상세보기</h1>
      </div>
      <!-- <img :src="require(`@/assets/images/stooges/${item.img}.jpg`)" /> -->
      <div class="row d-flex font-poor">
        <div class="media" style="width: 100%; word-break: break-all">
          <img :src="images.logo" width="50" class="mr-3" alt="..." />
          <div class="media-body text-justify">
            <h2 class="mt-0">{{ post.title }}</h2>
            <p class="font-1-5em font-lightgray">
              작성자:
              <router-link :to="{ name: 'Profile', params: { username: postUsername } }">{{
                postUsername
              }}</router-link>
            </p>
            <p>
              작성: {{ $moment(post.created_at).format('YYYY-MM-DD hh:mm:ss') }} | 최근수정:
              {{ $moment(post.updated_at).format('YYYY-MM-DD hh:mm:ss') }}
            </p>
            <p class="font-2em">
              {{ post.content }}
            </p>
            <hr :style="{ margin: '5px 30px' }" />
            <hr :style="{ margin: '5px 30px' }" />
            <div class="d-flex justify-content-end">
              <!--작성자와 접속자가 같다면, 수정/삭제 버튼 활성화-->
              <!--단, 관리자의 경우 삭제 버튼 활성화 -->
              <button @click="toggleLikePost" class="btn btn-primary">좋아요</button>
              <p>좋아요: {{ likesCount }}</p>
              <button
                class="btn btn-warning font-do mr-3 font-1-2em"
                v-if="postUsername === this.$store.state.username"
                @click="updatePostForm(post)"
              >
                글 수정
              </button>

              <button
                class="btn btn-danger font-do mr-3 font-1-2em"
                v-if="this.$store.state.is_admin"
                @click="deletePost(post)"
              >
                글 삭제
              </button>
              <button
                v-else-if="postUsername === this.$store.state.username"
                @click="deletePost(post)"
                class="btn btn-danger font-do mr-3 font-1-2em"
              >
                글 삭제
              </button>
            </div>
            <hr />
            <hr />
            <div>
              <button @click="backToPost" class="btn btn-pink">목록으로 가기</button>
            </div>
            <div class="mt-5">
              <CommentForm v-if="this.$store.state.login" :post="post" />
              <p v-else>댓글을 작성하려면 로그인이 필요합니다.</p>
            </div>

            <br />

            <hr :style="{ margin: '5px 30px' }" />
            <CommentList :post="post" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
import axios from 'axios';

import CommentList from '@/components/comment/CommentList';
import CommentForm from '@/components/comment/CommentForm';

export default {
  name: 'PostDetail',
  components: {
    CommentList,
    CommentForm,
  },
  data() {
    return {
      post: '',
      postUsername: '',
      postItem: '',
      all_comments: '',
      images: {
        logo: require('@/assets/images/logo.png'),
        flamingo: require('@/assets/images/flamingo.png'),
      },
      isPostLiked: false,
      likesCount: 0,
    };
  },
  methods: {
    setToken() {
      const token = localStorage.getItem('jwt');

      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        },
      };
      return config;
    },
    backToPost() {
      this.$router.push({
        name: 'Post',
      });
    },
    deletePost(post) {
      const config = this.setToken();
      axios
        .delete(`${SERVER_URL}/community/post_delete_update/${post.id}/`, config)
        .then(() => {
          this.$router.push({
            name: 'Post',
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    updatePostForm(post) {
      const postItem = {
        id: post.id,
        purpose: 'update',
        title: post.title,
        content: post.content,
      };
      this.$router.push({
        name: 'CreatePost',
        params: postItem,
      });
    },
    getAllComment() {
      axios
        .get(`${SERVER_URL}/community/${this.postItem}/comments/`)
        .then((res) => {
          if (res.data) {
            this.$store.state.comments = res.data;
            this.all_comments = this.$store.state.comments;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    toggleLikePost() {
      const config = this.setToken();
      axios
        .post(`${SERVER_URL}/community/posts/${this.post.id}/like/`, {}, config)
        .then((res) => {
          this.isPostLiked = res.data.liked;
          this.likesCount = res.data.likes_count;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getLikesCount() {
      const config = this.setToken();
      axios
        .get(`${SERVER_URL}/community/posts/${this.post.id}/like/`, config)
        .then((res) => {
          this.likesCount = res.data.likes_count;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    this.postItem = this.$route.params.id;
    axios
      .get(`${SERVER_URL}/community/${this.postItem}/`)
      .then((res) => {
        this.post = res.data;
        this.postUsername = this.post.user.username;
        this.getLikesCount();
      })
      .catch((err) => {
        console.log(err);
      });

    this.getAllComment();
  },
  mounted() {
    window.scrollTo(0, 0);
  },
};
</script>

<style scoped></style>
