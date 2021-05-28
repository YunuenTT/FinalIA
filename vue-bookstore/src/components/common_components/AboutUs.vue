<template>
  <b-navbar toggleable="md" type="dark" variant="success">
    <div class="container">
      <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
      <b-navbar-brand href="#" @click.prevent="route_to('/')" class="navbar-brand mx-auto"><v-icon name="book-open"/> Bookish</b-navbar-brand>
    </div>
  </b-navbar>
</template>

<script>
export default {
  name: 'AvoutUs',
  props: ['categories'],
  methods: {
    route_to (path) {
      this.$router.push(path)
    }
  }
}
</script>

<style scoped>

</style>
