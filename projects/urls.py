from django.urls import path
from . import views


urlpatterns = [
    path('',views.ProjectListView.as_view(), name= 'Project_List'),
    path('project/create',views.ProjectCreateView.as_view(), name= 'Project_Create'),
    path('project/edit/<int:pk>',views.ProjectUpdateView.as_view(), name= 'Project_update'),
    path('project/delete/<int:pk>',views.ProjectDeleteView.as_view(), name= 'Project_delete'),
    path('project/task/create',views.TaskCreateView.as_view(), name= 'Task_create'),
    path('project/task/edit/<int:pk>',views.TaskUpdateView.as_view(), name= 'Task_update'),
    path('project/task/delete/<int:pk>',views.TaskDeleteView.as_view(), name= 'Task_delete'),

]
