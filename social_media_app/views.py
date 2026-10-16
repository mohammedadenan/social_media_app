from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from social_media_app.models import *
from social_media_app.serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from social_media_app.permissions import IsOwner,Owner
# Create your views here.


class SignupView(CreateAPIView):
    serializer_class=UserSerializer

class Postcreate(CreateAPIView,ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def perform_create(self, serializer):
         return serializer.save(owner=self.request.user)
    
    
class PostView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsOwner]

    

class UserRetrieveView(RetrieveAPIView):
    serializer_class=UserRetrieveSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=CustomUser.objects.all()


class CommentPost(CreateAPIView,ListAPIView):
    serializer_class=CommentSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Comment.objects.all()

    def get_queryset(self):
        pk=self.kwargs.get('pk')
        return Comment.objects.filter(post_obj=pk)

    def perform_create(self, serializer):
        pk=self.kwargs.get('pk')
        post_obj=Post.objects.get(pk=pk)
        serializer.save(owner=self.request.user,post_obj=post_obj)

class CommentDelete(DestroyAPIView):
    serializer_class=CommentSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsOwner]
    queryset=Comment.objects.all()


class LikeView(CreateAPIView,ListAPIView):
    serializer_class=LikeSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Like.objects.all()


    def get_queryset(self):
         pk=self.kwargs.get('pk')
         return Like.objects.filter(post_obj=pk)
         

    def perform_create(self, serializer):
         pk=self.kwargs.get('pk')
         post_obj=Post.objects.get(pk=pk)
         serializer.save(owner_obj=self.request.user,post_obj=post_obj)



class UnLike(DestroyAPIView):
    serializer_class=LikeSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[Owner]
    queryset=Like.objects.all()



  
