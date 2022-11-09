<template>
  <div class="about">
    <h1>This is an about page</h1>
    <router-link :to="{ name: 'home' }">Home</router-link> |
    <button @click="toHome">홈으로!</button>
    <!-- 3. 컴포넌트 가드 -->
    <!-- 3.1 컴포넌트 가드 / 해당 컴포넌트를 렌더링하는 경로가 변경될 때 사용 -->
    <input type="text" v-model="inputData" @keyup.enter="goToHello" />
  </div>
</template>

<script>
export default {
  name: "AboutView",
  methods: {
    toHome() {
      this.$router.push({ name: "home" })
    },
    goToHello() {
      this.$router.push({ name: "hello", params: { userName: this.inputData } })
    },
  },
  data() {
    return {
      inputData: null,
    }
  },
}
</script>
