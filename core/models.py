from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Articles(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Владелец статьи', blank = True, null = True )
    create_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Статью'
        verbose_name_plural='Статьи'


class Comments(models.Model):
    article = models.ForeignKey(Articles, on_delete = models.CASCADE, verbose_name='Статья', blank = True, null = True,related_name='comments_articles' )
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Автор комментария', blank = True, null = True )
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='Текст комментария')
    status = models.BooleanField(verbose_name='Видимость статьи', default=False)
