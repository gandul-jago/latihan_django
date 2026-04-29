#ini ak komentarin keknya krn ikut modul 7
""" from django.contrib import admin
from pos_app.models import TableResto
from import_export.admin import ImportExportModelAdmin
from pos_app.models import StatusModel, Category, MenuResto
# Register your models here.

admin.site.register(TableResto)

@admin.register(StatusModel)
class StatusAdmin(ImportExportModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    pass

@admin.register(MenuResto)
class MenuAdmin(ImportExportModelAdmin):
    pass """

#ini gada tombol export
""" from django.contrib import admin
from pos_app.models import StatusModel, Category, MenuResto

admin.site.register(StatusModel)
admin.site.register(Category)
admin.site.register(MenuResto) """


from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from pos_app.models import StatusModel, Category, MenuResto

@admin.register(StatusModel)
class StatusAdmin(ImportExportModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    pass

@admin.register(MenuResto)
class MenuAdmin(ImportExportModelAdmin):
    pass