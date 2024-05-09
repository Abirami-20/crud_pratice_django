from django.contrib import admin
from crudapp.models import Student
class StudentAdmin(admin.ModelAdmin):
    list=['sno','sname','sclass','saddress']
admin.site.register(Student,StudentAdmin)
# Register your models here.
