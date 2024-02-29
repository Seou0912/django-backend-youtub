from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Subscription
from .serializers import SubscriptionSerializer


# Create your views here.
class SubscriptionList(APIView):
    def post(self, request):
        user_data = request.data
        serializer = SubscriptionSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save(subscriber=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.shortcuts import get_object_or_404


class SubscriptionDetail(APIView):
    def delete(self, request, pk):
        subs = get_object_or_404(Subscription, pk=pk, subscriber=request.user)
        subs.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

        # subscription = Subscription.objects.get(pk=pk)
        # subscription.delete()
