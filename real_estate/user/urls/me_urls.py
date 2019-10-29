from django.urls import path
from user import views

urlpatterns = [
    path('', views.MeView.as_view()),
    path('privateKey/', views.PrivateKeyView.as_view()),
    path('items/', views.MyItemView.as_view())
]