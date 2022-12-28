# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone


class User(models.Model):
    user_id = models.AutoField(primary_key=True, verbose_name='用户编号')
    user_name = models.CharField(max_length=20, verbose_name='用户昵称')
    user_password = models.CharField(max_length=20, verbose_name='用户密码')
    user_tel = models.CharField(max_length=11, verbose_name="用户电话")
    address = models.ForeignKey('Address', models.SET_NULL, null=True, blank=True, verbose_name='地址')
    user_status = models.IntegerField(choices=[(0, '离线'), (1, '在线')], default=0, verbose_name="用户状态")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        ordering = ['user_id']
        db_table = 'user'
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_name


class Address(models.Model):
    address_id = models.AutoField(primary_key=True, verbose_name='地址编号')
    district = models.CharField(max_length=20, verbose_name='校区')
    building = models.CharField(max_length=20, verbose_name='校内建筑')
    room = models.CharField(max_length=20, verbose_name='门牌号')

    class Meta:
        ordering = ['-address_id']
        db_table = 'address'
        verbose_name = "地址信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.district} {self.building} {self.room}'


