from django.db import models
from user.models import User


class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(default=0, max_digits=12, decimal_places=8)
    image = models.ImageField(upload_to='upload/item_images/')
    owner = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE, null=True)


class UserItem(models.Model):
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
