# 유튜브 백엔드 구현

## 1. REST API

### (1) 모델 구조

1. User (Custom)

- email
- password
- nickname
- is_business(boolean): personal, business

2. Video

- title
- likk
- description
- category
- views_count
- video_uploaded_url. (S3)
- videl_file(FileField)
- User:FK
-

3. Like/Dislike

- Video:FK

  Video:Like/Dislike (1:N)

4. Comment

- User:FK
- Video:FK
- like
- dislike

5. Subcription (Channel)

- User:Fk => subcriber (falow)
- User:Fk => subscriber_to ()

6. Notification

- User:Fk
- message
- is_read

7. Common

- created_at
- updated_at

8. Chatting (예정)

- User:Fk (nickname)

1일차 프로젝트 셋팅(Docker-> Django Github-> Github Actions
2일차 Project settings(PostgreSQL)
    - 연결하는 부분 작업(DB) 컨테이너가 준비될때까지 Django 커멘드 명령을 통해서 DB연결재시도)-wait_for_db

3일차 drf-sepectacular

1. User Model create
...
docker-compose run --rm app sh -c 'django-admin startapp users'
django에게 알려준다
user모델 만들고
userModel  생성
makemigrations -> test 코드 실행


custom UserModel migrate -> 디버깅
custom UserAdmin 생성
Swagger-API(API docs) ->drf-spetacular


polls/
    __init__.py
    models.py
    management/
        __init__.py
        commands/
            __init__.py
            _private.py
            closepoll.py
    tests.py
    views.py
