<template>
  <div>
    <div class="mb-5" style="max-width: 370px; margin-left: auto; margin-right: 5%">
      <h1 class="font-do my-3"></h1>
      <b-row class="d-flex justify-content-end"> </b-row>
      <b-row>
        <b-col class="d-flex justify-content-end">
          <b-carousel
            id="carousel-1"
            v-model="slide"
            :interval="2000"
            controls
            indicators
            background="#000000"
            style="text-shadow: 1px 1px 2px #333"
            @sliding-start="onSlideStart"
            @sliding-end="onSlideEnd"
            class="font-poor"
            ref="carouselRef"
            fade
          >
            <b-carousel-slide
              v-for="(movie, idx) in ordered"
              :key="idx"
              :caption="movie.title"
              img-blank-color="dark"
              img-height="480"
              style="width: auto"
            >
              <template #img>
                <div style="display: flex; justify-content: flex-end">
                  <img
                    class="d-block img-fluid"
                    :src="`https://image.tmdb.org/t/p/w185${movie.poster_path}`"
                    alt="image slot"
                    style="max-height: 480px"
                  />
                </div>
              </template>
            </b-carousel-slide>
          </b-carousel>
        </b-col>
      </b-row>
    </div>

    <div class="container mt-5" v-if="login && recommend_list.length > 0">
      <h1 class="font-do my-3">당신을 위한 영화 추천!</h1>
      <div class="row">
        <MovieListItem v-for="(movie, idx) in recommend_list" :key="idx" :movie="movie" class="col-3" />
      </div>
    </div>

    <div>
      <h1 class="font-do my-5">영화 리스트</h1>
    </div>
    <div class="container">
      <div class="row">
        <MovieListItem v-for="(movie, idx) in movies" :key="idx" :movie="movie" class="col-3" :search="search" />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';

import MovieListItem from '@/components/movie/MovieListItem';

export default {
  name: 'MovieList',
  data: function () {
    return {
      slide: 0,
      sliding: null,
      search: '',
      i: 0,
    };
  },
  components: {
    MovieListItem,
  },
  methods: {
    movieDetail: function (movie) {
      this.$router.push({
        name: 'MovieDetail',
        params: {
          movie: movie,
        },
      });
    },
    onSlideStart() {
      this.sliding = true;
    },
    onSlideEnd() {
      this.sliding = false;
    },
    // resetCarouselHeight() {
    //   const carousel = this.$refs.carouselRef;
    //   if (carousel) {
    //     const images = carousel.$el.querySelectorAll('.d-block.img-fluid');
    //     if (images) {
    //       let maxHeight = 0;
    //       images.forEach((image) => {
    //         maxHeight = Math.max(maxHeight, image.offsetHeight);
    //       });
    //       carousel.$el.style.height = `${maxHeight}px`;
    //     }
    //   }
    // },
  },
  created: function () {
    this.i = 0;
    if (this.login === true && this.is_admin === false) {
      this.$store.dispatch('recommendMovie');
    }
  },
  computed: {
    ...mapState(['login', 'login_user', 'is_admin', 'movie_list', 'ordered_movie_list', 'recommend_list']),

    movies: function () {
      return this.movie_list.filter((movie) => {
        if (movie.movie_no) {
          return movie;
        }
      });
    },
    ordered: function () {
      return this.ordered_movie_list.filter((movie) => {
        this.i++;
        if (this.i <= 8) {
          return movie;
        }
      });
    },
  },
  mounted() {
    window.scrollTo(0, 0);
    if (this.login === true && this.is_admin === false) {
      this.$store.dispatch('recommendMovie');
    }
    window.addEventListener('resize', this.resetCarouselHeight);
    this.$nextTick(() => {
      this.resetCarouselHeight();
    });
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.resetCarouselHeight);
  },
};
</script>

<style>
.carousel-caption {
  position: absolute;
  right: 15%;
  bottom: 20px;
  left: 25%;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  /* text-align: center; */
}

h1 {
  color: #e8d1d9;
}
</style>
