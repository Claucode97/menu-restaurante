<template>
  <div class="modal-wrapper" >
      <div class="modal-inner-wrapper">cace4155-1205-4cb6-819c-981c0d9bbd56
          {{this.$route.params.date}}
          <button class="close-btn" @click="copyModalClose">x</button>
          <p>¿En qué fecha quieres copiar el menú?</p>
          <input type="date" v-model="newDate">
    <router-link :to="{name: 'MenuModifyPage', params: {date:this.newDate}}">
          <button class="copy-btn" @click="sendDate">Copiar en esta fecha</button>
    </router-link>
      </div>
  </div>
</template>

<script>


export default {
    
    name: "CopyCalendar",
    
    data() {
    return {
      newDate: "",
      modalOpened: true,
      
    };
    },


    methods: {
    sendDate(){
      this.$emit("changedDate",this.newDate)

    },
    copyModalClose(){
      this.modalOpened = false
      this.$emit("modaltoFALSE" , this.modalOpened)
      console.log("clicc modal" + this.modalOpened)

    },


    
  },
  
}
</script>

<style scoped>

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
.modal-wrapper{
    width: 100vw;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: rgba(250, 246, 246, 0.37);
    position: absolute;
    top: 0;
    left:0;
    z-index: 999;

}
.modal-inner-wrapper{
    width:70%;
    height: 70%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    position: relative;
    background-color: rgba(224, 213, 213);
}

.modal-inner-wrapper p{
    font-size: 1.5em;
    margin-bottom: 2em;
}
.modal-inner-wrapper input{
    margin-bottom: 2em;
   
}

.modal-inner-wrapper .copy-btn{
    padding: 0.6em;
    font-size: 0.8em;
    cursor: pointer;
    user-select: none;
}

.close-btn {
    position: absolute;
    top: 1em;
    right: 1em;
    width: 25px;
    height: 25px;
    }

</style>