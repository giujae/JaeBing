<template>
  <div>
      <!-- <b-card
        v-if="!movie.poster_path.includes('#')"
        :img-src="`https://image.tmdb.org/t/p/w185${movie.poster_path}`"
        img-alt="Image"
<<<<<<< HEAD
        class="card-img my-2"
        @click="showDetail"></b-card> -->
<!-- 
=======
        img-top
        tag="article"
        class="my-2"
        style="max-width: 25rem; max-height: 20rem; min-height: 20rem"
        @click="showDetail"
      >
        <!-- <b-card-text>개봉일 : {{movie.release_date}}</b-card-text> -->
        <b-card-text class="font-1-8em font-do" :style="{ 'max-width': '20rem' }">
          💕 : {{ movie.vote_count }}
        </b-card-text>
        <!-- <b-button href="#" variant="primary">Go somewhere</b-button> -->
      </b-card>

>>>>>>> f79f0d8acd63af4b8a2e9f9b55b30d5e0a01181f
      <b-card
        v-else
        img-src="https://image.tmdb.org/t/p/w185/g3gpHLUuQLGI9gRmfraSQCN1TYk.jpg"
        img-alt="Image"
        img-top
        class="my-2"
        @click="showDetail">
      </b-card> -->

      <div>

        <div class="cards" v-if="!movie.poster_path.includes('#')">
          <figure>
            <img class="movielistitem m-0" :src="`https://image.tmdb.org/t/p/w185${movie.poster_path}`"
            @click="showDetail" >
          </figure>
        </div>

        <div class="cards" v-else>
          <figure>
            <img class="movielistitem" src="https://image.tmdb.org/t/p/w185/g3gpHLUuQLGI9gRmfraSQCN1TYk.jpg"
            @click="showDetail">
          </figure>
        </div>

      </div>


    <!-- 영화눌렀을때 이게 보이게 한다 -->
    <b-modal
      class="font-do"
      hide-footer
      v-model="show"
      size="xl"
      title="Movie information"
      footer-bg-variant="dark"
      footer-text-variant="dark"
    >
      <div class="modal-content" style="background-color: black">
        <!-- ... -->
      </div>
      <!-- 영화디테일 부분 -->
      <div class="detail-box">
        <div
          class="modal-backdrop"
          :style="`background-image: url(https://image.tmdb.org/t/p/original${movie.backdrop_path})`"
        ></div>

        <div class="detail-content">
          <div class="trailer">
            <!-- <youtube :video-id="trailerVideoId" :player-vars="playerVars" @playing="handlePlaying"></youtube> -->
            <iframe
              id="player"
              type="text/html"
              width="400"
              height="250"
              :src="`http://www.youtube.com/embed/${trailerVideoId}?autoplay=1&mute=1`"
              frameborder="0"
            ></iframe>
          </div>

          <!-- Poster -->
          <div class="poster">
            <img
              :src="`https://image.tmdb.org/t/p/w185${movie.poster_path}`"
              alt="movie poster"
              v-if="!movie.poster_path.includes('#')"
            />
            <img src="https://image.tmdb.org/t/p/w185/g3gpHLUuQLGI9gRmfraSQCN1TYk.jpg" alt="movie poster" v-else />
          </div>

          <div class="details text-right">
            <!-- Title -->
            <h2 class="font-do">{{ movie.title }}</h2>

            <!-- Release Date -->
            <h5 class="font-do">{{ movie.release_date }}</h5>

            <!-- Adult Rating -->
            <h5 class="font-do" v-if="movie.adult">19세 관람가</h5>

            <br />

            <!-- Overview -->
            <h4 class="font-poor">줄거리: {{ movie.overview | truncate(100, '...') }}</h4>

            <!-- Vote Average -->
            <h4 class="font-poor">평점: {{ movie.vote_average }}</h4>
          </div>
        </div>
      </div>
      <br />

      <!-- 리뷰부분 -->
      <div v-if="is_admin === false && login === true" :class="{ appear: showForm }">
        <h2 class="font-do">리뷰 작성하기</h2>
        <div id="reviewForm">
          <!-- 리뷰 작성 폼 내용 -->
          <div>
            <label for="rate" class="float-left font-jua font-1-5em">별점</label>
            <p class="float-left font-jua font-1-5em mr-3">: {{ selected_rate }}점</p>
            <input type="range" min="1" max="10" step="1" v-model="selected_rate" class="mt-2 justify-content-center" />
            <select id="rate" v-model="selected_rate" class="ml-1">
              <option v-for="(n, idx) in rate_options" :key="idx">{{ n }}</option>
            </select>

            <b-input-group>
              <b-input-group-prepend>
                <b-button @click="selected_rate = null">Clear</b-button>
              </b-input-group-prepend>
              <b-form-rating size="lg" id="rate" v-model="selected_rate" color="#DE5078" stars="10"></b-form-rating>
              <b-input-group-append>
                <b-input-group-text class="justify-content-center" style="min-width: 3em">
                  {{ selected_rate }}
                </b-input-group-text>
              </b-input-group-append>
            </b-input-group>
          </div>
          <div class="mt-3">
            <label for="like" class="mr-2 font-jua font-1-5em mr-1">이 영화를</label>
            <label for="like" class="font-jua font-1-5em mr-2" id="recommend-label">추천합니다.</label>
            <b-form-checkbox size="lg" id="like" checked="true" v-model="like" inline></b-form-checkbox>
          </div>

          <div class="input-group">
            <label for="content"></label>
            <textarea
              class="form-control my-3 font-poor"
              aria-label="With textarea"
              id="content"
              cols="60"
              rows="5"
              v-model.trim="content"
              placeholder="감상평을 남겨주세요."
            ></textarea>
          </div>

          <div>
            <div class="d-flex justify-content-center">
              <button @click="hideDetail" :class="{ appear: showAdd }" class="btn btn-secondary font-jua mr-1 ml-1">
                취소
              </button>
              <button :class="{ appear: showAdd }" class="btn btn-pink mr-1 ml-1" @click="addReview(movie)">
                확인
              </button>
              <button
                :class="{ appear: !showAdd }"
                class="btn btn-pink font-jua mr-1 ml-1"
                @click="updateReview(movie)"
              >
                수정
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- 리뷰목록 -->

      <h2 class="font-do">리뷰 목록</h2>
      <hr />
      <ul>
        <li v-for="(review, idx) in reviews" :key="idx">
          <div v-if="review.movie.id == movie.id || review.id == movie.id">
            <div class="row review-dottedline mt-5">
              <div class="col-3" id="review-rank">
                <!-- 리뷰 별점 부분 -->
                <div>
                  <b-form-rating color="#DE5078" inline size="sm" :value="review.rate | half()" readonly no-border>
                  </b-form-rating>
                </div>
              </div>

              <div class="col-6" id="review-content" style="word-break: break-all">
                <!-- 리뷰 내용 부분 -->
                <p>{{ review.content }}</p>
                <p>작성자 : {{ review.user.username }} | {{ $moment(review.created_at).format('YYYY-MM-DD') }}</p>
              </div>

              <div class="col-3" id="review-button" v-if="review.user.id == login_user">
                <!-- 리뷰 수정, 삭제 버튼 -->
                <button @click="updateReady(review)" :class="{ appear: showAdd }" class="btn btn-pink mr-1 ml-1">
                  수정
                </button>
                <button @click="deleteReview(movie)" :class="{ appear: showAdd }" class="btn btn-delete mr-1 ml-1">
                  삭제
                </button>
              </div>
            </div>
          </div>
        </li>
      </ul>
    </b-modal>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
import Vue from 'vue';
import VueYoutube from 'vue-youtube';
import axios from 'axios';
import _ from 'lodash';
import { mapState } from 'vuex';
Vue.use(VueYoutube);

export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  },
  components: {
    'vue-youtube': VueYoutube,
  },
  data: function () {
    return {
      selected_rate: null,
      like: false,
      content: null,
      show: false,
      showForm: false,
      showAdd: false,
      reviewId: null,
      rate_options: _.range(0, 11),
      variants: ['light', 'dark'],
      showTrailer: false,
      trailerVideoId: '',
      playerVars: {
        autoplay: 1,
        controls: 1,
      },
      reviews: [],
    };
  },
  methods: {
    showDetail: function () {
      // console.log('얘두');
      // console.log(this.review_list);
      this.show = true;
      const API_Key = 'AIzaSyDLytfpo-su6xYpTZ8OgrfNf941SBQzBiY';
      const movieTitle = this.movie.title;
      const query = '공식예고편 ' + movieTitle;
      this.avgRate = this.movie.rate;

      const apiUrl = `https://www.googleapis.com/youtube/v3/search?key=${API_Key}&q=${query}&part=snippet&type=video`;
      axios
        .get(`${SERVER_URL}/movies/${this.movie.id}/reviews/`)
        .then((res) => {
          // console.log(res.data, 'data');
          this.reviews = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
      axios
        .get(apiUrl)
        .then((response) => {
          const videos = response.data;
          console.log(response.request.status);
          if (response.request.status === 200) {
            // 필터링된 예고편 영상 가져오기
            this.trailerVideoId = videos.items[0].id.videoId;
            console.log(this.trailerVideoId);
          } else {
            console.log('예고편이 없습니다.');
          }
        })
        .catch((error) => {
          console.error('API 요청 중 오류 발생:', error);
        });
    },

    handlePlaying() {
      console.log('Video is playing');
    },
    hideDetail: function () {
      this.show = false;
    },
    setToken: function () {
      const token = localStorage.getItem('jwt');

      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        },
      };
      return config;
    },
    addReview: function (movie) {
      const config = this.setToken();
      const reviewInfo = {
        content: this.content,
        rate: this.selected_rate,
        like: this.like,
      };
      axios
        .post(`${SERVER_URL}/movies/${movie.id}/review/`, reviewInfo, config)
        .then((res) => {
          // console.log(res.data)
          const reviewerInfo = {
            movie_id: this.movie.id,
            reviewer_id: res.data.user.id,
          };
          this.$store.state.review_list.unshift(res.data);
          let acount = 0;
          for (const review of this.review_list) {
            if (review.movie.id == this.movie.id) {
              acount++;
            }
          }
          console.log('리뷰수:', acount);
          this.total[this.movie.id] += this.selected_rate;
          console.log('총점수:', this.total[this.movie.id]);
          this.$store.state.movie_list[this.movie.id - 1].rate = this.total[this.movie.id] / acount;
          console.log('평균:', this.$store.state.movie_list[this.movie.id - 1].rate);
          if (this.like) {
            this.$store.state.movie_list[this.movie.id - 1].vote_count += 1;
          }
          this.$store.dispatch('checkReviewer', reviewerInfo);
          this.$store.dispatch('recommendMovie');
          this.content = null;
          this.selected_rate = null;
          this.like = false;
          this.showForm = true;
          this.showDetail();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    deleteReview: function (movie) {
      const config = this.setToken();
      if (confirm('이 리뷰를 삭제하겠습니까?')) {
        axios
          .delete(`${SERVER_URL}/movies/${movie.id}/review/update/`, config)
          .then((res) => {
            console.log(res);
            const idx1 = this.review_list.findIndex((review) => {
              return review.id === movie.id;
            });
            this.$store.state.review_list.splice(idx1, 1);
            let dcount = 0;
            for (const review of this.review_list) {
              if (review.movie.id === this.movie.id) {
                dcount++;
              }
            }
            if (dcount <= 0) {
              dcount = 1;
            }
            console.log('리뷰수:', dcount);

            const idx2 = this.user_movie[this.login_user].findIndex((user) => {
              return user.id === movie.id;
            });
            this.$store.state.user_movie[this.login_user].splice(idx2, 1);

            this.total[this.movie.id] -= res.data.rate;
            console.log('총점수:', this.total[this.movie.id]);

            this.$store.state.movie_list[this.movie.id - 1].rate = this.total[this.movie.id] / dcount;
            console.log('평균', this.$store.state.movie_list[this.movie.id - 1].rate);

            if (res.data.like) {
              this.$store.state.movie_list[this.movie.id - 1].vote_count -= 1;
            }

            this.showForm = false;
            this.showAdd = false;
            this.showDetail();
          })
          .catch((err) => {
            console.log(err);
          });
        axios
          .get(`${SERVER_URL}/movies/${this.movie.id}/reviews/`)
          .then((res) => {
            // console.log(res.data, 'data');
            this.reviews = res.data;
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
    updateReady: function (review) {
      this.content = review.content;
      this.like = review.like;
      this.selected_rate = review.rate;
      this.showForm = false;
      this.showAdd = true;
      this.reviewId = review.id;
    },

    updateReview: function (movie) {
      const config = this.setToken();
      const reviewInfo = {
        id: this.reviewId,
        user: this.login_user,
        movie: movie.id,
        content: this.content,
        rate: this.selected_rate,
        like: this.like,
      };
      axios
        .put(`${SERVER_URL}/movies/${movie.id}/review/update/`, reviewInfo, config)
        .then((res) => {
          this.content = null;
          this.like = false;
          this.selected_rate = null;
          this.showForm = true;
          this.showAdd = false;
          this.reviewId = null;
          console.log(res);
          const idx = this.review_list.findIndex((review) => {
            return review.id === res.data.id;
          });
          this.total[this.movie.id] -= this.$store.state.review_list[idx].rate;
          this.$store.state.review_list[idx].content = res.data.content;
          this.$store.state.review_list[idx].rate = res.data.rate;

          if (this.$store.state.review_list[idx].like) {
            if (res.data.like === false) {
              this.$store.state.movie_list[this.movie.id - 1].vote_count -= 1;
            }
          } else {
            if (res.data.like === true) {
              this.$store.state.movie_list[this.movie.id - 1].vote_count += 1;
            }
          }

          this.$store.state.review_list[idx].like = res.data.like;

          let ucount = 0;
          for (const review of this.review_list) {
            if (review.movie.id === this.movie.id) {
              ucount++;
            }
          }
          console.log('리뷰수:', ucount);

          this.total[this.movie.id] += res.data.rate;
          console.log('총점수:', this.total[this.movie.id]);

          this.$store.state.movie_list[this.movie.id - 1].rate = this.total[this.movie.id] / ucount;
          console.log('평균', this.$store.state.movie_list[this.movie.id - 1].rate);
          this.showDetail();
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created: function () {
    if (this.user_movie[this.login_user] && this.user_movie[this.login_user].includes(this.movie.id)) {
      this.showForm = true;
    }
    this.avgRate = this.movie.rate;
  },
  computed: {
    ...mapState(['login', 'login_user', 'is_admin', 'user_movie', 'movie_list', 'review_list', 'total']),
  },
};
</script>

<style scoped>
.card-img {
  height: auto !important;
}

.appear {
  display: none;
}

.detail-box {
  position: relative;
  height: 500px;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

.detail-content {
  /* position: relative;
  z-index: 1;
  display: flex;
  height: 100%; */
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  transform: translateY(-50%);
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  z-index: 2;
}
.modal-content {
  background-color: #826592 !important;
}
.modal-backdrop {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  z-index: 0 !important;
  filter: blur(3px);
}

.poster {
  flex: 0 0 300px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 20px;
}

.poster img {
  width: 100%;
  height: 120%;
  border-radius: 4px;
}

.details {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-self: flex-end;
  position: absolute;
}

.modal-xl {
  max-width: 1000px;
}
/* .trailer-container {
  position: relative;
  padding-bottom: 56.25%;
  overflow: hidden;
  max-width: 100%;
  flex-grow: 1;
}
.trailer-container embed {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
} */

.appear {
  display: none;
}

.review-dottedline {
  border-bottom: 2px dotted gainsboro;
}

.btn-delete {
  background-color: gray;
  border: 1px dotted gainsboro;
  color: honeydew;
  font-family: Jua;
}

.btn-pink {
  font-family: Jua;
  background-color: #de5078;
  color: aliceblue;
}

.font-jua {
  font-family: 'Jua';
}

.font-do {
  font-family: 'Do Hyeon';
}

.font-poor {
  font-family: 'Poor Story';
}

.font-1em {
  font-size: 1em;
}

.font-2em {
  font-size: 2em;
}

.font-1-2em {
  font-size: 1.2em;
}

.font-1-5em {
  font-size: 1.5em;
}

.font-1-8em {
  font-size: 1.8em;
}

.card {
  background-color: #826592 !important;
  border: none !important;
}

.img-top {
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 0;
}

iframe {
  pointer-events: none;
}

.trailer {
  position: absolute;
  top: 20px; /* Adjust the top position as needed */
  right: 20px; /* Adjust the right position as needed */
  width: 400px !important; /* Adjust the width as needed */
  height: 225px !important; /* Adjust the height as needed */
  object-fit: cover;
  z-index: 1;
}

.movielistitem {
  width: auto;
  height: auto;
}
</style>
