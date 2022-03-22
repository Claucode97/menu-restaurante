<template>
  <div id="add-menu-container">
    <pre>{{$data}}</pre>
    <form action="">
      <h2>{{ loggedRestaurant }}</h2>
      <div class="date">
        <p>{{this.date}}</p>
      </div>
      <section class="plates_info">
        <select
          name="category-dishes"
          id="category-dishes"
          v-model="categoryDishes"
        >
          <option :value="null" disabled>Elige tipo de plato</option>
          <option value="firsts">Primeros</option>
          <option value="seconds">Segundos</option>
          <option value="desserts">Postres</option>
        </select>
        <input
          id="name-dish"
          type="text"
          placeholder="Introducir plato"
          v-model="nameDish"
        />
        <fieldset class="allergens-box">
          <legend>Alérgenos</legend>
          <label for="lactose">Lactosa</label>
          <input
            id="lactose"
            type="checkbox"
            value="lactose"
            v-model="this.allergens"
          />
          <label for="gluten">Gluten</label>
          <input
            id="gluten"
            type="checkbox"
            value="gluten"
            v-model="this.allergens"
          />
          <label for="egg">Huevo</label>
          <input id="egg" type="checkbox" value="egg" v-model="this.allergens" />
          <label for="seafood">Marisco</label>
          <input
            id="seafood"
            type="checkbox"
            value="seafood"
            v-model="this.allergens"
          />
          <label for="soy">Soja</label>
          <input id="soy" type="checkbox" value="soy" v-model="this.allergens" />
          <label for="nuts">Frutos de cascara</label>
          <input
            id="nuts"
            type="checkbox"
            value="nuts"
            v-model="this.allergens"
          />
        </fieldset>
      </section>
      <button @click.prevent="buttonAddDish()" class="btn">Guardar Plato</button>
    </form>
    
    <section class="menu-container">
      <h3>Primeros:</h3>
      <dl v-for="dish of this.dict_plates.firsts" :key="dish.id">
        <dt>{{ dish.name_dish }}</dt>
        <dd v-for="allergen of dish.allergens" :key="allergen.id">
          {{ allergen }}
        </dd>
        <button @click="deleteDishFrists(dish)" class="btn btn-delete-dish"> - </button>
      </dl>
      <h3>Segundos:</h3>
      <dl v-for="dish of this.dict_plates.seconds" :key="dish.id">
        <dt>{{ dish.name_dish }}</dt>
        <dd v-for="allergen of dish.allergens" :key="allergen.id">
          {{ allergen }}
        </dd>
        <button @click="deleteDishSeconds(dish)" class="btn btn-delete-dish"> - </button>
      </dl>
      <h3>Postres:</h3>
      <dl v-for="dish of this.dict_plates.desserts" :key="dish.id">
        <dt>{{ dish.name_dish }}</dt>
        <dd v-for="allergen of dish.allergens" :key="allergen.id">
          {{ allergen }}
        </dd>
        <button @click="deleteDishDesserts(dish)" class="btn btn-delete-dish"> - </button>
      </dl>
    </section>
    <button @click.prevent="onSaveClicked" class="btn">Agregar Menú</button>
  </div>
</template>

<script>
import config from "@/config.js";
import { v4 as uuidv4 } from "uuid";
export default {
  name: "MenuAdd",
  data() {
    return {
      date: this.$route.params.date,
      categoryDishes: null,
      nameDish: "",
      allergens: [],
      dict_plates: {
        firsts: [],
        seconds: [],
        desserts: [],
      },
      loggedRestaurant: localStorage.name,
    };
  },

  methods: {
    deleteDishFrists(dish){
      let indice = this.dict_plates.firsts.indexOf(dish)
      this.dict_plates.firsts.splice(indice,1)
    },
    deleteDishSeconds(dish){
      let indice = this.dict_plates.seconds.indexOf(dish)
      this.dict_plates.seconds.splice(indice,1)
    },
    deleteDishDesserts(dish){
      let indice = this.dict_plates.desserts.indexOf(dish)
      this.dict_plates.desserts.splice(indice,1)
    },
    buttonAddDish() {
      if (this.categoryDishes === "firsts" && this.nameDish != "") {
            let dictOfCategory = {
            name_dish: this.nameDish,
            allergens: this.allergens,
            id: uuidv4(),
            };
            this.dict_plates["firsts"].push(dictOfCategory);
            this.nameDish = "";
            this.allergens = [];
        }
      else if (this.categoryDishes === "seconds" && this.nameDish != "") {
        let dictOfCategory = {
        name_dish: this.nameDish,
        allergens: this.allergens,
        id: uuidv4(),
        };
        this.dict_plates["seconds"].push(dictOfCategory);
        this.nameDish = "";
        this.allergens = [];
        }
        
      else if (this.categoryDishes === "desserts" && this.nameDish != "") {
          let dictOfCategory = {
          name_dish: this.nameDish,
          allergens: this.allergens,
          id: uuidv4(),
          };
          this.dict_plates["desserts"].push(dictOfCategory);
          this.nameDish = "";
          this.allergens = [];
      }
      else{
          alert("Faltan datos por rellenar")
      }
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
        this.dictToSend = { date: this.date, desc: desc };
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