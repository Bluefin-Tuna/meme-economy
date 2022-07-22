from datetime import datetime, timedelta
import random
import factory, factory.fuzzy
from factory.django import DjangoModelFactory

from core.factories import ProfileFactory
from core.models import Profile
from auction.models import *

MU = 1
SIGMA = 1

def random_date_between_dates(start: datetime, end: datetime) -> datetime:

    delta = end - start
    secs = (delta.days * 24 * 60 * 60) + delta.seconds

    return start + timedelta(seconds = random.randrange(secs))

class BidFactory(DjangoModelFactory):
    
    class Meta:
        model = Bid

    profile = factory.Iterator(Profile.objects.all())
    auction = factory.Iterator(Auction.objects.all())

    @factory.post_generation
    def value(self, create, extracted, **kwargs):
        
        if not self.profile:
            self.profile = ProfileFactory.create()
        
        if not self.auction:
            self.auction = AuctionFactory.create()

        values = Bid.objects.filter(auction = self.auction.id).values_list('value').all()
        values = [v[0] for v in values if v[0] != None]
        if(len(values) <= 1):
            self.value = self.auction.initial_price
        else:
            self.value = max(values) + random.randint(1, 100)


class MemeFactory(DjangoModelFactory):
    
    class Meta:
        model = Meme
    
    name = factory.Faker('sentence', nb_words = 3)
    description = factory.Faker("paragraph", nb_sentences = 3)
    likes = factory.fuzzy.FuzzyInteger(0, 10000)
    views = factory.fuzzy.FuzzyInteger(0, 200000)
    price = factory.fuzzy.FuzzyInteger(0, 10000)

    file = factory.django.FileField(filename = "example.gif")

    @factory.post_generation
    def owner(self, create, extracted, **kwargs):

        if(extracted):
            self.owner = extracted
            return
        
        self.owner = random.choice(list(Profile.objects.all()))

class AuctionFactory(DjangoModelFactory):
    
    class Meta:
        model = Auction

    author = factory.Iterator(Profile.objects.all())
    initial_price = factory.fuzzy.FuzzyInteger(0, 10000)
    starts_at = factory.Faker('future_datetime', end_date = '+365d')

    @factory.post_generation
    def limit(self, create, extracted, **kwargs):

        print('entered')
        if(extracted):
            print('extracted found')
            self.limit = extracted
            return
        
        if(random.random() <= 0.667):
            print('entered limit creation')
            self.limit = round(self.initial_price * (1 + abs(random.normalvariate(MU, SIGMA))))
            print(self.limit)
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
    
    @factory.post_generation
    def memes(self, create, extracted, **kwargs):

        if(extracted):
            for obj in extracted:
                self.memes.add(obj)
        
        memes = MemeFactory.create_batch(random.randint(1, 3), owner = self.author)
        for meme in memes:
            self.memes.add(meme)
