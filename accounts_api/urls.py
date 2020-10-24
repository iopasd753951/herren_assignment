from rest_framework.routers import DefaultRouter

from accounts_api import views


router = DefaultRouter()
router.register('signup', views.UserAccountViewSet, basename="signup_up")
router.register('login', views.LoginViewSet, basename="login_api")

urlpatterns = router.urls
