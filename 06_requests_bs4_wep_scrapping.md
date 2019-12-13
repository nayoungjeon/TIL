# requests, BeautifulSoup 이용한 웹 스크래핑

## 1. PIP 다운

- **PIP**는 파이썬으로 작성된 패키지 소프트웨어를 설치·관리하는 패키지 관리 시스템이다.



### 1) requests ###

- 서버에서 요청을 받는 library



- Git Bash 에서 진행

  ```shell
  $ pip install requests # library package 설치
  $ pip list # 현재 package 확인
  ```

  

- Visual Code Studio 에서 진행

  ```python
  import requests
  
  response = requests.get("https://finance.naver.com/sise/") # url에서 응답을 받는다.
  print(response) # <개발자 도구>상의 tag까지 모두 출력; 지저분해
  ```

  

### 2) BeaustifulSoup ###

- requests로 가져온 html 파일을 해석해서 원하는 정보만 가져온다.



- Git Bash 에서 진행

```shell
$ pip install ps4
```



- Visual Studio Code에서 진행

``` python
import requests
from bs4 import BeautifulSoup

response = requests.get('https://finance.naver.com/sise/').text
soup = BeautifulSoup(response, 'html.parser')
kospi = soup.select_one('#KOSPI_now').text
print(kospi) # text만 출력
```

