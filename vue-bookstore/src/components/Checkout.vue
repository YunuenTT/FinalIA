<template>
  <div class="container">
    <div class="row mt-2">
      <div class="col-sm-8">
        <b-card header="Mi carrito">
          <p v-if="!purchase || purchase.length === 0 ">¡No hay libros en el carrito!</p>
          <div class="row mt-2 md-1" v-for="item in cartItems" :key="item.Item.Title">
            <div class="col-sm-3">
              <b-img fluid :src="item.Item.Cover" class="p-2"></b-img>
            </div>
            <div class="col-sm-9">
              <div>
                <h5>{{item.Item.Title}}</h5>
                <p>Autor: {{item.Item.Author}}</p>
                <p>Monto: {{item.amount}}</p>
                <p>Precio: {{item.Item.Price}}</p>
              </div>
            </div>
          </div>
          <hr>
        </b-card>
      </div>
      <div class="col-sm-4 text-center">
        <b-card header="Detalles de precios">
          <p>Precio total:</p>
          <h3>${{purchase}}</h3>
          <hr>
          <b-btn href="#" variant="outline-primary">Realizar pedido</b-btn>
        </b-card>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Checkout',
  props: ['cart', 'purchase'],
  computed: {
    cartItems () {
      return this.computeCart()
    }
  },
  methods: {
    computeCart: function () {
      let newCart = []
      this.cart.forEach((item) => {
        let index = newCart.findIndex((element) => {
          return element.Item === item
        })
        if (index >= 0) {
          newCart[index].amount += 1
        } else {
          newCart.push({
            Item: item,
            amount: 1
          })
        }
      })
      return newCart
    }
  }
}
</script>

<style scoped>

</style>
