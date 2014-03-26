from django.db import models
from django.forms import ModelForm

class Schools(models.Model):
    name = models.CharField(unique=True, max_length=100)
    #creation_date = models.DateField(auto_now_add=True)
    #last_modified = models.DateField(auto_now=True)
    population = models.TextField()
    city = models.TextField()
    state = models.TextField()
    newspaper = models.TextField()
    newspaper_link = models.TextField()
    newspaper_sexualassault = models.TextField()
    male_ratio = models.TextField()
    female_ratio = models.TextField()
    priv_pub = models.TextField()
    male_greeklife = models.TextField()
    female_greeklife = models.TextField()
    campus_health = models.TextField()
    sexual_health = models.TextField()
    counseling = models.TextField()
    lat = models.TextField()
    longitude = models.TextField()
    content = models.TextField()
    #articles = models.TextField()
    
    def __unicode__(self):
        return self.name
        return self.creation_date 

class Comment(models.Model):
    school = models.ForeignKey(Schools)
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'body', 'school']

#class SchoolStoryFeed(models.Model):
#    schools = models.ForeignKey(Schools)
#    title = models.CharField(max_length=1000)
#    body = models.TextField()
#    timestamp = models.DateTimeField(auto_now=True)

#    def __unicode__(self):
#        return self.title
#        return self.body
#        return self.timestamp
        




    
    
