from django.test import TestCase
from rest_framework.test import APITestCase
from users.models import User
from django.urls import reverse
from rest_framework import status
from .models import Subscription
import pdb


# Create your tests here.
class SubscriptionTestCase(APITestCase):
    def setUp(self):
        # self.client = APIClient()
        self.user1 = User.objects.create_user(
            email="user@gmail.com", password="pass1234"
        )
        self.user2 = User.objects.create_user(
            email="user2@test.com", password="pass1234"
        )
        self.client.login(email="user@gmail.com", password="pass1234")
        # self.subscription = Subscription.objects.create(user=self.user)

    # 구독 버튼 클릭
    def test_subs_list_post(self):
        # self.client.login(email="user@gmail.com", password="pass1234")
        url = reverse("subs-list")
        data = {
            "subscriber": self.user1.pk,
            "subscribed_to": self.user2.pk,
        }

        res = self.client.post(url, data)
        # pdb.set_trace()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subscription.objects.count(), 1)
        self.assertEqual(Subscription.objects.get().subscribed_to, self.user2)
        pass

    # 구독 취소
    def test_sub_detail_delete(self):
        subs = Subscription.objects.create(
            subscriber=self.user1, subscribed_to=self.user2
        )
        url = reverse("subs-detail", kwargs={"pk": subs.id})

        res = self.client.delete(url)
        # pdb.set_trace()
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Subscription.objects.count(), 0)
