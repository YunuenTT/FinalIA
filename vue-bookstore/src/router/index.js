import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import AllProducts from '@/components/AllProducts'
import Categories from '@/components/Categories'
import ProductDetails from '@/components/ProductDetails'
import Checkout from '@/components/checkout'
import Sesion from '@/components/Sesion'
import Registro from '@/components/Registro'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
      props: true
    },
    {
      path: '/todos-productos',
      name: 'AllProducts',
      component: AllProducts,
      props: true
    },
    {
      path: '/categorias/:type',
      name: 'Categories',
      component: Categories,
      props: true
    },
    {
      path: '/products/:productID',
      name: 'ProductDetails',
      component: ProductDetails
    },
    {
      path: '/checkout',
      name: 'Checkout',
      component: Checkout
    },
    {
      path: '/iniciar-sesion',
      name: 'Sesion',
      component: Sesion
    },
    {
      path: '/registro',
      name: 'Registro',
      component: Registro
    }
  ]
})
