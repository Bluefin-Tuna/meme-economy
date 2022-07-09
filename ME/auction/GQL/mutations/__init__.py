import graphene

from auction.GQL.mutations.auction import AuctionMutation
from auction.GQL.mutations.bid import BidMutation
from auction.GQL.mutations.meme import MemeMutation

class AuctionMutations(AuctionMutation, MemeMutation, BidMutation, graphene.ObjectType):
    pass
