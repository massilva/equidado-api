from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'cnpj', 'legal_name', 'trade_name', 'address')
    search_fields = ('cnpj', 'legal_name', 'trade_name')
