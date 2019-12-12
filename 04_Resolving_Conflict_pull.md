# Pull 상황에서 Conflict

---

> ##### 언제 일어나고 어떻게 해결하는지



- git stash
  - (pull을 하지 않은 상황을 몰랐을 때) 변경한 부분을 잠시 저장함
  - 수정 중인 상태를 임시 저장해두고 이전 head commit으로 되돌리기

```shell
$ git stash
$ git pull
```



- git checkout

  - 과거로 잠깐 돌아감

  - 상황: commit되지 않은 변경파일이 존재하는데

    ​          pull을 시도했을 경우

  - 변경된 파일을 commit하고 pull을 다시 시도하면 자동으로 파일이 합쳐지긴 함(auto merge)
  - 그렇지 않을 경우, 수동으로 파일을 합치고(merge), commit, push

```shell
$ git log --oneline
> c7f6979[노란색 파일값] a.txt

$ git checkout c7f6979

$ git checkout master # 현재로 돌아옴
```



---



- Visual Studio Code 설치
- Python 다운로드
  - 'Add Python 3.8 to PATH' check
- ```$ code .``` : code창 불러오기