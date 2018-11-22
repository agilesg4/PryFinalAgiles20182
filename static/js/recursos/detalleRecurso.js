$(document).ready(function() {
    getRecurso();
});

// HTTP
function getRecurso() {
    let id = getId();
    console.log(id);
    $.getJSON('/polls/api/recursos/' + id).done(function (data) {
        setModalInfo(data);
    });
}

function getId() {
    var url = window.location + "";
    if(url[url.length-1] === "/") {
        url = url.substring(0, url.length - 1);
    }
    let parts = url.split("/");
    let id = parts[parts.length-1];
    return id;
}

function setModalInfo(recurso) {
    recurso_id = recurso.id_recurso;
    $("#recurso_titulo").val(recurso.titulo);
    $("#recurso_descripcion").val(recurso.descripcion);
    $("#recurso_tipo").val(recurso.tipo.nombre);
    $("#recurso_ubicacion").val(recurso.ubicacion);
}