<template>
  <v-form
    class="create-meme-form"
    @submit.prevent="submit"
    ref="form"
    v-model="valid"
    lazy-validation
  >
    <v-text-field
      v-model="name"
      :counter="15"
      :rules="nameRules"
      label="Name"
      filled
      clearable
      required
    />
    <v-text-field
      v-model="caption"
      :rules="captionRules"
      :counter="30"
      label="Caption"
      filled
      clearable
      required
    />
    <v-file-input
      v-model="memeFile"
      :rules="memeFileRules"
      label="Upload Meme"
      prepend-icon="mdi-paperclip"
      placeholder="Meme"
    />
    <div class="create-meme-form-buttons">
      <v-btn color="error" class="mr-4" @click="reset"> Reset Form </v-btn>
      <v-btn
        type="submit"
        :disabled="!valid"
        class="mr-4"
        color="success"
        @click="submit"
      >
        Submit
      </v-btn>
    </div>
  </v-form>
</template>

<script scoped>
export default {
  data() {
    return {
      valid: true,
      name: '',
      nameRules: [
        (v) => !!v || 'Name is required',
        (v) => (v && v.length <= 15) || 'Name must be less than 10 characters',
      ],
      caption: '',
      captionRules: [
        (v) => !!v || 'Caption is required',
        (v) =>
          (v && v.length <= 30) || 'Caption must be less than 30 characters',
      ],
      memeFile: [],
      memeFileRules: [
        (v) => !v || v.size < 2000000 || 'Meme size should be less than 2 MB!',
      ],
    }
  },
  methods: {
    submit() {
      this.$refs.form.validate()
    },
    reset() {
      this.$refs.form.reset()
    },
  },
}
</script>

<style lang="scss" scoped>
.create-meme {
  &-form {
    padding: 40px;
  }
  &-form-buttons {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    margin-top: 20px;
  }
}
</style>
