import Vue from 'vue'
import VueRouter from 'vue-router'
import Lunch from '../views/Lunch.vue'
import Lotto from '@/views/Lotto.vue'
// @ => src/ 폴더부터 시작하겠다는 의미

Vue.use(VueRouter)

const routes = [
  {
    path: '/lunch', // 경로
    name: 'Lunch', // 경로의 이름
    component: Lunch // path로 접속했을 때 보여줄 컴포넌트
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/lotto/:lottoNumber',
    name: 'Lotto',
    component: Lotto,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
