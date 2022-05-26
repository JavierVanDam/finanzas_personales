<template>
  <div class="container">
    <div v-if="$store.getters.estaLogueado" class="row">
        <div class="col-6">
          <FormCuentas :regUpdate="regUpdate" @renderizar-lista="keyListado++"/>
      </div>
      <div class="col-6">
          <ListadoCuentas @registro-update="impresionRegistro" :key="keyListado"/>
      </div>
    </div>
    <div v-else class="row">
        <p>NO ESTAS LOGUEADO. 
          <router-link to='/'>
              LOGUEATE
          </router-link>
        POR FAVOR
        </p>
    </div>
  </div>
</template>

<script>
import FormCuentas from './FormCuentas.vue'
import ListadoCuentas from './ListadoCuentas.vue'

export default {

  data(){
    return {
      keyListado: 0,
      regUpdate: null
    }
  },
  methods:{
    cambiaKeyListadoCuentas(){
      this.keyListado++
    },
    impresionRegistro(evt){
        this.regUpdate = evt;
    }
  },
  components: {
    FormCuentas,
    ListadoCuentas
  },
};
</script>

<style>


.lista-cotizaciones{
    border: solid 1px #003366;;
}


.fondo-mariva{
    background-color: #003366;;
    color: white;
    width: 100%;
}

.encabezado{
    background-color: #003366;;
    color: white;
    font-size: 24px;
    font-weight: bold;

}


.encabezado-azul{
    background-color: #003366;
    color: white;
    padding: 10px;
}


.input-datagrid{
    width: 100px;
    text-align: center;
}

th, td{
    text-align: center; 
    vertical-align: middle;
}
</style>
