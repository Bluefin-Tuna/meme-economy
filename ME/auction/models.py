from django.db import models
from django.utils import timezone
from core.models import Profile


class Auction(models.Model):
    
    id = models.BigAutoField(primary_key = True)

    initial_price = models.PositiveBigIntegerField(nullable = False)
    limit = models.PositiveBigIntegerField(nullable = True)

    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.id} {self.starts_at}-{self.ends_at}"
    
    def __repr__(self) -> str:
        return f"<Auction {self.id}>"


class Meme(models.Model):
    
    id = models.BigAutoField(primary_key = True)
    owner = models.ForeignKey(Profile, related_name = "memes", on_delete = models.SET_NULL, null = True)
    auction = models.ForeignKey(Auction, related_name = "memes", on_delete = models.SET_NULL, null = True)

    name = models.CharField(max_length = 50, null = False)
    description = models.CharField(max_length = 200, default = "")
    likes = models.IntegerField(default = 0)
    views = models.IntegerField(default = 0)
    price = models.IntegerField(default = 0)
    file = models.FileField(upload_to = "memes", null = False, unique = True, editable = False)

    created_at = models.DateTimeField(editable = False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()

        return super(Meme, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def __repr__(self) -> str:
        return f"<Meme {self.id}>"


class Bid(models.Model):

    id = models.BigAutoField(primary_key = True)

    user = models.OneToOneField(
        Profile,
        related_name = "auction",
        on_delete = models.CASCADE,
        primary_key = False
    )
    auction = models.ForeignKey(Auction, related_name = "bids", on_delete = models.CASCADE)
    value = models.IntegerField()

    created_at = models.DateTimeField(editable = False)

    def save(self, *args, **kwargs):
        
        if not self.id:
            self.created_at = timezone.now()

        return super(Bid, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} {self.value}"
    
    def __repr__(self) -> str:
        return f"<Bid {self.id}>"