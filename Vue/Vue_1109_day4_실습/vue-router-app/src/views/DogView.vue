<template>
  <div>
    <p v-if="!imgSrc">{{ message }}</p>
    <!-- 4.5.3 Dog API Not Found / Dog 이미지 출력하기 -->
    <img :src="imgSrc" alt="" />
  </div>
</template>

<script>
// axios 설치 : $ npm i axios
import axios from "axios"

export default {
  name: "DogView",
  // 4.5.3 Dog API Not Found / Dog 이미지 출력하기
  data() {
    return {
      imgSrc: null,
      message: "로딩중...",
    }
  },
  methods: {
    getDogImage() {
      // url에서 breed 값 받아오기
      const breed = this.$route.params.breed
      const dogImageUrl = `https://dog.ceo/api/breed/${breed}/images/random`
      axios({
        method: "get",
        url: dogImageUrl,
      })
        .then((response) => {
          console.log(response)
          const imgSrc = response.data.message
          this.imgSrc = imgSrc
        })
        .catch((error) => {
          // this.message = `${this.$route.params.breed}는 없는 품종입니다.`
          // 4.5.4 Dog API Not Found / 페이지를 찾을 수 없는 경우 404 Not Found로 push
          this.$router.push("/404")
          console.log(error)
        })
    },
  },
  // 인스턴스가 생성될 때 자동으로 호출
  created() {
    this.getDogImage()
  },
}
</script>

<style></style>
