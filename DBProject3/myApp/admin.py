from django.contrib import admin
from myApp.models import Customer
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    l=['name','age','emailid','phoneNumber']
admin.site.register(Customer,CustomerAdmin)
