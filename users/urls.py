from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users import views


router = DefaultRouter()
router.register('', views.UserViewSet)
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('login/', views.UserLoginView.as_view()),
    path('', include(router.urls))
]