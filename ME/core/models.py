from django.db import models

class User(models.Model):

    email = models.EmailField(unique = True)
    username = models.CharField(max_length = 30, unique = True, null = False)
    password = models.CharField(max_length = 30, unique = False, null = False)
    profile_picture = models.Fil