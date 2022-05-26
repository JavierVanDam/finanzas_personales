<template>
  <table class="table text-center">
    <thead class="thead-dark">
      <tr>
        <th scope="col">id</th>

        <th scope="col">fecha</th>
        <th scope="col">monto pago</th>
        <th scope="col">cuotas</th>
        <th scope="col">comprobante</th>
        <th scope="col">usuario</th>
        <th scope="col">forma pago</th>
        <th scope="col">categoria</th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="item in listado"
        :key="item.id"
        @click="clickRow(item.id)"
        :class="item.id === filaClickeada ? 'bg-secondary' : ''"
      >
        <td>{{ item.id }}</td>
        <td>{{ item.fecha }}</td>
        <td>{{ item.monto }}</td>
        <td>{{ item.cuotas }}</td>

        <td>  <img :src="item.comprobante" alt="" style="width: 90px">  </td>
        <td>{{ item.usuario.username }}</td>
        <td>{{ item.forma_pago.nombre }}</td>
        <td>{{ item.categoria.nombre }}</td>
      </tr>

    </tbody>
  </table>
</template>


<script>
import { getCookie, setCookie } from "../../assets/helpers.js";
import axios from "axios";

export default {
  data() {
    return {
      seleccionMultiple: false,
      listado: null,
      filaClickeada: null,
    };
  },
  methods: {},

  mounted() {
    const token = this.$store.state.storeUsuario.tokenazo;
    console.log("Token + " + token);
    const url = "http://127.0.0.1:8000/api/gastos/";
    let config = {
      headers: { Authorization: "Token " + token },
    };

    axios
      .get(url, config)
      .then((resp) => (this.listado = resp.data))
      .catch((err) => console.log(err));
  },
};
</script>

