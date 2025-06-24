from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name= models.CharField(max_length= 255)


    def __str__(self):
        return self.name
    class Meta:
        verbose_name= _('Category')
        verbose_name_plural= _('Category')
    
class ProjectStatus(models.IntegerChoices):
    PENDING = 1, _('Pending')
    COMPLETE = 2, _('Complete')
    POSTPONED = 3, _('Postponed')
    CANCELED = 4, _('Canceled')
    
class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    status = models.IntegerField(
        choices=ProjectStatus.choices,
        default=ProjectStatus.PENDING,
        verbose_name=_('Status')
    )
    created_at= models.DateTimeField(auto_now_add=True,verbose_name=_('Created at'))
    updated_at= models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name=_("Category"))
    user= models.ForeignKey(AUTH_USER_MODEL , on_delete=models.CASCADE,verbose_name=_('User'), null=True)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name= _('Project')
        verbose_name_plural= _('Project')
    

class Task(models.Model):
    description = models.TextField(verbose_name=_('Description'))
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project , on_delete=models.CASCADE)

    def __str__(self):
        return self.description
    class Meta:
        verbose_name= _('Task')
        verbose_name_plural= _('Task')
    
    

    

    
