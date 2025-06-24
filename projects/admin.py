from django.contrib import admin
from . import models
from django.db.models import Count
from django.utils.translation import gettext_lazy as _

admin.site.register(models.Category)

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display= ['title', 'status','user', 'category','created_at','tasks_count']
    list_per_page = 10
    list_select_related= [ 'category','user']
    list_editable= ['status']
    def tasks_count(self,obj):
        return obj.tasks_count
    tasks_count.short_description = _("tasks count")

    def get_queryset(self, request):
        query= super().get_queryset(request)
        query =query.annotate(tasks_count=Count('task'))
        return query

@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display= ['id', 'description','project','is_completed']
    list_per_page = 10
    list_editable = ['is_completed']