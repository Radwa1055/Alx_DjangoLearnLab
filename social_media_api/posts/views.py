from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.contenttypes.models import ContentType
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_id'])

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@api_view(['POST'])
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if created and post.author != request.user:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            content_type=ContentType.objects.get_for_model(post),
            object_id=post.id
        )

    return Response({'detail': 'liked'})


@api_view(['POST'])
def unlike_post(request, pk):
    Like.objects.filter(user=request.user, post_id=pk).delete()
    return Response({'detail': 'unliked'})
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from posts.models import Post, Like
from notifications.models import Notification

class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            # Create notification
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked',
                target=post
            )
            return Response({'status': 'liked'})
        return Response({'status': 'already liked'})

class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({'status': 'unliked'})
        except Like.DoesNotExist:
            return Response({'status': 'not liked'})
