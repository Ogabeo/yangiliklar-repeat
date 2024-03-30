from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=('id', 'full_name', 'is_staff', 'email')
    list_display_links=('id', 'full_name')


admin.site.register(User, UserAdmin)
