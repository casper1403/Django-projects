from django.contrib import admin
from .models import BookModel,GameModel
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(BookModel,ImportExportModelAdmin)
admin.site.register(GameModel,ImportExportModelAdmin)
