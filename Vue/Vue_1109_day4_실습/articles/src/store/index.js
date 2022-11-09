import Vue from "vue"
import Vuex from "vuex"

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // 1.1 게시글 필드 설정하기
    article_id: 3, // 다음에 작성되는 글은 id를 3번을 쓴다는 가정
    articles: [
      {
        id: 1,
        title: "title1",
        content: "content1",
        createdAt: new Date().getTime(),
      },
      {
        id: 2,
        title: "title2",
        content: "content2",
        createdAt: new Date().getTime(),
      },
    ],
  },
  getters: {},
  mutations: {
    // 2.6 mutations에서는 전달된 article 객체를 사용해 게시글 작성 (다음 게시글을 위해 article_id 값 1 증가
    CREATE_ARTICLE(state, article) {
      state.articles.push(article)
      state.article_id = state.article_id + 1
    },
    // 4.2 mutations에서 id에 해당하는 게시글을 지움
    DELETE_ARTICLE(state, article_id) {
      state.articles = state.articles.filter((article) => {
        return !(article.id === article_id)
      })
    }
  },
  actions: {
    // 2.5 actions에서는 넘어온 데이터를 활용하여 article 생성 후 mutations 호출
    createArticle(context, payload) {
      const article = {
        id: context.state.article_id,
        title: payload.title,
        content: payload.content,
        createdAt: new Date().getTime(),
      }
      context.commit("CREATE_ARTICLE", article)
    },
  },
  modules: {},
})
