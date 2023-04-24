 # todo virtual
from . import views
from django.urls import path,include

urlpatterns = [

    path("", views.add, name="add"),
    path("delete/<int:taskid>/",views.delete, name="delete"),
    path("update/<int:id>/",views.update, name="update"),
    path("TaskListview/",views.TaskListview.as_view(), name="TaskListview"),
    path("Taskdetview/<int:pk>/",views.TaskDetailview.as_view(), name="TaskDetailview"),
    path("TaskUpdateview/<int:pk>/",views.TaskUpdateview.as_view(), name="TaskUpdateview"),
    path("Taskdeleteview/<int:pk>/",views.Taskdeleteview.as_view(), name="Taskdeleteview")
]