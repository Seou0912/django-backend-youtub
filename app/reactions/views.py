from .models import Reaction
from .serializers import ReactionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)

from videos.models import Video
from django.shortcuts import get_object_or_404


# Create your views here.
# ReactionDetil
class ReactionDetail(APIView):
    def post(self, request, video_id):
        user_data = request.data  # 유저가 서버로 보낸 데이터
        serializer = ReactionSerializer(data=user_data)

        if serializer.is_valid(raise_exception=True):
            reaction_obj, created = Reaction.objects.get_or_create(
                user=request.user,
                video=Video.objects.get(id=video_id),
                defaults={"reaction": serializer.validated_data["reaction"]},
            )
            # 기존 데이터 없댜면 create True
            if created:
                return Response(serializer.data, status=HTTP_201_CREATED)

            # 기존 데이터 존재한다면 update
            if not created:
                reaction_obj.reation = serializer.validated_data["reaction"]
                reaction_obj.save()

                return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    # [DELETE] - 좋아요, 싫어요 삭제
    def delete(self, request, video_id):
        user = request.user
        video = get_object_or_404(Video, pk=video_id)
        reaction = get_object_or_404(Reaction, user=user, video=video)

        if reaction:
            reaction.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        else:
            return Response(status=HTTP_404_NOT_FOUND)
