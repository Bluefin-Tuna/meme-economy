<template>
  <v-container fluid>
    <v-container fluid class="cards-grid">
      <v-col v-for="index in 10" :key="index">
        <AuctionCard />
      </v-col>
    </v-container>
    <AddAuctionButton />
  </v-container>
</template>

<script>
import MemeCard from './MemeCard.vue'
export default {
  components: { MemeCard },
  data() {
    return {}
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
