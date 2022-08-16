export default {
  SETMEMELIST(state, memeList) {
    state.list = memeList
  },
  ADDMEME(state, newMeme) {
    state.list.push(newMeme)
  },
  UPDATEMEME(state, updatedMeme) {
    for (const meme of state.list) {
      if (meme === updatedMeme) {
        meme = updatedMeme
        break
      }
    }
  },
  DELETEMEME(state, meme) {
    state.list.filter((currMeme) => currMeme !== meme)
  },
}
