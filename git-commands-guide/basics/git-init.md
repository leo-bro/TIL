# Git 초기화 (git init)

## 🎯 git init이란?
`git init` 명령어는 새로운 Git 레포지토리를 생성하여 디렉토리를 버전 관리할 수 있게 설정합니다.  
이 명령어를 실행하면 `.git`이라는 숨겨진 디렉토리가 생성되어 Git이 파일과 변경 사항을 추적할 수 있습니다.

---

## 📘 사용법
```bash
git init
```

### 옵션
- `--bare`: 파일을 저장하지 않고 Git 메타데이터만 저장하는 레포지토리를 생성합니다.  
  ```bash
  git init --bare
  ```

---

## 🛠️ 실습 예제
1. 새로운 디렉토리 생성:
   ```bash
   mkdir my-project
   cd my-project
   ```

2. Git 레포지토리 초기화:
   ```bash
   git init
   ```
   출력 예시:
   ```
   Initialized empty Git repository in /path/to/my-project/.git/
   ```

3. 파일 생성 후 Git으로 관리:
   ```bash
   echo "Hello, Git!" > hello.txt
   git add hello.txt
   git commit -m "Initial commit"
   ```

4. `.git` 디렉토리 확인:
   ```bash
   ls -a
   ```
   출력:
   ```
   .  ..  .git  hello.txt
   ```

---

## 📝 추가 정보
- `git init`은 기존 디렉토리에도 적용할 수 있습니다. 디렉토리 내 파일을 모두 Git이 추적하게 됩니다.
- 초기화 후, 원격 레포지토리를 연결하려면 다음 명령어를 사용하세요:
  ```bash
  git remote add origin <repository-URL>
  ```

---

## 🔗 참고 자료
- [Git 공식 문서 - git init](https://git-scm.com/docs/git-init)
