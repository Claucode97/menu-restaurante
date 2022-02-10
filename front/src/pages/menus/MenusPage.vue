<template>
  <router-link class="a" :to="{name: 'Menu', params: {date: dameFecha}}">
    <button> Menú del día</button>  
  </router-link> 
  <ul v-for="menuDate in listOfDates" :key="menuDate.id">
    <router-link :to="{name: 'Menu', params: {date: menuDate.date}}">
      <li>{{ menuDate.date }}</li>
    </router-link>
  </ul>
</template>


<script>

export default {
  name: "menu_dia",
  data() {
    return {
      listOfDates: [],
    };
  },

  mounted() {
    this.loadData();
  },
  computed:{
    dameFecha(){
      let current = new Date();
      let year = current.getFullYear();
      let month = current.getMonth()+1;
      let day = current.getDate();
      if (day < 10 ){
          day = "0" + day
      }
      if (month < 10 ){
          month = "0" + month
      }

      const hoy = year+'-'+month+'-'+day;
      return hoy

    },
  },
  methods: {
    

    async loadData() {
      const response = await fetch("http://localhost:5000/api/menus");
      this.listOfDates = await response.json();
    },
  },
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}
ul {
  list-style: none;
  text-align: center;
  margin: 1em;
}

a{
  text-decoration: none;
  
}
h1{
  border: 2px solid black; 

}
</style>