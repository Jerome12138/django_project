from django.db import models

# Create your models here.

class UserInfo(models.Model):
    email = models.EmailField(max_length=32, verbose_name='邮箱', unique=True)
    username = models.CharField(max_length=32, verbose_name='用户名', unique=True)
    nickname = models.CharField(max_length=32, verbose_name='昵称')
    password = models.CharField(max_length=32, verbose_name='密码')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    is_admin = models.IntegerField(default=0,verbose_name='是否管理员')

    def __str__(self):
        return self.nickname