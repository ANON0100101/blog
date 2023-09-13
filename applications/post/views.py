from rest_framework import generics,viewsets
from applications.post.models import Post,Comment,Like,Rating
from applications.post.serializers import PostSerializer,CommentSerializer,RatingSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from applications.post.permissions import IsOwnerAdminOrReadOnly
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

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
    # permission_classes = [IsAuthenticated]
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['owner', 'title']
    search_fields = ['title']
    ordering_fields = ['id']

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     filter_owner = self.request.query_params.get('owner')
    #     if filter_owner:
    #         queryset = queryset.filter(owner=filter_owner)
    #
    #     return queryset
    @action(methods=['POST'], detail=True)
    def like(self, request, pk, *args, **kwargs):
        try:
            user = request.user
            post_id = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'ошибка': 'Поста с указанным id не существует'}, status=status.HTTP_404_NOT_FOUND)
        like_obj, _ = Like.objects.get_or_create(owner=user,post_id=post_id)
        like_obj.is_like = not like_obj.is_like
        like_obj.save()
        status_text = 'liked' if like_obj.is_like else 'unliked'
        
        return Response({'status':status_text})
    
    @action(methods=['POST'], detail=True) #post/18/rating
    def rating(self, request, pk, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating_obj, _ = Rating.objects.get_or_create(owner=request.user, post_id=pk)
        rating_obj.rating = serializer.data['rating']
        rating_obj.save()
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentModelVIewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

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
    