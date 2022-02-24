<template>
  <router-link :to="{ name: 'Menu', params: { date: getToday } }">
    <button>Menú del día</button>
  </router-link>

  <article class="calendar">
    <section class="name-month">
      <button class="button-last-month" @click="prevMonth">⬅</button>
      <h2>
        {{ currentCalendar[this.currentMonth]["nameOfMonth"] }}
        {{ currentYear }}
      </h2>
      <button class="button-next-month" @click="nextMonth">➡</button>
      {{ currentMonth }} {{ showDays }}
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
      <li @click="onClikDay(1)" class="first-day selected-day">1</li>
      <li @click="onClikDay(2)">2</li>
      <li>3</li>
      <li>6</li>
      <li>5</li>
      <li>7</li>
      <li>4</li>
      <li>8</li>
      <li>9</li>
      <li>10</li>
      <li>11</li>
      <li>12</li>
      <li>13</li>
      <li>14</li>
      <li>15</li>
      <li>16</li>
      <li>17</li>
      <li>18</li>
      <li>19</li>
      <li>20</li>
      <li>21</li>
      <li>22</li>
      <li>23</li>
      <li>24</li>
      <li>25</li>
      <li>26</li>
      <li>27</li>
      <li>28</li>
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
      currentMonth: new Date().getMonth() + 1,
      currentYear: new Date().getFullYear(),
      dayOnClicked: null,
      currentCalendar: {
        1: {
          nameOfMonth: "Enero",
          days: new Date(this.currentYear, 1, 0).getDate(),
        },
        2: {
          nameOfMonth: "Febrero",
          days: new Date(this.currentYear, 2, 0).getDate(),
        },
        3: {
          nameOfMonth: "Marzo",
          days: new Date(this.currentYear, 3, 0).getDate(),
        },
        4: {
          nameOfMonth: "Abril",
          days: new Date(this.currentYear, 4, 0).getDate(),
        },
        5: {
          nameOfMonth: "Mayo",
          days: new Date(this.currentYear, 5, 0).getDate(),
        },
        6: {
          nameOfMonth: "Junio",
          days: new Date(this.currentYear, 6, 0).getDate(),
        },
        7: {
          nameOfMonth: "Julio",
          days: new Date(this.currentYear, 7, 0).getDate(),
        },
        8: {
          nameOfMonth: "Agosto",
          days: new Date(this.currentYear, 8, 0).getDate(),
        },
        9: {
          nameOfMonth: "Septiembre",
          days: new Date(this.currentYear, 9, 0).getDate(),
        },
        10: {
          nameOfMonth: "Octubre",
          days: new Date(this.currentYear, 10, 0).getDate(),
        },
        11: {
          nameOfMonth: "Noviembre",
          days: new Date(this.currentYear, 11, 0).getDate(),
        },
        12: {
          nameOfMonth: "Diciembre",
          days: new Date(this.currentYear, 12, 0).getDate(),
        },
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
    showDays() {
      //new Date(2022, 1, 0).getDate()
      return 28;
    },
  },
  methods: {
    nextMonth() {
      this.currentMonth += 1;
      if (this.currentMonth > 12) {
        this.currentMonth = 12;
      }
    },
    prevMonth() {
      this.currentMonth -= 1;
      if (this.currentMonth < 1) {
        this.currentMonth = 1;
      }
    },
    onClikDay(day) {
      console.log("el día es: ", day);
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
.first-day {
  grid-column-start: 2;
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