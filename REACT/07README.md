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