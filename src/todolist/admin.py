from django.contrib import admin
from .models import *

from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin

admin.site.register(User)


class TaskAdmin(admin.ModelAdmin):
    list_filter = (
        ('due_date', JDateFieldListFilter),
    )


admin.site.register(Task, TaskAdmin)

# Register your models here.
admin.site.register(Category)
