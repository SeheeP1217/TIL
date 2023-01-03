# Vue

### Vue with DRF
- Server & Client
  - Server
    - 클라이언트에게 정보와 서비스를 제공하는 컴퓨터 시스템
    - 서비스 전체를 제공 == Django Web Service
      - Django를 통해 전달받은 HTML에는 하나의 웹 페이지를 구성할 수 있는 모든 데이터가 포함
      - 즉, 서버에서 모든 내용을 렌더링 하나의 HTML 파일로 제공
      - 정보를 포함한 web 서비스를 구성하는 모든 내용을 서버 측에서 제공
    - 정보를 제공 == DRF API Service
      - Django를 통해 관리하는 정보만을 클라이언트에게 제공
      - DRF를 사용하여 JSON으로 변환
  - Client
    - Server가 제공하는 서비스에 적절한 요청을 통해 Server로부터 반환 받은 응답을 사용자에게 표현하는 기능을 가진 프로그램 혹은 시스템
    - Server가 제공하는 서비스에 적절한 요청
      - Server가 정의한 방식대로 요청 인자를 넘겨 요청
      - Server는 정상적인 요청에 적합한 응답 제공
    - Server로부터 반환 받은 응답을 사용자에게 표현
      - 사용자의 요청에 적합한 data를 server에 요청하여 응답 받은 결과로 적절한 화면을 구성
  - Server는 정보화 서비스를 제공 (DB와 통신하며 데이터를 생성, 조회, 수정, 삭제를 담당)
  - Client는 사용자의 정보 요청을 처리, server에게 응답 받은 정보를 표현(Server에게 정보(데이터)를 요청)

- Again DRF
- Vue with DRF
### CORS 
- CORS(Cross-Origin Resource Sharing)
  - 브라우저가 요청을 보내고 서버의 응답이 브라우저에 도착해서 Server는 정상적으로 응답했지만 브라우저가 막은 것
  - 보안 상의 이유로 브라우저는 동일 출처 정책(SOP)에 의해 다른 출처의 리소스와 상호작용 하는 것을 제한함
  - SOP(Same - Origin Policy)
    - "동일 출처 정책"
    - 불러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호작용하는 것을 제한하는 보안 방식
    - 잠재적으로 해로울 수 있는 문서를 분리함으로써 공격받을 수 있는 경로를 줄임
  - Origin - "출처"
    - URL의 Protocol, Host, Port를 모두 포함하여 출처라고 부름 (ex. http://localhost:3000/ 이 일치하면 동일 출처로 인정)
  - CORS - 교차 출처 리소스 공유
    - 추가 HTTP Header를 사용하여, 특정 출처에서 실행 중인 웹 어플리케니션이 다른 출처의 자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 체제 (어떤 출처에서 자신의 컨텐츠를 불러갈 수 있는지 서버에 지정할 수 있는 방법)
    - 리소스가 자신의 출처와 다를 때 교차 출처 HTTP 요청을 실행
      - 만약 다른 출처의 리소스를 가져오기 위해서는 이를 제공하는 서버가 브라우저에게 다른 출처지만 접근해도 된다는 사실을 알려야 함
      - "교차 출처 리소스 공유 정책 (CORS policy)"
        - 다른 출처에서 온 리소스를 공유하는 것에 대한 정책
        - CORS policy에 위배되는 경우 브라우저에서 해당 응답 결과를 사용하지 않음 (Server에서 응답을 주더라도 브라우저에서 거절)
        - 다른 출처의 리소스를 불러오려면 그 출철에서 올바른 CORS header를 포함한 응답을 반환해야함
- How to set CORS
  - CORS 표준에 의해 추가된 HTTP Response Header를 통해 이를 통제 가능
  - Access-Control-Allow-Origin : 단일 출처를 지정하여 브라우저가 해당 출처가 리소스에 접근하도록 허용

- Vue with DRF(feat.CORS)
  - Article Read
  - Article Create
  - Article Detail


### DRF Auth System
- Authentication & Authorization
  - Authentication - 인증, 입증
    - 자신이라고 주장하는 사용자가 누구인지 확인하는 행위
    - 모든 보안 프로세스의 첫번째 단계 (가장 기본 요소)
    - 401 Unauthorized(미승인(unauthorized)라고 하지만 의미상 비인증(unauthenticated)을 의미)
  - Authorization - 권한 부여, 허가
    - 사용자에게 특정 리소스 또는 기능에 대한 액세스 권한을 부여하는 과정
    - 보안 환경에서 권한 부여는 항상 인증이 먼저 필요함
      - 사용자는 조직에 대한 액세스 권한을 부여 받기 전에 먼저 자신의 ID가 진짜인지 먼저 확인해야 함
    - 서류의 등급, 웹 페이지에서 글을 조회&삭제&수정할 수 있는 방법, 제한 구역
      - 인증이 되었어도 모든 권한을 부여 받는 것은 아님
    - 403 Forbidden
      - 401과 다른 점은 서버는 클라이언트가 누구인지 알고 잇음
  - Authentication and authorization work together
    - 회원가입 후, 로그인 시 서비스를 이용할 수 있는 권한 생성 (인증 이후에 권한이 따라오는 경우가 많음)
    - 단, 모든 인증을 거쳐도 권한이 동일하게 부여X (다른 사람의 글 수정 삭제 불가능)
    - 세션, 토큰, 제 3자를 활용하는 등의 다양한 인증 방식이 존재
- How to authentication determined
  - 인증 여부 확인 방법
    - DRF 공식문서에서 제안하는 인증 절차 방법이 있음
    - TokenAuthentication 으로 모든 상황에 대한 인증 방식을 정의 (각 요청에 따라 다른 인증 방식을 거치고자 한다면 다른 방식이 필요)
  - 다양한 인증 방식
    - Basic Authentication : 가장 기본적인 수준의 인증 방식, 테스트에 적합
    - Session Authentication : Django에서 사용하였던 session 기반의 인증 시스템, DRF와 Django의 session 인증 방식은 보안적 측면을 구성하는 방법에 차이가 있음
    - RemoteUserAuthentication : Django의 Remote user 방식을 사용할 때 활용하는 인증 방식
    - TokenAuthentication : 매우 간단하게 구현할 수 있음, 기본적인 보안 기능 제공, 다양한 외부 패키지가 있음
      - settings.py에서 DEFAULT_AUTHENTICATION_CLASSES를 정의 (TokenAuthentication 인증 방식을 사용할 것임을 명시)
  - TokenAuthentication 사용 방법
    ```
    1. INSTALLED_APPS에 rest_framework.authtoken 등록
      INSTALLED_APPS = {
        ...
        'rest_framework.authtoken
      }

    2. 각 User마다 고유 Token 생성
      from rest_framework.authtoken.models import Token
      
      token = Token.objects.create(user=...)
      print(token.key)
    
    3. 생성한 Token을 각 User에게 발급
      - User는 발급 받은 Token을 요청과 함께 전송
      - Token을 통해 User 인증 및 권한 확인

    4. Token 발급 방법
      def some_view_func(request):
        token = Token.objects.create(user=...)
        return Response({ 'token': token.key })

    5. User는 발급 받은 Token을 headers에 담아 요청과 함께 전송
      - 단, 반드시 Token 문자열 함께 삽입 (Token 문자열과 발급받은 실제 token 사이를 ' '(공백)으로 구분)
      - ex) Authorization: Token {발급받은 실제 token}
    ```
  - 토큰 생성 및 관리 문제접
    - 기본 제공 방식에서 고려하여야 할 사항들
      1. Token 생성 시점
      2. 생성한 Token 관리 방법
      3. User와 관련된 각종 기능(회원가입, 로그인, 회원 정보 수정, 비밀번호 변경 등) 관리 방법

- dj-rest-auth
  - 회원가입, 인증(소셜미디어 인증 포함), 비밀번호 재설정, 사용자 세부 정보 검색, 회원 정보 수정등을 위한 REST API end point 제공
  - dj-rest-auth 사용 방법
    ```
    1. 패키지 설치
      pip install dj-rest-auth
    
    2. App 등록
      INSTALLED_APPS = [
        'dj_rest_auth'
      ]
    
    3. URL 등록
      urlpatterns = [
        path('dj-rest-auth/', include('dj_rest_auth.urls'))
      ]
    ```
  - Registration
    - Registration 기능을 사용하기 위해 추가 기능 등록 및 설치 필요
    - dj-rest-auth의 회원가입 기능을 사용하기 위해서는 django-allauth 필요 
    - django-allauth 설치
      ```
      1. 패키지 설치
        pip install 'dj-rest-auth[with_social]'
      2. App 등록
        INSTALLED_APPS = [
          'django.contrib.sites',
          'allauth',
          'allauth.account',
          'allauth.socialaccount',
          'dj_rest_auth.registration',
        ]
      3. URL 등록
        urlpatterns = [
          path('accounts/signup/', include('dj_rest_auth.registration.urls'))
        ]
      4. python manage.py migrate
      ```
  - permission setting
    - 권한 세부 설정
      1. 모든 요청에 대해 인증을 요구하는 설정
      2. 모든 요청에 대해 인증이 없어도 허용하는 설정
    - 설정 위치 == 인증 방법을 설정한 곳과 동일
      - 우선 모든 요청에 대해 허용 설정
      ```
      'DEFAULT_PERMISSION_CLASSES' : [
        'rest_framework.permission.AllowAny',
      ]

      REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
          'rest_framework.permissions.AllowAny',
        ]
      }
      ```

  - Article List Read
  - Article Create
  - Article Detail Read

### DRF Auth with Vue
- Signup Page
- SignUp Request
- 토큰 관리
  - 게시물 전체 조회와 달리, 인증 요청의 응답으로 받은 Token은 매번 요청하기 힘들고 비밀번호를 항상 보관하고 있을 수는 없음
  - localStorage에 token 저장을 위해 vuex-persistedstate 활용
  ```
  1. 패키지 설치
    npm install vuex-persistedstate

  2. store/index.js
    import createPersistedState from 'vuex-persistedstate'

    export default new Vuex.Store({
      plugins: [
        createPersistedState(),
      ]
    })
  ```
  - User 인증 정보는 localStorage에 저장할 때 쿠키를 사용해 관리하거나 로컬 저장소를 난독화하여 관리해야한다.
- Login Page
- Login Request
- IsAuthenticated in Vue
  - 회원가입, 로그인 요청에 대한 처리 후 state에 저장된 Token을 직접 확인하기 전까지 인증 여부 확인 불가
  - 인증되지 않았을 시 게시글 정보를 확인할 수 없으나 이유를 알 수 없음 (로그인 여부를 확인할 수 있는 수단이 없음)
- Request with Token
  - Article List Read with Token
  - Article Create with Token
  - Create Article with User

### DRF-spectacular
- swagger
  - 스웨거는 개발자가 REST 웹 서비스를 설계, 빌드, 문서화, 소비하는 일을 도와주는 오픈소스 소프트웨어 프레임워크
  - 즉, API를 설계하고 문서화하는데 도움을 주는 라이브러리
  - 스웨거를 생성할 수 있도록 도움을 주는 라이브러리 : DRF-spectacular

- DRF-spectacular
  - Open API 3.0을 지원하는 DRF API OpenAPI 생성기
  ```
  1. 설치
    pip install drf-spectacular
    pip freeze > requirements.txt

  2. 등록
  INSTALLED_APPS = [
    'drf_spectacular',
  ]
  ```