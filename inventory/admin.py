from django.contrib import admin

# Register your models here.

from inventory.models import Warehouse,Location,Stock


from import_export.admin import ImportExportModelAdmin
from imp_exp.admin import WarehouseResource,StockResource

class WareHouseADMin(ImportExportModelAdmin):
    resource_class = WarehouseResource

class StockAdmin(ImportExportModelAdmin):
    resource_class = StockResource


admin.site.register(Warehouse,WareHouseADMin)
admin.site.register(Location)
admin.site.register(Stock,StockAdmin)

