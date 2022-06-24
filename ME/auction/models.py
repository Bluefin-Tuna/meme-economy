from django.db import models
import ME.core.models


class Auction(models.Model):
    
    id = models.AutoField(primary_key = True)

    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()

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