from django.contrib import admin

from django.contrib import admin
from .models import Test

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['city','code','year','month','in_process','condition1','condition2','Condition3','total_condition']
    list_per_page = 10
