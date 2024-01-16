from django.contrib import admin
from .models import Phone

# Register your models here.
class PhoneAdmin(admin.ModelAdmin):
    list_filter = ('price','model_p')
    list_display = ('at_data','model_p')
    search_fields = ('name','price')

admin.site.register(Phone,PhoneAdmin)