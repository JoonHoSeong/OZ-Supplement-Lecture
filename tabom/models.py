from django.db import models


class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


# Create your models here.
class User(BaseModel):
    name = models.CharField(max_length=50)


class Article(BaseModel):
    title = models.CharField(max_length=255)


class Like(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
