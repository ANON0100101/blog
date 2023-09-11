from django.urls import path,include
from applications.post.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('', PostApiView)


urlpatterns = [
    # path('', include(router.urls)),
    # path('', PostViewSet.as_view({'get':'list'}))
#     path('',ListPostView.as_view()),
#     path('<int:pk>/',RetrievePostView.as_view()),
#     path('create/',CreatePostView.as_view()),
#     path('update/<int:pk>/',UpdatePostView.as_view()),
#     path('delete/<int:pk>/',DeletePostView.as_view()),
]
