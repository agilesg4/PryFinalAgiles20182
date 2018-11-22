let ACCEPTED_IMAGE_EXTENSIONS = [".png", ".jpg", ".jpeg", ".gif"];

$(document).ready(function() {
    let id = getId();
    getRecurso(id);
    getRecursoArtefactos(id);
});

function setModalInfo(recurso) {
    recurso_id = recurso.id_recurso;
    $("#recurso_titulo").val(recurso.titulo);
    $("#recurso_descripcion").val(recurso.descripcion);
    $("#recurso_tipo").val(recurso.tipo.nombre);
    $("#recurso_ubicacion").val(recurso.ubicacion);
}

function handleOnRecursoClick(artefacto) {
    if(!artefacto.archivo) return;

    let imageRelativePath = artefacto.archivo.trim();
    let parts = imageRelativePath.split("/");
    let imageName = parts[parts.length-1];
    window.open("/static/" + imageName);
}

// Helpers
function addArtefactos(artefactos) {
    for(var i = 0; i < artefactos.length; i++) {
       let current_artefacto = artefactos[i];
        let artefacto_column = getArtefacto(current_artefacto);
        $("#artefacto_list").append(artefacto_column);
    }
}

function getArtefacto(artefacto) {
    let artefacto_column = $("<div class='col-md-3'></div>");
    var artefacto_card = null;

    if(isArtefactoSelectable(artefacto)) {
       artefacto_card = $("<div class='artefacto_card artefacto_card_selectable'></div>")
        .click(function() {
            handleOnRecursoClick(artefacto);
        });
    } else {
        artefacto_card = $("<div class='artefacto_card'></div>")
    }

    let title = $("<div class='card_title'>" + artefacto.nombre_mostrar + "</div>")
    let description = $("<div class='card_description'>" + artefacto.descripcion + "</div>")

    let tipo_subtitle = $("<div class='card_subtitle'></div>");
    let tipo_subtitle_label = $("<span class='card_subtitle_label'>Tipo: </span>");
    let tipo_subtitle_ans = $("<span class='card_subtitle_ans'>" + artefacto.tipo_artefacto.nombre +"</span>");

    let date_string = artefacto.fecha_hora_carga;
    let date = new Date(date_string).toDateString();

    let actualizacion_subtitle = $("<div class='card_subtitle'></div>");
    let actualizacion_subtitle_label = $("<span class='card_subtitle_label'>Ultima Actualización:</br></span>");
    let actualizacion_subtitle_ans = $("<span class='card_subtitle_ans'>" + date +"</span>");

    let cargado_subtitle = $("<div class='card_subtitle'></div>");
    let cargado_subtitle_label = $("<span class='card_subtitle_label'>Cargado Por: </span>");
    let cargado_subtitle_ans = $("<span class='card_subtitle_ans'>" + artefacto.cargado_por.username + "</span>");

    // Integrar partes
    tipo_subtitle.append(tipo_subtitle_label)
        .append(tipo_subtitle_ans);

    actualizacion_subtitle.append(actualizacion_subtitle_label)
        .append(actualizacion_subtitle_ans);

    cargado_subtitle.append(cargado_subtitle_label)
        .append(cargado_subtitle_ans);

    artefacto_card.append(title)
        .append(description)
        .append(tipo_subtitle)
        .append(actualizacion_subtitle)
        .append(cargado_subtitle);

    artefacto_column.append(artefacto_card);

    return artefacto_column;
}

function isArtefactoSelectable(artefacto) {
    if(!artefacto.archivo) return false;
    let fileRelativePath = artefacto.archivo.toLowerCase();
    for(var i = 0; i < ACCEPTED_IMAGE_EXTENSIONS.length; i++) {
        let currentExtension = ACCEPTED_IMAGE_EXTENSIONS[i].toLowerCase();
        if(fileRelativePath.includes(currentExtension)) return true;
    }
    return false;
}

// HTTP
function getRecurso(id) {
    $.getJSON('/polls/api/recursos/' + id).done(function (data) {
        setModalInfo(data);
    });
}

function getRecursoArtefactos(id) {
    $.getJSON('/polls/api/recursos/' + id + '/artefactos').done(function(data) {
        addArtefactos(data);
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