import datetime
from django.db import models
from django.utils import timezone

# Create your models here.



class Post(models.Model):

	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	delete_date = models.DateTimeField(blank=True,null=True)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True,null=True)
	none_date = models.DateTimeField(blank=True,null=True)


class PostImage(models.Model):

	post = models.ForeignKey('blog.Post',related_name='image_set')
	picture = models.ImageField(upload_to='name/')

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.ForeignKey('auth.User',related_name='users')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    def approve(self):
        self.approved_comment = True
        self.save()
    def __str__(self):
        return self.text
def approved_comments(self):
    return self.comments.filter(approved_comment=True)
