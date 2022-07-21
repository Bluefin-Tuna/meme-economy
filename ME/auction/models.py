from django.db import models
from django.utils import timezone
from core.models import Profile


class Auction(models.Model):
    
    id = models.BigAutoField(primary_key = True)

    author = models.ForeignKey(Profile, related_name = "auctions_authored", on_delete = models.SET_NULL, null = True)
    participants = models.ManyToManyField(Profile, related_name = "auctions_participated", through = "Bid")

    initial_price = models.PositiveBigIntegerField(null = False, default = 0)
    limit = models.PositiveBigIntegerField(null = True)

    starts_at = models.DateTimeField(null = True)
    ends_at = models.DateTimeField(null = True)

    def __str__(self) -> str:
        return f"{self.id} {self.starts_at}-{self.ends_at}"
    
    def __repr__(self) -> str:
        return f"<Auction {self.id}>"


class Meme(models.Model):
    
    id = models.BigAutoField(primary_key = True)
    owner = models.ForeignKey(Profile, related_name = "memes", on_delete = models.SET_NULL, null = True)
    auction = models.ForeignKey(Auction, related_name = "memes", on_delete = models.SET_NULL, null = True)

    name = models.CharField(max_length = 50, null = False)
    description = models.TextField(max_length = 200, default = "")
    likes = models.IntegerField(default = 0)
    views = models.IntegerField(default = 0)
    price = models.IntegerField(default = 0)
    file = models.FileField(upload_to = "uploads/", null = False, unique = True, editable = False)

    created_at = models.DateTimeField(editable = False)
    updated_at = models.DateTimeField(default = timezone.now)

    def save(self, *args, **kwargs):
        
        if not self.id:
            self.created_at = timezone.now()
            self.updated_at = timezone.now()
        self.updated_at = timezone.now()

        return super(Meme, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def __repr__(self) -> str:
        return f"<Meme {self.id}>"


class Bid(models.Model):

    profile = models.ForeignKey(Profile, related_name = "bids", on_delete = models.SET_NULL, null = True) # Will be changed to model.SET logic later down the line.
    auction = models.ForeignKey(Auction, related_name = "bids", on_delete = models.CASCADE)
    
    value = models.IntegerField(null = True)

    created_at = models.DateTimeField(editable = False)

    def save(self, *args, **kwargs):
        
        if not self.id:
            self.created_at = timezone.now()

        return super(Bid, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} {self.value}"
    
    def __repr__(self) -> str:
        return f"<Bid {self.id}>"