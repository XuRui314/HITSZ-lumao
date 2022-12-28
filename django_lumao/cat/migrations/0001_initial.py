# Generated by Django 3.2.8 on 2022-12-28 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False, verbose_name='猫咪编号')),
                ('cat_name', models.CharField(max_length=10, verbose_name='猫咪名称')),
                ('cat_photo', models.ImageField(blank=True, null=True, upload_to='images/cat', verbose_name='猫咪照片')),
                ('cat_character', models.CharField(max_length=10, verbose_name='猫咪性格')),
                ('cat_color', models.CharField(max_length=10, verbose_name='猫咪颜色')),
                ('cat_breed', models.CharField(max_length=10, verbose_name='猫咪品种')),
                ('cat_location', models.CharField(max_length=10, verbose_name='经常出没的地点')),
                ('cat_food', models.CharField(max_length=10, verbose_name='喜欢吃的食物')),
            ],
            options={
                'verbose_name': '猫咪信息',
                'verbose_name_plural': '猫咪信息',
                'db_table': 'cat',
                'ordering': ['cat_id'],
            },
        ),
        migrations.CreateModel(
            name='CatManager',
            fields=[
                ('manager_id', models.AutoField(primary_key=True, serialize=False, verbose_name='饲养员编号')),
                ('manager_name', models.CharField(max_length=20, verbose_name='饲养员昵称')),
                ('manager_cat', models.ManyToManyField(to='cat.Cat')),
            ],
            options={
                'verbose_name': '饲养员信息',
                'verbose_name_plural': '饲养员信息',
                'db_table': 'cat_manager',
                'ordering': ['manager_id'],
            },
        ),
    ]