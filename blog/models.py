from django.db import models

# Create your models here.

class UserInfo(models.Model):
    email = models.EmailField(max_length=32, verbose_name='邮箱', unique=True)
    username = models.CharField(max_length=32, verbose_name='用户名', unique=True)
    nickname = models.CharField(max_length=32, verbose_name='昵称')
    password = models.CharField(max_length=32, verbose_name='密码')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __str__(self):
        return self.nickname


class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name='分类名称', unique=True)
    user = models.ForeignKey(
        UserInfo, verbose_name='作者', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='标签名称', unique=True)
    user = models.ForeignKey(
        UserInfo, verbose_name='作者', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=64, verbose_name='标题')
    content = models.TextField(verbose_name='内容', blank=True, null=True)
    user = models.ForeignKey(
        UserInfo, verbose_name='作者', on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    read_count = models.IntegerField(default=0, verbose_name='阅读数')
    comment_count = models.IntegerField(default=0, verbose_name='评论数')
    up_count = models.IntegerField(default=0, verbose_name='点赞数')
    down_count = models.IntegerField(default=0, verbose_name='踩数')
    category = models.ForeignKey(
        Category, verbose_name='分类', on_delete=models.CASCADE, default=0)
    tags = models.ManyToManyField(Tag, through='Article2Tag',
                                  through_fields=('article', 'tag'), verbose_name='标签', blank=True)


class Article2Tag(models.Model):
    article = models.ForeignKey(
        Article, verbose_name='文章', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, verbose_name='标签', on_delete=models.CASCADE)

    class Meta:
        unique_together = [('article', 'tag'), ]


class Comment(models.Model):
    article = models.ForeignKey(
        Article, verbose_name='评论文章', on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserInfo, verbose_name='评论者', on_delete=models.CASCADE)
    layer_id = models.IntegerField(verbose_name='楼层号')
    reply = models.ForeignKey(to='Comment', related_name='back', null=True, blank=True,
                              verbose_name='回复评论', on_delete=models.CASCADE)
    content = models.CharField(max_length=255, verbose_name='评论内容')
    create_time = models.DateTimeField(auto_now_add=True)


class UpDown(models.Model):
    article = models.ForeignKey(
        Article, verbose_name='文章', on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserInfo, verbose_name='用户', on_delete=models.CASCADE)
    up_down = models.BooleanField(verbose_name='赞或踩')  # true为赞，false为踩

    class Meta:
        unique_together = [('article', 'user'), ]
