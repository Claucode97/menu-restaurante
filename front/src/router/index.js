import { createRouter, createWebHistory } from 'vue-router'
import menu from '../pages/menu/menu.vue'
import home from '../pages/home/HomePage.vue'
import menus from '../pages/menus/menus.vue'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: home
  },
  {
    path :'/menu',
    name : 'Menu',
    component: menu
  },
  {
    path :'/menus',
    name : 'Menus',
    component: menus
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
