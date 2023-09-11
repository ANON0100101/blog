from rest_framework import generics,viewsets
from applications.post.models import Post
from applications.post.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from applications.post.permissions import IsOwnerAdminOrReadOnly
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
#region


# class ListPostView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticated]



# class CreatePostView(generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class RetrievePostView(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticated]



# class UpdatePostView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsOwnerAdminOrReadOnly]

# class DeletePostView(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsOwnerAdminOrReadOnly]

#endregion

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000


class PostApiView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LargeResultsSetPagination
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# ModelViewSet
# viewSet

# class PostViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Post.objects.all()
#         serializer = PostSerializer(queryset, many=True)
#         return Response(serializer.data)
    


    #retrieve (get_by_id)
    #create (post)
    #update (put)
    #partial_update (patch)
    #destroy (delete)
    