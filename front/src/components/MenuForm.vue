<template>
   <section>
   <div class="wrappedNameDish">
        <p>Primeros</p> 
        <button class="addDish" @click.prevent="addNewDish(dict_plates.firsts)">Añadir plato</button>
    </div>
    <div class="firsts" v-for="dish in dict_plates.firsts" :key="dish.id_dish">
        <input @keyup="onMenuChanges" class="input_plate" type="text"  v-model="dish.name_dish">
        <button @click.prevent="deleteDish(dish,dict_plates.firsts)" class="delete-button"> x </button>
        <div class="allergens-wrapped">
            <label for="lactose">Lactosa</label>
            <input @change="onMenuChanges" id="lactose" type="checkbox" value="lactose" v-model="dish.allergens"/>
            <label for="gluten">Gluten</label>
            <input @change="onMenuChanges" id="gluten" type="checkbox" value="gluten" v-model="dish.allergens"/>
            <label for="egg">Huevo</label>
            <input @change="onMenuChanges" id="egg" type="checkbox" value="egg" v-model="dish.allergens" />
            <label for="seafood">Marisco</label>
            <input @change="onMenuChanges" id="seafood" type="checkbox" value="seafood" v-model="dish.allergens"/>
            <label for="soy">Soja</label>
            <input @change="onMenuChanges" id="soy" type="checkbox" value="soy" v-model="dish.allergens" />
            <label for="nuts">Frutos de cascara</label>
            <input @change="onMenuChanges" id="nuts" type="checkbox" value="nuts" v-model="dish.allergens"/>
        </div>
        
    </div>
    <div class="wrappedNameDish"><p>Segundos</p> <button class="addDish" @click.prevent="addNewDish(dict_plates.seconds)">Añadir plato</button></div>
    <div class="seconds" v-for="dish in dict_plates.seconds" :key="dish.id_dish">
        <input @keyup="onMenuChanges" class="input_plate" type="text"  v-model="dish.name_dish">
        <button @click.prevent="deleteDish(dish,dict_plates.seconds)" class="delete-button"> x </button>

        <div class="allergens-wrapped">
            <label for="lactose">Lactosa</label>
            <input @change="onMenuChanges" id="lactose" type="checkbox" value="lactose" v-model="dish.allergens"/>
            <label for="gluten">Gluten</label>
            <input @change="onMenuChanges" id="gluten" type="checkbox" value="gluten" v-model="dish.allergens"/>
            <label for="egg">Huevo</label>
            <input @change="onMenuChanges" id="egg" type="checkbox" value="egg" v-model="dish.allergens" />
            <label for="seafood">Marisco</label>
            <input  @change="onMenuChanges" id="seafood" type="checkbox" value="seafood" v-model="dish.allergens"/>
            <label for="soy">Soja</label>
            <input @change="onMenuChanges"  id="soy" type="checkbox" value="soy" v-model="dish.allergens" />
            <label for="nuts">Frutos de cascara</label>
            <input @change="onMenuChanges" id="nuts" type="checkbox" value="nuts" v-model="dish.allergens"/>
        </div>
    </div>
    <div class="wrappedNameDish">
        <p>Postres</p> 
        <button class="addDish" @click.prevent="addNewDish(dict_plates.desserts)">Añadir plato</button></div>  
    <div class="desserts" v-for="dish in dict_plates.desserts" :key="dish.id_dish">
        <input @keyup="onMenuChanges" class="input_plate" type="text"  v-model="dish.name_dish">
        <button @click.prevent="deleteDish(dish,dict_plates.desserts)" class="delete-button"> x </button>
        <div class="allergens-wrapped">
            <label for="lactose">Lactosa</label>
            <input @change="onMenuChanges" id="lactose" type="checkbox" value="lactose" v-model="dish.allergens"/>
            <label for="gluten">Gluten</label>
            <input @change="onMenuChanges" id="gluten" type="checkbox" value="gluten" v-model="dish.allergens"/>
            <label for="egg">Huevo</label>
            <input @change="onMenuChanges"   id="egg" type="checkbox" value="egg" v-model="dish.allergens" />
            <label for="seafood">Marisco</label>
            <input  @change="onMenuChanges" id="seafood" type="checkbox" value="seafood" v-model="dish.allergens"/>
            <label for="soy">Soja</label>
            <input @change="onMenuChanges" id="soy" type="checkbox" value="soy" v-model="dish.allergens" />
            <label for="nuts">Frutos de cascara</label>
            <input @change="onMenuChanges" id="nuts" type="checkbox" value="nuts" v-model="dish.allergens"/>
        </div>
        
    </div>
    </section>
</template>

<script>
export default {
    props:{
        dictMenu:{
            type: Object,
            required: true,
        }
    },
    emits:["changed"],
    watch:{
        dictMenu: {
            handler(newValue){
                let menuAsJson = JSON.stringify(newValue)
                this.dict_plates = JSON.parse(menuAsJson)

            },
            inmediate: true
        }
    },
    data(){
        return{
            dict_plates:{firsts: [],seconds: [],desserts: [],},

        }
    },

    methods:{
    onMenuChanges(){
        this.$emit("changed",this.dict_plates)
    },

    addNewDish(typeOfDish){
        typeOfDish.push({name_dish:"", allergens:[]})
        this.$emit("changed",this.dict_plates)
    },

    deleteDish(dish,menu){
      let indice = menu.indexOf(dish)
      menu.splice(indice,1)
      this.$emit("changed",this.dict_plates)
    },


    
    },
}
</script>

<style scoped>
*{
    padding:0;
    margin:0;
}
.input_plate{
    margin:0.4em 0;
    width:92%;
    margin-right: 0.3em;
}
.delete-button{
    width: 20px;
    height: 20px;
}
.wrappedNameDish{
    margin-top: 2em;
    margin-bottom: 1em
}
.wrappedNameDish p{
    margin-bottom: 0.5em;
}
.wrappedNameDish .addDish{
    padding:0.2em;
    display:block;
}
.allergens-wrapped label{
    margin-right:0.3em;
    font-size: 0.8em;
}
.allergens-wrapped input{
    margin-right:1em;
    
}
p{
    text-align: left;
    margin-left: 1em;
}
.addDish{
    margin-left: 1em;
}




.date{
    display:flex;
    justify-content: flex-end;
}
</style>