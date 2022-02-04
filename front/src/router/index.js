import { createRouter, createWebHistory } from 'vue-router'
import menu from '../pages/menu/MenuPage.vue'
import home from '../pages/home/HomePage.vue'
import menus from '../pages/menus/MenusPage.vue'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: home
  },
  {
    path :'/by-date/:date',
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
