<template>
  <v-tabs fixed-tabs class="nav">
    <v-tab to="/"> Home </v-tab>
    <v-tab to="/auction"> Auction </v-tab>
    <v-tab to="/create-meme"> Create-Meme </v-tab>
    <v-tab to="profile"> Profile </v-tab>
  </v-tabs>
</template>

<script>
export default {
  name: 'Navbar',
}
</script>

<style scoped>
.nav {
  flex: none;
}
</style>
