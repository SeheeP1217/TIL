# Vue CLI

### Node.js
- Node.js
  - 자바스크립트는 브라우저를 조작하는 유일한 언어
    하지만 브라우저 밖에서는 구동할 수 없었음
  - 자바스크립트를 구동하기 위한 런타임 환경인 Node.js로 인해 브라우저가 아닌 환경에서도 구동할 수 있게 됨
    - Browser만 조작 가능했으나, Server-Side-Programming, 여러 OS 환경에서 가능

- NPM (Node Package Manage)
  - 자바스크립트 패키지 관리자
    - Python에 pip가 있다면 Node.js에는 npm
    - pip와 마찬가지로 다양한 의존성 패키지를 관리
  - Node.js의 기본 패키지 관리자라 함께 설치됨

### Vue CLI
- Vue CLI
  - Vue 개발을 위한 표준 도구
  - 프로젝트의 구성을 도와주는 역할
  - 확장 플러그인, GUI, Bable 등 다양한 tool 제공
- Vue CLI Quick Start
  ```
  [실습]
  설치
  git bash에 npm install -g @vue/cli 입력

  (pull 받아서 nodemodules만 없는 경우는 폴더 안에서 npm install)

  프로젝트 생성
  vscode 터미널에 vue create vue-cli(프로젝트 이름) 입력
  키보드 위아래 움직여서 Default ([Vue 2]) 선택 enter

  생성된 프로젝트로 이동
  cd vue-cli

  서버 키기
  npm run serve

  (서버 끄는 법 ctrl+c)
  ```

- Vue CLI 프로젝트 구조
  - gitignore 파일이 이미 있고 git init이 이미 되어있는 상태로 생성됨
  - node_modules
    - node.js 환경의 여러 의존성 모듈
    - python의 venv와 비슷한 역할을 함 -> 따라서 .gitignore에 넣어주어야하며, vue 프로젝트를 생성하면 자동으로 추가됨
  - node-modules - Bable
    - "JavaScript compiler"
    - 자바스크립트의 ES6+ 코드를 구버전으로 번역/변환 해주는 도구
    - 자바스크립트의 파편화, 표준화의 영향으로 작성된 코드의 스펙트럼이 매우 다양
      - 최신 문법을 사용해도 브라우저의 버전 별로 동작하지 않는 상황이 발생
      - 버전에 따른 같은 의미의 다른 코드를 작성하는 등의 대응이 필요해졌고, 이러한 문제를 해결하기 위한 도구
      - 원시 코드(최신 버전)를 목적 코드(구 버전)으로 옮기는 번역기가 등장하면서 이상 코드가 특정 브라우저에서 동작하지 않는 상황에 대해 크게 고민하지 않 ###교재 다시 확인###
  - node-modules - Webpack
    - "static module bundler"
    - 모듈 간의 의존성 문제를 해결하기 위한 도구
    - 프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드함
  - Module
    - 개발하는 애플리케이션의 크기가 커지고 복잡해지면 파일 하나에 모든 기능을 담기가 어려워짐
    - 따라서 자연스럽게 파일을 여러 개로 분리하여 관리를 하게 되었고, 이때 분리된 파일 각각이 모듈(module) 즉, js 파일 하나가 하나의 모듈
    - 모듈은 대개 기능 단위로 분리하며, 클래스 하나 혹은 특정한 목적을 가진 복수의 함수로 구성된 라이브러리 하나로 구성됨
    - 여러 모듈 시스템 (ESM(ECMA Script Module), AMD, CommonJS 등)
  - Module 의존성 문제
    - 모듈이 수가 많아지고 라이브러리 혹은 모듈 간의 의존성(연결성)이 깊어지면서 특정한 곳에서 발생한 문제가 어떤 모듈 간의 문제인지 파악하기 어려움
      - Webpack은 이 모듈간의 의존성 문제를 해결하기 위해 등장
  - Bundler
    - 모듈 의존성 문제를 해결해주는 작업이 Bundling
    - 이러한 일을 해주는 도구가 Bundler이고, Webpack은 다양한 Bundler 중 하나
    - 모듈들을 하나로 묶어주고 묶인 파일은 하나(혹은 여러개)로 만들어짐
    - Bundling된 결과물은 개별 모듈의 실행 순서에 영향을 받지 않고 동작하게 됨
    - snowpack, parcel, rollup.js 등의 webpack 이외에도 다양한 모듈 번들러 존재
    - Vue CLI는 이러한 Babel, Webpack에 대한 초기 설정이 자동으로 ###교재 다시 확인###
  - Webpack - static module bundler
    - 의존성을 Webpack이 담당해주므로 개발자는 npm install을 사용해 다양한 모듈을 한번에 설치하고 각 모듈을 사용해 개발에 집중할 수 있음
  - package.json
    - 프로젝트의 종속성 목록과 지원되는 브라우저에 대한 구성 옵션을 포함
  - package-lock.json
    - node_modules에 설치되는 모듈과 관련된 모든 의존성을 설치 및 관리
    - 협업 및 배포 환경에서 정확히 동일한 종속성을 설치하도록 보장하는 표현
    - 사용할 패키지의 버전을 고정
    - 개발 과정 간의 의존성 패키징 충돌 방지
    - python의 requirements.txt 역할
  - public/index.html
    - Vue 앱의 뼈대가 되는 html 파일
    - Vue 앱과 연결될 요소가 있음
  - src/
    - src/assets : 정적 파일을 저장하는 디렉토리
    - src/components : 하위 컴포넌트들이 위치
    - src/App.vue : 최상위 컴포넌트, public/index.html과 연결됨
    - src/main.js
      - webpack이 빌드를 시작할 때 가장 먼저 불러오는 entry point
      - public/index.html ###교재 다시 확인###

### Component
- Component
  - UI를 독립적이고 재사용 가능한 조각들로 나눈 것
    - 즉, 기능별로 분화한 코드 조각
  - CS에서는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소를 의미
  - 하나의 app을 구성할 때 중첩된 컴포넌트들의 tree로 구성하는 것이 보편적임
    - Web시간에 배운 HTML 요소들의 중첩을 떠올리면 Body tag를 root node로 하는 tree의 구조
      마찬가지로, Vue에서는 src/App.vue를 root node로 하는 tree의 구조를 띔
  - ###교재 다시 확인###
  - 우리가 사용하는 웹서비스도 여러개의 컴포넌트로 이루어져 있음
  - 하나의 컴포넌트를 만들어두면 반복되는 UI를 쉽게 처리할 수 있음

- Django에서의 예시
  - 우리는 base.html과 index.html을 분리하여 작성하였지만, 하나의 화면으로 볼 수 있다.
    - 즉, 한 화면은 여러 개의 컴포넌트로 이루어질 수 있음
  ###교재 다시 확인###
  - index.html에서 for문을 통해 여러 게시글들을
  ###교재 다시 확인###

- Componet based architecture 특징
###교재 다시 확인###

### SFC
- component in Vue
  - Vue에서 말하는 component = 이름이 있는 재사용 가능한 Vue instance
  - Vue instance = new Vue()로 만든 인스턴스

- SFC (Single File Component)
  - 하나의 .vue 파일이 하나의 Vue instance이고, 하나의 컴포넌트이다
    - 즉, Single File Component
  - Vue instance에서는 HTML, CSS, JavaScript 코드를 한번에 관리,
    - 이 Vue instance를 기능 단위로 작성하는 것이 핵심!
  - 컴포넌트 기반 개발의 핵심 기능

### Vue component
- Vue component 구조
  - 템플릿(HTML)
    - HTML의 body 부분
    - 눈으로
    ###교재 다시 확인###
  - 스크립트(JavaScript)
    - JavaScript 코드가 작성되는 곳
    - 컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스를 구성하는 대부분이 작성 됨
  - 스타일(CSS)
    - CSS가 작성되며 컴포넌트의 스타일을 담당

  - 컴포넌트들이 tree 구조를 이루어 하나의 페이지를 만듦
  - root에 해당하는 최상단의 component가 App.vue
  - 이 App.vue를 index.html과 연결
  - 결국 index.html 파일 하나만을 rendering
    - 이게 바로 SPA

- Vue component 등록
  1. 불러오기
    : import {instance name} from {위치}
    : instance name은 instance생성 시 작성한 name
    : @는 src의 shortcut
    : .vue 생략 가능
  2. 등록하기
  3. 보여주기

```
[실습]
- src/components/ 안에 컴포넌트 생성 Mycomponent.vue (vue + enter하면 기본 형태 생김(확장프로그램))
- MyComponent.vue의 script에 'MyComponent' 이름 등록
  <script>
  export default {
    name: 'MyComponent',
  }
  </script>
- template에 요소 추가
  <template>
    <div>
      <h1>이거는 내가 만든 새로운 컴포넌트다!</h1>
    </div>
  </template>

- component 등록 - 불러오기
  // 1. 불러오기
  // import MyComponent from './components/MyComponent.vue'

  // 절대 경로로 바꾸고, 확장자명 생략 가능
  import MyComponent from '@/components/MyComponent'

- component 등록 - 등록하기
  export default {
    name: 'App',
    components: {
      HelloWorld,
      // 2. 등록하기
      MyComponent
    }
  }

- component 등록 - 보여주기
  - 닫는 태그만 있는 요소처럼 사용
  <template>
    <div id="app">
      <img alt="Vue logo" src="./assets/logo.png">
      <!-- 3. 보여주기 (닫는 태그만 있는 요소처럼 사용) -->
      <MyComponent/>
      <HelloWorld msg="Welcome to Your Vue.js App"/>
    </div>
  </template>
```

- 자식 컴포넌트 작성
```
# MyComponentItem.vue
<template>
    <div>
      <h3>나는 MyComponent의 하위 컴포넌트</h3>
    </div>
</template>

<script>
export default {
  name: 'MyComponentItem'
}
</script>

# MyComponent.vue
<template>
  <div class="border">
    <h1>이거는 내가 만든 새로운 컴포넌트다!</h1>
    <MyComponentItem/>
  </div>
</template>

<script>
import MyComponentItem from '@/components/MyComponentItem'

export default {
  name: 'MyComponent',
  components: {
    MyComponentItem
  }
}
</script>
```

### Pass Props & Emit Events
- Data in components
  - 우리는 정적 웹페이지가 아닌, 동적 웹페이지를 만들고 있음
    - 즉, 웹페이지에서 다뤄야 할 데이터가 등장
    - user data, 게시글 data, 등등
  - 한 페이지 내에서 같은 데이터를 공유해야함
    - 하지만 페이지들은 component로 구분이 되어있음
  - MyComponent에 정의된 data를 MyChild에서 사용하기 (완전히 같은 data를 서로 다른 component에서 보여주기)
    - 필요한 컴포넌트들끼리 데이터를 주고받으면 데이터의 흐름을 파악하기 힘듦, 개발 속도 저하, 유지보수 난이도 증가
    - 컴포넌트는 부모-자식 관계를 가지고 있으므로, 부모-자식 관계만 데이터를 주고 받으면 데이터의 흐름을 파악하기 용이, 유지보수 쉬워짐
    - 부모 -> 자식 데이터 흐름 : pass props 방식
    - 자식 -> 부모 데이터 흐름 : emit event 방식

- Pass Props
  - 요소의 속성(property)을 사용하여 데이터를 전달
  - props는 부모(상위)컴포넌트의 정보를 전달하기 위한 사용자 지정 특정
  - 자식(하위) 컴포넌트는 props 옵션을 사용하여 수신하는 props를 명시적으로 선언해야 함
  - ###교재 다시 확인###
  - 이때 속성의 키 값은 kebab-case를 사용 (보내는 html은 대소문자를 구별하지 않는데 받는 JS는 구별하므로 -으로 구분해야함)

  ```
  1. 보내주기
  #MyComponent.vue template의 <MyComponent/>을 
  <MyComponentItem static-props="MyComponent에서 보낸 데이터"/> 로 수정
  
  2. 받기
  #MyComponentItem.vue script에 props 추가
  <script>
  export default {
    name: 'MyComponentItem',
    props: {
      staticProps: String,
    }
  }
  </script>

  3. 사용하기
  #MyComponentItem.vue template에 추가
  <p>{{staticProps}}</p>
  ```
  - Pass Props convention
  - Dynamic props
  - Emit Event
    ```
    [실습]
    #MyComponent script의 export default에 추가
      data: function () {
        return {
          dynamicProps: '이건 동적인 데이터!',
        }
      }

    # template의 MyComponentItem에 추가
    :dynamic-props="dynamicProps"


    # Vue CLI에서는 아래 형식으로 데이터를 넣어줘야함(스코프문제 때문)
    data: function () {
      return {

      }
    }

    # MyComponentItem script의 export default에 추가
    props: {
      staticProps: String,
      dynamicProps: String,
    }

    # template에 추가
    <p>{{dynamicProps}}</p>
    ```
  - 컴포넌트의 data 함수
  - Pass Props
  - 단방향 데이터의 흐름

- Emit Event
  - $emit
    ```
    # 위아래로 한단계씩만 움직일 수 있다.

    # MyComponentItem template에 button 생성, script에 method 추가
      <button @click="childToParent">클릭!</button>
      methods: {
        childToParent: function () {
          this.$emit('give-me-ma-money',  '나는 자식이 보낸 데이터다')      //kebab인 이유는 script에서 보내고 html에서 받을 것이기 때문 // 'give-me-ma-money'는 이름, '나는 자식이 보낸 데이터다'는 보낼 데이터(data: {}를 만들어서 받아 보낼 수 있다.)
        }
      }

    # MyComponent template에서 kebab 받기
      <MyComponentItem 
        static-props="MyComponent에서 보낸 데이터"
        :dynamic-props="dynamicProps"
        @give-me-ma-money="parentGetEvent"
      />

    # MyComponent script에서 받기
      methods: {
        parentGetEvent: function (childData) {
          console.log('용돈 없어!!')            ->childData는 $emit에서 보낸 데이터를 의미
          console.log(childData)
        }
      }
    ```

  - emit with data
  - emit with dynamic data
    ```
    [실습]
    # MyComponentItem의 template에 생성, script-methods에 추가
      <input 
        type="text" 
        v-model="childInputData"
        @keyup.enter="childInput"
      >

      childInput: function name() {
        this.$emit('child-input', this.childInputData)
        this.childInputData = null  //입력 후 데이터 입력창 비우기
      }

    # MyComponent의 template에 추가
      @child-input="getDynamicData"
    # MyComponent의 script-method에 추가
      getDynamicData: function (childInputData) {
        console.log(`사용자가 입력한 값은 ${childInputData}입니다.`)
      }

    ```
