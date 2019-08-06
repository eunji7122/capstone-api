from rest_framework import viewsets, permissions
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


