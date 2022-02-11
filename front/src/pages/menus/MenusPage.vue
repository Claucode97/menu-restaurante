<template>
  <router-link :to="{name: 'Menu', params: {date: getToday}}">
    <button> Menú del día</button>  
  </router-link> 
  <ul v-for="menu in listOfMenus" :key="menu.id">
    <router-link :to="{name: 'Menu', params: {date: menu.date}}">
      <li>{{ menu.date }}</li>
    </router-link>
  </ul>
</template>


<script>

export default {
 
  data() {
    return {
      listOfMenus: [],
    };
  },

  mounted() {
    this.loadData();
  },
  computed:{
    getToday(){
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

      const today = year+'-'+month+'-'+day;
      return today

    },
  },
  methods: {
    

    async loadData() {
      const response = await fetch("http://localhost:5000/api/menus");
      this.listOfMenus = await response.json();
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

h1{
  border: 2px solid black; 

}
</style>