# Git 초기화 (git init)

## 🎯 목적
`git init` 명령어는 새로운 Git 레포지토리를 생성하고, 디렉토리를 버전 관리할 수 있게 설정합니다.

## 📘 사용법
```bash
git init

🛠️ 실습
새로운 디렉토리를 생성:

bash
코드 복사
mkdir my-project
cd my-project
Git 초기화:

bash
코드 복사
git init
출력:

bash
코드 복사
Initialized empty Git repository in /path/to/my-project/.git/
새로운 파일 추가:

bash
코드 복사
echo "Hello, Git!" > hello.txt
파일을 Git으로 관리:

bash
코드 복사
git add hello.txt
git commit -m "Initial commit"
🔍 확인하기
.git 디렉토리가 생성되었는지 확인:
bash
코드 복사
ls -a
출력:
코드 복사
.  ..  .git  hello.txt
