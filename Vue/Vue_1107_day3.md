# Vue

### Vuex

- State Management
  - State(상태)란? 현재에 대한 정보(data)
  - Web Application 상태는 현재 App이 가지고 있는 Data로 표현 가능
  - 여러 component가 하나의 App을 만들고 있기 때문에 여러 개의 component가 같은 상태(data)를 유지할 필요가 있음 -> State Management(상태 관리) 필요
- Pass Props & Emit Event
  - 각 컴포넌트는 독립적으로 데이터를 관리
  - 같은 데이터는 공유하고 있으므로, 각 컴포넌트가 동일한 상태를 유지하고 있음
  - 데이터의 흐름을 직관적으로 파악 가능
  - 그러나 component의 중첩이 깊어지면 데이터 전달이 쉽지 않음
  - 공통의 상태를 유지해야 하는 component가 많아지면 데이터 전달 구조가 복잡해짐
- Centrlaized Store
  - 중앙 저장소(store)에 데이터를 모아서 상태 관리
  - 각 component는 중앙 저장소의 데이터를 사용
  - component의 계층에 상관없이 중앙 저장소에 접근해서 데이터를 얻거나 변경할 수 있음
  - 중앙 저장소의 데이터가 변경되면 각각의 component는 해당 데이터의 변화에 반응하여 새로 변경된 데이터를 반영함
  - 규모가 크거나 컴포넌트 중첩이 깊은 프로젝트의 관리가 매우 편리
- Vuex

  - "state management pattern + Library" for vue.js (상태 관리 패턴 + 라이브러리)
  - 중앙 저장소를 통해 상태 관리를 할 수 있도록 하는 라이브러리
  - 데이터가 예측 가능한 방식으로만 변경될 수 있도록 하는 규칙을 설정하며, Vue의 반응성을 효율적으로 사용하는 상태 관리 기능을 제공
  - Vue의 공식 도구로써 다양한 기능을 제공

  ```
  [실습] - vuex 시작하기
  $ vue create vuex-app
  $ cd vuex-app
  $ vue add vuex (-> y 선택)
  ```

- vuex의 핵심 컨셉 4가지

  1. State

  - vue 인스턴스의 data에 해당
  - 중앙에서 관리하는 모든 상태 정보
  - 개별 component는 state에서 데이터를 가져와서 사용
    - 개별 component가 관리하던 data를 중앙저장소(Vuex Store의 state)에서 관리하게 됨
  - state의 데이터가 변화하면 해당 데이터를 사용(공유)하는 component도 자동으로 다시 렌더링
  - $store.state로 state 데이터에 접근
  - Mutations만 state에 영향을 미침

  ```
  [실습1] - 중앙저장소에 있는 state에 접근하는 방법
  #index.js
    state: {
      // 중앙에서 관리하는 모든 상태 정보
      // $store.state로 접근 가능
      // store의 state에 message 데이터 정의
      message: 'message in store'
    },

  #App.vue
    <template>
      <div id="app">
        <h1>{{ message }} </h1>
      </div>
    </template>

    <script>
    export default {
      name: 'App',
      components: {
      },
      computed: {
        message() {
          return this.$store.state.message
        }
      }
    }
    </script>
  ```

  2. Mutations

  - 실제로 state를 변경하는 유일한 방법
  - vue 인스턴스의 methods에 해당하지만 Mutations에서 호출되는 핸들러(handler) 함수는 반드시 동기적이어야 함
    - 비동기 로직으로 mutations를 사용해서 state를 변경하는 경우, state의 변화의 시기를 특정할 수 없기 때문
  - 첫번째 인자로 state를 받으며, component 혹은 Actions에서 commit()메서드로 호출됨

  ```
  [실습3] - state 변경하기
  #index.js
    mutations: {
      CHANGE_MESSAGE(state, newMessage) {
        // console.log(state)
        // console.log(newMessage)
        state.message = newMessage
      }
    },
    actions: {
      changeMessage(context, newMessage) {
        // console.log(context)
        // console.log(newMessage)
        // context.commit('호출하고자 하는 mutations 메서드 이름', 추가데이터)
        context.commit('CHANGE_MESSAGE', newMessage)
      }
    },
  ```

  3. Actions

  - mutations와 비슷하지만 비동기 작업을 포함할 수 있다는 차이가 있음
  - state를 직접 변경하지 않고 commit()메서드로 mutations를 호출해서 state를 변경함
  - context 객체를 인자로 받으며, 이 객체를 통해 store.js의 모든 요소와 매서드에 접근할 수 있음 (== 즉, state를 직접 변경할 수 있지만 하지 않아야 함)
  - component에서 dispatch() 메서드에 의해 호츨됨

  ```
  [실습2] - 입력을 통해 message 값 바꾸기
  #App.vue
    <template>
      <div id="app">
        <h1>{{ message }} </h1>
        <input
          type="text"
          @keyup.enter="changeMessage"
          v-model="inputData"
        >
      </div>
    </template>

    <script>
    export default {
      name: 'App',
      data() {
        return {
          inputData: null,
        }
      },
      components: {
      },
      computed: {
        message() {
          return this.$store.state.message
        }
      },
      methods: {
        changeMessage() {
          const newMessage = this.inputData
          // this.$store.dispatch('액션 메서드 이름', 추가데이터)
          this.$store.dispatch('changeMessage', newMessage)
        }

      }
    }
    </script>

  #index.js
    actions: {
      changeMessage(context, newMessage) {
        console.log(context)
        console.log(newMessage)
      }
    },
    // actions의 첫번째 인자는 context(store의 전반적인 속성을 모두 가지고 있으므로 context.state와 context.getters를 통해 mutations를 호출하는 것이 모두 가능)
    // actions에서 state를 직접 조작하는 것은 삼가야 함
    // actions의 두번째 인자는 payload(넘겨준 데이터를 받아서 사용)
  ```

  - +) Mutations & Actions
    - vue component의 methods 역할이 vuex에서는 아래와 같이 분화됨
    - Mutations: state를 변경
    - Actions: state 변경을 제외한 나머지 로직

  4. Getters

  - vue 인스턴스의 computed에 해당
  - state를 활용하여 계산된 값을 얻고자 할 때 사용, state의 원본 데이터를 건들지 않고 계산된 값을 얻을 수 있음
  - computed와 마찬가지로 getters의 결과는 캐시(cache) 되며, 종속된 값이 변경된 경우에만 재계산됨
  - getters에서 계산된 값은 state에 영향을 미치지 않음
  - 첫번째 인자로 state, 두번째 인자로 getter를 받음

  ```
  [실습4] - state 길이 재는 문구 작성하기
  #index.js
    getters: {
      messageLength(state) {
        return state.message.length
      }
    // 첫번쨰 인자는 state, 두번쨰 인자는 getters
    // messageLength를 이용해서 새로운 값을 계산
      doubleLength(state, getters) {
        return getters.messageLength * 2
      },
    },

  #App.vue
    <h2>입력된 문자의 길이는 {{ messageLength }}</h2>
    <h3>문자 길이 2배 {{doubleLength}} </h3>

    computed: {
      message() {
        return this.$store.state.message
      },
      messageLength() {
        return this.$store.getters.messageLength
      },
      doubleLength() {
        return this.$store.getters.doubleLength
      }
    },
  ```

  ```
  [정리]
  state : 중앙에서 관리하는 모든 상태 정보
  mutations : state를 변경하기 위한 methods (동기 작업만 가능)
  actions : 비동기 작업이 포함될 수 있는 (외부 API와의 소통 등) methods, state를 변경하는 것 외의 모든 로직 진행
  getters : state를 활용해 계산된 새로운 변수 값

  component에서 데이터를 조작하기 위한 데이터의 흐름: component => (actions) => mutations => state
  component에서 데이터를 사용하기 위한 데이터의 흐름: state => (getters) => component
  ```

### Lifecycle Hooks

- Lifecycle Hooks

  - 각 Vue 인스턴스는 생성과 소멸의 과정 중 단계별 초기화 과정을 거침
    - Vue 인스턴스가 생성된 경우, 인스턴스를 DOM에 마운트하는 경우, 데이터가 변경되어 DOM을 업데이트하는 경우 등
  - 각 단계가 트리거가 되어 특정 로직을 실행할 수 있음
  - Lifecycle Hooks는 컴포넌트별로 정의할 수 있음
  - 특징
    - 부모 컴포넌트의 mounted hook이 실행되었다고 해서 자식이 mount 된 것이 아니고, 부모 컴포넌트가 updated hook이 실행되었다고 해서 자식이 updated 된 것이 아님
      - 부착 여부가 부모-자식 관계에 따라 순서를 가지고 있지 않은 것
    - instance마다 각각의 Lifecycle을 가지고 있기 때문

- create
  - Vue instance가 생성된 후 호출됨
  - data, computed 등의 설정이 완료된 상태
  - 서버에서 받은 데이터를 vue instance의 data에 할당하는 로직을 구현하기 적합
  - 단, mount 되지 않아 요소에 접근할 수 없음
  - JavaScript에서 학습한 Dog API 활용 실습의 경우 버튼을 누르면 강아지 사진을 보여줌 -> 버튼을 누르지 않아도 첫 실행 시 기본 사진이 출려되도록 하고 싶다면 created 함수에 강아지 사진을 가져오는 함수를 추가
- mounted
  - Vue instance가 요소에 mount 된 후 호출 됨
  - mount 된 요소를 조작할 수 있음
  - created의 경우, mount 되기 전이기 때문에 DOM에 접근할 수 없으므로 동작하지 않음
- updated
  - 데이터가 변경되어 DOM에 변화를 줄 때 호출됨

[Vue_1107_day3_DogAPI 폴더]

### Todo with Vuex

[Vue_1107_day3_TodoList 폴더]

- Local Storage (브라우저의 Local Storage에 todo 데이터를 저장하여 데이터 보존하기)
  - Window.localStorage
    - 브라우저에서 제공하는 저장공간 중 하나인 Local Storage에 관련된 속성
    - 만료되지 않고 브라우저를 종료하고 다시 실행해도 데이터가 보존됨
    - 데이터가 문자열 형태로 저장됨
    - 관련 메서드
      - setItem(key, value) - key, value 형태로 데이터 저장
      - getItem(key) - key에 해당하는 데이터 조회
