from django.contrib import admin

# Register your models here.

from .models import Cat, CatManager


# 在admin中注册绑定
class CatAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['cat_id','cat_name','cat_photo','cat_character','cat_color','cat_breed','cat_location','cat_food']


class CatManagerAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['manager_id', 'manager_name']


admin.site.register(Cat, CatAdmin)
admin.site.register(CatManager, CatManagerAdmin)

