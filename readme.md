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
<img width="785" alt="Screen Shot 2022-02-17 at 1 01 42 PM" src="https://user-images.githubusercontent.com/60867063/154402829-bf8e96be-672e-4d8a-a392-57f5acf8b600.png">

3. 파이썬 파일을 실행한다. 
```
python ./_util/runTest.py <FOLDER_NAME> <SUBJECT_NAME> <INDEX_1> <INDEX_2>
```
<파이썬 파일 경로> <폴더명> <과제명> <(생략가능)인덱스1> <(생략가능)인덱스2>

인덱스를 모두 생략할 경우 : 모든 문제를 테스트하여 보여준다.    
인덱스를 하나만 적을 경우 : 해당 인덱스의 한 문제만 테스트하여 보여준다.    
인덱스를 두개만 적을 경우 : 앞의 인덱스와 뒤의 인덱스를 포함하여 그 사이의 문제를 테스트하여 보여준다.

## 사용하는 모습
![Feb-17-2022 13-48-14](https://user-images.githubusercontent.com/60867063/154407381-01d2d646-a268-41f2-a225-6c18da0d55ee.gif)    
fileList를 먼저 보여주고, (.DS_Store 들어있는지 여기서 확인!)    
Norminette를 실행하여 결과 보여주고, (Norm 체크!)    
cat으로 하나씩 파일 보여주고, 테스트 케이스 성공/실패를 표시한다.    

## 원리 및 추가법
1. 테스트를 하고 싶은 과제가 있을 때, case 폴더의 하위로 과제명으로 폴더를 하나 만듭니다. (ex c00)
2. 해당 폴더에 data.json이라는 이름으로 json 파일을 하나 작성합니다.
```
{
    "c00":
    [
        {
            "path": "ex00",
            "fileName": "ft_putchar.c",
            "prototype": "void ft_putchar(char c);",
            "testCodes":
            [
                {
                    "expectedResultFile": "00-00",
                    "values":
                    ["K"]
                },
                {
                    "expectedResultFile": "00-01",
                    "values":
                    ["~"]
                },
                {
                    "expectedResultFile": "00-02",
                    "values":
                    [" "]
                },
                ...
            ]
        },
        ...
    ]
}
```
json파일은 일단, 해당 과제명을 이름으로 하는 배열을 가지고 있으며, 그 배열의 안에 들어있는 하나하나의 객체가 문제의 폴더명, 파일명, 프로토타입을 가집니다.     
또한 테스트 코드 정보 배열을 가지며, 테스트 코드 정보는 각각 결과 파일명과 인자 배열을 지닙니다.    
json의 특성 상, 인자에 '나 "와 같은 기호가 들어갈 때에는, 역슬래시를 앞에 적어서 \\", \\'와 같이 작성하여야합니다.    

3. _code 폴더에 각 문제의 폴더명을 이름으로 한 메인 함수의 내부를 채울 코드만을 적은 파일들을 넣습니다.    
이때, {0}과 같이 적은 부분은 위의 data.json에서 지닌 테스트 코드 정보의 인자 배열의 0번째 인덱스로 채워집니다.    
python의 String.format함수를 활용하므로, 다른 목적으로 (ex if문 등) '{}'을 쓸 때에는 '{{}}'와 같이 두 번 적어줍니다.
<img width="468" alt="Screen Shot 2022-02-17 at 1 29 50 PM" src="https://user-images.githubusercontent.com/60867063/154405575-c33173a9-f4e6-4f0c-b690-bb0df85d841c.png">

4. _result 폴더에, data.json에서 작성하였던 결과 파일명으로, 메인이 실행되었을 때 예상되는 결과값을 넣어 저장합니다.
실시간으로 실행한 메인 파일의 결과와, 이때 만든 파일을 비교하여 success와 fail이 감별됩니다.
<img width="339" alt="Screen Shot 2022-02-17 at 1 30 27 PM" src="https://user-images.githubusercontent.com/60867063/154405604-473355c1-b063-4ef7-8373-b20560c50cf1.png">

## 기여하고 싶은 분들께
테스트 케이스 추가 등 기여하고 싶은 분들은 풀 리퀘스트를 하시고 저에게 이메일로 연락 바랍니다. 확인하고 수락해드릴게요! 
yyn9704@gmail.com
