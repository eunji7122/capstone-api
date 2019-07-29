from rest_framework import viewsets, permissions, mixins
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import action
from item.serializers import UserItemSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password


class MyItemView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserItemSerializer(request.user.items.all(), many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ReadOnlyModelViewSet, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

    @action(detail=True)
    def items(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = UserItemSerializer(user.items.all(), many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(password=make_password(self.request.data['password']))
