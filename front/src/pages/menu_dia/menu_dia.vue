<template>
  <nav class="menu dia">
    <h1>MENU DEL DIA</h1>   
    <h2>Primeros</h2>
    <section  v-for="menu in menus.primeros" :key="menu.id">
        <ul class="split_the_dishes">
            <li>{{menu.nombre_plato}}  :</li> 
            <li>{{menu.descripcion}}</li>
        </ul>
    </section>
        <h2>Segundos</h2>
    <section  v-for="menu in menus.segundos" :key="menu.id">
        <ul class="split_the_dishes">
            <li>{{menu.nombre_plato}}  :</li>
            <li>{{menu.descripcion}}</li>
        </ul>
    </section>
        <h2>Postres</h2>
    <section v-for="menu in menus.postres" :key="menu.id">
        <ul class="split_the_dishes">
            <li>{{menu.nombre_plato}}  :</li>
            <li>{{menu.descripcion}}</li>
        </ul>
    </section>
  </nav>
</template>

<script>
export default {
    name:"menu_dia",
    data() {
      return {
        menus: []
      }
    },
    mounted() {
      this.loadData()
    },
    methods: {
      async loadData() {
        const response = await fetch('http://192.168.21.222:5000/api/menu_dia')
        this.menus = await response.json()
      }
    }


}
</script>

<style scoped>
*{
    padding: 0;
}


li{
    text-align: center;
    list-style: none;
    margin: 0.3em;
};
p{
    margin: 200px ;
    text-align: center;
  
}
.split_the_dishes{
    margin: 1.5em;
}

</style>
