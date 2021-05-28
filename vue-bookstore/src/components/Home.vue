<template>
  <div class="container">
    <div class="md-2">
      <carousel></carousel>
    </div>
    <div v-for="(category) in categories" :key="category">
      <item-deck  :products="getDisplayProducts(category)" :product_category="category" :updateCart="updateCart"></item-deck>
    </div>
  </div>
</template>

<script>
import Carousel from './home_components/Carousel'
import ItemCard from './common_components/ItemCard'
import ItemDeck from './home_components/ItemDeck'

export default {
  name: 'Home',
  props: ['dataset', 'updateCart'],
  data () {
    return {
      'collections': this.dataset,
      'categories': []
    }
  },
  components: {
    'carousel': Carousel,
    'item-card': ItemCard,
    'item-deck': ItemDeck
  },
  created () {
    this.categories = this.getCategories()
  },
  methods: {
    getCategories: function () {
      let listedCategories = []
      this.collections.filter((item) => {
        if (!listedCategories.includes(item.Genre)) {
          listedCategories.push(item.Genre)
        }
      })
      return listedCategories
    },
    getDisplayProducts (category) {
      let productList = this.collections.filter((element) => {
        if (element.Genre === category) {
          return element
        }
      })
      return productList.slice(0, 3)
    }
  }
}
</script>

<style scoped>

</style>
