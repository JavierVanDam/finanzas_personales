<template>
  <table class="table text-center">
    <thead class="thead-dark">
      <tr>
        <th scope="col">id</th>
        <th scope="col">nombre</th>
        <th scope="col">tipo cuenta</th>
        <th scope="col">permite cuotas</th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="item in listado"
        :key="item.id"
        @click="clickRow(item.id)"
        :class="item.id === filaClickeada ? 'bg-secondary' : ''"
      >
        <td scope="row">{{ item.id }}</td>
        <td>{{ item.nombre }}</td>
        <td>{{ item.tipo_cuenta }}</td>
        <td>{{ item.permite_cuotas }}</td>
      </tr>
    </tbody>
  </table>
</template>


<script>
import { getCookie, setCookie } from "../../assets/helpers.js";


export default {
  data() {
    return {
      seleccionMultiple: false,
      listado: null,
      filaClickeada: null,
    };
  },
  methods: {
    clickRow(id) {
      if (id === this.filaClickeada) {
        //estoy "desmarcando" lo q habia selecccionado para update. vuelvo a  filaClickeada: null p q sea un create
        this.filaClickeada = null;
        this.$emit("registro-update", null); //p q app le diga a form q no habilite el update
      } else {
        this.filaClickeada = id;
        this.$emit(
          "registro-update",
          this.listado.filter((x) => x.id === this.filaClickeada)[0]
        );
      }
    },
  },
  mounted() {
    const token = this.$store.state.storeUsuario.tokenazo;
    console.log('Token + ' + token )
    const url = "http://127.0.0.1:8000/api/cuentas/";

    fetch(url, {
      method: "GET",
      headers: {
        Authorization: "Token " + token,
      },
    })
      .then((response) => {
        if (response.ok) {
          return response.json();
        } else {
          return response.text().then((text) => {
            throw new Error(text);
          });
        }
      })
      .then((responseJson) => {
        this.rdoPost = "POST EXITOSO!";
        this.listado = responseJson;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>

<style scoped>

table thead th {
    vertical-align: middle;
    border: 5px solid #72fd6d;
}

table td{
  width: 45px;
  padding: 0.25rem;
  border: 1px solid #dee2e6;
  vertical-align: middle;
}

</style>