import Vue from "vue"
import VueRouter from "vue-router"
// 1.2 IndexView 컴포넌트 및 라우터 작성
import IndexView from "../views/IndexView.vue"
// 2.1 CreateView 컴포넌트 및 라우터 작성
import CreateView from "../views/CreateView.vue"
// 3.1 DetailView 컴포넌트 및 라우터 작성 (id를 동적인자로 전달)
import DetailView from "../views/DetailView.vue"
// 5.1 NotFound404 컴포넌트 및 라우터 작성
import NotFound404 from "../views/NotFound404.vue"

Vue.use(VueRouter)

const routes = [
  // 1.2 IndexView 컴포넌트 및 라우터 작성
  {
    path: "/",
    name: "index",
    component: IndexView,
  },
  // 2.1 CreateView 컴포넌트 및 라우터 작성
  {
    path: "/create",
    name: "create",
    component: CreateView,
  },
  // 5.1 NotFound404 컴포넌트 및 라우터 작성
  // (Detail에 대한 route보다 먼저 등록해줘야함, /404로 등록 시 404번째 게시글과 혼동할 수 있음)
  {
    path: "/404-not-found",
    name: "NotFound404",
    component: NotFound404,
  },
  // 3.1 DetailView 컴포넌트 및 라우터 작성 (id를 동적인자로 전달)
  {
    path: "/:id", //Detail은 각각의 번호가 필요하기 때문에 :id로 설정
    name: "detail",
    component: DetailView,
  },
  // 5.3 요청한 리소스가 존재하지 않는 경우 없는 id가 아닌 전혀 다른 요청에도 대비하여 404 page로 redirect 시키기
  {
    path: "*",
    redirect: { name: "NotFound404" },
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
})

export default router
