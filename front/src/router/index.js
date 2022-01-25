import { createRouter, createWebHistory } from 'vue-router'
import menu_dia from '../pages/menu_dia/menu_dia.vue'
import home from '../pages/home/HomePage.vue'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: home
  },
  {
    path :'/menu_dia',
    name : 'Menu_Dia',
    component: menu_dia
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
