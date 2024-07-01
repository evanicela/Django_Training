from django.contrib import admin
from .models import Service


class CourseAdmin(admin.ModelAdmin):
    list_display = ["servName", "coursePrice", "courseDuration"]
    list_editable = ["coursePrice"]


admin.site.register(Service)

