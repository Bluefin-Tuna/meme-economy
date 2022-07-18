import factory
from factory.django import DjangoModelFactory

from .models import *

class BidFactory(DjangoModelFactory):
    
    class Meta:
        model = Bid
    
    

class MemeFactory(DjangoModelFactory):
    
    class Meta:
        model = Meme
    
    

class AuctionFactory(DjangoModelFactory):
    
    class Meta:
        model = Auction
    
