from django.db import models
 

class BlogData(models.Model):
    blogtitle=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='pics')
    desc=models.TextField()
    files=models.FileField(upload_to='files')

    def __str__(self):
        return self.title