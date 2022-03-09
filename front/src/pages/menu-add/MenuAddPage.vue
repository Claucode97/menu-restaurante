<template>
  <form action="">
    <p>{{ loggedRestaurant }}</p>
    <div class="date">
      <input type="date" name="date" id="date" v-model="date" />
    </div>
    <section class="plates_info">
      <label for="first-dish">Primeros</label>
      <button class="btn">+</button>
      <input
        id="first-dish"
        class="input_plate"
        type="text"
        placeholder="Introducir plato"
        v-model="dict_plates.firsts[0].name_dish"
      />
      <fieldset>
        <legend>Alérgenos</legend>
        <label for="lactose">Lactosa</label>
        <input id="lactose" type="checkbox" value="lactose" />
        <label for="gluten">Gluten</label>
        <input id="gluten" type="checkbox" value="gluten" />
        <label for="egg">Huevo</label>
        <input id="egg" type="checkbox" value="egg" />
        <label for="seafood">Marisco</label>
        <input id="seafood" type="checkbox" value="seafood" />
        <label for="soy">Soja</label>
        <input id="soy" type="checkbox" value="soy" />
        <label for="nuts">Frutos de cascara</label>
        <input id="nuts" type="checkbox" value="nuts" />
      </fieldset>

      <label for="second-dish">Segundos</label>
      <button class="btn">+</button>
      <input
        id="second-dish"
        class="input_plate"
        type="text"
        placeholder="Introducir plato"
        v-model="dict_plates.seconds[0].name_dish"
      />
      <fieldset>
        <legend>Alérgenos</legend>
        <label for="lactose">Lactosa</label>
        <input id="lactose" type="checkbox" value="lactose" />
        <label for="gluten">Gluten</label>
        <input id="gluten" type="checkbox" value="gluten" />
        <label for="egg">Huevo</label>
        <input id="egg" type="checkbox" value="egg" />
        <label for="seafood">Marisco</label>
        <input id="seafood" type="checkbox" value="seafood" />
        <label for="soy">Soja</label>
        <input id="soy" type="checkbox" value="soy" />
        <label for="nuts">Frutos de cascara</label>
        <input id="nuts" type="checkbox" value="nuts" />
      </fieldset>

      <label for="dessert-dish">Postres</label>
      <button class="btn">+</button>
      <input
        id="dessert-dish"
        type="text"
        placeholder="Introducir plato"
        v-model="dict_plates.desserts[0].name_dish"
      />
      <fieldset>
        <legend>Alérgenos</legend>
        <label for="lactose">Lactosa</label>
        <input id="lactose" type="checkbox" value="lactose" />
        <label for="gluten">Gluten</label>
        <input id="gluten" type="checkbox" value="gluten" />
        <label for="egg">Huevo</label>
        <input id="egg" type="checkbox" value="egg" />
        <label for="seafood">Marisco</label>
        <input id="seafood" type="checkbox" value="seafood" />
        <label for="soy">Soja</label>
        <input id="soy" type="checkbox" value="soy" />
        <label for="nuts">Frutos de cascara</label>
        <input id="nuts" type="checkbox" value="nuts" />
      </fieldset>
    </section>
    <button @click.prevent="onSaveClicked">Agregar Menú</button>
  </form>
  <!-- {{$data}} -->
</template>

<script>
import config from "@/config.js";
import { v4 as uuidv4 } from "uuid";
export default {
  name: "MenuAdd",
  data() {
    return {
      date: "",
      dict_plates: {
        firsts: [
          { name_dish: "", desc_dish: "", id_dish: "01" },
          { name_dish: "", desc_dish: "", id_dish: "02" },
          { name_dish: "", desc_dish: "", id_dish: "03" },
        ],
        seconds: [
          { name_dish: "", desc_dish: "", id_dish: "04" },
          { name_dish: "", desc_dish: "", id_dish: "05" },
          { name_dish: "", desc_dish: "", id_dish: "06" },
        ],
        desserts: [
          { name_dish: "", desc_dish: "", id_dish: "07" },
          { name_dish: "", desc_dish: "", id_dish: "08" },
          { name_dish: "", desc_dish: "", id_dish: "09" },
          { name_dish: "", desc_dish: "", id_dish: "10" },
        ],
      },
      loggedRestaurant: localStorage.name,
    };
  },

  mounted() {},
  computed: {},
  methods: {
    areValidInputsFromMenu() {
      if (
        this.dict_plates.firsts[0].name_dish === "" ||
        this.dict_plates.firsts[0].desc_dish === "" ||
        this.dict_plates.firsts[1].name_dish === "" ||
        this.dict_plates.firsts[1].desc_dish === "" ||
        this.dict_plates.firsts[2].name_dish === "" ||
        this.dict_plates.firsts[2].desc_dish === "" ||
        this.dict_plates.seconds[0].name_dish === "" ||
        this.dict_plates.seconds[0].desc_dish === "" ||
        this.dict_plates.seconds[1].name_dish === "" ||
        this.dict_plates.seconds[1].desc_dish === "" ||
        this.dict_plates.seconds[2].name_dish === "" ||
        this.dict_plates.seconds[2].desc_dish === "" ||
        this.dict_plates.desserts[0].name_dish === "" ||
        this.dict_plates.desserts[0].desc_dish === "" ||
        this.dict_plates.desserts[1].name_dish === "" ||
        this.dict_plates.desserts[1].desc_dish === "" ||
        this.dict_plates.desserts[2].name_dish === "" ||
        this.dict_plates.desserts[2].desc_dish === "" ||
        this.dict_plates.desserts[3].name_dish === "" ||
        this.dict_plates.desserts[3].desc_dish === ""
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