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
      const response = await fetch("http://localhost:5000/api/menus");
      let menus = await response.json();

      for (let menu of menus) {
        if (menu.date == this.$route.params.date) {
          this.firsts = menu.desc.firsts;
          this.seconds = menu.desc.seconds;
          this.desserts = menu.desc.desserts;
        }
      }
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
