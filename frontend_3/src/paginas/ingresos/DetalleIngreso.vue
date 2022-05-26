<template>
  <div>
    {{ objeto }}

    <div class="card">
      <div class="card-body"><br>{{ objeto.monto}}<br>{{ objeto.fecha}}</div>
    </div>
  </div>
</template>W


<script>
export default {
  props: {
    objetoProps: {
      type: Object,
    },
  },
  data() {
    return {
      objeto: {},
    };
  },
  beforeCreate() {
    if (true) {
      console.log(this.objetoProps);
      const paramIdIngreso = this.$route.params.idIngreso;
      fetch(`http://127.0.0.1:8000/api/ingresos/${paramIdIngreso}/`)
        .then((resp) => {
          return resp.json();
        })
        .then((resp) => (this.objeto = resp))
        .catch((error) => console.log(error));
    }
  },
};
</script>