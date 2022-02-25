<template>
  <div class="home">
    <img alt="menu logo" src="@/assets/img/imagen_de_bienbenida_menu.png" />
    <h1>Bienvenido</h1>
  </div>

  <select v-model="selectedRestaurant">
    <option :value="null" disabled>Selecciona un restaurante</option>
    <option v-for="restaurant in restaurants" :value="restaurant" :key="restaurant.id_restaurant">{{restaurant.name}}</option>
    </select>
<button @click="onButtonClicked()">Ver los menus</button> 
</template>

<script>

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
      this.restaurants=[{
        id_restaurant:"restaurant-1",
        name:"rest x"
        },
        {
        id_restaurant:"restaurant-2",
        name:"rest y"
        },
        ]
    },
  onButtonClicked(){
      const settings = {
        method: "GET",
        headers: {
          Authorization: localStorage.id_restaurant,
        },
      }
      localStorage.id_restaurant=this.selectedRestaurant.id_restaurant
      localStorage.name=this.selectedRestaurant.name
      console.log('name',localStorage.name)
      console.log('id',localStorage.id_restaurant)
      console.log('settings',settings)
      this.$router.push('/menus',settings)
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
