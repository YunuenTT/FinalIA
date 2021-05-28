<template>
  <div class="mt-3">
    <b-carousel id="my-carousel"
                style="text-shadow: 1px 1px 2px #333;"
                controls
                indicators
                background="#CCCCCC"
                :interval="4000"
                v-model="slide"
                img-height="250px"
                @sliding-start="onSlideStart"
                @sliding-end="onSlideEnd"
    >
      <b-carousel-slide img-src="https://purewows3.imgix.net/images/articles/2017_12/best-books-2017-header.jpg?auto=format,compress&cs=strip" img-width="780px" img-height="250px" caption="Inmenso">
        <p>
          Gran colección de libros tanto clásicos como recientes.
        </p>
      </b-carousel-slide>
      <b-carousel-slide img-src="https://purewows3.imgix.net/images/articles/2018_12/2018-books-header.jpg?auto=format,compress&cs=strip" img-width="780px" img-height="250px" caption="Más rápido">
        <p>
          Entrega más rápida de su libro favorito.
        </p>
      </b-carousel-slide>
      <b-carousel-slide img-src="https://coverfiles.alphacoders.com/395/39523.jpg" img-width="780px" img-height="250px" caption="Estética">
        <p>
          Impresión de la mejor calidad, ¡cada página nos importa!
        </p>
      </b-carousel-slide>
    </b-carousel>
  </div>
</template>

<script>
export default {
  data () {
    return {
      slide: 0,
      sliding: null
    }
  },
  methods: {
    onSlideStart (slide) {
      this.sliding = true
    },
    onSlideEnd (slide) {
      this.sliding = false
    }
  }
}
</script>

<style scoped>
  #my-carousel {
    margin-top: auto;
  }
</style>
