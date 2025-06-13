from django.shortcuts import render
from . import models
from django.views.generic import ListView , CreateView, UpdateView , DeleteView
from . import forms
from django.urls import reverse_lazy , reverse
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin


class ProjectListView(LoginRequiredMixin, ListView):
    model= models.Project
    template_name = 'project/list.html'
    context_object_name = 'projects'
    paginate_by= 6

    def get_queryset(self):
        query_set= super().get_queryset()
        where= {'user_id':self.request.user}
        q = self.request.GET.get('q' , None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)
    

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model= models.Project
    form_class= forms.ProjectCreateForm
    template_name= 'project/create.html'
    success_url= reverse_lazy('Project_List')

    def form_valid(self, form):
        form.instance.user= self.request.user
        return super().form_valid(form)
    

class ProjectDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView ):
    model= models.Project
    template_name= 'project/delete.html'
    success_url= reverse_lazy('Project_List')
    def test_func(self):
        return self.get_object().user_id == self.request.user.id
class ProjectUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView,):
    model= models.Project
    form_class= forms.ProjectUpdateForm
    template_name= 'project/update.html'
    
    def test_func(self):
        return self.get_object().user_id == self.request.user.id
    
    def get_success_url(self):
        return reverse('Project_update', args= [self.object.id])
    
class TaskCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.Task
    fields = ['description']  # لا نعرض project للمستخدم

    def get_success_url(self):
        return reverse('Project_update', args=[self.kwargs['project_id']])

    def form_valid(self, form):
        # اربط المهمة بالمشروع قبل الحفظ
        project = models.Project.objects.get(pk=self.kwargs['project_id'])
        form.instance.project = project
        return super().form_valid(form)

    def test_func(self):
        # تحقّق من أن المشروع يخص المستخدم الحالي
        project = models.Project.objects.get(pk=self.kwargs['project_id'])
        return project.user == self.request.user
    
class TaskUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model=models.Task
    fields= ['is_completed']
    http_method_names = ['post']
    def get_success_url(self):
        return reverse('Project_update', args= [self.object.project.id])
    
    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id
    
class TaskDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model=models.Task
    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id

    def get_success_url(self):
        return reverse('Project_update', args= [self.object.project.id])





