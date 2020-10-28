from django.urls import path, include

from . import views


urlpatterns = [
    path('mail-system/', views.MailSystemAPIView.as_view()),
]

