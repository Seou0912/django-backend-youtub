from django.test import TestCase
from rest_framework.test import APITestCase
from users.models import User
from .models import Video
from django.urls import reverse
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
import pdb

# Create your tests here.


class VideoAPITestCase(APITestCase):
    # 테스트 코드가 실행되기전 유저생성, 비디오생성
    def setUp(self):
        # 유저 생성
        self.user = User.objects.create_user(
            email="myuni0912@gmail.com", password="wjdtjdn0912"
        )
        self.client.login(email="myuni0912@gmail.com", password="wjdtjdn0912")

        # 비디오 생성
        self.video = Video.objects.create(
            title="test video",
            link="http://test.com",
            user=self.user,
        )

    def test_video_list_get(self):
        url = reverse("video-list")
        print("url", url)

        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_video_detail_get(self):
        # kwaargs :keyword arguments
        url = reverse("video-detail", kwargs={"pk": self.video.pk})

        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    # video 생성이 잘 되었는지 확인하기위한 테스트
    def test_video_list_post(self):
        url = reverse("video-list")
        print("user: ", self.user)

        data = {
            "title": "test video2",
            "link": "http://test.com",
            "category": "test category",
            "thumbnail": "http://test.com",
            "video_uploaded_url": "http://test.com",
            "video_file": SimpleUploadedFile(
                "file.mp4", b"file_content", content_type="video/mp4"
            ),
            "user": self.user.pk,
        }
        res = self.client.post(url, data)
        print(res)
        # pdb.set_trace()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    # 비ㅣㄷ오 정보 업데이트
    def test_video_detail_put(self):
        # self.client.login(email="myuni0912@gmail.com", password="wjdtjdn0912")
        url = reverse("video-detail", kwargs={"pk": self.video.pk})

        data = {
            "title": "updated video",
            "link": "http://test.com",
            "category": "test category",
            "thumbnail": "http://test.com",
            "video_uploaded_url": "http://test.com",
            "video_file": SimpleUploadedFile(
                "file.mp4", b"file_content", content_type="video/mp4"
            ),
            "user": self.user.pk,
        }
        res = self.client.put(url, data, content_type="application/json")
        # pdb.set_trace()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["title"], "updated video")
        pass

    # 비디오 삭제
    def test_video_detail_delete(self):
        url = reverse("video-detail", kwargs={"pk": self.video.pk})

        res = self.client.delete(url)
        # pdb.set_trace()
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

        # 정상정 삭제 확인
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
