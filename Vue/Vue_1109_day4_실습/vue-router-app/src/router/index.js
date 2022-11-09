import Vue from "vue"
import VueRouter from "vue-router"
import HomeView from "../views/HomeView.vue"
import HelloView from "../views/HelloView.vue"
// 1.2 Global Before Guard / Login 여부에 따른 라우팅 처리
import LoginView from "../views/LoginView.vue"
// 4.2 404 Not Found / 사용자가 요청한 리소스가 존재하지 않을 때 응답
import NotFound404 from "../views/NotFound404.vue"
// 4.5.1 Dog API Not Found / Dog API 가져오기
import DogView from '../views/DogView.vue'

Vue.use(VueRouter)

// 2.2 라우터 가드 / 로그인 상태 설정
const isLoggedIn = true

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/hello/:userName",
    name: "hello",
    component: HelloView,
  },
  {
    // 1.3 Global Before Guard / Login 여부에 따른 라우팅 처리
    path: "/login",
    name: "login",
    component: LoginView,
    // 2. 라우터 가드
    // 2.1 라우터 가드 / 이미 로그인이 되어있는 경우 home view로 이동
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        console.log("이미 로그인 되어있음")
        next({ name: "home" })
      } else {
        next()
      }
    },
  },
  // 4.3 404 Not Found / 사용자가 요청한 리소스가 존재하지 않을 때 응답
  {
    path: "/404",
    name: "NotFound404",
    component: NotFound404,
  },
  // 4.5 Dog API Not Found
  // 4.5.2 Dog API Not Found / Dog API 가져오기
  {
    path: "/dog/:breed",  // 특정 품종만 가져오려면
    name: 'dog',
    component: DogView,
  },
  // 4.4 404 Not Found / 모든 경로에 대해서 404 page로 redirect 시키기 (routes의 최하단부에 작성해야함)
  {
    path: "*",
    redirect: "/404",
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
})

// // 1. Global Before Guard 실습
// router.beforeEach((to, from, next) => {
//   // console.log("to", to)
//   // console.log("from", from)
//   // console.log("next", next)
//   // next()

//   // 1.3 Global Before Guard / Login 여부에 따른 라우팅 처리
//   // 로그인 여부
//   const isLoggedIn = false
//   // 로그인이 필요한 페이지
//   const authPages = ["hello", "home", "about"]
//   // 앞으로 이동할 페이지(to)가 로그인이 필요한 페이지인지 확인
//   const isAuthRequired = authPages.includes(to.name)

//   // 로그인이 필요하지 않은 페이지로 설정하고 싶다면
//   // const allowAllPages = ["login"]
//   // const isAuthRequired = !allowAllPages.includes(to.name)

//   // 로그인이 되어있지 않고 로그인이 필요한 페이지이면
//   if (!isLoggedIn && isAuthRequired) {
//     console.log("Login으로 이동!")
//     next({ name: "login" })
//   } else {
//     console.log("to로 이동!")
//     next()
//     // next 인자가 없을 경우 to로 이동
//   }
// })

export default router
