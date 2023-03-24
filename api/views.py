from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import viewsets
from .serializers import TaskSerializer, UserSerializer, PostSerializer
from .models import Task, Post


# 新規でユーザを作成するためのview
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)# 新規ユーザーは認証が通せないのでだれでもアクセスできるようにする

# ブログ投稿データの一覧を見るためのAPIエンドポイント
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()# リスト化するためにPostの内容を取得してquerysetに入れる
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)

# 特定のブログ投稿IDに基づいて1つのブログデータを取得するためのview
class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)

# Taskの一覧リストのview
class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)

# 特定のタスクIDに基づいて1つのタスクデータを取得するためのview
class TaskRetrieveView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)

# タスクの新規作成更新削除をするためのview(ModelViewSetによってCRUDつかえる)
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer