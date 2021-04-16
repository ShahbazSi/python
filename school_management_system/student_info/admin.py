from django.contrib import admin
from .models import Details
# Register your models here.
admin.site.register(Details)
list_display=['student_name','father_name','PhoneNo']