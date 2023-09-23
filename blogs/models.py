from django.db import models


class Post(models.Model):
    _id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.title
