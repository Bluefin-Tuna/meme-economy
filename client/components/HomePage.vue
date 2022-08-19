<template>
  <v-container fluid>
    <h1 class="text-center mb-5">Memes</h1>
    <v-toolbar dark color="teal">
      <v-autocomplete
        v-model="select"
        :loading="loading"
        :items="items"
        :search-input.sync="search"
        cache-items
        class="mx-4"
        flat
        hide-no-data
        hide-details
        label="Search Meme"
        solo-inverted
      />
    </v-toolbar>
    <v-container fluid class="cards-grid">
      <v-col v-for="meme in memeList" :key="meme.id">
        <h1>{{ meme }}</h1>
        <MemeCard :meme="meme" />
      </v-col>
    </v-container>
  </v-container>
</template>

<script>
import { computed } from '@nuxtjs/composition-api'
import { mapState } from 'vuex'

export default {
  setup(props) {
    const memeList = computed(() => {
      return this.$store.state.memes.list
    })
    console.log(memeList)
    let loading = false
    let items = []
    let search = null
    let select = null

    const querySelections = (v) => {
      loading = true
      // Simulated ajax query
      setTimeout(() => {
        items = memeList.filter((e) => {
          return (e || '').toLowerCase().indexOf((v || '').toLowerCase()) > -1
        })
        loading = false
      }, 500)
    }
    return {
      ...mapState({ memeList: 'memes/list' }),
      querySelections,
      loading,
      items,
      search,
      select,
    }
  },
  mounted() {
    console.log('hello')
    this.$store.dispatch('memes/fetchMemeList')
    console.log(this.$store.state.memes.list)
  },
  /*watch: {
    search(val) {
      val && val !== this.select && this.querySelections(val)
    },
  },*/
}
</script>

<style scoped>
.cards-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  row-gap: 1.2em;
}
</style>
