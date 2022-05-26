<template>
  <div>
    {{ rdoPost }}
    {{ errores }}

    <form>
      <br />
      <div class="form-group">
        <label for="nombre">NOMBRE</label>
        <input
          type="text"
          class="form-control"
          id="nombre"
          placeholder="nombre"
          v-model="registroUpdateLocal.nombre"
        />
      </div>
      <hr />
      <div class="form-check form-check-inline">
        <input
          class="form-check-input"
          type="radio"
          name="tipo_cuenta"
          id="inlineRadio1"
          value="INGRESOS"
          v-model="registroUpdateLocal.tipo_cuenta"
        />
        <label class="form-check-label" for="inlineRadio1">INGRESOS</label>
      </div>

      <div class="form-check form-check-inline">
        <input
          class="form-check-input"
          type="radio"
          name="tipo_cuenta"
          id="inlineRadio2"
          value="GASTOS"
          v-model="registroUpdateLocal.tipo_cuenta"
        />
        <label class="form-check-label" for="inlineRadio2">GASTOS</label>
      </div>
      <div class="form-check form-check-inline">
        <input
          class="form-check-input"
          type="radio"
          name="tipo_cuenta"
          id="inlineRadio3"
          value="AMBOS"
          v-model="registroUpdateLocal.tipo_cuenta"
        />
        <label class="form-check-label" for="inlineRadio3">AMBOS</label>
      </div>
      <hr />
      <div class="form-check">
        <input
          type="checkbox"
          class="form-check-input"
          id="permite_cuotas"
          v-model="registroUpdateLocal.permite_cuotas"
        />
        <label class="form-check-label" for="permite_cuotas"
          >Permite Cuotas</label
        >
      </div>
      <button
        class="w-100 btn btn-primary"
        v-if="regUpdate == null"
        @click.prevent="postData"
      >
        NUEVA
      </button>
      <span v-else>
        <button class="w-100 btn btn-success" @click.prevent="putData">
          UPDATE
        </button>
        <br />
        <button class="w-100 btn btn-danger" @click.prevent="deleteData">
          DELETE
        </button>
      </span>
    </form>
  </div>
</template>

<script>
import axios from "axios";


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
      registroUpdateLocal: this.$props.regUpdate || {
        nombre: "",
        tipo_cuenta: "AMBOS",
        permite_cuotas: false,
      },
    };
  },
  watch: {
    regUpdate: function (valorNuevo) {
      this.registroUpdateLocal = valorNuevo || {
        nombre: null,
        tipo_cuenta: null,
        permite_cuotas: null,
      };
    },
  },
  methods: {
    deleteData() {
      const url = `http://127.0.0.1:8000/api/cuentas/${this.registroUpdateLocal.id}/`;

      fetch(url, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Token " + this.$store.state.storeUsuario.tokenazo,
        },
      })
        .then((response) => {
          if (response.ok) {
            console.log("response ok");
          } else {
            console.log("response error");
            // 
            // return response.text().then((text) => {
            //   throw new Error(text);
            // });
            //ya se q es un json, y no necesito el new Error
            return response.json().then(jsonError => {throw jsonError})
            
          }
        })
        .then(() => {
          this.rdoPost = "DELETE EXITOSO!";
          this.errores = "";
        })
        .catch((error) => {
          console.log(error);
          this.rdoPost = "ERROR EN EL DELETE ";
        })
        .finally(() => this.$emit("renderizar-lista"));
    },
    // postData() {
    //   const url = "http://127.0.0.1:8000/api/cuentas/";
    //   const cuerpo = this.registroUpdateLocal;
    //   const metodo = "POST";
    //   const callbackExito = (responseJson) => {
    //     this.$data.rdoPost = "POST EXITOSO!";
    //     this.$data.errores = "";
    //     console.log(responseJson);
    //   };
    //   const callbackError = (error) => {
    //     this.$data.rdoPost = "ERROR EN EL POST";
    //     this.$data.errores = JSON.parse(error.message); //mensaje propio del backend
    //   };
    postData() {
      const url = "http://127.0.0.1:8000/api/cuentas/";
      const cuerpo = this.registroUpdateLocal;
      axios
        .post(url, cuerpo, {
          headers: {
            "Content-Type": "application/json",
            Authorization: "Token " + this.$store.state.storeUsuario.tokenazo,
          },
        })
        .then((responseJson) => {
          this.rdoPost = "POST EXITOSO!";
          this.errores = "";
          console.log(responseJson);
        })
        .catch((error) => {
          
          console.log(error.response.data)
          this.errores = error.response.data; //mensaje propio del backend
        })
        .finally(() => this.$emit("renderizar-lista"));
    },
    putData() {
      const objUpdate = Object.assign({}, this.registroUpdateLocal);
      delete objUpdate.id;

      const url = `http://127.0.0.1:8000/api/cuentas/${this.registroUpdateLocal.id}/`;
      const metodo = "PUT";
      const callbackExito = (responseJson) => {
        this.$data.rdoPost = "PUT EXITOSO!";
        this.$data.errores = "";
        console.log(responseJson);
      };
      const callbackError = (error) => {
        this.$data.rdoPost = "ERROR EN EL PUT";
        this.$data.errores = JSON.parse(error.message); //mensaje propio del backend
      };
      // httpBackend(url, objUpdate, metodo, callbackExito, callbackError, this);
      axios
        .put(url, objUpdate, {
          headers: {
            "Content-Type": "application/json",
            Authorization: "Token " + this.$store.state.storeUsuario.tokenazo,
          },
        })
        .then((responseJson) => {
          this.$data.rdoPost = "PUT EXITOSO!";
          this.$data.errores = "";
          console.log(responseJson);
        })
        .catch((error) => {
          this.$data.rdoPost = "ERROR EN EL PUT";
          this.$data.errores = JSON.parse(error.message); //mensaje propio del backend
        })
        .finally(() => this.$emit("renderizar-lista"));
    },
  },
};
</script>