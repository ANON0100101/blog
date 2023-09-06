
from django.urls import path
from applications.account.views import RegisterAPIView
urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    # path('login/',)
    
]