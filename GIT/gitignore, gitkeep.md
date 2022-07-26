# gitignore / gitkeep
보안 관련 파일이나 쓸모 없는 파일은 굳이 git에 commit할 필요가 없다.
하지만 commit할 파일을 일일이 적는 것은 번거로운 일

commit하지 않을 파일을 .gitignore에 적어놓으면 된다.
repository를 처음 생성할 때 .gitignore을 일단 만들어 두어야 한다.

1. vscode 탐색기에서 파일 추가
  파일이름: .gitignore

2. .gitignore에 들어가서 add하지 않을 파일이나 폴더 이름 적기
  텍스트파일: test.txt
  폴더: del/
  텍스트파일 모두: *.txt

3. 폴더 안에 .gitignore 파일만 있다면 폴더도 commit 되지 않는다.
  commit하고 싶다면 폴더 안에 .gitkeep 을 만들어주면 push 가능

4. 프로젝트를 하거나 다른 프로그램을 사용하면서 commit할 필요가 없는 프로그램을 미리 설정해놓자
  - gitignore.io 사이트에 들어가서 사용하는 프로그램 모두 적고 검색
    (ex. windows, macos, visualstudiocode, etc)
  - 나오는 거 모두 복사해서 .gitignore에 붙여넣기