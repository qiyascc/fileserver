from django.urls import path
from .views import all_files, file_detail

urlpatterns = [
    path('all/', all_files, name='all_files'),
    path('<int:file_id>/', file_detail, name='file_detail'),
]
