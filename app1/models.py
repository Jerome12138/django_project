from django.db import models


# Create your models here.

class WorkData(models.Model):
    company_name = models.CharField(max_length=32, verbose_name='公司名称')
    products = models.CharField(max_length=32, verbose_name='主要产品')
    work_place = models.CharField(max_length=32, verbose_name='工作地点')
    salary = models.CharField(max_length=32, verbose_name='薪资', null=True)
    preaching_time = models.CharField(max_length=32, verbose_name='宣讲时间')
    preaching_place = models.CharField(max_length=32, verbose_name='宣讲地点')
    preaching = models.CharField(max_length=32, verbose_name='宣讲')
    delivery = models.CharField(max_length=32, verbose_name='投递')
    delivery_time = models.CharField(max_length=32, verbose_name='投递时间')
    position_1 = models.CharField(max_length=32, verbose_name='职位1')
    position_2 = models.CharField(max_length=32, verbose_name='职位2')
    assessment = models.CharField(max_length=32, verbose_name='测评')
    examination = models.CharField(max_length=32, verbose_name='笔试')
    interview = models.CharField(max_length=32, verbose_name='面试')
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    notes = models.CharField(max_length=32, verbose_name='备注', null=True)
    preaching_information_link = models.CharField(max_length=32, verbose_name='宣讲信息', null=True)
    delivery_link = models.CharField(max_length=32, verbose_name='网申链接', null=True)


class Status(models.Model):
    status = models.CharField(max_length=32, verbose_name='状态')

# python manage.py makemigrations
# python manage.py migrate
