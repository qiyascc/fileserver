from django.urls import path
from .views import serve_file_by_type_and_name

urlpatterns = [
    path('<str:file_type>/<str:file_name>/', serve_file_by_type_and_name, name='serve_file_by_type_and_name'),
]
