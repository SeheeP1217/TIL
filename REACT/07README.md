# 07-new-starting-project 정리본

## ROUTER

- 새로운 서드파티 패키지 설치 (npm install react-router-dom)

  - 새로운 HTML페이지를 불러오지 않고 URL을 통해 화면에 보이는 내용을 변경할 수 있도록 도와줌
  - 강의에서 사용하는 버전의 react-router 설치하기
    ```
    npm install --save react-router-dom@5
    ```

- 라우터는 특별한 도구로서 URL에서 변화를 감지하고 URL에 기초하여 화면에 보이는 내용을 변경해줌
  -> 라우터를 이용하면 사용자들을 페이지가 다시 로딩되는 듯 착각하게 만들 수 있음

---

## 폴더 구성

- component 안에 임베드 될 components는 components 폴더에 저장
- 페이지에 로딩될 컴포넌트들은 pages 폴더에 저장 -> URL을 방문했을 때 라우터가 로딩
- 컴포넌트 세팅

  ```js
  function AllMeetupsPage() {
    return <div>All Meetups Page</div>
  }

  export default AllMeetupsPage
  ```

---

## 라우터가 언제 어떤 페이지를 로딩할 것인지 정의

- index.js에 렌더링 되고 있는 App.js를 다른 컴포넌트로 감싸줘야함

  ```js
  // index.js

  import { BrowserRouter } from "react-router-dom"
  // BrouserRouter 은 컴포넌트

  ReactDOM.render(
    <BrowserRouter>
      <App />
    </BrowserRouter>,
    document.getElementById("root")
  )
  ```

- 라우터 패키지 초기화 (라우터가 이 앱을 인식, URL 감지하게 하는 것)

  ```js
  // App.js

  import { Route } from 'react-router-dom';
  // Route 도 BrouserRouter와 같은 컴포넌트
  // URL 내의 각기 다른 경로를 정의하고 각 경로별로 어떤 컴포넌트를 로딩할 건지 결정

  // 페이지에 로딩할 components을 import
  import AllMeetupsPage from './pages/AllMeetups';
  import FavoritesPage from './pages/Favorites';
  import NewMeetupPage from './pages/NewMeetup';

  function App() {
    return (<div>
  	  <Route path='/'>
        <AllMeetupsPage />
      </Route>
      <Route path="/new-meetup">
        <NewMeetupPage />
      </Route>
      <Route path="/favorites">
        <FavoritesPage />
      </Route>
      <!-- path에 URL에서 도메인(ex. localhost:3000/) 다음에 나올 경로 -->
    </div>);
  }

  export default App;
  ```
  - 지금 상태에서는 '/favorites'로 이동하면 '/', '/favorites'의 화면이 모두 렌더링 됨
  - 분리하기 위해서는 <switch>컴포넌트 사용하면 됨
    ```js
    import { Route, Switch } from "react-router-dom"

    function App() {
      // localhost:3000/
      // my-page.com/
      return (
        <div>
          <Switch>
            <Route path="/" exact={true}>
              <AllMeetupsPage />
            </Route>
            <Route path="/new-meetup">
              <NewMeetupPage />
            </Route>
            <Route path="/favorites">
              <FavoritesPage />
            </Route>
          </Switch>
        </div>
      )
    }
    ```
  - 하지만 URL과 page가 정확히 맞지 않음 ROUTE가 매칭되는 방법 때문
  - 리액트 라우터는 디폴트로 현재 경로의 URL로 page가 시작되는지 확인하고 있으면 멈춤
  - exact를 추가해서 정확한 경우의 page를 렌더링하도록 설정
    ```js
    function App() {
      // localhost:3000/
      // my-page.com/
      return (
        <div>
          <Switch>
            <Route path="/" exact={true}>
              <AllMeetupsPage />
            </Route>
            <Route path="/new-meetup">
              <NewMeetupPage />
            </Route>
            <Route path="/favorites">
              <FavoritesPage />
            </Route>
          </Switch>
        </div>
      )
    }
    ```

---

## 링크 및 탐색 추가하기

- 내비게이션 바 추가하기 
  - components 폴더 안에 layout 폴더를 생성해서 component 추가
  - 라우터를 통해 페이지에 로딩되는 것이 아니기 때문
  - 다른 코드들 안에 삽입될 것
  - Link
    - <a href="">태그를 사용하면 이동은 가능하지만 브라우저가 서버로 request를 한다.
    - 이를 방지하기 위한 것이 {LINK} 컴포넌트
    - react-router-dom이 클릭 리스너를 추가함
    - 추가 request 없이 페이지에 로드할 수 있음
  ```js
  import {Link} from 'react-router-dom'

  function MainNavigation() {
    return <header>
      <div>React Meetups</div>
      <nav>
        <ul>
          <li>
            <!-- Link에 이동할 경로를 설정하려면 to prop 추가 -->
            <Link to='/'>All Meetups</Link>
          </li>
          <li>
            <Link to='/new-meetup'>Add New Meetup</Link>
          </li>
          <li>
            <Link to='/favorites'>My Favorites</Link>
          </li>
        </ul>
      </nav>
    </header>
  }

  export default MainNavigation
  ```

- css 모듈로 스타일링 하기
  - css 모듈 : 스타일을 컴포넌트에 한정하는 기능
  - css 파일 이름을 ****.module.css 로 설정해야함 (ex. MainNavigation.module.css)
  - .js 파일에서 .css 파일을 import 하면 빌드 프로세스가 알아서 css 코드를 로딩되는 페이지에 추가해 줌
  ex. import classes from './MainNavigation.module.css';

- 데이터 목록 출력하기
  ```javascript
  const DUMMY_DATA = [
    {
      id: "m1",
      title: "This is a first meetup",
      image:
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Stadtbild_M%C3%BCnchen.jpg/2560px-Stadtbild_M%C3%BCnchen.jpg",
      address: "Meetupstreet 5, 12345 Meetup City",
      description:
        "This is a first, amazing meetup which you definitely should not miss. It will be a lot of fun!",
    },
    {
      id: "m2",
      title: "This is a second meetup",
      image:
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Stadtbild_M%C3%BCnchen.jpg/2560px-Stadtbild_M%C3%BCnchen.jpg",
      address: "Meetupstreet 5, 12345 Meetup City",
      description:
        "This is a first, amazing meetup which you definitely should not miss. It will be a lot of fun!",
    },
  ]

  <ul>
    {DUMMY_DATA.map((meetup) => {
      return <li key={meetup.id}>{meetup.title}</li>
    })}
  </ul>
  ```
  - .map인 자바스크립트 문법을 사용해서 DUMMY_DATA의 각 항목을 리스트로 각각 가져올 수 있다.
  - 리액트의 특성 상 리스트를 효과적으로 업데이트하고 렌더링 하기 위해서 key값(meetup.id)을 지정해줘야한다. 

- 리액트로 데이터베이스에 직접 접근하지 않는 이유는 보안 때문
- 모든 리액트 코드가 페이지를 방문하는 이들에게 노출됨
- 그래서 백엔드 API로 request를 보내야함