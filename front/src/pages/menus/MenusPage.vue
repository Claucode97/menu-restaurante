<template>
  <ul v-for="dates in listOfDates" :key="dates.id">
    <router-link v-bind:to="/menu/ + dates.date">
      <li>{{ dates.date }}</li>
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
      //const response = await fetch("http://localhost:5000/api/menu_dia");
      //this.menus = await response.json();
      this.listOfDates = [
        {
          desc: {
            postres: [
              {
                desc_dish: "alto contenido de huevo",
                id_dish: "07",
                name_dish: "flan horneado",
              },
              {
                desc_dish: "sin tacc",
                id_dish: "08",
                name_dish: "helado",
              },
              {
                desc_dish: "bizcocho",
                id_dish: "09",
                name_dish: "lemon pie",
              },
              {
                desc_dish: "derivado lacteo",
                id_dish: "10",
                name_dish: "natilla de chocolate",
              },
            ],
            primeros: [
              {
                desc_dish: "ensalada con cebolla",
                id_dish: "01",
                name_dish: "ensalada mixta",
              },
              {
                desc_dish: "tocino, chorizo, morcilla",
                id_dish: "02",
                name_dish: "Alubias con sus sacramentos",
              },
              {
                desc_dish: "salsa de tomate",
                id_dish: "03",
                name_dish: "Spaguetti a la bolognesa",
              },
            ],
            segundos: [
              {
                desc_dish: "asado a las brasas",
                id_dish: "04",
                name_dish: "lomo con patatas",
              },
              {
                desc_dish: "verduras, curry",
                id_dish: "05",
                name_dish: "arroz cremoso de carne",
              },
              {
                desc_dish: "asado a las brasas, verduras salteadas",
                id_dish: "06",
                name_dish: "Muslo de pollo relleno",
              },
            ],
          },
          id: "MM",
          date: "2021-05-10",
        },
        {
          desc: {
            postres: [
              {
                desc_dish: "alto contenido de huevo",
                id_dish: "07",
                name_dish: "flan horneado",
              },
              {
                desc_dish: "sin tacc",
                id_dish: "08",
                name_dish: "helado",
              },
              {
                desc_dish: "bizcocho",
                id_dish: "09",
                name_dish: "lemon pie",
              },
              {
                desc_dish: "derivado lacteo",
                id_dish: "10",
                name_dish: "natilla de chocolate",
              },
            ],
            primeros: [
              {
                desc_dish: "ensalada con cebolla",
                id_dish: "01",
                name_dish: "ensalada mixta",
              },
              {
                desc_dish: "tocino, chorizo, morcilla",
                id_dish: "02",
                name_dish: "Alubias con sus sacramentos",
              },
              {
                desc_dish: "salsa de tomate",
                id_dish: "03",
                name_dish: "Spaguetti a la bolognesa",
              },
            ],
            segundos: [
              {
                desc_dish: "asado a las brasas",
                id_dish: "04",
                name_dish: "lomo con patatas",
              },
              {
                desc_dish: "verduras, curry",
                id_dish: "05",
                name_dish: "arroz cremoso de carne",
              },
              {
                desc_dish: "asado a las brasas, verduras salteadas",
                id_dish: "06",
                name_dish: "Muslo de pollo relleno",
              },
            ],
          },
          id: "MX",
          date: "2021-05-15",
        },
        {
          desc: {
            postres: [
              {
                desc_dish: "alto contenido de huevo",
                id_dish: "07",
                name_dish: "flan horneado",
              },
              {
                desc_dish: "sin tacc",
                id_dish: "08",
                name_dish: "helado",
              },
              {
                desc_dish: "bizcocho",
                id_dish: "09",
                name_dish: "lemon pie",
              },
              {
                desc_dish: "derivado lacteo",
                id_dish: "10",
                name_dish: "natilla de chocolate",
              },
            ],
            primeros: [
              {
                desc_dish: "ensalada con cebolla",
                id_dish: "01",
                name_dish: "ensalada mixta",
              },
              {
                desc_dish: "tocino, chorizo, morcilla",
                id_dish: "02",
                name_dish: "Alubias con sus sacramentos",
              },
              {
                desc_dish: "salsa de tomate",
                id_dish: "03",
                name_dish: "Spaguetti a la bolognesa",
              },
            ],
            segundos: [
              {
                desc_dish: "asado a las brasas",
                id_dish: "04",
                name_dish: "lomo con patatas",
              },
              {
                desc_dish: "verduras, curry",
                id_dish: "05",
                name_dish: "arroz cremoso de carne",
              },
              {
                desc_dish: "asado a las brasas, verduras salteadas",
                id_dish: "06",
                name_dish: "Muslo de pollo relleno",
              },
            ],
          },
          id: "MT",
          date: "2021-05-16",
        },
      ];
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
</style>