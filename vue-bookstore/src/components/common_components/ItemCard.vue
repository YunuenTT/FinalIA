<template>
  <div class="container">
    <b-card :title="item.Title"
            :img-src="item.Cover"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2 text-center">
      <p class="card-text">
        Autor: {{item.Author}}
      </p>
      <hr>
      <p>Precio: ${{item.Price}}</p>
      <hr>
      <b-button variant="success" @click.prevent="updateCart(item)"><v-icon name="cart-plus" /> </b-button>
      <b-button variant="success" @click="details(item.Title)"><v-icon name="list" /> </b-button>
    </b-card>
  </div>
</template>

<script>
export default {
  name: 'ItemCard',
  props: ['item', 'updateCart'],
  methods: {
    details (title) {
      this.$router.push('/products/' + title)
    }
  }
}
</script>

<style scoped>

</style>
