from rest_framework.routers import DefaultRouter
from django.urls import path, include

from accounts_api import views


router = DefaultRouter()
router.register('signup', views.UserAccountViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view()),
]
