from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from auth.models import UserProfile


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    starts_on = models.DateField()
    ends_on = models.DateField()
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CourseModules(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


EVALUATION_TYPE = (
    ('quiz', 'Quiz'),
    ('assignment', 'Assignment')
)


class CourseEvaluations(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='evaluations')
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    type = models.CharField(max_length=20, choices=EVALUATION_TYPE)
    evaluation_on = models.DateTimeField()
    total_marks = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CourseEnrolments(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrolments')
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.name} - {self.course.name}"
