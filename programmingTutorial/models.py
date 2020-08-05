from django.db import models

# Create your models here.


class Language(models.Model):
    LanguageName = models.CharField(max_length=200, primary_key=True)   

    def __str__(self):
        return self.LanguageName



class ProgrammingTutorial(models.Model):
    languageName = models.ForeignKey(Language, on_delete=models.CASCADE)
    ptAuthor = models.CharField(max_length=200)
    postId = models.AutoField(primary_key=True, auto_created=True)
    ptTitle = models.CharField(max_length=200)
    ptTimeDate = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    ptDescriptions = models.TextField()
    ptCode = models.TextField()
    ptUrl = models.TextField(blank=True)
    ptImage = models.ImageField(blank=True, null=True)
    views = models.IntegerField(default=0)
    
    