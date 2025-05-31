from django.shortcuts import render
from . import models
from django.views.generic import ListView , CreateView
from . import forms
from django.urls import reverse_lazy


class ProjectListView(ListView):
    model= models.Project
    template_name = 'project/list.html'
    context_object_name = 'projects'

class ProjectCreateView(CreateView):
    model= models.Project
    form_class= forms.ProjectCreateForm
    template_name= 'project/create.html'
    success_url= reverse_lazy('Project_List')



