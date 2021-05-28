<template>
    <div class="container">
      <div class="row mt-4">
        <div class="col-sm-4">
          <img :src="product.Cover"/>
        </div>
        <div class="col-sm-8">
          <h3>{{product.Title}}</h3>
          <hr>
          <p>Autor: {{product.Author}}</p>
          <p>Editora: {{product.Publisher}}</p>
          <p>Genero: {{product.Genre}}</p>
          <hr>
          <p>Clasificación Promedio: 8/10 </p>
          <p>Precio: ${{product.Price}}</p>
          <hr>
          <p>{{product.Description}}</p>
          <hr>
          <b-btn variant="success" @click.prevent="updateCart(product)">Añadir al carrito</b-btn>
          <hr>
        </div>
      </div>
      <recc :item="product.ISBN" :updateCart="updateCart"></recc>
    </div>
</template>

<script>
import Recc from './Recc'

import Data from '../assets/book_list.json'
export default {
  name: 'ProductDetails',
  components: {
    'recc': Recc
  },
  props: ['updateCart'],
  data () {
    return {
      collection: Data.collection,
      product: []
    }
  },
  created () {
    this.product = this.collection.find((item) => {
      return item.Title === this.$route.params.productID
    })
  }
}
</script>

<style scoped>

</style>
