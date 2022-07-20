from datetime import datetime, timedelta
import random
import factory, factory.fuzzy
from factory.django import DjangoModelFactory

from core.models import Profile
from auction.models import *

MU = 2
SIGMA = 1

def random_date_between_dates(start: datetime, end: datetime) -> datetime:

    delta = end - start
    secs = (delta.days * 24 * 60 * 60) + delta.seconds

    return start + timedelta(seconds = random.randrange(secs))

class BidFactory(DjangoModelFactory):
    
    class Meta:
        model = Bid
    



class MemeFactory(DjangoModelFactory):
    
    class Meta:
        model = Meme
    
    

class AuctionFactory(DjangoModelFactory):
    
    class Meta:
        model = Auction

    author = factory.Iterator(Profile.objects.all())

    initial_price = factory.fuzzy.FuzzyInteger(0, 10000)
    
    starts_at = factory.Faker('future_datetime', end_date = '+365d')

    @factory.post_generation
    def limit(self, create, extracted, **kwargs):

        if(extracted):
            self.limit = extracted
            return
        
        if(random.random() <= 0.667):
            self.limit = round(self.initial_price + self.initial_price * random.normalvariate(MU, SIGMA))
        
        return
    
    @factory.post_generation
    def ends_at(self, create, extracted, **kwargs):

        if(extracted):
            self.ends_at = extracted
            return
        
        self.ends_at = random_date_between_dates(
            start = self.starts_at,
            end = self.starts_at + timedelta(days = 30)
        )