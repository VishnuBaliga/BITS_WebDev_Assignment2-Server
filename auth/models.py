from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.db import models

# Create your models here.


USER_TYPE = (
    ('student', 'Student'),
    ('teacher', 'Teacher')
)


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, validators=[validate_email])
    dob = models.DateField()
    type = models.CharField(max_length=20, choices=USER_TYPE)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
