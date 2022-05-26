const httpBackend = ( url, cuerpo, metodo, callbackOk, callbackError, objVue) => {
    // if(callbackazo){callbackazo()}
    const bodyRequest = {
        method: metodo,
        headers: {
            //   "X-CSRFToken": csrftoken,
            "Content-Type": "application/json",
        },
        body: JSON.stringify(cuerpo),
    };
    console.log(url);
    console.log(bodyRequest);
    fetch(url, bodyRequest)
        .then(response => {
            if (response.ok) {
                console.log('response ok')
                return response.json();
            } else {
                console.log('response error')
                return response.text().then((text) => { throw new Error(text)});
            }
        })
        .then( responseJson => {
            callbackOk(responseJson)
          })
          .catch((error) => {
            callbackError(error)           
          })
          .finally(() => objVue.$emit('renderizar-lista'))
}

export default httpBackend;