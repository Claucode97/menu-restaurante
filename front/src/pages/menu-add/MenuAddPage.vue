<template>
  <form action="">
    <p>{{ loggedRestaurant }}</p>
    <div class="date">
      <input type="date" name="date" id="date" v-model="date" />
    </div>

    <section class="plates_info">
      <select
        name="category-dishes"
        id="category-dishes"
        v-model="categoryDishes"
      >
        <option value="firsts">Primeros</option>
        <option value="seconds">Segundos</option>
        <option value="desserts">Postres</option>
      </select>

      <input
        id="first-dish"
        class="input_plate"
        type="text"
        placeholder="Introducir plato"
        v-model="nameDish"
      />

      <fieldset>
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

  <h3>Primeros:</h3>
  <dl v-for="dish of this.dict_plates.firsts" :key="dish.id">
    <dt>{{ dish.name_dish }}</dt>
    <dd v-for="allergen of dish.allergens" :key="allergen.id">
      {{ allergen }}
    </dd>
  </dl>
  <h3>Segundos:</h3>
  <dl v-for="dish of this.dict_plates.seconds" :key="dish.id">
    <dt>{{ dish.name_dish }}</dt>
    <dd v-for="allergen of dish.allergens" :key="allergen.id">
      {{ allergen }}
    </dd>
  </dl>
  <h3>Postres:</h3>
  <dl v-for="dish of this.dict_plates.desserts" :key="dish.id">
    <dt>{{ dish.name_dish }}</dt>
    <dd v-for="allergen of dish.allergens" :key="allergen.id">
      {{ allergen }}
    </dd>
  </dl>

  <button @click.prevent="onSaveClicked">Agregar Menú</button>
</template>

<script>
import config from "@/config.js";
import { v4 as uuidv4 } from "uuid";
export default {
  name: "MenuAdd",
  data() {
    return {
      date: "",
      categoryDishes: "",
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

  mounted() {},
  computed: {},
  methods: {
    buttonAddDish() {
      console.log("CLICK ADDBUTTON");
      if (this.categoryDishes === "firsts") {
        let dictOfCategory = {
          name_dish: this.nameDish,
          allergens: this.allergens,
          id: "01",
        };
        this.dict_plates["firsts"].push(dictOfCategory);
        this.nameDish = "";
        this.allergens = [];
      }
      if (this.categoryDishes === "seconds") {
        let dictOfCategory = {
          name_dish: this.nameDish,
          allergens: this.allergens,
          id: "01",
        };
        this.dict_plates["seconds"].push(dictOfCategory);
        this.nameDish = "";
        this.allergens = [];
      }
      if (this.categoryDishes === "desserts") {
        let dictOfCategory = {
          name_dish: this.nameDish,
          allergens: this.allergens,
          id: "01",
        };
        this.dict_plates["desserts"].push(dictOfCategory);
        this.nameDish = "";
        this.allergens = [];
      }
    },

    areValidInputsFromMenu() {
      if (
        this.dict_plates.firsts ||
        this.dict_plates.seconds ||
        this.dict_plates.desserts
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
body {
  padding: 0;
  margin: 0;
}

.date {
  display: flex;
  justify-content: flex-end;
}
.firsts,
.seconds,
.desserts {
  display: grid;
  grid-template-columns: 1fr 3fr;
  margin-top: 0.5em;
  padding: 0.2em;
}
.input_plate {
  margin-bottom: 0.3em;
  margin-right: 0.1em;
}
p {
  text-align: left;
}
button {
  margin-top: 1em;
}
</style>