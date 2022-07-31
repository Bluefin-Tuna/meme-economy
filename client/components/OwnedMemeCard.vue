<template>
  <v-card class="card">
    <v-card-title>title</v-card-title>
    <v-card-subtitle class="card-date">Created: 8/20/2022</v-card-subtitle>
    <v-img
      src=""
      class="white--text"
      gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
      height="200px"
    >
    </v-img>
    <v-card-text>This is a meme</v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-icon>mdi-eye</v-icon
      ><v-card-text class="card-likes-views-text">24</v-card-text>
      <v-icon color="light-blue lighten-2">mdi-thumb-up</v-icon>
      <v-card-text class="card-likes-views-text">50</v-card-text>
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
  transition: 0.3s;

  &:hover {
    transform: scale(1.05);
  }

  &-date {
    position: absolute;
    top: 20px;
    right: 7px;
    padding: 0;
  }

  &-likes-views-text {
    padding: 5px;
    width: fit-content;
    margin: 5px;
  }
}
</style>
