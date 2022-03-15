<template>
    <ul class="menu-date" v-for="menu in listOfMenus" :key="menu.id">
    <div>
    <router-link :to="{ name: 'Menu', params: { date: menu.date } }">
      <li>{{ menu.date }}</li>
    </router-link>
    </div>
  </ul>
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
* {
  margin: 0;
  padding: 0;
  font-size: 16px;
  box-sizing: border-box;
}
.menu-date {
  list-style: none;
  text-align: center;
  margin: 1em;
}

</style>