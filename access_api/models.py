from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=50)
    access = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title

    def set_post_access(self, id, access_key):
        queryset = Post.objects.filter(id=id)
        for model in queryset:
            model.access = access_key
            model.save()
