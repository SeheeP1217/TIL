<template>
  <div>
    <h1>게시글 작성</h1>
    <!-- 2.2 Form 생성 및 데이터 정의 -->
    <!-- 2.3 submit 이벤트 동작을 취소하기 (v-on) :{event}.prevent -->
    <form @submit.prevent="createArticle">
      <input type="text" v-model.trim="title" /><br />
      <textarea v-model.trim="content"></textarea>
      <input type="submit" />
    </form>
    <!-- 2.7 CreateView 컴포넌트에 Index 페이지로 이동하는 뒤로가기 링크 추가 -->
    <router-link :to="{ name: 'index' }">뒤로가기</router-link>
  </div>
</template>

<script>
export default {
  // 2.1 CreateView 컴포넌트 및 라우터 작성
  name: "CreateView",
  // 2.2 Form 생성 및 데이터 정의
  data() {
    return {
      title: null,
      content: null,
    }
  },
  // 2.3 submit 이벤트 동작을 취소하기 (v-on) :{event}.prevent
  methods: {
    // 2.4 actions에 여러 개의 데이터를 넘길 때 하나의 object로 만들어서 전달
    createArticle() {
      const title = this.title
      const content = this.content
      const payload = {
        title,
        content,
      }
      this.$store.dispatch("createArticle", payload)
      // 2.8 게시글 생성 후 Index 페이지로 이동하도록 네비게이터 작성
      this.$router.push({ name: "index" })
    },

    // // 데이터가 없는 경우 alert & 데이터가 있는 경우 actions로 전달하고 싶다면
    // createArticle() {
    //   const title = this.title
    //   const content = this.content
    //   if (!title) {
    //     alert('제목을 입력해주세요')
    //   } else if (!content) {
    //     alert('내용을 입력해주세요')
    //   } else {
    //     const payload = {
    //       title,
    //       content,
    //   }
    //   this.$store.dispatch("createArticle", payload)
    // },
  },
}
</script>

<style></style>
