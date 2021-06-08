from django.contrib import admin
from course.models import Course, CourseModules, CourseEvaluations, CourseEnrolments

# Register your models here.


admin.site.register([Course, CourseModules, CourseEvaluations, CourseEnrolments])