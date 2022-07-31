<template>
  <v-card class="card">
    <v-card-title>title</v-card-title>
    <v-card-subtitle>By: Justin S</v-card-subtitle>
    <v-card-subtitle class="card-date">Created: 8/20/2022</v-card-subtitle>
    <v-img
      src=""
      class="white--text"
      gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
      height="200px"
    >
    </v-img>
    <v-card-text>This is a meme</v-card-text>
    <v-card-text>End: 4:22 PM - 8/22/2023</v-card-text>
    <v-card-text>Highest Bidder: John Cena - $200</v-card-text>
    <v-card-text>Price: $450</v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn text> Place Bid </v-btn>
      <v-btn text>Buy</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: {},
  data() {
    return {}
  },
}
</script>

<style lang="scss" scoped>
.card {
  &:hover {
    transform: scale(1.05);
    transition: 0.3s;
  }

  &-date {
    position: absolute;
    top: 5px;
    right: 7px;
    padding: 0;
  }
}
</style>
