from django.db import models
import ME.auction.models

class User(models.Model):

    id = models.AutoField(primary_key = True)

    email = models.EmailField(unique = True)
    username = models.CharField(max_length = 30, unique = True, null = False)
    password = models.CharField(max_length = 30, unique = False, null = False)
    profile_picture = models.ImageField(upload_to = "pfp", null = True)
    currency = models.BigIntegerField(default = 1000)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User {self.id}>"

class Meme(models.Model):
    
    id = models.AutoField(primary_key = True)
    owner = models.ForeignKey(User, related_name = "memes", on_delete = models.SET_NULL)
    auction = models.ForeignKey(ME.auction.models.Auction, related_name = "memes", on_delete = models.SET_NULL)

    name = models.CharField(max_length = 50, null = False)
    description = models.CharField(max_length = 200, default = "")
    likes = models.IntegerField(default = 0)
    views = models.IntegerField(default = 0)
    price = models.IntegerField(default = 0)
    file = models.FileField(upload_to = "memes", null = False)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name
    
    def __repr__(self) -> str:
        return f"<Meme {self.id}>"