function setCookie(name, value, daysToLive) {
    // Encode value in order to escape semicolons, commas, and whitespace
    var cookie = name + "=" + encodeURIComponent(value);

    if (typeof daysToLive === "number") {
        /* Sets the max-age attribute so that the cookie expires
        after the specified number of days */
        cookie += "; max-age=" + (daysToLive * 24 * 60 * 60);

        document.cookie = cookie;
    }
}


function getCookie(name) {
    // Split cookie string and get all individual name=value pairs in an array
    var cookieArr = document.cookie.split(";");

    // Loop through the array elements
    for (var i = 0; i < cookieArr.length; i++) {
        var cookiePair = cookieArr[i].split("=");

        /* Removing whitespace at the beginning of the cookie name
        and compare it with the given string */
        if (name == cookiePair[0].trim()) {
            // Decode the cookie value and return
            return decodeURIComponent(cookiePair[1]);
        }
    }

    // Return null if not found
    return null;
}



function deleteCookie(name) {
    document.cookie = name + '=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}


function traeCuentas() {
    const token = getCookie("tokenazo");
    fetch("http://127.0.0.1:8000/api/cuentas/", {
        method: "GET",
        headers: {
            Authorization: "Token " + this.$store.state.storeUsuario.tokenazo,
        },
    })
        .then((resp) => {
            return resp.json();
        })
        .then((resp) => (this.cuentas = resp))
        .catch((error) => console.log(error))
        .finally(() => this.$emit("renderizar-lista"));
}


// function traeCategoriasHelper(token) {

//     return fetch("http://127.0.0.1:8000/api/categ_ingresos/", {
//         method: "GET",
//         headers: {
//             'Accept': 'application/json',
//             'Content-Type': 'application/json',
//             Authorization: "Token " + token,
//         },
//     })
//     .then((resp) => {
//         return resp.json();
//     })
//     .then((resp) => { return resp })
//     .catch((error) => { return error });
// }

async function traeCategoriasHelper(token) {
    try {
        const resp = await fetch("http://127.0.0.1:8000/api/categ_ingresos/", {
            method: "GET",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                Authorization: "Token " + token,
            },
        });
        const respJson = await resp.json();
        return respJson;
    } catch (error) {
        return error;
    }
}

async function traeCuentasHelper(token) {
    try {
        const resp = await fetch("http://127.0.0.1:8000/api/cuentas/", {
            method: "GET",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                Authorization: "Token " + token,
            },
        });
        const respJson = await resp.json();
        return respJson;
    } catch (error) {
        return error;
    }
}



async function traeCategoriaGastosHelper(token) {
    try {
        const resp = await fetch("http://127.0.0.1:8000/api/categ_gastos/", {
            method: "GET",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                Authorization: "Token " + token,
            },
        });
        const respJson = await resp.json();
        return respJson;
    } catch (error) {
        return error;
    }
}



export { getCookie, setCookie, deleteCookie, traeCategoriasHelper, traeCuentasHelper, traeCategoriaGastosHelper }