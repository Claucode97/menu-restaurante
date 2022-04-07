<template>
    <div class="menus-list">
      <h3>Menus disponibles</h3>
      <ul class="available-menus-list">
        <li class="menu-date" v-for="menu in listOfMenus" :key="menu.id">
          <router-link :to="{ name: 'Menu', params: { date: menu.date } }">
        {{ menu.date }}
        </router-link>
        </li>
      
      </ul>
    </div>
</template>

<script>
import {getListOfMenus} from "@/services/api.js"
export default {
    name : "ListOfMenus",
    data() {
    return {
      listOfMenus : [],
    };
  },
 mounted(){
     this.loadData();
 },
 methods:{
    async loadData(){
         this.listOfMenus = await getListOfMenus()
     }
 }
}
</script>

<style scoped>

.menus-list {
  color:#a31d1e;
}
.menu-date {
  list-style: none;
  text-align: center;
  margin: 1em;
  
}
.menu-date a{
  color:#a31d1e;
}
.menu-date a:hover{
  font-weight:bold;
}

</style>