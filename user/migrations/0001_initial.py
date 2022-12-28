# Generated by Django 3.2.8 on 2022-12-28 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False, verbose_name='地址编号')),
                ('district', models.CharField(max_length=20, verbose_name='校区')),
                ('building', models.CharField(max_length=20, verbose_name='校内建筑')),
                ('room', models.CharField(max_length=20, verbose_name='门牌号')),
            ],
            options={
                'verbose_name': '地址信息',
                'verbose_name_plural': '地址信息',
                'db_table': 'address',
                'ordering': ['-address_id'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, verbose_name='用户编号')),
                ('user_name', models.CharField(max_length=20, verbose_name='用户昵称')),
                ('user_password', models.CharField(max_length=20, verbose_name='用户密码')),
                ('user_tel', models.CharField(max_length=11, verbose_name='用户电话')),
                ('user_status', models.IntegerField(choices=[(0, '离线'), (1, '在线')], default=0, verbose_name='用户状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.address', verbose_name='地址')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'user',
                'ordering': ['user_id'],
            },
        ),
    ]
