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
      <p><strong>팔로워:</strong> {{ followersCount }}</p>
      <div v-if="!isCurrentUser">
        <button v-if="!isCurrentUser" @click="toggleFollow" class="btn btn-primary">
          {{ isFollowing ? '언팔로우' : '팔로우' }}
        </button>
      </div>

      <div>
        <h2>작성한 리뷰</h2>
        <ul>
          <li v-for="review in reviews" :key="review.id">
            <p><strong>영화:</strong> {{ review.movie.title }}</p>
            <p><strong>평점:</strong> {{ review.rate }}</p>
            <p><strong>내용:</strong> {{ review.content }}</p>
          </li>
        </ul>
      </div>

      <div>
        <h2>작성한 게시글</h2>
        <ul>
          <li v-for="post in posts" :key="post.id">
            <p><strong>제목:</strong> {{ post.title }}</p>
            <p><strong>내용:</strong> {{ post.content }}</p>
          </li>
        </ul>
      </div>

      <div>
        <h2>작성한 댓글</h2>
        <ul>
          <li v-for="comment in comments" :key="comment.id">
            <p><strong>내용:</strong> {{ comment.content }}</p>
          </li>
        </ul>
      </div>
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
      reviews: [], // 리뷰
      posts: [], // 게시글
      comments: [], // 댓글
      followersCount: 0, // 팔로워 수
      isFollowing: false,
      isCurrentUser: false,
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
    formatDate(date) {
      return this.$moment(date).format('YYYY-MM-DD');
    },
    toggleFollow() {
      const username = this.$route.params.username;
      const config = this.setToken();

      if (this.isFollowing) {
        axios
          .post(`${SERVER_URL}/accounts/profile/${username}/unfollow/`, {}, config)
          .then((res) => {
            this.isFollowing = false;
            this.followersCount--; // 팔로워 수 감소
            alert('언팔로우되었습니다.'); // 알림 표시
          })
          .catch((err) => {
            console.log(err);
          });
      } else {
        axios
          .post(`${SERVER_URL}/accounts/profile/${username}/follow/`, {}, config)
          .then((res) => {
            this.isFollowing = true;
            this.followersCount++; // 팔로워 수 증가
            alert('팔로우되었습니다.'); // 알림 표시
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
  },
  created() {
    const currentusername = localStorage.getItem('username');
    const username = this.$route.params.username;
    axios
      .get(`${SERVER_URL}/accounts/profile/${username}/`)
      .then((res) => {
        this.profile = res.data;
        this.followersCount = this.profile.followers_count; // 팔로워 수 설정
        this.isCurrentUser = this.profile.username === currentusername;
        console.log(this.isCurrentUser);
      })
      .catch((err) => {
        console.log(err);
      });

    // 추가된 부분: 팔로워 수 가져오기
    axios
      .get(`${SERVER_URL}/accounts/profile/${username}/followers/`)
      .then((res) => {
        this.followersCount = res.data.length; // 팔로워 수 설정
      })
      .catch((err) => {
        console.log(err);
      });

    axios
      .get(`${SERVER_URL}/movies/${username}/reviews/`)
      .then((res) => {
        this.reviews = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
    axios
      .get(`${SERVER_URL}/community/${username}/posts/`)
      .then((res) => {
        this.posts = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
    axios
      .get(`${SERVER_URL}/community/${username}/comments/`)
      .then((res) => {
        this.comments = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>
