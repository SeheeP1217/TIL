# GIT

- Branch : 독립적으로 어떤 작업을 진행하기 위한 개념
    - Merge(병합)을 통해 합칠 수 있음
    
    - Git-flow
        - master, develop, feature, release, hotfix 브랜치로 구성
    - Github-flow
        - hotfix, feature를 구분하지 않고 master, feature 브랜치만 사용
        - 기능이 하나 구현될 때마다 master에 병합되어 배포
    - Gitlab-flow
        - master, pre-production, production으로 배포 전 staging 가능


- Commit
    - Jira 이슈번호 + 어떤 작업을 했는지

- Merge Request
    - 병합 대상 브랜치를 확인하고 merge
    - Title, description 약속하고 꼭 적는 걸 추천

- 충돌(Conflict) 방지
    - 다른 사람이 작성한 코드는 건딜이지 않고
    - git pull을 통해 원격 저장소와 로컬 저장소를 자주 동기화
    - commit & push 생활화
---
# Jira
- 이슈 추적을 위한 소프트 웨어

- 백로그 : 프로젝트에서 해야하는 일(요구사항)을 보여줌
- 스프린트 : 스크럼 보드의 개발 주기 단위
- 이슈 : Epic, Story, task, sub-tast, bug

- 백로그를 다 작성한 후 스프린트를 시작해야 번다운 차트가 정상적으로 시작함
    - 번다운 차트: story point 할당 후 차근차근 줄여나가기



