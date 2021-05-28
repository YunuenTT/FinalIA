<template>
  <div id="app">
    <nav-bar :categories="categories" :purchase="totalPrice"></nav-bar>
    <router-view :dataset="collections" :updateCart="addToCart" :cart="cart" :purchase="totalPrice" />
    <about :categories="categories"></about>
  </div>
</template>

<script>
import Navbar from './components/common_components/Navbar'
import AboutUs from './components/common_components/AboutUs'
import Data from './assets/book_list.json'

export default {
  name: 'App',
  data () {
    return {
      'collections': Data.collection,
      'categories': [],
      'cart': []
    }
  },
  computed: {
    totalPrice () {
      let total = 0
      for (let i = 0; i < this.cart.length; i++) {
        total += Number(this.cart[i].Price)
      }
      return total
    }
  },
  components: {
    'nav-bar': Navbar,
    'about': AboutUs
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
    addToCart: function (item) {
      this.cart.push(item)
    }
  }
}
</script>

<style>

</style>
