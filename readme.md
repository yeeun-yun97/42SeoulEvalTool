## 42SeoulEvalTool


#### 사용법
1. 어떤 특정 폴더에서 git clone한다.
git clone https://github.com/yeeun-yun97/42SeoulEvalTool.git _util

2. 같은 폴더에서 평가받을 리파지토리를 git clone한다.
git clone "" ev01

3. 같은 폴더 위치에서 터미널을 열어서, 파이썬 파일을 실행한다.
python ./_util/runTest.py <folderName> <subjectName>
앞의 폴더네임은, 2.에서 클론한 폴더명이고, 뒤의 서브젝 네임은 c00과 같이 과제명이다.

4. 실행하면, 첫번째로 파일 목록, 두번째로 노미네이트 결과, 세번째로 각 소스코드와 테스트용 메인, 실행결과가 표시된다.
