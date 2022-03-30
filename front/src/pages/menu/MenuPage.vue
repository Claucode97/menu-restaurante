<template>
<h2>-{{loggedRestaurant}}-</h2>
  <h3>
    Menú del día 
  </h3>
  <p>{{ dateParsed }}</p>
  <div class="modify_div_btn">
    <router-link :to="{name: 'MenuModifyPage', params: {date: this.$route.params.date}}">
    <button @click="saveMenuId">Modificar menu</button>
    </router-link>
    
    
  </div> 
  <button class="copy-button" @click="copyModalClicked">Copiar Menu</button>
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

<SelectDateCopyMenu  v-show="modalOpened" @changedDate="copyMenu" @modaltoFALSE="modaltoFalse()"/>
</template>

<script>
import {getMenuByDate} from "@/services/api.js"
import SelectDateCopyMenu from "@/pages/menu-add/SelectDateCopyMenu.vue"
import config from "@/config.js";
import { v4 as uuidv4 } from "uuid";

export default {
  
  components: { SelectDateCopyMenu },
  data() {
    return {
      firsts: [],
      seconds: [],
      desserts: [],
      date: this.$route.params.date,
      dateToCopy : "",
      parsedDate:'',
      loggedRestaurant:localStorage.name,
      menu : {},
      modalOpened: false
    };
  },

  mounted() {
    this.loadData();
  },
  methods: {

    async copyMenu(newDate){
       this.dateToCopy = newDate
        let desc = this.menu.desc;
        this.dictToSend = { date: this.dateToCopy, desc: desc, id_restaurant: localStorage.id_restaurant };
        this.dictToSend.id = uuidv4();
        localStorage.id_menu = this.dictToSend.id

        const settings = {
          method: "POST",
          body: JSON.stringify(this.dictToSend),
          headers: {
            Authorization: localStorage.id_restaurant,
            "Content-Type": "application/json",
          },
        };
        await fetch(`${config.API_PATH}/menus/${this.date}/copy/${this.dateToCopy}`, settings);

   

    },
    async loadData() {
      this.menus = await getMenuByDate(this.date)
      
      this.firsts = this.menus.desc.firsts;
      this.seconds = this.menus.desc.seconds;
      this.desserts = this.menus.desc.desserts;
    },
    saveMenuId(){
      localStorage.id_menu = this.menus.id
    },
    copyModalClicked(){
      this.modalOpened = true
      console.log("clicc modal" + this.modalOpened)

    },
  
    modaltoFalse(newvalue){
      this.modalOpened = newvalue
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
    }
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
