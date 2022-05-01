from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=20)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    hits = models.PositiveIntegerField(default = 0)
    image = models.ImageField(upload_to = "blog/", blank=True, null=True)
    def __str__(self):
        return self.title
        
    def summary(self):
        return self.contents[:100]

   
