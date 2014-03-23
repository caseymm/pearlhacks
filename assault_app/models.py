from django.db import models

# Create your models here.

class Schools(models.Model):
    title = models.CharField(unique=True, max_length=100)
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    content = models.TextField()
    
    
    def __unicode__(self):
        return self.title
        return self.creation_date 

        




    
    
