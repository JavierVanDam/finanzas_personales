<template>
  <div class="container">
    <div v-if="$store.getters.estaLogueado" class="row">
      <div class="col-12 col-md-3">
        <FormGastos />
      </div>
      <div class="col-12 col-md-9">
        <ListadoGastos />
      </div>
    </div>
    <div v-else class="row">
      <p>
        NO ESTAS LOGUEADO.
        <router-link to="/"> LOGUEATE </router-link>
        POR FAVOR
      </p>
    </div>
  </div>
</template>

<script>
import ListadoGastos from "./ListadoGastos.vue";
import FormGastos from "./FormGastos.vue";

export default {
  data() {
    return {
      keyListado: 0,
      regUpdate: null,
    };
  },
  methods: {},
  components: {
    ListadoGastos,
    FormGastos,
  },
};
</script>

<style>
.lista-cotizaciones {
  border: solid 1px #003366;
}

.fondo-mariva {
  background-color: #003366;
  color: white;
  width: 100%;
}

.encabezado {
  background-color: #003366;
  color: white;
  font-size: 24px;
  font-weight: bold;
}

.encabezado-azul {
  background-color: #003366;
  color: white;
  padding: 10px;
}

.input-datagrid {
  width: 100px;
  text-align: center;
}

th,
td {
  text-align: center;
  vertical-align: middle;
}
</style>
