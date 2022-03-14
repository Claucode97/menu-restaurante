<template>
<h2>{{loggedRestaurant}}</h2>
  <router-link :to="{ name: 'Menu', params: { date: getToday } }">
    <button class="menu-day">Menú del día</button>
  </router-link>
  <article class="calendar">
    <section class="name-month">
      <button class="button-last-month" @click="prevMonth">⬅</button>
      <h2 @click="comeBackCurrentMonth()">
        {{ nameMonths[this.currentMonth] }} {{ currentYear }}
      </h2>
      <button class="button-last-month" @click="nextMonth">➡</button>
    </section>
    <ul class="name-of-week">
      <li v-for="index in nameDaysOfWeek" :key="index">{{ index }}</li>
    </ul>
    <ul class="days-of-month">
      <li
        class="empty-list"
        v-for="i in initialPositionOfFirstDay"
        :key="i"
      ></li>
      <li @click="onClickDay(index.day)"
        v-for="index of daysOfMonthSelected"
        :key="index" v-bind:class="{underline:index.menuExists}">
        {{index.day}}
      </li>
    </ul>
  </article>

  <ul class="menu-date" v-for="menu in listOfMenus" :key="menu.id">
    <div>
    <router-link :to="{ name: 'Menu', params: { date: menu.date } }">
      <li>{{ menu.date }}</li>
    </router-link>
    </div>
  </ul>
</template>

<script>
import {getListOfMenus} from "@/services/api.js"
export default {
  data() {
    return {
      currentDay: new Date().getDate(),
      currentMonth: new Date().getMonth(),
      currentYear: new Date().getFullYear(),
      nameDaysOfWeek: ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"],
      nameMonths: [
        "Enero","Febrero","Marzo","Abril","Mayo","Junio",
        "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],
      listOfMenus: [],
      loggedRestaurant: localStorage.name,
      days:[],
      months:[],
      dates:[],
     
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
    initialPositionOfFirstDay() {
      let initialDayWeek = new Date(
        this.currentYear,
        this.currentMonth,
        1
      ).getDay();
      if (initialDayWeek === 0) {
        return (initialDayWeek = 6);
      }
      let currentInitialDayweek = initialDayWeek - 1;
      return currentInitialDayweek;
    },
    daysOfMonthSelected() {
      let bindMenusOfMonthToCal=[]
      let totaldays = new Date(
        this.currentYear,
        this.currentMonth + 1,0).getDate();
      let menusOfTheMonth=this.extractMenusOfTheMonth()
      for (let i=1;i<=totaldays;i++){
        let menuExists=false
        let dayToStr=i.toString()
        if (menusOfTheMonth.includes(dayToStr)){ menuExists=true }
        if (dayToStr < 10) { dayToStr = "0" + dayToStr }
        bindMenusOfMonthToCal.push({'day':dayToStr,'menuExists':menuExists})
      }
      return bindMenusOfMonthToCal
    },
  },
  methods: {
    extractMenusOfTheMonth(){
      let monthExtracted=''
      let daysConnected=[]
      let current_month=this.currentMonth+1
      let day=''
      if (current_month < 10) {
        current_month = "0" + current_month;
      }
      for (let menu of this.listOfMenus){
        monthExtracted=menu.date.slice(5,7)
        if (monthExtracted===current_month){
          day=menu.date.slice(8,10)
          if (day.slice(0,1)==='0') {
            day = day.slice(1,2);
           }
          daysConnected.push(day)
        }
      }
      return daysConnected
    },
    comeBackCurrentMonth() {
      let comebackMonth = new Date().getMonth();
      this.currentMonth = comebackMonth;
      
    },
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
    onClickDay(day) {
      let month = this.currentMonth + 1;
      if (month < 10){
        month = "0" + month
      }
      const clickedDay = this.currentYear + "-" +month + "-" + day;
      const settings = {
        method: "GET",
        headers: {
          Authorization: localStorage.id_restaurant,
        },
      } 
      for (let menu of this.listOfMenus){
      if (menu.date === clickedDay){ 
      this.$router.push("/menus/by-date/" + clickedDay,settings)
      return
      }
      }
      this.$router.push("/menu/add")

      
    },
    async loadData() {
      this.listOfMenus = await getListOfMenus();
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
}
.days-of-month > li {
  padding: 25% 25%;
}
.days-of-month > .empty-list {
  background: none;
}
.days-of-month > .not-empty-list:hover {
  font-size: 1.07rem;
  font-weight: bolder;
  color: darkblue;
  background-color: lightblue;
  border-radius: 50%;
  cursor: pointer;
}
.name-month {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.name-month > h2 {
  text-decoration: underline;
  cursor: pointer;
}
.button-last-month,
.button-next-month {
  width: 50px;
}

.underline {
  text-decoration: underline double;
  cursor:pointer;
}
.menu-day{
  margin-top:1em
}
</style>