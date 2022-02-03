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
      primeros: [],
      segundos: [],
      postres: [],
      date: this.$route.params.date,
    };
  },

  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const response = await fetch("http://192.168.21.222:5000/api/menus");
      let menus = await response.json();

      for (let menu of menus) {
        if (menu.date == this.$route.params.date) {
          this.primeros = menu.desc.primeros;
          this.segundos = menu.desc.segundos;
          this.postres = menu.desc.postres;
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
