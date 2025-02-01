# Git repository 관리

Github에 입문하면서 repository를 깔끔하고 효율적으로 관리하는 법을 하나 하나 기록하는 페이지

## Github에 이미 올라간 repository를 다른 폴더에 병합하기

처음에 깃을 공부하면서 my-git-journey라는 프로젝트 폴더를 만들어 활용했는데, 추후에 TIL 폴더에 공부한 자료들을 정리하면서 이 프로젝트를 TIL로 병합, 수정 및 삭제 등을 하고 싶어졌다.

- TIL/git 하위 폴더로 my-git-journey 프로젝트 내용을 병합한다.
- 이전 커밋 기록이 사라지지 않았으면 좋겠다.

해결 방법

```bash
git subtree add prefix=(하위 디렉토리 이름 설정) (옮길 레포지토리 디렉토리) (옮길 레포지토리 브랜치)
git add .
git push
```
다음과 같이 하위폴더 생성과 함께 이전 커밋 기록이 담긴 브랜치와 병합할 수 있었다.

![sourcetree.png](sourcetree.png)

참고 사이트: https://mgyo.tistory.com/385

## [에러] 푸시 오류 메세지 : Permission denied (publickey). fatal: Could not read from remote repository.

Sourcetree로 푸시를 할 때 다음과 같은 에러가 발생하였다.

Pushing to github.com:깃허브주소  
git@github.com: Permission denied (publickey).  
fatal: Could not read from remote repository.

#### 원인

이 메세지는 소스트리에서 새로운 커밋 사항을 깃허브 저장소에 푸시하려고 할 때, SSH 키 인증 문제가 발생하는 에러임을 확인하였다.

#### 해결방법

터미널에서 다음 명령을 수행한다.

```bash
cd ~/.ssh
open .
```

ssh 디렉토리로 이동해 id_rsa와 id_rsa.pub 파일이 있는지 확인 후, 없다면 다음 명령어를 수행한다.

```bash
ssh-keygen -t ed25519 -C "나의깃허브이메일주소"
```
이 명령어는 아래와 같이 두개의 키를 생성해준다.

```bash
~/.ssh/id_ed25519 # 개인키
~/.ssh/id_ed25519.pub # 공개키
```

다음 명령어를 통해 공개키의 내용을 복사한다.

```bash
pbcopy < ~/.ssh/id_ed25519.pub
```

마지막으로 깃허브에 들어가 복사해둔 키를 등록한다.

깃허브 오른쪽 상단 > settings > 왼쪽 메뉴의 SSH and GPG keys > New SSH Key 버튼

Key 부분에 복사해둔 키를 붙여넣으면 완료된다.

이 후, 소스트리에서 깃헙으로 잘 푸쉬되는 것을 확인할 수 있다.



참고 사이트: https://velog.io/@posinity/에러-푸시-오류-메세지-Permission-denied-publickey.fatal-Could-not-read-from-remote-repository