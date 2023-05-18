import Vue from 'vue';
import VueRouter from 'vue-router';
import Signup from '@/views/accounts/Signup';
import Login from '@/views/accounts/Login';
import Profile from '@/views/accounts/Profile';
import MovieList from '@/views/movies/MovieList';
import ManageMovie from '@/views/admin/ManageMovie';
import AdminManagement from '@/views/admin/AdminManagement';
import Post from '@/views/community/Post';
import CreatePost from '@/views/community/CreatePost';
import PostDetail from '@/views/community/PostDetail';

Vue.use(VueRouter);

const routes = [
  {
    path: '/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/profile/:username',
    name: 'Profile',
    component: Profile,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/movies',
    name: 'MovieList',
    component: MovieList,
  },
  {
    path: '/managemovie',
    name: 'ManageMovie',
    component: ManageMovie,
  },
  {
    path: '/management',
    name: 'AdminManagement',
    component: AdminManagement,
  },
  {
    path: '/post',
    name: 'Post',
    component: Post,
  },
  {
    path: '/createpost',
    name: 'CreatePost',
    component: CreatePost,
  },
  {
    path: '/postdetail',
    name: 'PostDetail',
    component: PostDetail,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
