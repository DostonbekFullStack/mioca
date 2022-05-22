from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

# Register your models here.

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['id', 'username','first_name','last_name','type','is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ('type', 'phone')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(Logo)
admin.site.register(Info)
admin.site.register(Slider)
admin.site.register(Categorie)
admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(Facilities)
admin.site.register(Forsale)
admin.site.register(Bestsell)
admin.site.register(Latestblog)
admin.site.register(Newsletter)
admin.site.register(TeamMembers)
admin.site.register(Client)
admin.site.register(Sponsor)
admin.site.register(LeaveMsg)
admin.site.register(Map)