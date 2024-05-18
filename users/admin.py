from django.contrib import admin

from users.models import UserModel

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('date_joined', 'email')
    search_fields = ('email',)
