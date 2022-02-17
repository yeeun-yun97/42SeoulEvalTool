# 42SeoulEvalTool
#### 제작자: 윤예은 (intra: yeyun)

## 지원 범위 
```
c00
```
```
c01
```
```
c02
```

## 사용법
하나의 폴더 안에 이 프로젝트를 클론한 _util폴더와, 평가를 받을 프로젝트를 클론한 폴더를 함께 넣어서 사용한다.

1. 깃 클론을 통해 이 프로젝트를 내려받는다.
```
git clone https://github.com/yeeun-yun97/42SeoulEvalTool.git _util
```
<img width="847" alt="Screen Shot 2022-02-17 at 12 36 18 PM" src="https://user-images.githubusercontent.com/60867063/154400376-4b89533d-ad52-4f40-858a-fe1fbe681375.png">

2. 같은 폴더에서 깃 클론으로 평가받을 과제를 내려받는다.
```
git clone <YOUR_REPOSITORY_URL> <FOLDER_NAME>
```
                                                                  
3. 파이썬 파일을 실행한다. 
```
./_util/runTest.py <FOLDER_NAME> <SUBJECT_NAME> <INDEX_1> <INDEX_2>
```
<파이썬 파일 경로> <폴더명> <과제명> <(생략가능)인덱스1> <(생략가능)인덱스2>

인덱스를 모두 생략할 경우 : 모든 문제를 테스트하여 보여준다.    
인덱스를 하나만 적을 경우 : 해당 인덱스의 한 문제만 테스트하여 보여준다.    
인덱스를 두개만 적을 경우 : 앞의 인덱스와 뒤의 인덱스를 포함하여 그 사이의 문제를 테스트하여 보여준다.

#### 
