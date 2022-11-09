<template>
  <div>
    <h1>hello, {{ userName }}</h1>
  </div>
</template>

<script>
export default {
  name: "HelloView",
  data() {
    return {
      userName: this.$route.params.userName,
    }
  },
  // 3.2 컴포넌트 가드 / userName을 이동할 params에 있는 userName으로 재할당(파라미터에 있는 경로를 감지)
  beforeRouteUpdate(to, from, next) {
    this.userName = to.params.userName
    next()
  },
}
</script>

<style></style>
