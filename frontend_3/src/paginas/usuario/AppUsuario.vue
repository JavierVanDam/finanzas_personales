<template>
  <div class="container">
    <div class="row">
      <div class="col-8 offset-2">
        <div v-show="$store.state.storeUsuario.errores.formLogin" 
        class="alert alert-danger alert-dismissible fade show" 
        role="alert" >
          {{ $store.state.storeUsuario.errores.formLogin }}
          <button type="button" class="close" data-dismiss="alert" aria-label="Close" >
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <form @submit.prevent="loginLocal">
          <div class="form-group">
            <label for="username">Email address</label>
            <input
              type="text"
              class="form-control"
              id="username"
              v-model="objUsuario.username"
            />
          </div>
          <div class="form-group">
            <label for="pass">Password</label>
            <input
              type="password"
              class="form-control"
              id="pass"
              v-model="objUsuario.password"
            />
          </div>

          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { getCookie, setCookie } from "../../assets/helpers.js";

export default {
  data() {
    return {
      rdoLogin: null,
      erroresLogin: null,
      objUsuario: {},
    };
  },

  methods: {
    loginLocal() {
      this.$store.commit("login", this.objUsuario);
      console.log(this.$store.getters.estaLogueado);
    },
  },
};
</script>

<style>
</style>
