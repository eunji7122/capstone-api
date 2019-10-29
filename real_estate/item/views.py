from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Item, UserItem
from .serializers import ItemSerializer, UserItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def get_queryset(self):
    #     return self.request.user.items.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['POST'])
    def purchase(self, request, *args, **kwargs):
        item = self.get_object()
        user = request.user

        item.owner = user
        item.save()
        serializer = ItemSerializer(item)
        return Response(serializer.data)
