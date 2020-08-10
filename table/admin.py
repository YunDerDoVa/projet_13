from django.contrib import admin

from .models import TablePost, TableLike, TableComment


# Register your models here.
class TablePostAdmin(admin.ModelAdmin):
    model = TablePost

admin.site.register(TablePost, TablePostAdmin)
