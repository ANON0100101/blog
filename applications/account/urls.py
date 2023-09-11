
from django.urls import path
from applications.account.views import RegisterAPIView,ActivationAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('activate/<uuid:activation_code>/', ActivationAPIView.as_view()),

    # path('login/', LoginAPIView.as_view()),
    # path('logout/', LogoutAPIView.as_view()),

    # path('password/',ChangePasswordAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    
    
]