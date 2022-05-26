<template>
  <div class="container">
    <div v-if="$store.getters.estaLogueado" class="row">
      <div class="col-12 col-md-3">
        <FormIngresos :regUpdate="regUpdate" @renderizar-lista="keyListado++" />
      </div>
      <div class="col-12 col-md-9">
        <ListadoIngresos
          @registro-update="impresionRegistro"
          :key="keyListado"
        />
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
import FormIngresos from "./FormIngresos.vue";
import ListadoIngresos from "./ListadoIngresos.vue";

export default {
  data() {
    return {
      keyListado: 0,
      regUpdate: null,
    };
  },
  methods: {
    cambiaKeyListadoIngresos() {
      this.keyListado++;
    },
    impresionRegistro(evt) {
      this.regUpdate = evt;
    },
  },
  components: {
    FormIngresos,
    ListadoIngresos,
  },
};
</script>

<style>
</style>
