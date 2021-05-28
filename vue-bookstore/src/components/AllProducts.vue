<template>
  <div class="container">
    <div class="row mt-3">
      <div v-for="(item) in collections" :key="item.Title + item.Price" class="col-sm-4">
        <item-card :item="item" :updateCart="updateCart"></item-card>
      </div>
    </div>
  </div>
</template>

<script>
import ItemCard from '@/components/common_components/ItemCard'

export default {
  name: 'AllProducts',
  props: ['dataset', 'updateCart'],
  data () {
    return {
      collections: this.dataset
    }
  },
  components: {
    'item-card': ItemCard
  }
}
</script>

<style scoped>

</style>
