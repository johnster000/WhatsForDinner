from django.contrib import admin
from .models import *

class DinnerAdmin(admin.ModelAdmin):
    model = Dinner
    list_display = ['id', 'dish', 'Created_By']

class DateAdmin(admin.ModelAdmin):
    model = Date
    list_display = ['id', 'Date', 'get_dinner']

    def get_dinner(self, obj):
        return obj.Dinner.dish
    get_dinner.admin_order_field = 'Dinner'  #Allows column order sorting
    get_dinner.short_description = 'Dinner'  #Renames column head
  
admin.site.register(Dinner, DinnerAdmin)
admin.site.register(Date, DateAdmin)