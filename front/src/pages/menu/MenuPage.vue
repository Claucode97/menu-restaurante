<template>
  <h1>
    MENÚ DEL DÍA: <span>{{ this.date }}</span>
  </h1>

  <h2>Primeros</h2>
  <section v-for="menu in this.primeros" :key="menu.id_dish">
    <ul class="split_the_dishes">
      <li>Nombre: {{ menu.name_dish }}</li>
      <li>Descripción: {{ menu.desc_dish }}</li>
    </ul>
  </section>
  <h2>Segundos</h2>
  <section v-for="menu in this.segundos" :key="menu.id_dish">
    <ul class="split_the_dishes">
      <li>Nombre: {{ menu.name_dish }}</li>
      <li>Descripción: {{ menu.desc_dish }}</li>
    </ul>
  </section>
  <h2>Postres</h2>
  <section v-for="menu in this.postres" :key="menu.id_dish">
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
      menus: [],
      primeros: [],
      segundos: [],
      postres: [],
      date: "2022-01-31",
    };
  },
  computed: {
    filteredMenus() {
      return NaN;
    },
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const response = await fetch("http://localhost:5000/api/menu_dia");
      this.menus = await response.json();

      this.primeros = this.menus.desc.primeros;
      this.segundos = this.menus.desc.segundos;
      this.postres = this.menus.desc.postres;
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
