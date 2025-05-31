from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL

class Category(models.Model):
    name= models.CharField(max_length= 255)


    def __str__(self):
        return self.name
    
class ProjectStatus(models.IntegerChoices):
    PENDING = 1, 'pending'
    COMPLETE = 2,'complete'
    POSTPNED = 3,'postponed'
    CANCELED = 4, 'canceled'
    
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.IntegerField(
        choices=ProjectStatus.choices,
        default=ProjectStatus.PENDING
    )
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    category= models.ForeignKey(Category, on_delete=models.PROTECT)
    user= models.ForeignKey(AUTH_USER_MODEL , on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title
    

class Task(models.Model):
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project , on_delete=models.CASCADE)

    def __str__(self):
        return self.description
    
    

    

    
