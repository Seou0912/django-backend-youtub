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

## 1일차

프로젝트 셋팅(Docker-> Django Github-> Github Actions

## 2일차

Project settings(PostgreSQL) - 연결하는 부분 작업(DB) 컨테이너가 준비될때까지 Django 커멘드 명령을 통해서 DB연결재시도)-wait_for_db

## 3일차

drf-sepectacular

1. User Model create  
   ...
   docker-compose run --rm app sh -c 'django-admin startapp users'  
   django에게 알려준다  
   user모델 만들고  
   userModel 생성  
   makemigrations -> test 코드 실행

custom UserModel migrate -> 디버깅  
custom UserAdmin 생성  
Swagger-API(API docs) ->drf-spetacular

polls/
**init**.py
models.py
management/
**init**.py
commands/
**init**.py
\_private.py
closepoll.py
tests.py
views.py

## 4일차

4일차: REST API -> Video 관련 API
(1) startapp을 통해서 각 모델별 app폴더 생성 1.Common 2.Videos 3.Comments 4.Reactions (좋아요,싫어요) 5.Subcriptions 6.Notifications

docker-compose run --rm app sh -c 'python manage.py startapp common'
docker-compose run --rm app sh -c 'python manage.py startapp videos'
docker-compose run --rm app sh -c 'python manage.py startapp comments'
docker-compose run --rm app sh -c 'python manage.py startapp reactions'
docker-compose run --rm app sh -c 'python manage.py startapp subscriptions'
docker-compose run --rm app sh -c 'python manage.py startapp notifications'
(2) Model정의

(3) settings.py의 INSTALLED_APPS에 등록

(4) DB migration

docker-compose run --rm app sh -c 'python manage.py makemigrations'
docker-compose run --rm app sh -c 'python manage.py migrate'
(5) Video API create VideoList api/v1/videos

GET: 전체 비디오 목록 조회
POST: 새로운 비디오 생성
DELETE, PUT: X
VideoDetail api/v1/videos/{video_id}

GET: 특정 비디오 상세 조회
POST: X
PUT: 특정 비디오 정보 업데이트(수정)
DELETE: 특정 비디오 삭제
urls.py 등록

(6) Subscription API

- 구독하기 POST
- 구독리스트 Get
- 구독삭제 delete

api/v1/subscriptions
SubscriptionList
[POST] 구독버튼

api/v1/subscriptions/{user_id}
SubscriptonDetail
[DELETE] 구독취소

(7) Reaction API
