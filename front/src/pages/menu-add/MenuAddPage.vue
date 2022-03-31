<template>
  <div id="add-menu-container">
      <h2>{{ loggedRestaurant }}</h2>
      <div class="date">
        <p>{{this.date}}</p>
      </div>
    <MenuForm :dictMenu="dict_plates" @changed="onMenuChanged"/>
    <button @click.prevent="onSaveClicked" class="btn">Agregar Menú</button>
  </div>
</template>

<script>
import config from "@/config.js";
import { v4 as uuidv4 } from "uuid";
import MenuForm from "@/components/MenuForm.vue" 
export default {
  name: "MenuAdd",
  components:{MenuForm},
  data() {
    return {
      date: this.$route.params.date,
      categoryDishes: null,
      nameDish: "",
      allergens: [],
      dict_plates: {
        firsts: [{name_dish:"", allergens:[]}],
        seconds: [{name_dish:"", allergens:[]}],
        desserts: [{name_dish:"", allergens:[]}],
      },
      loggedRestaurant: localStorage.name,
    };
  },

  methods: {
    onMenuChanged(newValue){
        this.dict_plates = newValue

    },
    
    areValidInputsFromMenu() {
      if (
        this.dict_plates.firsts.name_dish ||
        this.dict_plates.seconds.name_dish ||
        this.dict_plates.desserts.name_dish
      ) {
        return false;
      } else {
        return true;
      }
    },
    async onSaveClicked() {
      if (this.areValidInputsFromMenu() === true && this.date !== "") {
        let desc = this.dict_plates;
        this.dictToSend = { date: this.date, desc: desc,id_restaurant:localStorage.id_restaurant };
        this.dictToSend.id = uuidv4();
        const settings = {
          method: "POST",
          body: JSON.stringify(this.dictToSend),
          headers: {
            Authorization: localStorage.id_restaurant,
            "Content-Type": "application/json",
          },
        };
        var response = await fetch(`${config.API_PATH}/menus`, settings);

        if (response.status === 200) {
          alert("Menu agregado con éxito!");
          this.$router.push("/menus");
        }
      } else {
        if (this.date === "") {
          alert("Fecha vacía");
        }
        if (this.areValidInputsFromMenu() === false) {
          alert("Inputs vacíos!");
        }
      }
    },
  },
};
</script>
<style scoped>
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
h2{text-align: center;}
.date {
  display: flex;
  justify-content: flex-end;
}
form *{margin-bottom: 0.6em;}
.plates_info *{
  padding: 0.4em;
}

#add-menu-container {
  text-align: left;
}
#name-dish{width:100%}

.allergens-box {
  font-size: 0.8em;
  padding: 0 0.5em;
}
.allergens-box input {margin-right: 0.7em}
.allergens-box label {margin-right: 0.2em}

.btn {
  cursor:pointer;
  user-select: none;
  margin: 0 auto;
  display: block;
  padding: 0.5em;
}
.menu-container dt {
  font-weight: bold;
;}
.menu-container h3 {
  text-decoration: underline double;
  margin-bottom: 0.8em;
  }

.menu-container dd{
  display: inline;
  margin-right: 0.2em;
  font-size: 0.9em;
}

.menu-container dl{
  position: relative;
  margin-bottom: 0.6em;
}
.menu-container .btn{
  position: absolute;
  top: 50%;
  right: 5%;
  transform: translateY(-50%);
  padding: 0.1em 0.5em;
}
</style>