from django.contrib import admin

from .models import User, Address


# 在admin中注册绑定
class UserAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['address__building']
    list_display = ['user_id', 'user_name', 'user_tel', 'address', 'user_status', 'create_time']


class AddressAdmin(admin.ModelAdmin):
    search_fields = ['building']
    list_per_page = 10
    list_display = ['address_id', 'district', 'building', 'room']




admin.site.register(User, UserAdmin)
admin.site.register(Address, AddressAdmin)


admin.site.site_header = 'HITSZ撸猫管理系统'
admin.site.site_title = 'HITSZ撸猫管理系统'
