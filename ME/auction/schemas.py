import graphene
from graphene_django import DjangoObjectType, DjangoListField
from auction.models import Auction, Meme, Bid

class AuctionType(DjangoObjectType):

    class Meta:

        model = Auction
        fields = "__all__"


class MemeType(DjangoObjectType):

    class Meta:

        model = Meme
        fields = "__all__"


class BidType(DjangoObjectType):

    class Meta:

        model = Bid
        fields = "__all__"