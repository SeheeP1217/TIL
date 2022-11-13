# articles

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

1. Index 구현
  // 1.1 게시글 필드 설정하기
  // 1.2 IndexView 컴포넌트 및 라우터 작성
  // 1.3 state에서 불러온 articles 출력하기
  // 1.4 ArticleItem 컴포넌트 작성
  // 1.5 IndexView 컴포넌트에서 ArticleItem 컴포넌트 등록 및 props 데이터 전달
  // 1.6 props 데이터 선언 및 게시글 출력

2. Create 구현
  // 2.1 CreateView 컴포넌트 및 라우터 작성
  // 2.2 Form 생성 및 데이터 정의
  // 2.3 submit 이벤트 동작을 취소하기 (v-on) :{event}.prevent
  // 2.4 actions에 여러 개의 데이터를 넘길 때 하나의 object로 만들어서 전달
  // 2.5 actions에서는 넘어온 데이터를 활용하여 article 생성 후 mutations 호출
  // 2.6 mutations에서는 전달된 article 객체를 사용해 게시글 작성 (다음 게시글을 위해 article_id 값 1 증가)
  // 2.7 CreateView 컴포넌트에 Index 페이지로 이동하는 뒤로가기 링크 추가
  // 2.8 게시글 생성 후 Index 페이지로 이동하도록 네비게이터 작성
  // 2.9 IndexView 컴포넌트에 게시글 작성 페이지로 이동하는 링크 추가

3. Detail 구현
  // 3.1 DetailView 컴포넌트 및 라우터 작성 (id를 동적인자로 전달)
  // 3.2 article 정의 및 state에서 articles 가져오기
  // 3.3 articles에서 동적인자를 통해 받은 id에 해당하는 article 가져오기 (동적 인자를 통해 받은 id는 str이므로 형변환을 해서 비교)
  // 3.4 article 출력
  // 3.5 created lifecycle hook을 통해 인스턴스가 생성되었을 때 article을 가져오는 함수 호출
  // 3.6 글 작성시간을 로컬 시간으로 변환 (자정과의 시간 차이를 밀리초로 나타내는 정수 값인 상태)
  // 3.7 DetailView 컴포넌트에서 뒤로가기 링크 추가
  // 3.8 각 게시글을 클릭하면 detail 페이지로 이동하도록 ArticleItem에 이벤트 추가 (v-on 이벤트 핸들러에도 인자 전달 가능)

4. Delete 구현
  // 4.1 DetailView 컴포넌트에 삭제 버튼을 만들고, mutations를 호출
  // 4.2 mutations에서 id에 해당하는 게시글을 지움
  // 4.3 삭제 후 index 페이지로 이동하도록 네비게이션 작성

5. 404 Not Found 구현
  // 5.1 NotFound404 컴포넌트 및 라우터 작성 (Detail에 대한 route보다 먼저 등록해줘야함, /404로 등록 시 404번째 게시글과 혼동할 수 있음)
  // 5.2 DetailView 컴포넌트에 id에 대항하는 article이 없으면 404 페이지로 이동
  // 5.3 요청한 리소스가 존재하지 않는 경우 없는 id가 아닌 전혀 다른 요청에도 대비하여 404 page로 redirect 시키기
