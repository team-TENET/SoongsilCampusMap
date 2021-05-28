from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = "post/", blank=True, null=True)
    author = models.ForeignKey(User, related_name="post", on_delete=CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
