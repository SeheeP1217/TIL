# 📖 chapter 1 - SQL 언어 series 1

## 📕 목차

- 관계형 데이터베이스 개요
- DCL
- DDL
- TCL
- DML (SELECT 외)

📙 📗 📘 📖 ⭕ ❌ ✔️ ▶️ ❗ ❓

## 📙 관계형 데이터베이스 개요

#### SQL 문장 종류

- DCL : Data Control Language
  - GRANT : 권한 부여
    ```
    [기본 문법]
    GRANT 권한
    ON    테이블
    To    유저;
    ```
  - REVOKE : 권한 회수
    ```
    [기본 문법]
    REVOKE  권한
    ON      테이블
    FROM    유저;
    ```
  ```
  ❗ [point 1] 권한의 종류
    SELECT
    INSERT
    UPDATE
    DELETE

    REFERENCES
    ALTER
    INDEX

    ALL
  ```
  ```
  [point 2] GRANT 옵션
    - TO 유저 WITH GRANT OPTION;
      --> 특정 사용자에게 권한 부여가능한 권한을 부여함
      --> 단, 엄마가 회수될 때 자식도 회수됨
    - TO 유저 WITH ADMIN OPTION; 
      --> 테이블에 대한 모든 권한 부여
      --> 엄마의 권한 회수는 나랑 상관 없음
  ```

- DDL : Data Definition Language
  - CREATE : 구조 생성
  - ALTER : 구조 변경
  - DROP : 구조 삭제
  - RENAME : 이름 변경
  - TRUNCATE : 테이블 초기화
- DML : Data Manipulation Language
  - INSERT : 데이터 입력
  - UPDATE : 데이터 수정
  - DELETE : 데이터 삭제
  - SELECT : 데이터 조회
