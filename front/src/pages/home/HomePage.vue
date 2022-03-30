<template>
  <div class="home">
    <img alt="menu logo" src="@/assets/img/imagen_de_bienbenida_menu.png" />
    <h1>Bienvenido</h1>
  </div>

  
    <label for="user-name">Usuario</label>
    <input type="text" id="user-name" v-model="restaurants.name">
    <br />
    <label for="password">Contraseña</label>
    <input type="password" id="password" v-model="restaurants.password">
    <br/>
    
<button @click="onButtonClicked()">Ver los menus</button> 
</template>

<script>
import {getRestaurants} from "@/services/api.js"

export default {
  name: 'Home',
  data(){
    return{
      restaurants:[],
      selectedRestaurant:null,
    }
  },
  mounted(){
    this.loadData()
  },
  methods:{
    async loadData(){
      
      this.restaurants = await getRestaurants()
    },
  onButtonClicked(){
      localStorage.id_restaurant=this.selectedRestaurant.id_restaurant
      localStorage.name=this.selectedRestaurant.name
      this.$router.push('/menus')
    }
  }
}
</script>

<style scoped>
h1 {
  font-style: italic;
}
img{
  width: 30vw;

}
</style>
