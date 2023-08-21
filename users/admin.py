from django.contrib import admin
from users.models import User
from main.admin import BasketAdmin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display =('username',)
    inlines = (BasketAdmin,)
