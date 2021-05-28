<template lang="html">
  <div class="mt-3">
    <div class="col-sm-8">
      <h3>Si te gusta este libro te recomendamos...</h3>
      <hr>
    </div>
    <b-card no-body class="mt-3">
        <b-card-header header-text-variant="white" header-bg-variant="success"></b-card-header>
        <b-card-body>
            <b-card-group deck class="col d-flex justify-content-center">
                <div  v-for="book in mensaje" :key="book">
                    <recc-card :item="book" :updateCart="updateCart"></recc-card>
                </div>
            </b-card-group>
        </b-card-body>
    </b-card>
  </div>
</template>

<script>
import axios from 'axios'
import Data from '../assets/book_list.json'
import ReccCard from '@/components/common_components/reccCard'

export default {
  name: 'Recc',
  components: {
    'recc-card': ReccCard
  },
  props: ['item', 'updateCart'],
  data () {
    return {
      slide: 0,
      sliding: null,
      mensaje: 'libro recomendados',
      collections: Data.collection,
      product: []
    }
  },
  methods: {
    onSlideStart (slide) {
      this.sliding = true
    },
    onSlideEnd (slide) {
      this.sliding = false
    },
    findBook (recc) {
      var results = []
      var searchField = 'Title'
      for (var i = 0; i < recc.length; i++) {
        console.log(this.recc[i])
        for (var j = 0; j < this.collections.length; j++) {
          if (this.collections[j][searchField] === this.recc[i]) {
            console.log('gggggg')
            results.push(this.collections[i])
          }
        }
      }
    },
    getMensaje () {
      const path = 'http://localhost:5000/api/recc/' + this.item
      axios.get(path).then((respuesta) => {
        this.mensaje = respuesta.data
      })
        .catch((error) => {
          console.error(error)
        })
    }
  },
  created () {
    this.getMensaje()
  }
}
</script>

<style scoped>
  #my-carousel {
    margin-top: auto;
  }
</style>
