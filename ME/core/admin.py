from django.contrib import admin
from auction.models import Auction, Bid, Meme
from core.models import User

# Register your models here.
admin.site.register(User)

admin.site.register(Auction)
admin.site.register(Meme)