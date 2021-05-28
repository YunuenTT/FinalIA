<template>
  <div>
    <b-card :sub-title="results.Title"
            :img-src="results.Cover"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 10rem;"
            class="mb-2 text-center">
      <hr>
      <p>Precio: ${{results.Price}}</p>
      <hr>
      <b-button variant="success" @click.prevent="updateCart(results)"><v-icon name="cart-plus" /> </b-button>
      <b-button variant="success" @click="details(results.Title)"><v-icon name="list" /> </b-button>
    </b-card>
  </div>
</template>

<script>
import Data from '@/assets/book_list.json'

export default {
  name: 'ReccCard',
  props: ['item', 'updateCart'],
  data () {
    return {
      slide: 0,
      sliding: null,
      mensaje: 'libro recomendados',
      collections: Data.collection,
      product: [],
      results: {}
    }
  },
  methods: {
    details (title) {
      this.$router.push('/products/' + title)
    },
    find (item) {
      var searchField = 'Title'
      for (var j = 0; j < this.collections.length; j++) {
        if (this.collections[j][searchField] === item) {
          console.log(this.collections[j])
          this.results = this.collections[j]
        }
      }
      console.log(this.results)
    }
  },
  created () {
    this.find(this.item)
  }
}
</script>

<style scoped>

</style>
