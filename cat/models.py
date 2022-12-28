from django.db import models

# Create your models here. 评论呢？我还没写，。。。
# class Cat(models.Model)

from django.db import models


class Cat(models.Model):
    cat_id = models.AutoField(primary_key=True, verbose_name='猫咪编号')
    cat_name = models.CharField(max_length=10, verbose_name='猫咪名称')
    cat_photo = models.ImageField(upload_to='images/cat', null=True, blank=True, verbose_name='猫咪照片')
    cat_character= models.CharField(max_length=10, verbose_name='猫咪性格')
    cat_color = models.CharField(max_length=10, verbose_name='猫咪颜色')
    cat_breed = models.CharField(max_length=10, verbose_name='猫咪品种')
    cat_location = models.CharField(max_length=10, verbose_name='经常出没的地点')
    cat_food = models.CharField(max_length=10, verbose_name='喜欢吃的食物')


    class Meta:
        ordering = ['cat_id']
        db_table = 'cat'
        verbose_name = "猫咪信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cat_name


class CatManager(models.Model):
    manager_id = models.AutoField(primary_key=True, verbose_name='饲养员编号')
    manager_name = models.CharField(max_length=20, verbose_name='饲养员昵称')
    manager_cat = models.ManyToManyField('Cat')

    class Meta:
        ordering = ['manager_id']
        db_table = 'cat_manager'
        verbose_name = "饲养员信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.manager_name