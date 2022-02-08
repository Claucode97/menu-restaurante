<template>
<form action="addNewMenu" >
    <div class="date">
        <input type="date" name="date" id="date">
    </div>
    <p class="title">Nombre</p> <p class="title">Descripción</p>
    <p>Primeros:</p>
    <section class="firsts" v-for="i in 3" :key="i">
        <pre>{{i}}</pre><input class= "name_dish" id="f1" type="text" placeholder="Introducir plato" v-model="name_dish" 
        v-show= !block_input>
        <input class= "desc_dish" type="text" placeholder="Introducir descripción" v-model="desc_dish" @keydown.tab="addDishToDict(i)" this.name_dish='' v-show= !block_input>
        
        
    </section>
    <p>Segundos:</p>
    <section class="seconds">
        1.<input class= "name_dish" type="text" placeholder="Introducir plato">
        <input class= "desc_dish" type="text" placeholder="Introducir descripción">
        2.<input class= "name_dish" type="text" placeholder="Introducir plato">
        <input class= "desc_dish" type="text" placeholder="Introducir descripción">
        3.<input class= "name_dish" type="text" placeholder="Introducir plato">
        <input class= "desc_dish" type="text" placeholder="Introducir descripción">
    </section>
    <p>Postres:</p>
    <section class="desserts">
        1.<input class= "name_dish" type="text" placeholder="Introducir plato">
        <input class= "desc_dish" type="text" placeholder="Introducir descripción">
        2.<input class= "name_dish" type="text" placeholder="Introducir plato">
        <input class= "desc_dish" type="text" placeholder="Introducir descripción">
        3.<input class= "name_dish" type="text" placeholder="Introducir plato">
        <input class= "desc_dish" type="text" placeholder="Introducir descripción">
        4.<input class= "name_dish" type="text" placeholder="Introducir plato">
        <input class= "desc_dish" type="text" placeholder="Introducir descripción">
    </section>
    <button type="addNewMenu">Añadir Menú</button>
</form>
{{$data}}
</template>
<!-- /addNewMenu?date=2022-02-10 -->
<script>
export default {
  name: "",
  data() {
    return {
        block_input: false,
        name_dish:'',
        desc_dish:'',
        firsts:[],
        id_dish:'',
        date:'',
        id:''
     };
  },

  mounted() {
    
  },
  computed:{
      isDisabled(){
          return this.form.validated;
      }
  },
  methods: {
    addDish(){
        console.log(this.firsts.length)
    },
    addDishToDict(number_dish) { 
        let toDict={'name_dish':this.name_dish, 'desc_dish':this.desc_dish, 'id_dish':number_dish}
        this.firsts.push(toDict)
        this.block_input = true
        this.name_dish=''
        this.desc_dish=''

    },
  },
};
</script>
<style scoped>
body{
    padding:0;
    margin:0;
}
.title{
    display:inline-flex;
    flex-direction: row;
    justify-content: space-between;
    
}
.date{
    display:flex;
    justify-content: flex-end;

}
.firsts{
    display:grid;
    grid-template-columns: 0.01fr 1fr 3fr;
}
.seconds{
    display:grid;
    grid-template-columns:0.01fr 1fr 3fr;
}
.desserts{
    display:grid;
    grid-template-columns: 0.01fr 1fr 3fr;
}
input{
    margin-bottom:0.2em;
}


</style>
