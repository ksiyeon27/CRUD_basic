from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(verbose_name='제목', max_length=100)
    writer = models.CharField(verbose_name='글쓴이', max_length=50)
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        # 정체성을 달아주는 느낌. 화면에 이걸로보이지. postobject~이런식이 아니라.
