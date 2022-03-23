<template>
  <div class="modal-wrapper">
      <div class="modal-inner-wrapper">
          <p>¿En qué fecha quieres copiar el menú?</p>
          <input type="date">
          <button>Copiar en esta fecha</button>
      </div>
  </div>
</template>

<script>
export default {
    
    name: "CopyCalendar",
    props: {
        title: {
            type: String,
            required: true
                        
        },
        
    },
    data() {
    
  },

}
</script>

<style>

*{
    
}
.modal-wrapper{
    width: 100vw;
    height: 100vh;
}


</style>