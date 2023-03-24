from django.contrib import admin
from .models import Task, Post
#PostとTaskを登録
admin.site.register(Post)
admin.site.register(Task)