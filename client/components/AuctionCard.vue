<template>
  <v-card class="card">
    <v-card-title>{{ title }}</v-card-title>
    <v-card-subtitle>By: {{ author }}</v-card-subtitle>
    <v-card-subtitle class="card-date"
      >Created: {{ memes.createdAt }}</v-card-subtitle
    >
    <v-img
      src=""
      class="white--text"
      gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
      height="200px"
    >
    </v-img>
    <v-card-text>{{ memes.description }}</v-card-text>
    <v-card-text>End: {{ endsAt }}</v-card-text>
    <v-card-text>Limit: {{ limit }}</v-card-text>
    <v-card-text>Price: {{ initialPrice }}</v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn text> Place Bid </v-btn>
      <v-btn text>Buy</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: ['auction'],
  setup(props) {
    const { author, initialPrice, limit, startsAt, endsAt, memes, bids } =
      toRefs(props)
    return {
      author,
      initialPrice,
      limit,
      startsAt,
      endsAt,
      memes,
      bids,
    }
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
