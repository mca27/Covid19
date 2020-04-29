from django.contrib import admin

# Register your models here.
from .models import IndiaCases, Districts

admin.site.register(IndiaCases)
admin.site.register(Districts)
