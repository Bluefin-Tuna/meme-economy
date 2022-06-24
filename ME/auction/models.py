from django.db import models
import ME.core.models


class Auction(models.Model):
    
    id = models.AutoField(primary_key = True)

    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.id} {self.starts_at}-{self.ends_at}"
    
    def __repr__(self) -> str:
        return f"<Auction {self.id}>"

class Bid(models.Model):

    id = models.AutoField(primary_key = True)

    user = models.OneToOneField(
        ME.core.models.User,
        related_name = "auction",
        on_delete = models.CASCADE,
        primary_key = False
    )
    auction = models.ForeignKey(Auction, related_name = "bids", on_delete = models.CASCADE)
    value = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user} {self.value}"
    
    def __repr__(self) -> str:
        return f"<Bid {self.id}>"