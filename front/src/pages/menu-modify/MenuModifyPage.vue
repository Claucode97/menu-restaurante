<template>
<form >
  <div class="dateNameRestaurant">
    <p>{{loggedRestaurant}}</p>
    <p>{{dateParsed()}}</p>
  </div>

  <MenuForm :dictMenu="dict_plates" @changed="onMenuChanged"/>
  

    <button @click.prevent="onSaveClicked" class="add-menu-button">Modificar Menú</button>
</form>
{{$data}}
</template>
<script>
import config from "@/config.js"
import {getMenuModify} from "@/services/api.js"
import MenuForm from "@/components/MenuForm.vue"
export default {
  name: "modifymenu",
  components:{MenuForm},
  data() {
    return {
       dateReceived:this.$route.params.date,
       dict_plates:{},
       loggedRestaurant:localStorage.name,
       areThereEmpties:true,
       
    };
  },

    mounted() {
       this.loadData()
    },

   methods: {
    onMenuChanged(newValue){
        this.dict_plates = newValue

    },

    async loadData(){
      
      this.dict_plates = await getMenuModify();
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
        for (let plate of this.dict_plates.desc.firsts){
            let platesFirsts=String(plate.name_dish)
            platesTot.push(platesFirsts)
        }
        for (let plate of this.dict_plates.desc.seconds){
            let platesSeconds=String(plate.name_dish)
            platesTot.push(platesSeconds)
        }
        for (let plate of this.dict_plates.desc.desserts){
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
        else{return false, alert("Hay campos vacios")}
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
            this.$router.push("/menus/by-date/"+ this.dateReceived)
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
*{
    padding:0;
    margin:0;
}
.add-menu-button {
    padding: 0.5em;
    margin: 2em 0;
}

p{
    text-align:left
}
.dateNameRestaurant{
  display: flex;
  justify-content: space-between;
}



</style>