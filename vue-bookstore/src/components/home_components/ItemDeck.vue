<template>
  <b-card no-body class="mt-3">
    <b-card-header header-text-variant="white" header-bg-variant="success">{{ product_category }} <b-btn class="float-right btn-success btn-sm"  v-on:click="seeAll(product_category)" >Ver todo</b-btn></b-card-header>
    <b-card-body>
      <b-card-group deck class="row">
          <div class="col-sm-4" v-for="product in products" :key="product.Title">
            <item-card :item="product" :updateCart="updateCart"></item-card>
          </div>
      </b-card-group>
    </b-card-body>
  </b-card>
</template>

<script>
import ItemCard from '@/components/common_components/ItemCard'

export default {
  name: 'ItemDeck',
  components: {
    'item-card': ItemCard
  },
  props: ['products', 'product_category', 'updateCart'],
  methods: {
    seeAll (category) {
      this.$router.push('/categories/' + category)
    }
  }
}
</script>

<style scoped>

</style>
