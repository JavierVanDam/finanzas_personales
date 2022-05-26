<template>
  <form action="">
    {{ rdoHttp }}
    <form @submit.prevent="postNuevoGasto">
      <div class="form-group">
        <label for="fecha">fecha</label>
        <input
          type="date"
          class="form-control"
          id="fecha"
          placeholder="fecha"
          v-model="objForm.fecha"
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
          v-model="objForm.monto"
        />
      </div>

      <div class="form-group">
        <label for="monto">cuotas</label>
        <input
          type="number"
          class="form-control"
          id="cuotas"
          placeholder="cuotas"
          v-model="objForm.cuotas"
        />
      </div>
      <hr />

      <div class="form-group">
        <input
          type="file"
          class="form-control"
          id="comprobante"
          placeholder="comprobante"
          @change="adjuntoComprobante"
        />
      </div>

      <div class="form-group">
        <label for="categ_ingreso">forma_pago</label>
        <select
          class="form-control"
          id="categ_ingreso"
          v-model="objForm.forma_pago"
        >
          <option v-for="cu in formaPago" :key="cu.id" :value="cu.id">
            {{ cu.nombre }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label for="categ_ingreso">CATEG GASTO</label>
        <select
          class="form-control"
          id="categ_ingreso"
          v-model="objForm.categoria"
        >
          <option v-for="cg in categsGasto" :key="cg.id" :value="cg.id">
            {{ cg.nombre }}
          </option>
        </select>
      </div>

      <button type="submit" class="btn btn-danger">NUEVO GASTO</button>
    </form>

    comprobante
  </form>
</template>


<script>
import axios from "axios";
import {
  traeCuentasHelper,
  traeCategoriaGastosHelper,
} from "../../assets/helpers.js";

export default {
  data() {
    return {
      rdoHttp: 'chiche',
      categsGasto: [],
      formaPago: [],
      comprobante: null,
      objForm: {}
    };
  },
  props: {},
  methods: {
    postNuevoGasto() {
      this.objForm.usuario = this.$store.state.storeUsuario.usuario.id;
      axios.post("http://127.0.0.1:8000/api/gastos/", this.objForm,
        {
        headers: {
          "Content-Type": "application/json",
          Authorization: "Token " + this.$store.state.storeUsuario.tokenazo,
        }
      })
        .then((responseJson) => {
          this.rdoHttp = "POST EXITOSO!";

          const idNuevoGasto = responseJson.data.id;
          console.log(idNuevoGasto)
          if(this.comprobante){
             this.putComprobante(idNuevoGasto)
              .then(resp => console.log(resp))
              .catch(err => console.log(err))
          }else{
            console.log("SIN COMPROBANTE IMAGENES")
          }

          this.errores = "";
          this.objForm = {};

        })
        .catch((error) => {
          this.rdoHttp = "POST ERRORES!";
          console.log(error)
          this.errores = error; //mensaje propio del backend
        })
        .finally(() => this.$emit("renderizar-lista"));
      // console.log(JSON.stringify(this.objForm))

    },

    adjuntoComprobante(e) {
      console.log( e.target.files[0])
      this.comprobante = e.target.files[0];

    },
    putComprobante(id){
      let formData = new FormData();
      formData.append("file", this.comprobante);
      return axios.put(
        `http://127.0.0.1:8000/api/archivazo/comprobante_gasto/${id}/`,
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
            Authorization: "Token 9a488c8786e0cd95dc71de18319fe2f7b69a76ee",
          },
        }
      )   
      // .then(resp => console.log(resp))
      // .catch(err => console.log(err));

    }
  },
  mounted() {
    traeCategoriaGastosHelper(this.$store.state.storeUsuario.tokenazo).then(
      (resp) => (this.categsGasto = resp)
    );
    traeCuentasHelper(this.$store.state.storeUsuario.tokenazo).then(
      (resp) => (this.formaPago = resp)
    );
  },
};
</script>