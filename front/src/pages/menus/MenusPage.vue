<template>
  <ul v-for="dates in listOfDates" :key="dates.id">
    <router-link :to="{name: 'Menu', params: {date: dates.date}}">
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

  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const response = await fetch("http://192.168.21.125:5000/api/menus");
      this.listOfDates = await response.json();
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