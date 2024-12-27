
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from genres.views import genre_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', genre_view, name='genre-list'),
]
