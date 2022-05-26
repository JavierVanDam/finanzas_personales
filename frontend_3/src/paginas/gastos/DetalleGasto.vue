<template>
  <div class="card text-center" style="width: 18rem">
    <img class="mx-auto" alt="..."  :src="objGasto.comprobante" style="width: 50%"/>
    <div class="card-body">
      <h5 class="card-title">ID {{ objGasto.id }} </h5>
      <p class="card-text">
       <ul>
         <li>$ {{ objGasto.monto }} </li>
         <li>Fh: {{ objGasto.fecha }} </li>
         <li>Cuotas: {{ objGasto.cuotas }} </li>
         <li> {{ objGasto.monto }} </li>
       </ul>
      </p>
      <a href="#" class="btn btn-primary">Go somewhere</a>
    </div>
  </div>
</template>

<script>
export default {
  props: {

    objGasto: {
      type: Object,
      default: {
        id: 4,
        fecha: "2022-05-12",
        monto: 1234.0,
        cuotas: 7,
        comprobante:
          "http://127.0.0.1:8000/media/comprobantes_gastos/IMG_20210909_223404783.jpg",
        categoria: 1,
        forma_pago: 1,
        usuario: 1,
      },
    },
  },
};
</script>