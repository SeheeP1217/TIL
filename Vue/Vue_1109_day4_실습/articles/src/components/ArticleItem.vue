<template>
  <!-- 3.8 각 게시글을 클릭하면 detail 페이지로 이동하도록 ArticleItem에 이벤트 추가 
      (v-on 이벤트 핸들러에도 인자 전달 가능) -->
  <div @click="goDetail(article.id)">
    <!-- 1.6 props 데이터 선언 및 게시글 출력 -->
    <p>글 번호: {{ article.id }}</p>
    <p>글 제목: {{ article.title }}</p>
    <hr>
  </div>
</template>

<script>
export default {
  // 1.4 ArticleItem 컴포넌트 작성
  name: "ArticleItem",
  // 1.6 props 데이터 선언 및 게시글 출력
  props: {
    article: Object,
  },
  // 3.8 각 게시글을 클릭하면 detail 페이지로 이동하도록 ArticleItem에 이벤트 추가 
  // (v-on 이벤트 핸들러에도 인자 전달 가능)
  methods: {
    goDetail(id) {
      this.$router.push({ name: 'detail', params:{id} })
    }
  }
}
</script>

<style></style>
