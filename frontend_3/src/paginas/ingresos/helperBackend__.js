const callbackExitoso = (responseJson) => {
    objVue.$data.rdoPost = "POST EXITOSO!";
    objVue.$data.errores = "";
    console.log(responseJson);
};

const callbackErroroso = (error) => {
    objVue.$data.rdoPost = "ERROR EN EL POST";
    objVue.$data.errores = JSON.parse(error.message); //mensaje propio del backend
};

const httpBackend = (objVue, url, cuerpo, metodo, callbackOk, callbackError) => {
    console.log(objVue)
    console.log(url)
    console.log(cuerpo)
    console.log(metodo)
    callbackOk()
    // console.log(callbackError)
}

export default httpBackend;