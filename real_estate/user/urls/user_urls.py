from django.urls import include, path
from rest_framework.routers import DefaultRouter
from user import views


router = DefaultRouter()
router.register('', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]