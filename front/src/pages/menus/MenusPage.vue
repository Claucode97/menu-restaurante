<template>
<h2>{{loggedRestaurant}}</h2>
  <router-link :to="{ name: 'Menu', params: { date: getToday } }">
    <button class="menu-day">Menú del día</button>
  </router-link>

  <Calendar />

  <ListOfMenus />
</template>

<script>
import ListOfMenus from './ListOfMenu.vue'
import Calendar from './Calendar.vue'
export default {
  components: {Calendar,ListOfMenus},
  data() {
    return {
      loggedRestaurant: localStorage.name,
      
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



.menu-day{
  margin-top:1em
}
</style>