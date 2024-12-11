from django.urls import path
from .views import TaskViewSetAPI, custom_middleware

urlpatterns = [
    path('tasks/',TaskViewSetAPI.as_view() , name='task'),
    path("custom_middleware/",custom_middleware)
]
