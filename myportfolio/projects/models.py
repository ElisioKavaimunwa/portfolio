from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')

    #image = models.FilePathField(path="/img")
    #image = models.FilePathField(path="/djangoApp/personal_portfolio/projects/static/img")
    
    def __str__(self):
        return self.title
