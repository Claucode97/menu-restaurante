<template>
  {{ currentMonth }} {{ daysOfMonthSelected }}
  <router-link :to="{ name: 'Menu', params: { date: getToday } }">
    <button>Menú del día</button>
  </router-link>

  <article class="calendar">
    <section class="name-month">
      <button class="button-last-month" @click="prevMonth">⬅</button>
      <h2>
        {{ nameMonths[this.currentMonth] }}
        {{ currentYear }}
      </h2>
      <button class="button-last-month" @click="nextMonth">➡</button>
    </section>
    <ul class="name-of-week">
      <li>Lun</li>
      <li>Mar</li>
      <li>Mié</li>
      <li>Jue</li>
      <li>Vier</li>
      <li>Sáb</li>
      <li>Dom</li>
    </ul>
    <ul class="days-of-month">
      <li v-for="i in showInitialDayOfMonth - 1" :key="i"></li>
      <li v-for="index in daysOfMonthSelected" :key="index">
        {{ index }}
      </li>
    </ul>
  </article>
  <ul class="menu-date" v-for="menu in listOfMenus" :key="menu.id">
    <router-link :to="{ name: 'Menu', params: { date: menu.date } }">
      <li>{{ menu.date }}</li>
    </router-link>
  </ul>
</template>


<script>
export default {
  data() {
    return {
      currentDay: new Date().getDate(),
      currentMonth: new Date().getMonth(),
      currentYear: new Date().getFullYear(),
      nameMonths: {
        0: "Enero",
        1: "Febrero",
        2: "Marzo",
        3: "Abril",
        4: "Mayo",
        5: "Junio",
        6: "Julio",
        7: "Agosto",
        8: "Septiembre",
        9: "Octubre",
        10: "Noviembre",
        11: "Diciembre",
      },
      listOfMenus: [],
    };
  },

  mounted() {
    this.loadData();
  },
  computed: {
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
      return today;
    },
    showInitialDayOfMonth() {
      let initialDayWeek = new Date(
        this.currentYear,
        this.currentMonth,
        1
      ).getDay();
      return initialDayWeek;
    },
    daysOfMonthSelected() {
      let totaldays = new Date(
        this.currentYear,
        this.currentMonth + 1,
        0
      ).getDate();
      return totaldays;
    },
  },
  methods: {
    nextMonth() {
      this.currentMonth = this.currentMonth + 1;
      if (this.currentMonth > 11) {
        this.currentMonth = 11;
      }
    },
    prevMonth() {
      this.currentMonth -= 1;
      if (this.currentMonth < 0) {
        this.currentMonth = 0;
      }
    },
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
  font-size: 16px;
  box-sizing: border-box;
}
.menu-date {
  list-style: none;
  text-align: center;
  margin: 1em;
}

h1 {
  border: 2px solid black;
}

.calendar {
  width: 100%;
  max-width: 300px;
  margin: 2em auto;
}

.name-of-week {
  background: rgba(173, 216, 230, 0.74);
  margin: 0.2em 0;
  padding: 0.5em;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-auto-rows: 10px;
  align-items: center;
}
.days-of-month {
  font-size: 1rem;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-auto-rows: 40px;
  cursor: pointer;
  justify-content: center;
  align-items: center;
}

.days-of-month > li:hover {
  font-weight: bolder;
  background-color: lightblue;
  border-radius: 45%;
}
.name-month {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.button-last-month,
.button-next-month {
  width: 40px;
}
</style>