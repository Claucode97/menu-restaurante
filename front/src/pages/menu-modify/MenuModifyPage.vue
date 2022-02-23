<template>
<form >
    <div class="date">
        <input type="date" v-model="date" name="date" id="date" @click="getMenuFromDate">
    </div>
    <!-- <button @click.prevent="getMenuFromDate">Cargar menu</button> -->
    <section class="plates_info"  >
        <p>Primeros</p>
        <div class="firsts">
            <input class="input_plate" type="text"  v-model="dict_plates.desc.firsts[0].name_dish">
            <input class="input_plate" type="text"  v-model="dict_plates.desc.firsts[0].desc_dish">
            <input class="input_plate" type="text"  v-model="dict_plates.desc.firsts[1].name_dish">
            <input class="input_plate" type="text"  v-model="dict_plates.desc.firsts[1].desc_dish">
            <input class="input_plate" type="text"  v-model="dict_plates.desc.firsts[2].name_dish">
            <input class="input_plate" type="text"  v-model="dict_plates.desc.firsts[2].desc_dish">
        </div>
        <p>Segundos</p>
        <div class="seconds">
            <input class="input_plate" type="text"  v-model="dict_plates.desc.seconds[0].name_dish">
            <input class="input_plate" type="text"  v-model="dict_plates.desc.seconds[0].desc_dish">
            <input class="input_plate" type="text"  v-model="dict_plates.desc.seconds[1].name_dish">
            <input class="input_plate" type="text"  v-model="dict_plates.desc.seconds[1].desc_dish">
            <input class="input_plate" type="text"  v-model="dict_plates.desc.seconds[2].name_dish">
            <input class="input_plate" type="text"  v-model="dict_plates.desc.seconds[2].desc_dish">
        </div>
        <p>Postres</p>
        <div class="desserts">
            <input class="input_plate" type="text"  v-model="dict_plates.desc.desserts[0].name_dish">
            <input class="input_plate" type="text"  v-model="dict_plates.desc.desserts[0].desc_dish">
            <input class="input_plate" type="text"  v-model="dict_plates.desc.desserts[1].name_dish">
            <input class="input_plate" type="text"  v-model="dict_plates.desc.desserts[1].desc_dish">
            <input class="input_plate" type="text"  v-model="dict_plates.desc.desserts[2].name_dish">
            <input class="input_plate" type="text"  v-model="dict_plates.desc.desserts[2].desc_dish">
            <input class="input_plate" type="text"  v-model="dict_plates.desc.desserts[3].name_dish">
            <input class="input_plate" type="text"  v-model="dict_plates.desc.desserts[3].desc_dish">
        </div>
    </section>
    <button @click.prevent="onSaveClicked">Modificar Menú</button>
</form>
    <!-- {{$data}} -->
</template>

<script>

export default {
  name: "modifymenu",
  data() {
    return {
       date:'',
       dateReceived:this.$route.params.date,
    //    idReceived:this.$route.params.id,
       dict_plates:{'desc':{'firsts':[{'name_dish':'','desc_dish':'', 'id_dish':'01'},
                              {'name_dish':'','desc_dish':'', 'id_dish':'02'},
                              {'name_dish':'','desc_dish':'', 'id_dish':'03'}],
                     'seconds':[{'name_dish':'','desc_dish':'','id_dish':'04'},
                              {'name_dish':'','desc_dish':'', 'id_dish':'05'},
                              {'name_dish':'','desc_dish':'','id_dish':'06'}],
                     'desserts':[{'name_dish':'','desc_dish':'','id_dish':'07'},
                              {'name_dish':'','desc_dish':'','id_dish':'08'},
                              {'name_dish':'','desc_dish':'','id_dish':'09'},
                              {'name_dish':'','desc_dish':'','id_dish':'10'}]          
                    }
                    }
    };
  },

  mounted() {
      console.log('date',this.dateReceived)
      this.loadData()
  },
  computed:{
  },
  methods: {
    async loadData(){
      const response = await fetch("http://localhost:5000/api/menus/by-date/" + this.dateReceived);
      this.dict_plates = await response.json();
    },
    
  },
};
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
    margin-top:0.5em;
    padding: 0.2em
}
.input_plate{
    margin-bottom:0.3em;
    margin-right:0.1em;
}
p{
    text-align:left
}
button{
    margin-top:1em
}
</style>