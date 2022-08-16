export default {
  async fetchUser({ commit }, userId) {
    var query = `query GetUser($id: Int) {
      user(id: $id) {
        lastLogin
        isSuperuser
        firstName
        lastName
        isStaff
        isActive
        id
        email
        username
        dateJoined
        dateUpdated
        profile
      }
    }`
    try {
      const res = await fetch('http://127.0.0.1:8000/graphql', {
        method: 'POST',
        body: JSON.stringify({
          query,
          variables: {
            userId,
          },
        }),
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
      })
      if (res.status === 200) {
        const data = await res.json()
        commit('SETUSER', data.user)
      }
    } catch (err) {
      // set state error
    }
    // trigger setUser mutation
  },
  async createUser({ commit }, newUser) {
    var mutation = `mutation CreateUser($newUser: CreateUserInput!) {
      createUser(information: $newUser) {
      }
    }`
    try {
      const res = await fetch('/graphql', {
        method: 'POST',
        body: JSON.stringify({
          mutation,
          variables: {
            newUser,
          },
        }),
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
      })
      if (res.status === 200) {
        commit('SETUSER', newUser)
      }
    } catch (err) {
      // set state error
    }
  },
  async updateUser({ commit }, updatedUser) {
    var mutation = `mutation UpdateUser($updatedUser: UpdateUserInput!) {
      updateUser(information: $updatedUser) {
      }
    }`
    try {
      const res = await fetch('/graphql', {
        method: 'POST',
        body: JSON.stringify({
          mutation,
          variables: {
            updatedUser,
          },
        }),
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
      })
      if (res.status === 200) {
        commit('SETUSER', updatedUser)
      }
    } catch (err) {
      // set state error
    }
  },
  async deleteUser({ commit }) {
    var mutation = `mutation DeleteUser($user: DeleteUserInput!) {
      deleteUser(information: $user) {
      }
    }`
    try {
      const res = await fetch('/graphql', {
        method: 'POST',
        body: JSON.stringify({
          mutation,
          variables: {
            updatedUser,
          },
        }),
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
      })
      if (res.status === 200) {
        commit('DELETEUSER')
      }
    } catch (err) {
      // set state error
    }
  },
}
