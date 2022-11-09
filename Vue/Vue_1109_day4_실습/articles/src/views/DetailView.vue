<template>
  <div>
    <h1>Detail</h1>
    <!-- 3.4 article 출력 -->
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <!-- 3.6 글 작성시간을 로컬 시간으로 변환 
      (자정과의 시간 차이를 밀리초로 나타내는 정수 값인 상태) -->
    <!-- <p>작성시간 : {{ article?.createdAt }}</p> -->
    <p>작성시간 : {{ articleCreatedAt }}</p>
    <!-- optional chaining(?.)을 통해 article 객체가 있을 때만 출력되도록 설정 
        -> 서버에서 데이터를 가져오는 시간이 줄어듦 
        -> 평가대상이 undefined나 null이면 에러가 발생하지 않고 undefined를 반환 -->

    <!-- 4.1 DetailView 컴포넌트에 삭제 버튼을 만들고, mutations를 호출 -->
    <button @click="deleteArticle">삭제</button><br />
    <!-- 3.7 DetailView 컴포넌트에서 뒤로가기 링크 추가 -->
    <router-link :to="{ name: 'index' }">뒤로가기</router-link>
  </div>
</template>

<script>
export default {
  // 3.1 DetailView 컴포넌트 및 라우터 작성 (id를 동적인자로 전달)
  name: "DetailView",
  // 3.2 article 정의 및 state에서 articles 가져오기
  data() {
    return {
      article: null,
    }
  },
  computed: {
    articles() {
      return this.$store.state.articles
    },
    // 3.6 글 작성시간을 로컬 시간으로 변환 (자정과의 시간 차이를 밀리초로 나타내는 정수 값인 상태)
    articleCreatedAt() {
      const article = this.article
      const createdAt = new Date(article?.createdAt).toLocaleString()
      return createdAt
    },
  },
  methods: {
    // 4.1 DetailView 컴포넌트에 삭제 버튼을 만들고, mutations를 호출
    deleteArticle() {
      this.$store.commit("DELETE_ARTICLE", this.article.id)
      // 4.3 삭제 후 index 페이지로 이동하도록 네비게이션 작성
      this.$router.push({ name: "index" })
    },
    // 3.3 articles에서 동적인자를 통해 받은 id에 해당하는 article 가져오기
    // (동적 인자를 통해 받은 id는 str이므로 형변환을 해서 비교)
    getArticleById(id) {
      // const id = this.$route.params.id
      for (const article of this.articles) {
        if (article.id === Number(id)) {
          this.article = article
          break
        }
      }
      // 5.2 DetailView 컴포넌트에 id에 대항하는 article이 없으면 404 페이지로 이동
      if (!this.article) {
        this.$router.push({ name: "NotFound404" })
      }
    },
  },
  // 3.5 created lifecycle hook을 통해 인스턴스가 생성되었을 때 article을 가져오는 함수 호출
  created() {
    this.getArticleById(this.$route.params.id)
  },
}
</script>

<style></style>
