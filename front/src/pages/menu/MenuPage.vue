<template>
  <h1>
    MENÚ DEL DÍA: <span>{{ this.date }}</span>
  </h1>

  <h2>Primeros</h2>
  <section v-for="menu in this.firsts" :key="menu.id_dish">
    <ul class="split_the_dishes">
      <li>Nombre: {{ menu.name_dish }}</li>
      <li>Descripción: {{ menu.desc_dish }}</li>
    </ul>
  </section>
  <h2>Segundos</h2>
  <section v-for="menu in this.seconds" :key="menu.id_dish">
    <ul class="split_the_dishes">
      <li>Nombre: {{ menu.name_dish }}</li>
      <li>Descripción: {{ menu.desc_dish }}</li>
    </ul>
  </section>
  <h2>Postres</h2>
  <section v-for="menu in this.desserts" :key="menu.id_dish">
    <ul class="split_the_dishes">
      <li>Nombre: {{ menu.name_dish }}</li>
      <li>Descripción: {{ menu.desc_dish }}</li>
    </ul>
  </section>
</template>

<script>
export default {
  name: "menu_dia",
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
      const response = await fetch("http://192.168.21.125:5000/api/menus/by-date/" + this.$route.params.date);
      let menus = await response.json();
      this.firsts = menus.desc.firsts;
      this.seconds = menus.desc.seconds;
      this.desserts = menus.desc.desserts;
        
      
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
  list-style: none;
  margin: 0.3em;
}
p {
  margin: 200px;
  text-align: center;
}
.split_the_dishes {
  margin: 1.5em;
}
</style>
