export default {
  SETUSER(state, user) {
    state.user = user
  },
  DELETEUSER(state) {
    state.user = null
  },
}
