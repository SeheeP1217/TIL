# Vue

### Vue intro
- Front-end Framework
  - Front-end 개발: 사용자에게 보여주는 화면 만들기
  - Web App(SPA)을 만들 때 사용하는 도구
    - Web App
      - 웹 브라우저에서 실행되는 어플리케이션 소프트웨어
    - SPA (Single Page Application)
      - 서버에서 최초 1장의 HTML만 전달받아 모든 요청에 대응하는 방식을 의미 (CSR(Client Side Rendering) 방식으로 요청을 처리하기 때문)
      - +) SSR (Server Side Rendering)이란?
        - 기존의 요청 처리 방식은 SSR
        - Server가 사용자의 요청에 적합한 HTML을 렌더링하여 제공하는 방식
        - 전달받은 새 문서를 보여주기 위해 브라우저는 새로고침을 진행
      - +) CSR (Client Side Rendering)이란?
        - 최초 한 장의 HTML(빈 HTML)을 받아오는 것은 동일
        - 각 요청에 대한 대응을 JavaScript를 사용하여 필요한 부분만 다시 렌더링
        1. 새로운 페이지를 서버에 AJAX로 요청
        2. 서버는 화면을 그리기 위해 필요한 데이터를 JSON 방식으로 전달
        3. JSON 데이터를 JavaScript로 처리, DOM 트리에 반영(렌더링)
        - CSR 방식을 사용하는 이유
          1. 모든 HTML 페이지를 서버로부터 받는 것이 아니기 때문
            - 클라이언트-서버 간 통신 즉, 트래픽이 감소 -> 응답 속도 빨라짐
          2. 매번 새 문서를 받아 새로고침하는 것이 아니라 필요한 부분만 고쳐나가므로 각 요청이 끊김없이 진행
            - 요청이 자연스럽게 진행 => UX 향상
          3. BE와 FE의 작업 영역을 명확히 분리할 수 있음 (협업이 용이)
        - 단점
          1. 첫 구동 시 필요한 데이터가 많으면 많을수록 최초 작동 시작까지 오랜 시간이 소요
          2. Naver, Netflix, Disney+ 등 모바일에 설치된 Web-App을 실행하게 되면 잠깐의 로딩 시간이 필요
          3. 검색 엔진 최적화(SEO, Search Engine Optimization)가 어려움
            - 서버가 제공하는 것은 텅 빈 HTML
            - 내용을 채우는 것은 AJAX 요청으로 얻은 JSON 데이터로 클라이언트(브라우저)가 진행
          4. 대체적으로 HTML에 작성된 내용을 기반으로 하는 검색 엔진에 빈 HTML을 공유하는 SPA 서비스가 노출되기는 어려움
      - +) SEO (Search Engine Optimization)이란?
        - google, bing과 같은 검색 엔진 등에 내 서비스나 제품 등이 효율적으로 검색 엔진에 노출되도록 개선하는 과정
        - 검색 = 각 사이트가 운용하는 검색 엔진에 의해 이루어지는 작업
        - 검색엔진 = 웹 상에 존재하는 가능한 모든 정보들을 긁어 모으는 방식으로 동작
          - 정보의 대상은 주로 HTML에 작성된 내용
          - JavaScript가 실행된 이후의 결과를 확인하는 과정이 없음
        - 최근에는 SPA, 즉 CSR로 구성된 서비스의 비중이 증가
          - SPA 서비스는 검색 대상으로 넓히기 위해 JS를 지원하는 방식으로 발전
        - 단, 단순 HTML만을 분석하는 것보다 몇 배의 리소스가 필요한 작업이기에 여전히 CSR의 검색 엔진 최적화 문제가 모두 해결된 것은 아님
    - CSR vs SSR
      - CSR과 SSR은 흑과 백이 아님, 내 서비스에 적합한 렌더링 방식을 적절하게 활용할 수 있어야 함
      - SPA 서비스에서도 SSR을 지원하는 Framework도 발전하고 있음 (Vue의 Nuxt.js, React의 Next.js, Angular Universal 등)
- Vue로 작업을 시작하기 위하여 CDN 가져와야함 (https://v2.vuejs.org/)
  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>

```html
<body>
  <div id="app">
    <p id="name">name : {{ message }}</p>                     // {{ message }}를 추가했더니 밑의 data의 message가 출력
    <input id="inputName" type="text" v-model="message">      // v-model을 추가했더니 실시간 문자열 출력 가능
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    // CODE HERE
    const app = new Vue({                                     // CDN
      el: '#app',
      data: {
        message: '',
      }
    })
  </script>
</body>
```

### Vue instance
- MVVM Pattern
  - 소프트웨어 아키텍처 패턴의 일종
  - 마크업 언어로 구현하는 그래픽 사용자 인터페이스(view)의 개발을 Back-end(model)로부터 분리시켜 view가 어느 특정한 모델 플랫폼에 종속되지 않도록 함
  - View : 우리 눈에 보이는 부분 = DOM
  - Model : 실제 데이터 = JSON
  - View Model(Vue)
    - View를 위한 Model
    - View와 연결(binding)되어 Action을 주고 받음
    - Model이 변경되면 View Model도 변경되고 바인딩된 View도 변경됨
    - View에서 사용자가 데이터를 변경하면 View Model의 데이터가 변경되고 바인딩된 다른 View도 변경됨
- Vue instance
  - Vue instance === 1개의 객체
  - 아주 많은 속성과 메서드를 이미 가지고 있고, 이러한 기능들을 사용하는 것
  - +) 생성자 함수
    - 함수 이름은 반드시 대문자로 시작
    - 생성자 함수를 사용할 떄는 반드시 new 연산자를 사용

```html
<body>

  <div id="app">
    {{ message }}
  </div>

  <div>
    {{ message }}
  </div>

  <!-- Vue CDN -->
  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    // CODE HERE
    // 1. Vue instance constructor
    // const vm = new Vue()
    // console.log(vm)

    // 2. el
    const app = new Vue({
      el: '#app',
      // 3. data
      data: {
        message: 'Hello, Vue!'
      },

      // 4. methods
      methods: {
        print: function () {
          console.log(this.message)   //this = Vue
          // = console.log(this.$data.message)
        },

        bye: function () {
          this.message = 'Bye, Vue!'
        },

        // 4-1. arrow function
        // arrowBye: () => {
        //   this.message = 'Arrow Function?'
        //   console.log(this)
        // }
      }
    })
    console.log(app)
  </script>
```
- el (element)
  - Vue instance와 DOM을 mount(연결)하는 옵션
    - View와 Model을 연결하는 역할
    - HTML id 혹은 class와 마운트 가능
  - Vue instance와 연결되지 않은 DOM 외부는 Vue 영향을 받지 않음
    - Vue 속성 및 메서드 사용 불가
- data
  - Vue instance의 데이터 객체 혹은 인스턴스 속성
  - 데이터 객체는 반드시 기본 객체 {} (Object)여야 함
  - 객체 내부의 아이템은 value로 모든 타입의 객체를 가질 수 있음
  - 정의된 속성은 interpolation {{}} 을 통해 view에 렌더링 가능함
  - 추가된 객체의 각 값들은 this.message 형태로 접근 가능
- methods
  - Vue instance의 method들을 정의하는 곳
  - methods 객체 정의
    - 객체 내 print method 정의
    - print method 실행 시 Vue instance의 data 내 message 출력
    - 콘솔창에서 app.print() 실행하면 출력 확인 가능
- methods with Arrow Function
  - 메서드를 정의할 때, Arrow Function을 사용하면 안됨
  - Arrow Function의 this는 함수가 선언될 때 상위 스코프를 가리킴 (콜백 함수에서는 가능)
  - 즉 this가 상위 객체 window를 가리킴
  - 호출은 문제 없이 가능하나 this로 Vue의 data를 변경하지 못함

### Basic of syntax
- Template Syntax
  - 렌더링 된 DOM을 기본 Vue instance의 data에 선언적으로 바인딩할 수 있는 HTML 기반 template syntax를 사용
    - 렌더링 된 DOM-브라우저에 의해 보기 좋게 그려질 HTML 코드
    - HTML 기반 template syntax - HTML 코드에 직접 작성할 수 있는 문법 제공
    - 선언적으로 바인딩-Vue instance와 DOM을 연결
- Template Interpolation
  - 가장 기본적인 바인딩(연결) 방법
  - 중괄호 2개로 표기
  - DTL과 동일한 형태로 작성
  - Template interpolation 방법은 HTML을 일반 텍스트로 표현
- RAW HTML
  - v-html directive을 사용하여 data와 바인딩
  - directive-HTML 기반 template syntax
  - HTML의 기본 속성이 아닌 Vue가 제공하는 특수 속성의 값으로 data를 작성
```html
<body>
  <!-- 1. Text interpolation -->
  <div id="app">
    <p>메시지: {{ msg }}</p>   
    <p>HTML 메시지 : {{ rawHTML }}</p>
    <p>HTML 메시지 : <span v-html="rawHTML"></span></p> // 문자열로 쓰여진 style 태그 사용하기
    <p>{{ msg.split('').reverse().join('') }}</p>       // 자바스크립트의 완성된 표현식도 통으로 넣을 수 있다.
  </div>
  <script>
  // 1. Text interpolation
  const app = new Vue({
    el: '#app',
    data: {
      msg: 'Text interpolation',
      rawHTML: '<span style="color:red"> 빨간 글씨</span>'
    }
  })
  </script>
</body>
```
### Directives
- Directives 기본 구성
  - v-접두사가 있는 특수 속성에는 값을 할당할 수 있음
    - 값에는 JS 표현식을 작성할 수 있음
  - directive의 역할은 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 것
  - v-on:submit.prevent="onSubmit"
    - ':'을 통해 전달 인자를 받을 수 있음
    - '.'으로 표시되는 특수 접미사 - directive를 특별한 방법으로 바인딩 해야함
  - v-text
    - Template Interpolation과 함께 가장 기본적인 바인딩 방법
    - {{ }}와 동일한 역할
  - v-html
    - RAW HTML을 표현할 수 있는 방법
    - 단, 사용자가 입력하거나 제공하는 컨텐츠에는 절대 사용 금지
  ```html
  <body>
    <!-- 2. v-text & v-html -->
    <div id="app2">
      <!-- 2-1. v-text & {{}} -->
      <p v-text="message"></p>
      <!-- 같음 -->
      <p>{{ message }}</p>

      <!-- 2-2. v-html -->
      <p v-html="html"></p>
    </div>
    <script>
      // 2. v-text && v-html
      const app2 = new Vue({
        el: '#app2',
        data: {
          message: 'Hello!',
          html: '<a href="https://www.google.com">GOOGLE</a>'
        }
      })
    </script>
  </body>
  ```
  - v-show
    - 표현식에 작성된 값에 따라 element를 보여줄 것인지 결정
      - boolean 값이 변경 될 때마다 반응
    - 대상 element의 display 속성을 기본 속성과 none으로 toggle
    - 요소 자체는 항상 DOM에 렌더링 됨
    - 바인딩 된 isActive의 값이 false이므로 첫 방문 시 p tag는 보이지 않음
      - vue dev tools에서 isActive 변경 시 화면에 출력
      - 값을 false로 변경 시 다시 사라짐
    - 화면에서만 사라졌을 뿐, DOM에는 존재한다.(display 속성이 변경된 것)
  - v-if
    - v-show와 사용 방법은 동일
    - isActive의 값이 변경될 때 반응
    - 단, 값이 false인 경우 DOM에서 사라짐
    - v-if, v-else-if, v-else 형태로 사용
  - v-show VS v-if
    - v-show (Expensive initial load, cheap toggle)
      - 표현식 결과와 관계 없이 렌더링 되므로 초기 렌더링에 필요한 비용은 v-if보다 높을 수 있음
      - display 속성 변경으로 표현 여부를 판단하므로 렌더링 후 toggle 비용은 적음
    - v-if (Cheap initial load, expensive toggle)
      - 표현식 결과가 false인 경우 렌더링조차 되지 않으므로 초기 렌더링 비용은 v-show보다 낮을 수 있음
      - 단, 표현식 값이 자주 변경되는 경우 잦은 렌더링으로 비용이 증가할 수 있음
  ```html
  <body>
    <!-- 3. v-show && v-if -->
    <div id="app3">
      <p v-show="isActive">보이니? 안보이니?</p>
      <p v-if="isActive">안보이니? 보이니?</p>
    </div>
    <script>
      // 3. v-show && v-if
      const app3 = new Vue({
        el: '#app3',
        data: {
          isActive: True
        }
      })
    </script>
  </body>
  ```
  - v-for
    - for .. in .. 형식으로 작성
    - 반복한 데이터 타입에 모두 사용 가능
    - index를 함께 출력하고자 한다면 (char, index)형태로 사용 가능
    - 배열 역시 문자열과 동일하게 사용 가능
    - 각 요소가 객체라면 dot notation으로 접근할 수 있음
    - 객체 순회 시 value가 할당되어 출력 (value가 key보다 먼저)
    - 2번째 변수 할당 시 key 출력 가능
    - +) 특수 속성 key
      - "v-for 사용 시 반드시 key 속성을 각 요소에 작성"
      - 주로 v-for directive 작성 시 사용
      - vue 화면 구성 시 이전과 달라진 점을 확인하는 용도로 활용 (key값이 중복되면 안됨)
      - 각 요소가 고유한 값을 가지고 있지 않다면 생략할 수 있음
    ```html
    <body>
    <!-- 3. v-for -->
    <div id="app">
      <h2>String</h2>
      <div v-for="char in myStr">
        {{ char }}
      </div>
      <div v-for="(char, index) in myStr" :key="index">
        <p>{{ index }}번째 문자열 {{ char }}</p>
      </div>

      <h2>Array</h2>
      <div v-for="(item, index) in myArr" :key="index">
      <!-- <div v-for="(item, index) in myArr" :key="another-${index}"> --> // key 값이 위와 같아서 뜨는 warning을 없애려면 key값을 바꿔주어야한다.
        <p>{{ index }}번째 아이템 {{ item }}</p>
      </div>

      <div v-for="(item, index) in myArr2" :key="`arry-${index}`">
        <p>{{ item.id }}번째 아이템</p>
        <p>{{ item.name }}</p>
      </div>

      <h2>Object</h2>
      <div v-for="value in myObj">    // 각 요소가 고유한 값을 가지고 있어서 key 속성을 생략할 수 있음
        <p>{{ value }}</p>
      </div>

      <div v-for="(value, key) in myObj"  :key="key">     //객체에서는 key 값이 어차피 겹치지 않기 때문에 key="key"로 바로 쓰는 게 일반적임
        <p>{{ key }} : {{ value }}</p>
      </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
    <script>
      const app = new Vue({
        el: '#app',
        data: {
          // 1. String
          myStr: 'Hello, World!',

          // 2-1. Array
          myArr: ['python', 'django', 'vue.js'],

          // 2-2. Array with Object
          myArr2: [
            { id: 1, name: 'python', completed: true},
            { id: 2, name: 'django', completed: true},
            { id: 3, name: 'vue.js', completed: false},
          ],
          
          // 3. Object
          myObj: {
            name: 'harry',
            age: 27
          },
        }
      })
    </script>
  </body>
  ```
  - v-on
    - ':'을 통해 전달받은 인자를 확인
    - 값으로 JS표현식 작성
    - addEventListener의 첫번째 인자와 동일한 값들로 구성
    - 대기하고 있던 이벤트가 발생하면 할당된 표현식 실행
    - method를 통한 data 조작도 가능
    - method에 인자를 넘기는 방법은 일반 함수를 호출할 때와 동일한 방식
    - ':'을 통해 전달된 인자에 따라 특별한 modifiers(수식어)가 있을 수 있음 (ex. v-on:keyup.enter -> enter 키를 눌렀을 때 등)
    - '@' shortcut 제공 (ex. @keyup.click)
  - v-bind
    - HTML 기본 속성에 Vue data를 연결
    - class의 경우 다양한 형태로 연결 가능
      - 조건부 바인딩
        - {'class Name':'조건 표현식'}
        - 삼항 연산자도 가능
      - 다중 바인딩
        - ['JS 표현식', 'JS 표현식', ...]
  - v-model
### Vue advanced