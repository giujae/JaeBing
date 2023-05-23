<template>
<<<<<<< HEAD
  <div class="profile-container">


    <!-- 프로필 카드 -->
    <div class="profile-card">
      <strong><h1 class="my-4 text-left">프로필</h1></strong>
      <div v-if="profile">
        <h2 class="text-left my-3">
          <span class="username pr-2 pl-0">{{ profile.username }}</span>
          <span class="follower">Follower: {{ followersCount }}</span> 
          <span class="grade">Grade: {{ isAdmin ? "관리자" : "일반회원" }}</span>
        </h2>
        <!-- <p class="text-left">
          <strong>가입일:</strong> {{ formatDate(profile.date_joined) }}
        </p> -->
        <p class="text-left p-auto my-1">
          <strong>생일:</strong> {{ profile.date_of_birth }}
        </p>
        <p class="text-left"><strong>이메일:</strong> {{ profile.email }}</p>
      </div>
    </div>
    <!-- 프로필 카드 끝 -->
=======
  <div class="container">
    <strong><h1 class="font-do my-3 text-left">프로필</h1></strong>
    <div v-if="profile">
      <h2 class="text-left">아이디: {{ profile.username }}</h2>
      <p class="text-left"><strong>팔로워:</strong> {{ followersCount }}</p>
      <p class="text-left"><strong>가입일:</strong> {{ formatDate(profile.date_joined) }}</p>
      <p class="text-left"><strong>생일:</strong> {{ profile.date_of_birth }}</p>
      <p class="text-left"><strong>이메일:</strong> {{ profile.email }}</p>
      <p class="text-left"><strong>등급:</strong> {{ isAdmin ? '관리자' : '일반회원' }}</p>
    </div>
>>>>>>> 9ecbb50d16aef7338244768d01cffa6f16c2cad6

    <div v-if="profile">
      <!-- <p><strong>회원코드:</strong> {{ profile.id }}</p> -->

      <div v-if="!isCurrentUser">
        <button
          v-if="!isCurrentUser"
          @click="toggleFollow"
          class="btn btn-primary"
        >
          {{ isFollowing ? "언팔로우" : "팔로우" }}
        </button>
      </div>

<<<<<<< HEAD
      <!-- 전체적인 작성한 디브 -->
      <div class="created-div">
      <!-- 버튼 넣을 div 박스 -->
      <div class="btn-div">
        <!-- 게시글 -->
        <button class="created-btn" @click="selectedTab = 'posts'">
          작성한 게시글
        </button>

        <!-- 리뷰 -->
        <button class="created-btn" @click="selectedTab = 'reviews'">
          작성한 리뷰
        </button>

        <!-- 댓글 -->
        <button class="created-btn" @click="selectedTab = 'comments'">
          작성한 댓글
        </button>
      </div>

      <!-- 작성한 게시글 테이블 -->
      <table
        class="created-table table table-hover"
        v-if="selectedTab === 'posts'"
      >
=======
      <!-- 버튼 넣을 div 박스 -->
      <div class="btn-div">
        <!-- 게시글 -->
        <button class="created-article" @click="selectedTab = 'posts'">작성한 게시글</button>

        <!-- 리뷰 -->
        <button class="created-review" @click="selectedTab = 'reviews'">작성한 리뷰</button>
        <!-- <ul>
          <li v-for="review in reviews" :key="review.id">
            <p><strong>영화:</strong> {{ review.movie.title }}</p>
            <p><strong>평점:</strong> {{ review.rate }}</p>
            <p><strong>내용:</strong> {{ review.content }}</p>
          </li>
        </ul> -->

        <!-- 댓글 -->
        <button class="created-comment" @click="selectedTab = 'comments'">작성한 댓글</button>
        <!-- <ul>
          <li v-for="comment in comments" :key="comment.id">
            <p><strong>내용:</strong> {{ comment.content }}</p>
          </li>
        </ul> -->
      </div>

      <table class="table table-hover" v-if="selectedTab === 'posts'">
>>>>>>> 9ecbb50d16aef7338244768d01cffa6f16c2cad6
        <tr>
          <th>No.</th>
          <th>TITLE</th>
          <th>CONTENT</th>
          <th>DATE</th>
        </tr>
        <tr v-for="(post, idx) in posts" :key="idx">
          <th>{{ post.id }}</th>
          <th>{{ post.title }}</th>
          <th>{{ post.content }}</th>
<<<<<<< HEAD
          <th>{{ $moment(post.created_at).format("YYYY-MM-DD hh:mm:ss") }}</th>
        </tr>
      </table>

      <!-- 작성한 리뷰 테이블 -->
      <table class="created-table table table-hover" v-if="selectedTab === 'reviews'">
        <tr>
          <th>No.</th>
          <th>MOIVE</th>
          <th>RATE</th>
          <th>CONTENT</th>
          <th>DATE</th>
        </tr>
        
        
        <tr v-for="review in reviews" :key="review.id">
          <th>{{ review.id }}</th>
          <th>{{ review.movie.title }}</th>
          <th>{{ review.rate }}</th>
          <th>{{ review.content }}</th>
          <th>
            {{ $moment(review.created_at).format("YYYY-MM-DD hh:mm:ss") }}
          </th>
        </tr>
      </table>

      <!-- 작성한 댓글 테이블 -->
      <table class="created-table table table-hover" v-if="selectedTab === 'comments'">
        <tr>
          <th>No.</th>
          <th>POST NO.</th>
          <th>CONTENT</th>
          <th>DATE</th>
        </tr>
        <tr v-for="comment in comments" :key="comment.id">
          <th>{{ comment.id }}</th>
          <th>{{ comment.post }}</th>
          <th>{{ comment.content }}</th>
          <th>
            {{ $moment(comment.created_at).format("YYYY-MM-DD hh:mm:ss") }}
          </th>
        </tr>
      </table>
=======
          <th>{{ $moment(post.created_at).format('YYYY-MM-DD hh:mm:ss') }}</th>
        </tr>
      </table>
      <table class="table table-hover" v-if="selectedTab === 'reviews'">
        <tr>
          <th>No.</th>
          <th>MOIVE</th>
          <th>RATE</th>
          <th>CONTENT</th>
          <th>DATE</th>
        </tr>
        <tr v-for="review in reviews" :key="review.id">
          <th>{{ review.id }}</th>
          <th>{{ review.movie.title }}</th>
          <th>{{ review.rate }}</th>
          <th>{{ review.content }}</th>
          <th>{{ $moment(review.created_at).format('YYYY-MM-DD hh:mm:ss') }}</th>
        </tr>
      </table>
      <table class="table table-hover" v-if="selectedTab === 'comments'">
        <tr>
          <th>No.</th>
          <th>POST NO.</th>
          <th>CONTENT</th>
          <th>DATE</th>
        </tr>
        <tr v-for="comment in comments" :key="comment.id">
          <th>{{ comment.id }}</th>
          <th>{{ comment.post }}</th>
          <th>{{ comment.content }}</th>
          <th>{{ $moment(comment.created_at).format('YYYY-MM-DD hh:mm:ss') }}</th>
        </tr>
      </table>
>>>>>>> 9ecbb50d16aef7338244768d01cffa6f16c2cad6
    </div>
  </div>

    <p v-else>Loading...</p>
  </div>
</template>

<script>
import axios from "axios";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: "Profile",
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
<<<<<<< HEAD
      selectedTab: "posts",
=======
      selectedTab: 'posts',
>>>>>>> 9ecbb50d16aef7338244768d01cffa6f16c2cad6
    };
  },
  methods: {
    setToken() {
      const token = localStorage.getItem("jwt");

      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        },
      };
      return config;
    },
    formatDate(date) {
      return this.$moment(date).format("YYYY-MM-DD");
    },
    toggleFollow() {
      const username = this.$route.params.username;
      const config = this.setToken();

      if (this.isFollowing) {
        axios
          .post(
            `${SERVER_URL}/accounts/profile/${username}/unfollow/`,
            {},
            config
          )
          .then((res) => {
            this.isFollowing = false;
            this.followersCount--; // 팔로워 수 감소
            alert("언팔로우되었습니다."); // 알림 표시
          })
          .catch((err) => {
            console.log(err);
          });
      } else {
        axios
          .post(
            `${SERVER_URL}/accounts/profile/${username}/follow/`,
            {},
            config
          )
          .then((res) => {
            this.isFollowing = true;
            this.followersCount++; // 팔로워 수 증가
            alert("팔로우되었습니다."); // 알림 표시
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
  },
  created() {
    const currentusername = localStorage.getItem("username");
    const username = this.$route.params.username;
    axios
      .get(`${SERVER_URL}/accounts/profile/${username}/`)
      .then((res) => {
        this.profile = res.data;
        this.followersCount = this.profile.followers_count; // 팔로워 수 설정
        this.isCurrentUser = this.profile.username === currentusername;
        // console.log(this.isCurrentUser);
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
        console.log(this.comments);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style>
/* 전체적인 프로필 디브 */
.profile-container {
  color: #e8d1d9;
  min-height: 100vh;
  width: 100%;
  padding: 0 10%;
  background-image: linear-gradient(
      to top,
      rgba(20, 20, 20, 0.25) 10%,
      rgba(20, 20, 20, 0.5) 25%,
      rgba(20, 20, 20, 0.5) 50%,
      rgba(20, 20, 20, 0.75) 75%,
      rgba(20, 20, 20, 1) 100%
    ),
    url('https://png.pngtree.com/thumb_back/fh260/background/20221111/pngtree-nobody-interface-of-pixel-game-platform-image_1456637.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  backdrop-filter: blur(20px);
  color: #e8d1d9;
}

/* 작성한~ 버튼 디브 */
.btn-div {
  display: flex;
  justify-content: flex-start;
  /* margin-top: 20px; */
}

<<<<<<< HEAD
/* 작성한 게시글 */
.created-btn {
=======
.created-article {
>>>>>>> 9ecbb50d16aef7338244768d01cffa6f16c2cad6
  width: auto;
  padding-left: 0px;
}

<<<<<<< HEAD
/* 버튼 클릭시 테두리 삭제 */
.created-btn:focus {
  outline: none;
}

/* 작성한~ 테이블 속성 */
.created-table {
  
  font-family: "NeoDunggeunmo";
=======
.created-review {
  width: auto;
}

.created-comment {
  width: auto;
}

table {
  font-family: 'NeoDunggeunmo';
>>>>>>> 9ecbb50d16aef7338244768d01cffa6f16c2cad6
  font-size: 20px;
  color: #e8d1d9 !important;
  border-style: dashed;
  /* border-color: #4c4d81b2; */
  border-color: #e8d1d969;
<<<<<<< HEAD
  background-color: #101130d1;
  /* margin: 2px; */
}

.created-div{
  padding: 0px 20px 20px 20px;;
}

/* 프로필 카드 */
.profile-card {
  /* background-color: #101130; */
  color: white;
  padding: 20px;
}

/* 팔로워 속성 */
.follower {
  font-size: 16px;
}

/* 회원 등급 속성 */
.grade {
  font-size: 16px;
}

/* 유저 이름 속성 */
.username {
  padding-right: 8px;
  padding-left: 4px;
  margin: auto;
  font-size: 40px;
}

/* 테이블 요소 속성 */
th {
  padding: 2px !important;
}

=======
}
>>>>>>> 9ecbb50d16aef7338244768d01cffa6f16c2cad6
</style>
