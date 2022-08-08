<template>
  <v-container fluid>
    <v-container fluid class="cards-grid">
      <v-col v-for="auction in auctionList" :key="auction.id">
        <AuctionCard :auction="auction" />
      </v-col>
    </v-container>
    <AddAuctionButton />
  </v-container>
</template>

<script>
import MemeCard from './MemeCard.vue'
export default {
  components: { MemeCard },
  setup(props) {
    const title = 'Auction Page'
    onBeforeMount(() => {
      this.$store.dispatch('auction/fetchAuctionList')
    })
    return {
      title,
      ...mapState({ auctionList: 'auction/list' }),
    }
  },
}
</script>

<style scoped>
.cards-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  row-gap: 1.2em;
}
</style>
