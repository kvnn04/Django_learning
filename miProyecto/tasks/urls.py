from django.urls import path, include
from . import views
urlpatterns = [
    # include('tasks',views.task_list)
    path(route='', view=views.task_list)
]