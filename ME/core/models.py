from typing import List
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    id = models.AutoField(primary_key = True)

    email = models.EmailField(unique = True)
    username = models.CharField(max_length = 50, unique = True, null = False, blank = False)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    USERNAME_FIELD: str = "email"
    REQUIRED_FIELDS: List[str] = ["password", "first_name", "last_name"]

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User {self.id}>"


class Profile(models.Model):

    id = models.AutoField(primary_key = True)
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