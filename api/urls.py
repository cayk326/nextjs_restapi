"""
viewとURLパスを関連付けてRESTAPIを構成する
#ModelViewSetを使ってviewを作ったときrouterで関連性を定義
#Genericsを使ってviewを作ったとき時
"""

from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import TaskViewSet, CreateUserView, TaskListView, TaskRetrieveView,\
    PostListView, PostRetrieveView


router = routers.DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')# 関連性登録 tasksというパスとTaskViewSetを関連付ける

# 関連性登録(Genericsで作ったview用)
urlpatterns = [
    path('list-post/', PostListView.as_view(), name='list-post'),# list-postとPostListView
    path('detail-post/<str:pk>/', PostRetrieveView.as_view(), name='detail-post'),# detail-post/<str:pk>/とPostRetrieveView
    path('list-task/', TaskListView.as_view(), name='list-task'),
    path('detail-task/<str:pk>/', TaskRetrieveView.as_view(), name='detail-task'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('auth/', include('djoser.urls.jwt')),#JWTトークンを得るためのパス
    path('', include(router.urls)),
]