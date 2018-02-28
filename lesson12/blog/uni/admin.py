from django.contrib import admin

# Register your models here.

from uni.models import University
from uni.models import Student
from uni.models import StudentTicket
from uni.models import ExtraClass

admin.site.register(University)
admin.site.register(Student)
admin.site.register(StudentTicket)
admin.site.register(ExtraClass)