<template>
  <div>
    <h1>Articles</h1>
    <!-- 2.9 IndexView 컴포넌트에 게시글 작성 페이지로 이동하는 링크 추가 -->
    <router-link :to="{ name: 'create' }">게시글 작성</router-link>
    <hr>
    <!-- 1.5 IndexView 컴포넌트에서 ArticleItem 컴포넌트 등록 및 props 데이터 전달 -->
    <ArticleItem 
      v-for="article in articles"
      :key="article.id"
      :article=article
    ></ArticleItem>
  </div>
</template>

<script>
// 1.5 IndexView 컴포넌트에서 ArticleItem 컴포넌트 등록 및 props 데이터 전달
import ArticleItem from '@/components/ArticleItem'
export default {
  // 1.2 IndexView 컴포넌트 및 라우터 작성
  name: "IndexView",
  // 1.5 IndexView 컴포넌트에서 ArticleItem 컴포넌트 등록 및 props 데이터 전달
  components: { ArticleItem },
  // 1.3 state에서 불러온 articles 출력하기
  computed: {
    articles() {
      return this.$store.state.articles
    },
  },
}
</script>

<style></style>
