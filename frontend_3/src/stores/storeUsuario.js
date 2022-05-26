import { deleteCookie } from '../assets/helpers.js'
import axios from 'axios'


const storeUsuario = {
    state() {
        return {
            usuario: JSON.parse(localStorage.getItem('user')) || { username: null, password: null },
            tokenazo: localStorage.getItem('tokenazo') || null,
            errores: {
                formLogin: null
            },
        }
    },
    getters: {
        estaLogueado(state, _) {
            return state.tokenazo !== null
        }
    },
    mutations: {
        funcionMutadora(state, payload) {
            console.log("funcion mutadora")
            console.log(state)
            console.log(payload)
        },

        logout(state) {
            const opcionesRequestLogout = {
                method: "POST",
                headers: { 'Content-Type': 'application/json'},
                body: JSON.stringify({ tokenazo: state.tokenazo })
            };
            fetch('http://127.0.0.1:8000/api/logout/',opcionesRequestLogout)
            .then((response) => {
                if (response.ok) {
                    console.log("response ok desde vuex"); return response.json();
                } else {
                    console.log("response error desde vuex"); return response.text().then((text) => { throw new Error(text); });
                }
            }).then((responseJson) => {
                    console.log("LOGOUT EXITOSO")
                    state.usuario = { username: null, password: null };
                    state.tokenazo = null;
                    localStorage.removeItem('user');
                    localStorage.removeItem('tokenazo');
                })
                .catch(err => {
                    console.log(err)
                })
        },

        login(state, payload) {
            // fetch("http://127.0.0.1:8000/api/v1/dj-rest-auth/login/", {
            fetch("http://127.0.0.1:8000/api/login/", {

                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(payload),
            })
                .then((response) => {
                    if (response.ok) {
                        return response.json();
                    } else {
                        //ya se q devuelve un json si hay error:
                        return response.json().then((jsonDevuelto) => { 
                            throw jsonDevuelto; 
                        });
                    }
                })
                .then((responseJson) => {
                    console.log(responseJson)
                    state.usuario = payload
                    state.usuario.id = responseJson.id
                    state.tokenazo = responseJson.token;
                    state.errores.formLogin = '';
                    localStorage.setItem('user', JSON.stringify(state.usuario))
                    localStorage.setItem('tokenazo', state.tokenazo)
                })
                .catch((error) => {
                    console.log(error)
                    state.errores.formLogin = error.error;
                });
        }

    },

}


export default storeUsuario;