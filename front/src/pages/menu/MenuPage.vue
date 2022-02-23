<template>
  <h2>
    MENÚ DEL DÍA: <span>{{ this.date }}</span>
  </h2>
  <div class="modify_div_btn">
    <router-link :to="{name: 'MenuModifyPage', params: {date: this.$route.params.date}}">
    <button>Modificar menu</button>
    </router-link>
  </div> 
  <h3>Primeros</h3>
  <section v-for="menu in this.firsts" :key="menu.id_dish">
    <ul class="split_the_dishes">
      <li>{{ menu.name_dish }}</li>
      <li class="menu_detail">{{ menu.desc_dish }}</li>
    </ul>
  </section>
  <h3>Segundos</h3>
  <section v-for="menu in this.seconds" :key="menu.id_dish">
    <ul class="split_the_dishes">
      <li>{{ menu.name_dish }}</li>
      <li class="menu_detail">{{ menu.desc_dish }}</li>
    </ul>
  </section>
  <h3>Postres</h3>
  <section v-for="menu in this.desserts" :key="menu.id_dish">
    <ul class="split_the_dishes">
      <li>{{ menu.name_dish }}</li>
      <li class="menu_detail">{{ menu.desc_dish }}</li>
    </ul>
  </section>
</template>

<script>
export default {
  
  data() {
    return {
      firsts: [],
      seconds: [],
      desserts: [],
      date: this.$route.params.date,
    };
  },

  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const response = await fetch("http://localhost:5000/api/menus/by-date/" + this.$route.params.date);
      let menus = await response.json();
      console.log('Menus',menus)
      this.firsts = menus.desc.firsts;
      this.seconds = menus.desc.seconds;
      this.desserts = menus.desc.desserts;
      // let x=new Date().toJSON().slice(0,10)
      // let day=x.toJSON().slice(8,10)
      // console.log('Obj Date',x,day)  
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
.menu_detail{
  font-size:11px;
  font-style: italic;
}
.modify_div_btn{
  display:flex;
  justify-content: flex-end
}
</style>
