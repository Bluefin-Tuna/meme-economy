import graphene
from auction.GQL.queries.auction import AuctionQuery
from auction.GQL.queries.bid import BidQuery
from auction.GQL.queries.meme import MemeQuery

class AuctionQueries(AuctionQuery, BidQuery, MemeQuery):
    pass