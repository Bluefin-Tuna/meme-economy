import graphene
from ME.auction.GQL.inputs.auction import CreateAuctionInput, UpdateAuctionInput, DeleteAuctionInput
from ME.auction.models import Auction
from ME.auction.GQL.types import AuctionType