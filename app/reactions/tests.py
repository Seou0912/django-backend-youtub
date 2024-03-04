from rest_framework.test import APITestCase
from users.models import User
from videos.models import Video
from .models import Reaction
from django.urls import reverse
from rest_framework import status
import pdb

# Create your tests here.
# ReactionDefail


class ReactionAPITestCase(APITestCase):
    # 테스트 코드 실행전에 필요한 더미 데이터 생성
    def setUp(self):
        self.user = User.objects.create_user(
            email="myuni0912@gmail.com", password="wjdtjdn0912"
        )

        self.video = Video.objects.create(
            title="test video", link="http://test.com", user=self.user
        )

        self.client.login(email="myuni0912@gmail.com", password="wjdtjdn0912")

    # [POST] 종아요 싫어요 생성 및 업데이트
    def test_reaction_detail_post(self):
        url = reverse("video-reaction", kwargs={"video_id": self.video.id})
        data = {"reaction": Reaction.LIKE}

        res = self.client.post(url, data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reaction.objects.count(), 1)
        self.assertEqual(Reaction.objects.get().reaction, Reaction.LIKE)

    # [DELETE] 좋아요, 싫어요 삭제
    def test_reaction_detail_delete(self):
        Reaction.objects.create(
            user=self.user, video=self.video, reaction=Reaction.LIKE
        )
        url = reverse("video-reaction", kwargs={"video_id": self.video.id})
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Reaction.objects.count(), 0)
