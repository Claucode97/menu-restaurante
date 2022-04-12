<template>
  <article v-if="!isMenuEmpty">
  
    

<div class="menu-detail-header">
      <div class="header-text-wrapper">
        <h2>{{ loggedRestaurant }}</h2>
        <p>Menú del {{ dateParsed }}</p>
      </div>
      
    </div>
    <h3>Primeros</h3>
    <section v-for="menu in this.firsts" :key="menu.id_dish">
      <ul class="split_the_dishes">
        <li>{{ menu.name_dish }}</li>
        <li
          class="allergen-detail"
          v-for="allergen in menu.allergens"
          :key="allergen.id"
        >
          <img
            alt="allergensIcons.lactose"
            :src="
              require('@/assets/img/allergens_icons/' +
                allergensIcons[allergen])
            "
          />
        </li>
      </ul>
    </section>
    <h3>Segundos</h3>
    <section v-for="menu in this.seconds" :key="menu.id_dish">
      <ul class="split_the_dishes">
        <li>{{ menu.name_dish }}</li>
        <li
          class="allergen-detail"
          v-for="allergen in menu.allergens"
          :key="allergen.id"
        >
          <img
            alt="allergensIcons.lactose"
            :src="
              require('@/assets/img/allergens_icons/' +
                allergensIcons[allergen])
            "
          />
        </li>
      </ul>
    </section>
    <h3>Postres</h3>
    <section v-for="menu in this.desserts" :key="menu.id_dish">
      <ul class="split_the_dishes">
        <li>{{ menu.name_dish }}</li>
        <li
          class="allergen-detail"
          v-for="allergen in menu.allergens"
          :key="allergen.id"
        >
          <img
            alt="allergensIcons.lactose"
            :src="
              require('@/assets/img/allergens_icons/' +
                allergensIcons[allergen])
            "
          />
        </li>
      </ul>
    </section>
  </article>
  <p v-else>Hoy no hay menu</p>
</template>

<script>
import { getMenuToday } from "@/services/api.js";

export default {
  data() {
    return {
      allergensIcons: {
        lactose: "lactose.png",
        gluten: "gluten.png",
        egg: "egg.png",
        seafood: "seafood.png",
        soy: "soy.png",
        nuts: "nut.png",
      },
      firsts: [],
      seconds: [],
      desserts: [],
      date: "",
      parsedDate: "",
      loggedRestaurant: this.$route.params.name_restaurant.replace("-", " "),
      menu: {},
      isMenuEmpty: false,
    };
  },

  mounted() {
    this.getToday();
    this.loadData();
  },
  methods: {
    async loadData() {
      const response = await getMenuToday(this.loggedRestaurant);
      console.log(response.status);
      if (response === 404) {
        this.isMenuEmpty = true;
      } else {
        this.menus = response;
        this.firsts = this.menus.firsts;
        this.seconds = this.menus.seconds;
        this.desserts = this.menus.desserts;
      }
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
  computed: {
    dateParsed() {
      let year = this.date.slice(0, 4);
      let day = this.date.slice(8, 10);
      let month = this.date.slice(5, 7);
      let months = {
        "01": "Enero",
        "02": "Febrero",
        "03": "Marzo",
        "04": "Abril",
        "05": "Mayo",
        "06": "Junio",
        "07": "Julio",
        "08": "Agosto",
        "09": "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre",
      };
      let fullDate = day + " de " + months[month] + " de " + year;
      return fullDate;
    },
  },
};
</script>

<style scoped>

.menu-detail-header {
  padding: 1.3em 0;
  border-bottom: 1px solid #a31d1e;
  margin: 0 0 1.3em 0;
  
}
.main-menu-detail-wrapper {
  text-align: left;
  padding: 0 0.5em;
}
.courses-wrapper {
  margin-bottom: 2em;
  font-family: "Oswald", sans-serif;
  font-size: 1em;
  text-align: center;
  color: #3b0b06;
  letter-spacing: 0.1em;
}
.courses-wrapper h3 {
  font-weight: 500;
}
.courses-wrapper li {
  font-weight: 300;
  margin-top: 1em;
}
.allergen-detail {
  font-size: 11px;
  font-style: italic;
  display: inline;
}
.allergen-detail img{
  width: 6%;
  margin-right: 0.5em;
}

</style>
