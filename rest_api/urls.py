from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),# adminに行くためのエンドポイント
    path('api/', include('api.urls')),# apiに行くためのエンドポイント
]