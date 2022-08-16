export default {
  async fetchMemeList({ commit }) {
    console.log('hi')
    var query = `{ allMemes { id } }`
    try {
      const res = await fetch(`http://127.0.0.1:8000/graphql?query=${query}`, {
        method: 'GET',

        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
      })
      if (res.status === 200) {
        const data = await res.json()
        console.log(data)
        commit('SETMEMELIST', data.auctionList)
      }
    } catch (err) {
      console.log(err)
    }
  },
  async createMeme({ commit }, newMeme) {
    var mutation = `mutation CreateMeme($newMeme: CreateMemeInput!) {
      createMeme(information: $newMeme) {
      }
    }`
    try {
      const res = await fetch('/graphql', {
        method: 'POST',
        body: JSON.stringify({
          mutation,
          variables: {
            newMeme,
          },
        }),
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
      })
      if (res.status === 200) {
        commit('ADDMEME', newMeme)
      }
    } catch (err) {
      // set state error
    }
  },
  async updateMeme({ commit }, updatedMeme) {
    var mutation = `mutation UpdateMeme($updatedMeme: UpdateMemeInput!) {
      updateMeme(information: $updatedMeme) {}
    }`
    try {
      const res = await fetch('/graphql', {
        method: 'POST',
        body: JSON.stringify({
          mutation,
          variables: {
            updatedMeme,
          },
        }),
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
      })
      if (res.status === 200) {
        commit('UPDATEMEME', updatedMeme)
      }
    } catch (err) {
      // set state error
    }
  },
  async deleteMeme({ commit }, meme) {
    var mutation = `mutation DeleteMeme($meme: DeleteMemeInput!) {
      deleteMeme(information: $meme) {}
    }`
    try {
      const res = await fetch('/graphql', {
        method: 'POST',
        body: JSON.stringify({
          mutation,
          variables: {
            meme,
          },
        }),
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
      })
      if (res.status === 200) {
        commit('DELETEMEME', meme)
      }
    } catch (err) {
      // set state error
    }
  },
}
