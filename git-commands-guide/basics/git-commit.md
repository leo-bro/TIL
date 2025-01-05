# Git 커밋 (git commit)

## 🎯 git commit이란?
`git commit` 명령어는 변경된 파일의 스냅샷을 저장소에 기록하는 작업입니다.  
각 커밋은 고유한 ID를 가지며, 프로젝트의 변경 이력을 추적할 수 있게 해줍니다.

---

## 📘 사용법
### 기본 명령어
```bash
git commit -m "Commit message"
```
- `-m`: 커밋 메시지를 작성합니다.

### 모든 변경 사항 커밋
```bash
git commit -a -m "Commit message"
```
- `-a`: Git이 추적 중인 모든 파일을 자동으로 추가합니다.

### 편집기를 사용한 커밋 메시지 작성
```bash
git commit
```
- 기본 편집기를 열어 상세한 메시지를 작성할 수 있습니다.

---

## 🛠️ 실습 예제
1. 변경 사항 확인:
   ```bash
   echo "New content" >> example.txt
   git status
   ```

2. 변경 사항 추가:
   ```bash
   git add example.txt
   ```

3. 커밋:
   ```bash
   git commit -m "Add example.txt with new content"
   ```

4. 마지막 커밋 수정:
   ```bash
   git commit --amend -m "Update commit message"
   ```

---

## 📝 커밋 메시지 작성 규칙
1. **짧고 명확하게 작성:**
   - 좋음: `Fix login bug`
   - 나쁨: `Update files`
2. **현재형 동사 사용:**
   - `Add`, `Fix`, `Update`와 같은 현재형 사용.
3. **작업 의도를 설명:**
   - 왜 이 작업을 했는지 간략히 기술.

---

## 🔄 커밋 되돌리기
### 마지막 커밋 되돌리기 (커밋 기록 유지)
```bash
git revert HEAD
```

### 마지막 커밋 수정 (기록 덮어쓰기)
```bash
git commit --amend
```

---

## 🔗 참고 자료
- [Git 공식 문서 - git commit](https://git-scm.com/docs/git-commit)
