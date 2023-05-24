<template>
  <div class="post-detail-div">
    <div class="create-post-container my-5">
      <div class="htag mt-5">
        <h1 v-if="this.purpose == 'create'" class="my-4">글 작성하기</h1>
        <h1 v-else-if="this.purpose == 'update'" class="my-3">글 수정하기</h1>
      </div>  
      
      <div class="row justify-content-center">
        <form v-if="this.purpose == 'create'" v-on:submit.prevent="createPostForm">
          <div class="post-form-group my-4">
            <label for="title">Title: </label>
            <div>
              <input type="text" class="form-control create-form-control" id="title" v-model.trim="title" />
            </div>
          </div>

          <div class="post-form-group my-3">
            <label for="content">Content: </label>
              <textarea class="form-control create-form-control" id="content" v-model="content"></textarea>
          </div>
          <button class="submit-btn" type="submit">등록하기</button>
        </form>

        <form v-if="this.purpose == 'update'" v-on:submit.prevent="updatePost">
          <div>
            <label for="title">Title: </label>
            <input type="text" id="title" v-model.trim="title" />
          </div>
          <div>
            <label for="content">Content: </label>
            <input type="text" id="content" v-model="content" />
          </div>
          <button type="submit-btn">등록하기</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
import axios from 'axios';

export default {
  name: 'CreatePost',
  data: function () {
    return {
      posts: [],
      title: '',
      content: '',
      purpose: '',
      updateId: '',
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
    createPostForm: function () {
      const config = this.setToken();

      const postItem = {
        title: this.title,
        content: this.content,
      };
      axios
        .post(`${SERVER_URL}/community/post_create/`, postItem, config)
        .then((res) => {
          //console.log(res)
          this.$router.push({
            name: 'PostDetail',
            params: {
              id: res.data.id,
            },
          });
        })
        .catch((err) => {
          console.log(err);
          alert('잘못된 정보를 입력했습니다.');
        });
    },
    updatePost: function () {
      const config = this.setToken();

      const postItem = {
        title: this.title,
        content: this.content,
        post_code: 1,
      };
      axios
        .put(`${SERVER_URL}/community/post_delete_update/${this.updateId}/`, postItem, config)
        .then((res) => {
          this.$router.push({
            name: 'PostDetail',
            params: {
              id: res.data.id,
            },
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created: function () {
    this.purpose = this.$route.params.purpose;
    this.updateId = this.$route.params.id;
    this.title = this.$route.params.title;
    this.content = this.$route.params.content;
  },
  mounted() {
    window.scrollTo(0, 0);
  },
};
</script>

<style>
.create-post-container{
  width: 100%;
  min-height: 70vh;
  color:#e8d1d9;
  font-size: 20px;
}

.submit-btn {
  width: 100%;
}

.create-form-control{
  /* background-color: #e8d1d986 !important; */
}

</style>
