
<template>
    <form action="">
        <div class="date">
            <input type="date" name="date" id="date" v-model="date">
        </div>
        <p class="title">Nombre</p> <p class="title">Descripción</p>
        <p v-show="!isHiddenFirsts">Primeros:</p>
            <section class="namePlates" v-for="(i,index) in 3" :key="index">
                <pre v-show="!isHiddenFirsts">{{index +1}}</pre><input class= "name_dish"  type="text" placeholder="Introducir plato" v-model="nameDishFirsts[index]" v-show="!isHiddenFirsts">
                <input class= "descPlates" type="text" placeholder="Introducir descripción" v-model="descDishFirsts[index]" v-show="!isHiddenFirsts">
            </section>
            <button @click.prevent="addFirsts" v-show="!isHiddenFirsts" >Agrega Primeros</button>
        <p v-show="!isHiddenSeconds">Segundos:</p>
        <section class="namePlates" v-for="(i,index) in 3" :key="index">
                <pre v-show="!isHiddenSeconds">{{index +1}}</pre><input class= "name_dish"  type="text" placeholder="Introducir plato" v-model="nameDishSeconds[index]" v-show="!isHiddenSeconds">
                <input class= "descPlates" type="text" placeholder="Introducir descripción" v-model="descDishSeconds[index]" v-show="!isHiddenSeconds">
            </section>
            <button @click.prevent="addSeconds" v-show="!isHiddenSeconds">Agregar Segundos</button>
        
        <p v-show="!isHiddenDesserts">Postres:</p>
        <section class="namePlates" v-for="(i,index) in 4" :key="index">
                <pre v-show="!isHiddenDesserts">{{index +1}}</pre><input class= "name_dish"  type="text" placeholder="Introducir plato" v-model="nameDishDesserts[index]" v-show="!isHiddenDesserts">
                <input class= "descPlates" type="text" placeholder="Introducir descripción" v-model="descDishDesserts[index]" v-show="!isHiddenDesserts">
            </section>
            <button @click.prevent="addDesserts" v-show="!isHiddenDesserts">Agrega Postres</button>
            <button @click.prevent="onSaveClicked" class="submitButton" v-show="isHiddenDesserts && isHiddenSeconds && isHiddenFirsts">Enviar formulario</button>
    </form>
</template>
<!-- /addNewMenu?date=2022-02-10 -->
<script>
import {v4 as uuidv4} from "uuid";
export default {
  name: "",
  data() {
    return {
        nameDishFirsts:{},
        descDishFirsts:{},
        nameDishSeconds:{},
        descDishSeconds:{},
        nameDishDesserts:{},
        descDishDesserts:{},
        firsts:[],
        seconds:[],
        desserts:[],
        desc:{},
        isHiddenFirsts:false,
        isHiddenSeconds:false,
        isHiddenDesserts:false,
        date:'',
        dictToSend:{}
     };
  },

  mounted() {},
  computed:{
  },
  methods: {
    addFirsts() { 
        for (let plate in this.nameDishFirsts){
            let toDict={'name_dish':this.nameDishFirsts[plate], 'desc_dish':this.descDishFirsts[plate], 'id_dish':plate}
            this.firsts.push(toDict)
        }
        console.log('Resultado:',this.firsts)
        this.isHiddenFirsts=true
    },
    addSeconds() { 
        for (let plate in this.nameDishSeconds){
            let toDict={'name_dish':this.nameDishSeconds[plate], 'desc_dish':this.descDishSeconds[plate], 'id_dish':plate}
            this.seconds.push(toDict)
        }
        console.log('Resultado:',this.seconds)
        this.isHiddenSeconds=true
    },
    addDesserts() { 
        for (let plate in this.nameDishDesserts){
            let toDict={'name_dish':this.nameDishDesserts[plate], 'desc_dish':this.descDishDesserts[plate], 'id_dish':plate}
            this.desserts.push(toDict)
        }
        console.log('Resultado:',this.desserts)
        this.isHiddenDesserts=true
    },
    async onSaveClicked(){
        this.desc={'firsts':this.firsts,'seconds':this.seconds,'desserts':this.desserts}
        this.dictToSend={'date':this.date,'desc':this.desc}
        this.dictToSend.id=uuidv4();
        console.log(JSON.stringify(this.dictToSend))
        const settings={
            method:"POST",
            body: JSON.stringify(this.dictToSend),
            headers:{
                'Content-Type':'application/json'
                }
        }
        var response = await fetch("http://localhost:5000/api/menus",settings)
        console.log(response)
    }
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
.namePlates{
    display:grid;
    grid-template-columns: 0.01fr 1fr 3fr;
}
.descPlates{
    display:grid;
    grid-template-columns:0.01fr 1fr 3fr;
}

input{
    margin-bottom:0.2em;
}


</style>
