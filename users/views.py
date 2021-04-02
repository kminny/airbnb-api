from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import ReadUserSerializer


class MeView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return Response(
                data=ReadUserSerializer(request.user).data, status=status.HTTP_200_OK
            )

    def put(self, request):
        pass


@api_view(["GET"])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
        return Response(ReadUserSerializer(user).data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
