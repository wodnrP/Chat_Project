# Chat_Project

해당 프로젝트는 Django Channels를 활용한 실시간 채팅 프로그램 튜토리얼입니다.

[개인 블로그 참조](https://velog.io/@wodnr_09/Swagger%EC%A0%81%EC%9A%A9](https://velog.io/@wodnr_09/Django-%EC%8B%A4%EC%8B%9C%EA%B0%84-%EC%B1%84%ED%8C%85-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC))

---

### 실행 가이드

**Requirements**
```
Install Python3.8
Install redis

$ python3 -m venv ./{your venv name}    가상환경 생성
$ source {your venv name}/bin/activate  가상환경 실행
```
**Installation**
```
$ git clone https://github.com/wodnrP/Chat_Project.git
$ pip install -r requirements.txt       프로젝트 패키지 설치 
```

**.env file create**
- 프로젝트 폴더와 같은 위치에 .env file 생성
- https://djecrety.ir/ 에서 django secret_key 생성 후 .env file에 작성
```
DEBUG=...   
SECRET_KEY=...
```

**static setting**
- 프로젝트 폴더와 같은 위치에 static 디렉토리 생성
- static 디렉토리 하위에 css, image, js 디렉토리 생성
- 이후 다음과 같은 코드 실행
```
$ python3 manage.py collectstatic
```

**Migration**
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

**RUN**
```
$ python3 manage.py runserver
```

- `/chat` 을 통해 index.html 메인 화면 확인, 브라우저의 다른 탭에서도 같은 채팅방 이름 입력 후 접속

**Result**
<img src="https://velog.velcdn.com/images/wodnr_09/post/29f3b695-a331-4471-ab56-fd1cd48ad0d4/image.gif" width="100%" height="100%">
