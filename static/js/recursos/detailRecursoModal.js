$(document).ready(function() {
    getTipos();
});

// Tipos a los que puede pertenecer un recurso
var availableTipos = [];
var recurso_id = null;

function buildModal() {
    let modal = $("<div class='modal fade' id='recurso_build_modal' tabindex='-1' role='dialog' aria-labelledby='recurso_modal_label' aria-hidden='true'></div>");
    let modal_dialog = $("<div class='modal-dialog' role='document'></div>");
    let modal_content = $("<div class='modal-content'></div>")
    let modal_header = $("<div class='modal-header'></div>");
    let modal_body = $("<div class='modal-body'></div>");
    let modal_footer = $("<div class='modal-footer'></div>");

    // Add content to modal
    modal_header.append("<h5 class='modal_title'>Detalle Recurso</h5>");

    let data_form = buildModalForm();
    modal_body.append(data_form);

    let save_button = $("<input type='submit' id='modal_save_button' form='recurso_form' class='btn btn-secondary' value='Guardar Cambios'>")
        .css("visibility", "hidden");

    modal_footer.append(save_button)
        .append("<button type='button' class='btn btn-secondary' data-dismiss='modal' onclick='clearModalInfo();'>Cancelar</button>");

    // Build modal
    modal_content.append(modal_header)
        .append(modal_body)
        .append(modal_footer);

    modal_dialog.append(modal_content);

    modal.append(modal_dialog);
    return modal;
}

function buildModalForm() {
    let form = $("<form onsubmit='handleSubmit();return false;' id='recurso_form'></form>");
    let error_field = $("<div id='form_error_field'></div>")
    let titulo_field = $("<div class='form-group form-inline'></div>");
    let tipo_field = $("<div class='form-group form-inline'></div>");
    let descripcion_field = $("<div class='form-group form-inline'></div>");
    let ubicacion_field = $("<div class='form-group form-inline'></div>");


    // Add content to form
    titulo_field.append("<label for='recurso_titulo' class='col-form-label col-md-3'>Titulo:</label>")
        .append("<input type='text' class='form-control col-md-9' id='recurso_titulo' autocomplete='nope' disabled>");


    let tipo_select = $("<select class='select form-control col-md-9' id='recurso_tipo_select' disabled></select>")
        .append("<option value='' disabled selected>---------</option>");

    for(var i = 0; i < availableTipos.length; i++) {
        let option = availableTipos[i];
        tipo_select.append("<option value='" + option.id_tipo + "'>" + option.nombre + "</option>");
    }

    tipo_field.append("<label for='recipient-name' class='col-form-label col-md-3'>Tipo:</label>")
        .append(tipo_select);

    descripcion_field.append("<label for='recurso_descripcion' class='col-form-label col-md-3'>Descripción:</label>")
        .append("<textarea class='form-control col-md-9' id='recurso_descripcion' autocomplete='nope' disabled></textarea>");

    let file_dialog_button = $("<button class='load_file_button btn-secondary' id='file_dialog_button'>Cargar</button>")
        .css("visibility","hidden")
        .click(function() {
            $("#form_file").click();
            return false;
        });

    let path_field = $("<div class='col-md-9 row input_container_row'></div>")
        .append("<input type='text' class='form-control col-md-12' id='load_file_name_input' oninput='handleFilePathChange(this);' autocomplete='nope' disabled>")
        .append("<input type='file' id='form_file' class='load_file_button btn-secondary' onchange='handleFileSelected(this);'>")
        .append(file_dialog_button);

    ubicacion_field.append("<label for='load_file_name_input' class='col-form-label col-md-3'>Ubicación:</label>")
        .append(path_field);



    // Build form
    form.append(error_field)
        .append(titulo_field)
        .append(tipo_field)
        .append(descripcion_field)
        .append(ubicacion_field);

    return form;
}

function setModalInfo(recurso) {
    clearModalInfo();
    recurso_id = recurso.id_recurso;
    $("#recurso_titulo").val(recurso.titulo);
    $("#recurso_descripcion").val(recurso.descripcion);
    if($("#recurso_tipo_select option[value='" + recurso.tipo.id_tipo + "']").length !== 0) {
        $("#recurso_tipo_select").val(recurso.tipo.id_tipo);
    }
    if(recurso.ubicacion) {
        $("#load_file_name_input").val(recurso.ubicacion)
            .prop("disabled", true);
        $("#modal_save_button").css("visibility", "hidden");
        $("#file_dialog_button").css("visibility","hidden");
    } else {
        $("#load_file_name_input").prop("disabled", false);
        $("#modal_save_button").css("visibility", "visible");
        $("#file_dialog_button").css("visibility","visible");
    }
}

function clearModalInfo() {
    recurso_id = null;
    $("#recurso_titulo").val("");
    $("#recurso_descripcion").val("");
    $("#recurso_tipo_select").val("");
    $("#load_file_name_input").val("");
    removeErrorToForm();
}

// Submit helpers
function handleSubmit() {
    let titulo = $("#recurso_titulo").val().trim();
    let descripcion = $("#recurso_descripcion").val().trim();
    let tipo = $("#recurso_tipo_select").val();
    let ubicacion = $("#load_file_name_input").val().trim();
    if(titulo === "" || descripcion === "" || tipo === "" || tipo === null || ubicacion === "") {
        addErrorToForm("Por favor complete todos los campos");
    } else {
        removeErrorToForm();
        let recursoData = {
            titulo: titulo,
            descripcion: descripcion,
            tipo: parseInt(tipo),
            ubicacion: ubicacion
        };
        updateRecurso(recursoData);
    }
}

function updateRecurso(data) {
    $.ajax({
        type: 'PUT',
        url: '/polls/api/recursos/' + recurso_id + '/update',
        contentType: 'application/json',
        data: JSON.stringify(data),
    }).done(function() {
        window.location.reload(true);
    }).fail(function() {
        addErrorToForm("Oops, hubo un error actualizando el recurso.");
    });
}

function handleFilePathChange(input) {
    if(input.value.trim() === "") {
        $("#file_dialog_button").css("visibility","visible");
    } else {
        $("#file_dialog_button").css("visibility","hidden");
    }
}

// File helpers
function handleFileSelected(input) {
    let files = input.files;
    if(files.length <= 0) return;
    $("#load_file_name_input").val(files[0].name);
    $("#file_dialog_button").css("visibility","hidden");
}

// Error helpers
function addErrorToForm(error) {
    let found_error_container = $("#error_container");
    if (found_error_container.length === 0) {
        let error_container = $("<div class='alert alert-danger' id='error_container'></div>")
            .append("<div>" + error + "</div>");

        $("#form_error_field").append(error_container);
    } else {
        found_error_container.html("<div>" + error + "</div>");
    }
}

function removeErrorToForm() {
    $("#form_error_field").html("");
}

// HTTP
function getTipos() {
    $.getJSON('/polls/api/recursos/tipos').done(function (data) {
        availableTipos = data;
        let modal = buildModal();
        $("#recurso_modal").append(modal);
    });

}