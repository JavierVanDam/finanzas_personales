<template>
  <div class="container">
    <nav class="navbar navbar-expand-md navbar-light bg-light">
      <a class="navbar-brand" href="/">FINANZAS PERSONALES</a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNav"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <router-link class="nav-link" to="/"> Inicio </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/cuentas"> Cuentas </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/ingresos">
              Ingresos
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/gastos">
              Gastos
            </router-link>
          </li>
        </ul>
        <ul class="navbar-nav">
          <li v-show="$store.getters.estaLogueado" class="nav-item">
            <button class="btn btn-success" @click="otroMetodo">
              {{ this.$store.state.storeUsuario.usuario.username }}
            </button>
          </li>
          &nbsp;&nbsp;&nbsp;
          <li v-show="$store.getters.estaLogueado" class="nav-item">
            <button class="btn btn-warning" @click="otroMetodo">LOGOUT</button>
          </li>
          <li v-show="!$store.getters.estaLogueado" class="nav-item">
            <router-link class="nav-link" to="/login">LOGIN</router-link>
          </li>
        </ul>
      </div>
    </nav>

    <br />
    <br />

    <!-- <div class="row">
      <div class="col-12"> -->
        <router-view></router-view>
      <!-- </div>
    </div> -->
  </div>
</template>

<script>
import { deleteCookie } from "./assets/helpers.js";

export default {
  name: "App",
  data() {
    return {
      usuario: null,
      keyListado: 0,
      regUpdate: null,
    };
  },
  methods: {
    logautazo() {
      this.$store.commit("logout");
    },
    otroMetodo() {
      console.log("en otra cosa");
      this.$store.commit("logout");
    },
  },
};
</script>

<style>
.fragmento {
  display: inline;
}

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

.router-link-active {
  background-color: rgb(191, 161, 230);
  border-radius: 5px;
}
</style>

