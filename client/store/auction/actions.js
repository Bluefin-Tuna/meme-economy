export default {
  async fetchAuctionList({ commit }) {
    var query = `query GetAllAuctions() {
      getAllAuctions() {
        id
        author
        initialPrice
        limit
        startsAt
        endsAt
        memes
        bids
      }
    }`
    try {
      const res = await fetch('http://127.0.0.1:8000/graphql', {
        method: 'POST',
        body: JSON.stringify({
          query,
        }),
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
      })
      if (res.status === 200) {
        const data = await res.json()
        console.log(data)
        commit('SETAUCTIONLIST', data.auctionList)
      }
    } catch (err) {
      // set state error
    }
  },
  async createAuction({ commit }, newAuction) {
    var mutation = `mutation CreateAuction($newAuction: CreateAuctionInput!) {
      createAuction(information: $newAuction) {      
      }
    }`
    try {
      const res = await fetch('/graphql', {
        method: 'POST',
        body: JSON.stringify({
          mutation,
          variables: {
            newAuction,
          },
        }),
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
      })
      if (res.status === 200) {
        commit('ADDAUCTION', newAuction)
      }
    } catch (err) {
      // set state error
    }
  },
  async deleteAuction({ commit }, auction) {
    var mutation = `mutation DeleteAuction($auction: DeleteAuctionInput!) {
      deleteAuction(information: $auction) {      
      }
    }`
    try {
      const res = await fetch('/graphql', {
        method: 'POST',
        body: JSON.stringify({
          mutation,
          variables: {
            auction,
          },
        }),
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
      })
      if (res.status === 200) {
        commit('DELETEAUCTION', auction)
      }
    } catch (err) {
      // set state error
    }
  },
}
