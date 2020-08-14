from django.contrib import admin

from .models import TablePost, TableLike, TableComment


# Register your models here.
class TablePostAdmin(admin.ModelAdmin):
    model = TablePost


class TableLikeAdmin(admin.ModelAdmin):
    model = TableLike


admin.site.register(TablePost, TablePostAdmin)
admin.site.register(TableLike, TableLikeAdmin)
