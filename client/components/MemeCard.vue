<template>
  <v-card class="card">
    <v-card-title>{{ name }}</v-card-title>
    <v-card-subtitle>By: {{ owner }}</v-card-subtitle>
    <v-card-subtitle class="card-date"
      >Created: {{ createdAt }}</v-card-subtitle
    >
    <v-img
      :src="file"
      class="white--text"
      gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
      height="200px"
    >
    </v-img>
    <v-card-text>{{ description }}}}</v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-icon>mdi-eye</v-icon
      ><v-card-text class="card-likes-views-text">{{ views }}</v-card-text>
      <v-btn icon>
        <v-icon>mdi-thumb-up</v-icon>
      </v-btn>
      <v-card-text class="card-likes-views-text">{{ likes }}</v-card-text>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: ['meme'],
  setup(props) {
    const { owner, name, description, likes, views, file, createdAt } = toRefs(
      props.meme
    )
    return {
      owner,
      name,
      description,
      likes,
      views,
      file,
      createdAt,
    }
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
    top: 5px;
    right: 7px;
    padding: 0;
  }

  &-likes-views-text {
    padding: 5px;
    width: fit-content;
  }
}
</style>
