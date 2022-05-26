import fetch from "node-fetch";


fetch('http://127.0.0.1:8000/api/ingresos/', {
    method: "GET",
    headers: {
        //   "X-CSRFToken": csrftoken,
        "Content-Type": "application/json",
    },
    })
    .then(resp => console.log(resp.json()))
    .then(resp => console.log(resp))
    .catch(err => console.log(err))