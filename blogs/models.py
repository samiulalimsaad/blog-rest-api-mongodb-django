from django.db import models


class Post(models.Model):
    pid = models.CharField(max_length=200, primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.title
