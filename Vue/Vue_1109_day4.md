# Vue

### UX & UI

- UX (User Experience)
  - 유저와 가장 가까이에 있는 분야, 데이터를 기반으로 유저를 조사하고 분석해서 개발자, 디자이너가 이해할 수 있게 소통
  - 유저 리서치, 데이터 설계 및 정제, 유저 시나리오, 프로토타입 설계 등이 필요
  - 직무: UX Researcher, User Researcher
- UI (User Interface)
  - 유저에게 보여지는 화면을 디자인
  - UX를 고려한 디자인을 반영, 이 과정에서 기능 개선 혹은 추가가 필요한 경우 Front-end 개발자와 가장 많이 소통
  - Interface
    - 서로 다른 시스템, 장치 사이에서 정보나 신호를 주고받는 경우의 접점 -> 사용자가 기기를 쉽게 동작시키는데 도움을 주는 시스템
    - ex) CLI(command-line interface), GUI(Graphic User interface)를 사용해서 컴퓨터를 조작
  - 사용자가 보다 쉽고 편리하게 사용할 수 있도록 하는 부분까지 고려되어야함
  - 통일된 디자인을 위한 디자인 시스템, 소통을 위한 중간 산출물, 프로토타입 등이 필요
  - UI 디자인에 있어 가장 중요한 것은 협업
  - 직무: Product Designer, Interaction Designer
- 학문으로서의 UX & UI
  - UX와 UI는 단순히 누군가의 직감에 의해서 결정되는 것이 아님
  - 하나의 학문으로서 연구되고 있는 분야, 심리학과도 밀접한 연관이 있음
  - UX/UI 그리고 HCI
    - GUI: 유저가 보는 일반적인 시각적인 디자인
    - UI: 유저가 보거나 듣는 등 비시각적인 부분까지 포함한 디자인
    - UX: 유저가 겪는 모든 경험(컴퓨터와 관련이 없는 부분까지도 포함)
    - HCI(Human Computer Interaction): 인간과 컴퓨터 사이의 상호작용에 대한 학문
- Prototyping
  - Software prototyping
    - 개발 중인 소프트웨어 프로그램의 완성되기 전 버전을 만드는 것
  - Figma (인터페이스 디자인을 위한 협업 웹 애플리케이션)
    - 웹 기반 시스템을 가짐 (웹환경에서 동작) (매우 가벼운 환경에서 실행 가능, 모든 작업 내역이 웹에 저장)
    - 실시간으로 팀원들과 협업할 수 있는 기능
    - 직관적이고 다양한 디자인 툴을 제공
    - Figma 사용자들이 만든 다양한 플러그인이 존재

### Vue Router

- Routing

  - 네트워크에서 경로를 선택하는 프로세스
  - 웹 서비스에서의 라우팅: 유저가 방문한 URL에 대해 적절한 결과를 응답하는 것
  - Routing in SSR
    - Server가 모든 라우팅을 통제
    - URL로 요청이 들어오면 응답으로 완성된 HTML 제공 (Django로 보낸 요청의 응답 HTML은 완성본인 상태였음)
    - Routing(URL)에 대한 결정권을 서버가 가짐
  - Routing in SPA/CSR
    - 서버는 하나의 HTML(index.html) 만을 제공
    - 이후에 모든 동작은 하나의 HTML 문서 위에서 JavaScript 코드를 활용
      - DOM을 그리는데 필요한 추가적인 데이터가 있다면 axios와 같은 AJAX 요청을 보낼 수 있는 도구를 사용하여 데이터를 가져오고 처리
    - 즉, 하나의 URL만 가질 수 있음
  - Rounting이 없다면
    - 유저가 URL을 통한 페이지의 변화를 감지할 수 없음
    - 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음
      - 새로고침 시 처음 페이지로 돌아감
      - 링크를 공유할 시 처음 페이지만 공유 가능
    - 브라우저의 뒤로 가기 기능을 사용할 수 없음

- Vue Router

  - Vue의 공식 라우터
  - SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공
  - routes에 컴포넌트를 매핑한 후, 어떤 URL에서 렌더링할지 알려줌
    - 즉, SPA를 MPA처럼 URL을 이동하면서 사용 가능
    - SPA의 단점 중 하나인 "URL이 변경되지 않는다."를 해결
  - +) MPA (Multiple Page Application)
    - 여러 개의 페이지로 구성된 애플리케이션
    - SSR 방식으로 렌더링
  - History mode
    - 브라우저의 History API를 활용한 방식(새로고침 없이 URL 이동 기록을 남길 수 있음)
    - 우리에게 익숙한 URL 구조로 사용 가능
      - https://localhost:8080/index
      - 사용하지 않으면 hash mode로 설정(https://localhost:8080#index)

  ```
  # Vue Router 시작하기
   $ vue create vue-router-app
   $ cd vue-router-app
   $ vue add router

   history mode 사용여부 -> Yes

   => App.vue에 router-link 요소 및 router-view가 추가됨
   => router/index.js, views 폴더 생성됨
  ```

  - router-link
    - a 태그와 비슷한 기능 -> URL을 이동시킴
      - routes에 등록된 컴포넌트와 매핑됨
      - 히스토리 모드에서 router-link는 클릭 이벤트를 차단하여 a태그와 달리 브라우저가 페이지를 다시 로드하지 않도록 함
    - 목표 경로는 'to' 속성으로 지정됨
    - 기능에 맞게 HTML에서 a 태그로 rendering 되지만 필요에 따라 다른 태그로 바꿀 수 있음
  - router-view
    - 주어진 URL에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트
    - 실제 component가 DOM에 부착되어 보이는 자리를 의미
    - router-link를 클릭하면 routes에 매핑된 컴포넌트를 렌더링
    - Django에서의 block tag와 비슷함
      - App.vue는 base.html의 역할
      - router-view는 block 태그로 감싼 부분
  - src/router/index.js
    - 라우터에 관련된 정보 및 설정이 작성되는 곳
    - Django에서의 urls.py에 해당
    - routes에 URL와 컴포넌트를 매핑
  - src/Views
    - router-view에 들어갈 component 작성
    - 기존에 컴포넌트를 작성하던 곳은 components 폴더 뿐이었지만 이제 두 폴더로 나누어짐
    - 각 폴더 안의 .vue 파일들이 기능적으로 다른 것은 아님
    - views/
      - routes에 매핑되는 컴포넌트, 즉 <route-view>의 위치에 렌더링되는 컴포넌트를 모아두는 폴더
      - 다른 컴포넌트롸 구분하기 위해 View로 끝나도록 만드는 것을 권장
      - ex) App 컴포넌트 내부의 AboutView & HomeView 컴포넌트
    - components/
      - routes에 매핑된 컴포넌트의 하위 컴포넌트를 모아두는 폴더
      - ex) HomeView 컴포넌트 내부의 HelloWorld 컴포넌트

- Vue Router 실습

  - 선언적 방식 네이게이션
    - router-link의 'to' 속성으로 주소 전달 -> routes에 등록된 주소와 매핑된 컴포넌트로 이동
    - Namend Routes
      - 이름을 가지는 routes (Django 에서 path함수의 name 인자의 활용과 같은 방식)
    - 동적인 값을 사용하기 때문에 v-bind를 사용해야 정상적으로 작동
    ```vue
    // App.vue
    <router-link :to="{ name: 'home' }">Home</router-link>
    |
    <router-link :to="{ name: 'about' }">About</router-link>
    ```
  - 프로그래밍 방식 네비게이션

    - Vue 인스턴스 내부에서 라우터 인스턴스에 $router로 접근할 수 있음
    - 다른 URL로 이동하려면 this.$router.push를 사용
      - history stack에 이동할 URL을 넣는 push 방식
      - history stack에 기록이 남기 때문에 사용자가 브라우저의 뒤로 가기 버튼을 클릭하면 이전 URL로 이동할 수 있음
      - => <router-link :to="...">를 클릭하는 것과 $router.push(...)를 호출하는 것은 같은 동작

    ```vue
    // AboutView.vue
    <router-link :to="{ name: 'home' }">Home</router-link>
    <button @click="toHome">홈으로!</button>

    methods: { toHome() { this.$router.push({ name: "home" }) }, },
    ```

  - Dynamic Route Matching

    - 동적 인자 전달
      - URL의 특정 값을 변수처럼 사용할 수 있음
    - ex) Django에서의 variable routing

    ```vue
    // router/index.js import HelloView from "../views/HelloView.vue"
    {path:"/hello/:userName", name: "hello", component: HelloView, }, //
    HelloView.vue
    <h1>hello, {{ userName }}</h1>
    data() { return { userName: this.$route.params.userName, } },
    ```

    ```vue
    // AboutView.vue # AboutView에서 input한 data를 HelloView.vue의
    {{ userName }}에서 보이기

    <input type="text" v-model="inputData" @keyup.enter="goToHello" />

    data() { return { inputData: null, } }, methods: { goToHello() {
    this.$router.push({ name: "hello", params: { userName: this.inputData } })
    }, }
    ```

  - lazy-loading
    - 모든 파일을 한번에 로드하려고 하면 모든 걸 다 읽는 시간이 매우 오래 걸림
    - 미리 로드를 하지 않고 특정 라우트에 방문할 때 매핑된 컴포넌트의 코드를 로드하는 방식을 활용할 수 있음
      - 모든 파일을 한번에 로드하지 않아도 되기 때문에 최초에 로드하는 시간이 빨라짐
      - 당장 사용하지 않을 컴포넌트는 먼저 로드하지 않는 것이 핵심
    ```
    {
      // lazy-loading 방식 (첫 로딩에 렌더링 하지 않고 해당 라우터가 동작할 때 컴포넌트를 렌더링 한다.)
      path: "/about",
      name: "about",
      component: () =>
        import("../views/AboutView.vue"),
    },
    ```

### Navigation Guard

- 네비게이션 가드
  - Vue router를 통해 특정 URL에 접근할 때 다른 url로 redirect를 하거나 해당 URL로의 접근을 막는 방법
  - (ex. 사용자의 인증정보가 없으면 특정 페이지에 접근하지 못하게 함)
- 네비게이션 가드의 종류
  - 전역 가드: 애플리케이션 전역에서 동작
  - 라우터 가드: 특정 URL에서만 동작
  - 컴포넌트 가드: 라우터 컴포넌트 안에 정의
- 전역 가드
  - Global Before Guard
    - 다른 url 주소로 이동할 때 항상 실행
    - router/index.js에 router.beforeEach()를 사용하여 설정
    - 콜백 함수의 값으로 다음과 같이 3개의 인자를 받음
      - to: 이동할 URL 정보가 담긴 Route 객체
      - from: 현재 URL 정보가 담긴 Route 객체
      - next: 지정한 URL로 이동하기 위해 호출하는 함수
        - 콜백 함수 내부에서 반드시 한 번만 호출되어야 함
        - 기본적으로 to에 해당하는 URL로 이동
    - URL이 변경되어 화면이 전환되기 전 router.beforeEach()가 호출됨
      - 화면이 전환되지 않고 대기 상태가 됨
    - 변경된 URL로 라이팅하기 위해서는 next()를 호출해줘야 함
      - next()가 호출되기 전까지 화면이 전환되지 않음
- 라우터 가드
  - 전체 route가 아닌 특정 route에 대해서만 가드를 설정하고 싶을 때 사용
  - beforeEnter()
    - route에 진입했을 때 실행됨
    - 라우터를 등록한 위치에 추가
    - 단 매개변수, 쿼리, 해시 값이 변경될 때는 실행되지 않고 다른 경로에서 탐색할 때만 실행됨
    - 콜백 함수는 to, from, next를 인자로 받음
- 컴포넌트 가드
  - 특정 컴포넌트 내에서 가드를 지정하고 싶을 때 사용
  - beforeRouteUpdate()
    - 해당 컴포넌트를 렌더링하는 경로가 변경될 때 실행
- 404 Not Found
  - 사용자가 요청한 리소스가 존재하지 않을 때 응답
  - 요청한 리소스가 존재하지 않는 경우 모든 경로에 대해서 404 page로 redirect 시키기
    - 기존에 명시한 경로가 아닌 모든 경로가 404 page로 redirect 됨
    - 이 때 routes의 최하단부에 작성해야함

  - 형식은 유효하지만 특정 리소스를 찾을 수 없는 경우
    - ex) Django에게 이미 삭제한 articles/1/로 요청을 보냈을 때 path: '*'을 만나 404 page가 렌더링 되는 것이 아니라 기존에 명시한 articles/1/ 에 대한 components가 렌더링 됨 (설정해준 형식대로 형식은 맞기 때문에)
      - 하지만 데이터가 존재하지 않기 때문에 정상적으로 렌더링 되지 않음
      - -> 해결책 : 데이터가 없음을 명시, 404 page로 이동해야함

### Articles app with Vue
