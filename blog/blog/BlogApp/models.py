from django.db import models
from  django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class BlogPost(models.Model):
    title = models.CharField(max_length = 40)
    content = models.CharField(max_length=5000,  null=True)
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('Blog:Index')

        # kwargs={'pk':self.pk})

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment = models.CharField(max_length = 200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('Blog:Post-detail',kwargs={'pk':self.post.pk})
