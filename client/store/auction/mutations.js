export default {
  SETAUCTIONLIST(state, auctionList) {
    state.list = auctionList
  },
  ADDAUCTION(state, newAuction) {
    state.list.push(newAuction)
  },
  DELETEAUCTION(state, auction) {
    state.filter((currAuction) => currAuction !== auction)
  },
}
