from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)  # the title of the blog
    category = models.CharField(max_length = 50, blank = True)  # the label of the blog
    date_time = models.DateTimeField(auto_now_add = True)  # the publish time of the blog
    content = models.TextField(blank = True, null = True)  # the content of the blog

    def _unicode_(self):
        return self.title

    class Meta: # be ordered by time
        ordering = ['-date_time']