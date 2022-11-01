1. id에 text 넣기
```html
<body>
  <div id="app">이름: </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = document.querySelector('#app')
    let name = 'aiden'
    app.innerText = name
  </script>
</body>
```

2. vue의 data 출력하기
```html
<body>
  <div id="app">
    <!-- 선언적 렌더링 -->
    {{message + ' Nice to meet you!'}}
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const vm = new Vue({
      el: '#app',
      data: {
        // vue 인스턴스가 가지고 있는 data를 넣어주는 곳
        message: 'Hello, vue!'
      }
    })
  </script>
</body>
```

3. computed & data 값 연산하기
```html
<body>
  <div id="app">
    <h3> 금액 : {{money}} </h3>
    <h3> 포인트 : {{point}} </h3>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    new Vue ({
      el: '#app',
      data: {
        money: 50000,
        ratio: 0.05,
        // point: this.money * this.ratio   이렇게 하면 숫자가 아니라고 뜸
      },

      computed: {
      //   point: function() {
      //     return this.money * this.ratio
      //   },  
      // -> : funtion 축약 가능
      point() {
        return this.money * this.ratio
      }
      },
    })
  </script>
</body>
```

4. v-on (@), method로 버튼 클릭할 때마다 숫자 올리기
```html
<body>
  <div id="app">
    <button id="myBtn" @click='plusNum'>click me</button>
    <p id="myElem">{{myNum}}</p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    new Vue({
      el:'#app',
      data:{
        myNum: 0,
      },
      methods: {
        plusNum() {
          this.myNum += 1
        },
      },
    })
  </script>
  <!-- <script>
    const myBtn = document.querySelector('#myBtn')
    const myElem = document.querySelector('#myElem')
    let value = parseInt(myElem.innerText)
    myBtn.addEventListener('click', (event) => {
      value += 1
      myElem.innerText = value
    })
  </script> -->
</body>
```

5. @, if, style 적용하기
```html
  <style>
    #before {
      background-color: greenyellow;
    }
    #after {
      background-color: yellow;
    }
  </style>
</head>
<body>
  <div id="app">
    <p @click="clickActive" :id=elemId>Click Me</p>

  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    new Vue ({
      el: '#app',
      data: {
        elemId: 'before'
      },
      methods: {
        clickActive() {
          if (this.elemId === 'before') {
            this.elemId = 'after'          
          } else {
            this.elemId = 'before'
          }
        },
      }
    })

  </script>
</body>
```

6. if,else-if,else & if VS show
```html
<body>
  <div id="app">
    <div v-if="member === 'aiden'">기다려주세요</div>
    <div v-else-if="member === 'harry'">환영합니다</div>
    <div v-else>누구세요?</div>

    <div v-if="seen">보인다옹</div>
    <div v-show="seen">보인다옹</div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    new Vue({
      el: '#app',
      data: {
        seen: true,
        member: 'harry',
      },
    })
  </script>
</body>
```

7. v-model 입력하는 즉시 화면에 보이기
```html
<body>
  <div id="app">
    <input type="text" v-model="message">
    <h3>{{message}}</h3>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    new Vue({
      el: '#app',
      data: {
        message: '',
      },
    })
  </script>
</body>
```

8. watch (디버깅에 사용)
```html
<body>
  <div id="app">
    <h1>{{num}}</h1>
    <h3> x2 : {{doubleNum}}</h3>
    <button @click="plusBtn">+</button>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    new Vue({
      el: '#app',
      data: {
        num:0,
      },
      methods: {
        plusBtn() {
          this.num += 1
        }
      },
      watch: {
        num(newValue, oldValue) {
          console.log(oldValue, newValue)
        }
      },
      computed: {
        doubleNum() {
          return this.num * 2
        }
      }
    })
  </script>
</body>
```

9. computed
```html
  <style>
    .errorColor {
      color: red;
    }
  </style>
</head>
<body>
  <div id="app">
    <h3 :class="errorText">ERROR</h3>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    new Vue({
      el: '#app',
      data: {
        isError: false,
      },
      computed: {
        errorText(){
          return this.isError ? 'errorColor' : null   //삼항연산자
        }
      }
    })
  </script>
</body>
```

10. 리스트, 딕셔너리 데이터 & v-for, v-if 동시에 쓰기
```html
<body>
  <div id="app">
    <ul>
      <li v-for="(fruit, idx) in fruits">
        {{idx}} - {{fruit}}
      </li>
    </ul>

    <ul>
      <template v-for="todo in todos" :key="`todo-${idx}`">
        <!-- key는 v-for이 더 효과적으로 돌게 해줌. 없어도 괜찮 -->
        <li v-if="!todo.completed">
          {{todo.context}}
        </li>
      </template>
      <!-- 공식문서에서는 v-for, v-if를 한 element 안에 사용하는 것을 권장하지 않는다. template을 이용해서 나눠주는 것을 추천. 이 때 for, if 중 뭐가 먼저 들어가야하는지 유의 -->
    </ul>

  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    new Vue({
      el: '#app',
      data: {
        fruits: ['딸기', '복숭아', '귤'],
        todos: [
          {id: 1, context: 'todo1', completed: false},
          {id: 2, context: 'todo2', completed: true},
          {id: 3, context: 'todo3', completed: false},
        ]
      },
    })
  </script>
</body>
```