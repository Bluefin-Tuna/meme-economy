<template>
  <v-container fluid>
    <h1 class="text-center ma-4 text-decoration-underline">Owned Memes</h1>
    <v-container fluid class="cards-grid">
      <v-col v-for="index in 10" :key="index">
        <OwnedMemeCard />
      </v-col>
    </v-container>
    <h1 class="text-center ma-4 text-decoration-underline">Bought Memes</h1>
    <v-container fluid class="cards-grid">
      <v-col v-for="index in 10" :key="index">
        <BoughtMemeCard />
      </v-col>
    </v-container>
  </v-container>
</template>

<script>
export default {
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
