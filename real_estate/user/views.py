from rest_framework import viewsets, permissions, mixins
from rest_framework.generics import GenericAPIView
from .models import User
from .serializers import UserSerializer, PrivateKeySerializer
from rest_framework.decorators import action
from item.serializers import UserItemSerializer, ItemSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from eth_keys import keys
from eth_utils import decode_hex
from rest_framework import status


class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


# class MyItemView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get(self, request):
#         serializer = UserItemSerializer(request.user.items.all(), many=True)
#         return Response(serializer.data)

class MyItemView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ItemSerializer

    def get(self, request):
        serializer = self.get_serializer(request.user.items.all(), many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ReadOnlyModelViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

    @action(detail=True)
    def items(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = UserItemSerializer(user.items.all(), many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        private_key = keys.PrivateKey(decode_hex(self.request.data['private_key']))
        public_key = private_key.public_key
        serializer.save(
            password=make_password(self.request.data['password']),
            address=public_key.to_checksum_address(),
        )


class PrivateKeyView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = PrivateKeySerializer(request.user)
        return Response(serializer.data)


class Auth(APIView):
    def post(self, request):
        try:
            p_num = request.data['phone']
        except KeyError:
            return Response({'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            User.objects.update_or_create(phone=p_num)
            return Response({'message': 'OK'})

    def get(self, request):
        try:
            p_num = request.query_params['phone']

            a_num = request.query_params['auth_number']
        except KeyError:
            return Response({'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            result = User.check_auth_number(p_num, a_num)
            return Response({'message': 'OK', 'result': result})
