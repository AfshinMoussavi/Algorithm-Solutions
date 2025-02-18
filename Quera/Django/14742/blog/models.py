from django.db import models
from datetime import datetime, timezone



class Author(models.Model):
    name = models.CharField(max_length=50)
    

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def copy(self):
        new_copy = self.__class__.objects.create(
            title=self.title,
            body=self.body,
            date_created= datetime.now(timezone.utc),
            author = self.author
            )
        for comment in self.comment_set.all():
            Comment.objects.create(blog_post=new_copy, text=comment.text)

        return new_copy.id

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    


