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

2. Like/Dislike

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
