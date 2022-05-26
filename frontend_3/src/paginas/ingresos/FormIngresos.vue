<template>
  <div>
    {{ rdoPost }}
    {{ errores }}

    <form @submit.prevent="postIngreso">
      <div class="form-group">
        <label for="fecha">fecha</label>
        <input
          type="date"
          class="form-control"
          id="fecha"
          placeholder="fecha"
          v-model="objIngreso.fecha"
        />
      </div>
      <hr />
      <div class="form-group">
        <label for="monto">monto</label>
        <input
          type="number"
          class="form-control"
          id="monto"
          placeholder="monto"
          v-model="objIngreso.monto"
        />
      </div>
      <hr />
      <div class="form-group">
        <label for="categ_ingreso">CUENTA</label>
        <select
          class="form-control"
          id="categ_ingreso"
          v-model="objIngreso.cuenta"
        >
          <option v-for="cu in cuentas" :key="cu.id" :value="cu.id">
            {{ cu.nombre }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label for="categ_ingreso">CATEG INGRESO</label>
        <select
          class="form-control"
          id="categ_ingreso"
          v-model="objIngreso.categoria"
        >
          <option v-for="ci in categsIngreso" :key="ci.id" :value="ci.id">
            {{ ci.nombre }}
          </option>
        </select>
      </div>

      <button type="submit" class="btn btn-danger">NUEVO INGRESO</button>
    </form>
  </div>
</template>

<script>
import { getCookie, traeCategoriasHelper } from "../../assets/helpers.js";

export default {
  props: {
    regUpdate: {
      type: Object,
    },
  },
  data() {
    return {
      rdoPost: null,
      errores: null,
      objIngreso: {},
      cuentas: {},
      categsIngreso: {},
    };
  },
  methods: {
    postIngreso() {
      console.log(this.$store.state.storeUsuario);
      this.objIngreso.usuario = this.$store.state.storeUsuario.usuario.id;
      console.log(this.objIngreso);
      fetch("http://127.0.0.1:8000/api/ingresos/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Token " + this.$store.state.storeUsuario.tokenazo,
        },
        body: JSON.stringify(this.objIngreso),
      })
        .then((resp) => {
          return resp.json();
        })
        .then((resp) => {
          console.log(resp);
          this.objIngreso = {}; //para q se blanquee el form
        })
        .catch((error) => console.log(error))
        .finally(() => this.$emit("renderizar-lista"));
    },
  },
  mounted() {
    traeCategoriasHelper(this.$store.state.storeUsuario.tokenazo).then(
      (resp) => (this.cuentas = resp)
    );
    traeCategoriasHelper(this.$store.state.storeUsuario.tokenazo).then(
      (resp) => (this.categsIngreso = resp)
    );
  },
};
</script>

