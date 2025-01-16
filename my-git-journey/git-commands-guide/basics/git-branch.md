# Git 브랜치 (git branch)

## 🎯 브랜치란?
브랜치는 **독립적인 작업 공간**을 제공합니다.  
- 새 기능 개발, 버그 수정 등 다양한 작업을 별도의 브랜치에서 수행한 뒤 메인 브랜치(`main`)에 병합합니다.
- 프로젝트의 안정성을 유지하면서 병렬 작업이 가능합니다.

---

## 📘 주요 명령어
### 1. **브랜치 목록 확인**
```bash
git branch
```
- 현재 존재하는 브랜치 목록을 출력합니다.
- 현재 작업 중인 브랜치는 `*` 기호로 표시됩니다.

### 2. **새 브랜치 생성**
```bash
git branch <branch-name>
```
- 새로운 브랜치를 생성합니다.
- 생성된 브랜치는 자동으로 전환되지 않으며, `git checkout`을 통해 이동해야 합니다.

### 3. **브랜치 전환**
```bash
git checkout <branch-name>
```
- 작업 중인 브랜치를 전환합니다.
- 브랜치를 생성하며 전환하려면:
  ```bash
  git checkout -b <branch-name>
  ```

### 4. **브랜치 삭제**
```bash
git branch -d <branch-name>
```
- 브랜치를 삭제합니다.
- 병합되지 않은 브랜치를 강제로 삭제하려면:
  ```bash
  git branch -D <branch-name>
  ```

### 5. **브랜치 병합**
```bash
git merge <branch-name>
```
- 다른 브랜치를 현재 브랜치에 병합합니다.

---

## 🛠️ 실습 예제
### 브랜치 생성 및 전환
1. 새로운 브랜치 생성:
   ```bash
   git branch feature-1
   ```
2. 브랜치 전환:
   ```bash
   git checkout feature-1
   ```
   또는 한꺼번에:
   ```bash
   git checkout -b feature-1
   ```

3. 새 브랜치에서 파일 수정:
   ```bash
   echo "Feature work in progress" > feature.txt
   git add feature.txt
   git commit -m "Add feature.txt"
   ```

### 병합 작업
1. 메인 브랜치로 전환:
   ```bash
   git checkout main
   ```

2. 브랜치 병합:
   ```bash
   git merge feature-1
   ```

3. 병합 후 상태 확인:
   ```bash
   git log --oneline
   ```

---

## 🌟 충돌 해결
병합 도중 충돌이 발생하면 다음 단계를 따릅니다:
1. 충돌 상태 확인:
   ```bash
   git status
   ```
2. 충돌난 파일 수정.
3. 수정 후 병합 완료:
   ```bash
   git add <conflicted-file>
   git commit
   ```

---

## 📝 추가 정보
- `git switch`를 사용하여 브랜치를 전환할 수도 있습니다:
  ```bash
  git switch <branch-name>
  ```
- `git branch -r`로 원격 브랜치를 확인할 수 있습니다.

---

## 🔗 참고 자료
- [Git 브랜치 공식 문서](https://git-scm.com/docs/git-branch)
- [Git 학습 자료](https://learngitbranching.js.org/)
