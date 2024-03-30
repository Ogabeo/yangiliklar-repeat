from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

# Create your models here.

class User(AbstractUser):
    phone=models.CharField(max_length=15, null=True, blank=True)
    avatar=models.ImageField(upload_to="image_avatar", null=True, blank=True, 
                            validators=[FileExtensionValidator(  allowed_extensions=('jpeg', 'heic', 'png', 'jpeg')) ])
    
    @property

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    