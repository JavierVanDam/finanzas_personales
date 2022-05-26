import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import { createStore } from 'vuex'

import App from './App.vue'


// import 'bootstrap/dist/css/bootstrap.min.css'
// import 'bootstrap/dist/css/bootstrap.min.css'
// import 'jquery/src/jquery.js'
// import 'bootstrap/dist/js/bootstrap.js'
// import 'popper.js/dist/popper.js'





import AppCuentas from './paginas/cuentas/AppCuentas.vue'
import AppIngresos from './paginas/ingresos/AppIngresos.vue'
import AppUsuario from './paginas/usuario/AppUsuario.vue'
import MainGastos from './paginas/gastos/MainGastos.vue'  
import DetalleIngreso from './paginas/ingresos/DetalleIngreso.vue'
import DetalleGasto from './paginas/gastos/DetalleGasto.vue'




import storeUsuario from './stores/storeUsuario.js'


const routes = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: AppUsuario },
    { path: '/login', component: AppUsuario },
    { path: '/cuentas', component: AppCuentas },
    { path: '/ingresos', component: AppIngresos },
    { path: '/ingresos/:idIngreso', component: DetalleIngreso },
    { path: '/gastos', component: MainGastos },
   
  ]
})

const store = createStore({
  modules: { 
    storeUsuario: storeUsuario 
  },
  // plugins: [vuexLocal.plugin]
  
})


const app = createApp(App)
app.use(store)
app.use(routes)

app.mount("#app")