<template>
<form >
  <div class="dateNameRestaurant">
    <p>{{loggedRestaurant}}</p>
    <p >{{dateParsed()}}</p>
  </div>
    <section class="plates_info"  >
    <p>Primeros</p>
    <div class="firsts" v-for="dish in firsts" :key="dish.id_dish">
        <input class="input_plate" type="text"  v-model="dish.name_dish">
        <input class="input_plate" type="text"  v-model="dish.allergens">
    </div>
    <p>Segundos</p>
    <div class="seconds" v-for="dish in seconds" :key="dish.id_dish">
        <input class="input_plate" type="text"  v-model="dish.name_dish">
        <input class="input_plate" type="text"  v-model="dish.allergens">
    </div>
    <p>Postres</p>
    <div class="desserts" v-for="dish in desserts" :key="dish.id_dish">
        <input class="input_plate" type="text"  v-model="dish.name_dish">
        <input class="input_plate" type="text"  v-model="dish.allergens">
    </div>
    </section>
    <p v-show="!this.areThereEmpties">Existen vacíos!</p>
    <button @click.prevent="onSaveClicked">Modificar Menú</button>
</form>
</template>

<script>
import config from "@/config.js"
export default {
  name: "modifymenu",
  data() {
    return {
       dateReceived:this.$route.params.date,
       idReceived:this.$route.params.id,
       dict_plates:{},
       firsts:[],
       seconds:[],
       desserts:[],
       loggedRestaurant:localStorage.name,
       areThereEmpties:true
    };
  },

  mounted() {
    this.loadData()
  },
  computed:{},
  methods: {
    async loadData(){
      const settings = {
         method: "GET",
         headers: {
           Authorization: localStorage.id_restaurant,
         },
      }        
      const response = await fetch(`${config.API_PATH}/menus/` + localStorage.id_menu,settings);
      this.dict_plates = await response.json();
      this.firsts = this.dict_plates.desc.firsts;
      this.seconds = this.dict_plates.desc.seconds;
      this.desserts = this.dict_plates.desc.desserts;
      return this.dict_plates
      
    },
    dateParsed(){
        let completeDate =  this.dateReceived
        let year = completeDate.slice(0,4)
        let day = completeDate.slice(8,10)
        let month = completeDate.slice(5,7)
        return day + "-" + month + "-" + year
      },
    areValidInputsFromMenu(){
        let platesTot=[]
        let countEmpties=0
        for (let plate of this.firsts){
            let platesFirsts=String(plate.name_dish)
            platesTot.push(platesFirsts)
        }
        for (let plate of this.seconds){
            let platesSeconds=String(plate.name_dish)
            platesTot.push(platesSeconds)
        }
        for (let plate of this.desserts){
            let platesDesserts=String(plate.name_dish)
            platesTot.push(platesDesserts)
        }
        for (let dish of platesTot){
            if (dish===''){
                countEmpties+=1
            }
        }
        if (countEmpties===0){
            return true}
        else{return false}
    }, 

    async onSaveClicked(){
       if (this.areValidInputsFromMenu()===true){ 
            let desc=this.dict_plates.desc
            this.dictToSend={'date':this.dateReceived,'desc':desc, 'id':this.dict_plates.id, 'id_restaurant':localStorage.id_restaurant}
            const settings={
            method:"PUT",
            body: JSON.stringify(this.dictToSend),
            headers:{
                Authorization: localStorage.id_restaurant,
                'Content-Type':'application/json'
                }
            }
            var response = await fetch(`${config.API_PATH}/menus`,settings)
            if (response.status===200){
            alert('Menu modificado con éxito!')
            this.$router.push("/menus")
            }
        }
        else{
            this.areThereEmpties=false
        }
    },
    }
}


</script>
<style scoped>
body{
    padding:0;
    margin:0;
}

.date{
    display:flex;
    justify-content: flex-end;
}
.firsts,
.seconds,
.desserts{
    display:grid;
    grid-template-columns:1fr 3fr;
    padding: 0.2em
}
.input_plate{
    margin-right:0.1em;
}
p{
    text-align:left
}
button{
    margin-top:1em
}
.dateNameRestaurant{
  display: flex;
  justify-content: space-between;
}
.empty{
    border-color:solid 1px red;
}
</style>