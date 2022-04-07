<template>
<div class="menu-list-page">
  <HeaderMenu/>
  <h2>{{loggedRestaurant}}</h2>
    <router-link :to="{ name: 'Menu', params: { date: getToday } }">
      <button class="menu-day-btn btn">Menú del día</button>
    </router-link>
  
    <Calendar />
  
    <ListOfMenus />
</div>
</template>

<script>
import HeaderMenu from '@/components/HeaderMenu.vue';
import ListOfMenus from './ListOfMenu.vue'
import Calendar from './Calendar.vue'
import {getRestaurantName} from "@/services/localStorage.js";
export default {
  components: {Calendar,ListOfMenus, HeaderMenu},
  data() {
    return {
      loggedRestaurant: getRestaurantName(),
      
    };
  },

  computed: {
    getToday() {
      let current = new Date();
      let year = current.getFullYear();
      let month = current.getMonth() + 1;
      let day = current.getDate();
      if (day < 10) {
        day = "0" + day;
      }
      if (month < 10) {
        month = "0" + month;
      }

      const today = year + "-" + month + "-" + day;
      return today;
    },
  },

};
</script>

<style scoped>

.menu-list-page{
  background-color: #fae8b9;
}
.menu-list-page h2{
  margin: 1.5em 0 1em;
  color: #a31d1e;
  font-size: 1.8em;
  font-weight: normal;
}

.menu-day-btn{
  border: 2px solid #a31d1e;
  padding: 1em;
  font-size: 0.9em;
  font-weight: bold;
  background-color:#a31d1e;
  color:rgb(247, 225, 181);

}


.menu-day-btn:hover{
  background-color:rgb(247, 225, 181);
  color:#a31d1e;
  
}

</style>