import warnings
from django.core.management.base import BaseCommand, CommandError
from halo import Halo
from core.models import User
from auction.models import Auction
from core.factories import UserFactory
from auction.factories import AuctionFactory, BidFactory

DEFAULT = 100

class Command(BaseCommand):

    help = 'Generate fake data for models. Default is 100.'

    def add_arguments(self, parser) -> None:

        parser.add_argument('--users', type = int, help = 'Amount of users you want to create.')
        parser.add_argument('--auctions', type = int, help = 'Amount of auctions you want to create.')
        parser.add_argument('--bids', type = int, help = '''Amount of bids you want to create distributed across ALL auctions.\nIf no auctions a default of 100 auction entries will be created before bid generation''')
    
    def _generate_users(self, amount) -> None:

        UserFactory.create_batch(amount)
    
    def _generate_auctions(self, amount) -> None:

        if(len(User.objects.all()) == 0):

            warnings.warn('User table empty! Generating 100 users...')
            UserFactory.create_batch(DEFAULT)

        AuctionFactory.create_batch(amount)
    
    def _generate_bids(self, amount) -> None:

        if(len(Auction.objects.all()) == 0):

            warnings.warn('Auction table empty! Generating 100 auctions...')
            AuctionFactory.create_batch(DEFAULT)

        BidFactory.create_batch(amount)
    
    @Halo(text='Generating...', spinner='dots', color='blue', text_color='blue')
    def handle(self, *args, **options):

        self._generate_users(options.get('users') or 0)
        self._generate_auctions(options.get('auctions') or 0)
        self._generate_bids(options.get('bids') or 0)