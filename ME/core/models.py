from typing import List
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):

    id = models.BigAutoField(primary_key = True)
    
    email = models.EmailField(unique = True)
    username = models.CharField(max_length = 50, unique = True, null = False, blank = False)

    date_joined = models.DateTimeField(editable = False)
    date_updated = models.DateTimeField()

    USERNAME_FIELD: str = "email"
    REQUIRED_FIELDS: List[str] = ["username", "password", "first_name", "last_name"]

    def save(self, *args, **kwargs):
        
        if not self.id:
            self.date_joined = timezone.now()
        self.date_updated = timezone.now()

        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User {self.id}>"


class Profile(models.Model):

    id = models.BigAutoField(primary_key = True)
    user = models.OneToOneField(
        User,
        related_name = "profile",
        on_delete = models.CASCADE,
        primary_key = False
    )

    assets = models.BigIntegerField(default = 1000)
    profile_picture = models.ImageField(upload_to = "pfp", null = True)

    def __str__(self) -> str:
        return f"{self.user} {self.assets}"

    def __repr__(self) -> str:
        return f"<Profile {self.id}>"