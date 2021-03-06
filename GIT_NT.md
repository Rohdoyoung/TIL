# Git - Github 연결

* `git config --global user.naem <user_name>` : username
* `git config --global user.email <email>` : email
  * config : 내 로컬과 깃허브 연결 시켜줄 때 최초 1회
  * 컴터 포멧하지 않는 이상 더이상 할 일 없음
* `git config --global user.name`
  * 설정한 username 이 나옴
* `git config --global user.email`
  * 설정한 email 이 나옴

<br>

## Connect to Repositories

* `git init` : 레포를 만들고 워킹 디렉토리랑 연결시켜줄때 최초 1회
  * → 레포를 만들 때마다 계속 해줘야 함

* `git status` : 워킹 디렉토리에 어떤 변화가 있는지 알아보는 명령어
  * 워킹 디렉토리 단계와 스테이징 에리아 단계의 변화

* `git remote add origin <github 주소>` : 내 워킹 디렉토리와 레포지토리 연결
  * `git remote -v` : 리모트가 잘 들어갔는지 확인

<br>

## Select Add

* `git add` + `.` : 전체 다 staging area 로 올리기

* `git add <file_name.ext>` : 이것 만 올리기
  * ex) `git add 파일1 파일2 파일3` : 파일 여러개 올리기
* `git add <folder_name>`  : 폴더 올리기

<br>

## Staging Area

* `git commit -m "commit message"`:
  * 되도록 명령어로 적기
    * 동사형으로 시작하기
    * 영어로 적기
  * 약속일뿐 법은 아니다

* `git push origin master` : 최종적으로 깃허브에 올린다!!

<br>

* `git log --oneline` : `-`(하이픈) 두개
  * `commit`된 상황에서 어떤 메시지로 언제 뭐가 올라갔는지 알기 위한 명령어

<br>

## pull

* 로컬에서 파일이 삭제 되었던지 등등의 이유로 깃허브에서 로컬로 파일들을 가져 올 때 사용
* `git pull origin master` : 기 연결된 레포지토리의 모든 파일들을 다운 받는다.

<br>

## Branch

* `git branch` : 브랜치의 종류, 어느 브랜치인지 확인하기
* `git branch <branch_name>` : 브랜치 생성
  * `git  baranch haley` : haley 라는 브랜치 생성
  * 이미 있는 브랜치 명을 작성 했을땐 에러 발생
* `git checkout <branch_name>` : 브랜치 이동
  * `git checkout haley` : haley 라는 브랜치로 이동
  * 없는 브랜치 명으로 이동 할 수 없음

<br>

## Merge

* `git merge haley` : (현재 브랜치 master 인 상태에서) haley 브랜치를 master 브랜치로 머지(합병) 함

