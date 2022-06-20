<template>
  <v-container fluid>
    <v-btn
      class="add-auction-btn mx-2"
      fab
      dark
      large
      @click="showFormDialog = true"
    >
      <v-icon dark> mdi-plus </v-icon>
    </v-btn>
    <AddAuctionDialog v-if="showFormDialog" />
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      showFormDialog: false,
    }
  },
}
</script>

<style lang="scss" scoped>
.add-auction-btn {
  position: fixed;
  bottom: 20px;
  right: 40px;
}
</style>
