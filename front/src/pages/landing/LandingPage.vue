<template>
<h2>-{{loggedRestaurant}}-</h2>
  <h3>
    Menú del día 
  </h3>
  <p>{{ dateParsed }}</p>
  <h3>Primeros</h3>
  <section v-for="menu in this.firsts" :key="menu.id_dish">
    <ul class="split_the_dishes">
      <li>{{ menu.name_dish }}</li>
      <li class="allergen-detail" v-for="allergen in menu.allergens" :key="allergen.id" >{{ allergen }}</li>
    </ul>
  </section>
  <h3>Segundos</h3>
  <section v-for="menu in this.seconds" :key="menu.id_dish">
    <ul class="split_the_dishes">
      <li>{{ menu.name_dish }}</li>
      <li class="allergen-detail" v-for="allergen in menu.allergens" :key="allergen.id" >{{ allergen }}</li>
    </ul> 
  </section>
  <h3>Postres</h3>
  <section v-for="menu in this.desserts" :key="menu.id_dish">
    <ul class="split_the_dishes">
      <li>{{ menu.name_dish }}</li>
      <li class="allergen-detail" v-for="allergen in menu.allergens" :key="allergen.id">{{ allergen}}</li>
    </ul>
  </section>

</template>

<script>
import {getMenuToday} from "@/services/api.js"


export default {
  data() {
    return {
      firsts: [],
      seconds: [],
      desserts: [],
      date: "",
      parsedDate:'',
      loggedRestaurant:this.$route.params.name_restaurant.replace("-"," "),
      menu : {},
    };
  },

  mounted() {
    this.getToday();
    this.loadData();
  },
  methods: {

    async loadData() {
      this.menus = await getMenuToday(this.loggedRestaurant)
      
      this.firsts = this.menus.firsts;
      this.seconds = this.menus.seconds;
      this.desserts = this.menus.desserts;
    },
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
      this.date = today;
    },

  },
  computed:{
    dateParsed() {
      let year=this.date.slice(0,4)
      let day=this.date.slice(8,10)
      let month=this.date.slice(5,7)
      let months={'01':'Enero','02':'Febrero','03':'Marzo','04':'Abril','05':'Mayo','06':'Junio','07':'Julio','08':'Agosto','09':'Septiembre','10':'Octubre','11':'Noviembre','12':'Diciembre'}
      let fullDate=day+' de '+months[month]+' de '+year
      return fullDate
    },

  },
};
</script>

<style scoped>
* {
  padding: 0;
  margin: 0;
}

li {
  text-align: center;
  margin: 0.3em;
  list-style: none;
  font-style: bold;
}

.split_the_dishes {
  margin: 0.8em;
}
.allergen-detail{
  font-size:11px;
  font-style: italic;
  display: inline;
}
.modify_div_btn{
  display:flex;
  justify-content: flex-end
}

</style>
