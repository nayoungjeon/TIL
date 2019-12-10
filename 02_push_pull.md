# Push & Pull 워크플로우

## 1. Clone

- 다른 장소에서도 같은 저장소를 관리할 수 있도록 *처음* 만 실행

```shell
$ pwd # home directory 확인
$ mkdir house

$ get clone 저장소주소.git
```



## 2. Push

- 작업한 파일을 github에 올리기
- add, commit, push

```shell
$ touch 파일명.확장자 # file 만들기
$ git status        # git 상태 확인

$ git add 파일명.확장자
$ git commit -m "간결한 명령문"

$ git log --oneline # 한 줄로 log 보기

$ git push origin master
```



 ## 3. Pull

- github에 있는 파일을 내려받기
- pull

```shell
$ git status # working tree clean 일 때 실행

$ git pull orgin master

$ git log --oneline
$ ls
```



##### cf.

```shell
$ git diff        # file 내용 뭐가 바뀌었는지
$ cat 파일명.확장자 # file 내용 프린트
```



