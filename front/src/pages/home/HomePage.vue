<template>
  <div class="home">
    <img alt="menu logo" src="@/assets/img/imagen_de_bienbenida_menu.png" />
    <h1>Bienvenido</h1>
  </div>

  
    <div class="login-wrapper">
      <label for="user-name">Usuario</label>
      <input type="text" id="user-name" v-model="restaurants.id_restaurant">
      <br />
      <label for="password">Contraseña</label>
      <input type="password" id="password" v-model="restaurants.password" @keyup.enter="onButtonClicked">
      
      <br/>
    </div>
    
<button @click="onButtonClicked()" @keyup.enter="onButtonClicked">Ver los menus</button> 
</template>

<script>

import { login } from "@/services/auth.js";
import { useStorage } from "@vueuse/core";


export default {
  name: 'Home',
  data(){
    return{
      restaurants:[],
      selectedRestaurant:null,
      auth: useStorage("auth", {}),
      
    }
  },
  
  methods:{
    
    async onButtonClicked(){
      const response = await login(this.restaurants.id_restaurant, this.restaurants.password);
      const loginStatus = response.status;
      console.log("response", response);

      if (loginStatus === 401) {
        alert("unauthorized");
      } else {
        const auth = await response.json();
        console.log("auth", auth);

        this.auth = auth;

      this.$router.push('/menus')
      }
    }
  },
}
</script>

<style scoped>
h1 {
  font-style: italic;
}
img{
  width: 30vw;

}
.login-wrapper{
  display: flex;
  flex-direction: column;
  max-width: 300px;
  margin: 3em auto 0;
}

</style>
