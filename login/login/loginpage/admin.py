
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Products

@admin.register(Products)
class ProductsAdmin(ImportExportModelAdmin):
    pass
