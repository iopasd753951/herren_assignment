from rest_framework.routers import DefaultRouter
from django.urls import path, include

from accounts_api import views


router = DefaultRouter()
router.register('signup', views.UserAccountViewSet, basename='회원가입')
router.register('mail-list', views.UserMailListViewSet, basename='메일링리스트')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view()),
]
