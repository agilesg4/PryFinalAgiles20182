$(document).ready(function() {
    let modal = buildModal();
    $("#recurso_modal").append(modal);
});

function buildModal() {
    let modal = $("<div class='modal fade' id='exampleModal' tabindex='-1' role='dialog' aria-labelledby='exampleModalLabel' aria-hidden='true'></div>");
    let modal_dialog = $("<div class='modal-dialog' role='document'></div>");
    let modal_content = $("<div class='modal-content'></div>")
    let modal_header = $("<div class='modal-header'></div>");
    let modal_body = $("<div class='modal-body'></div>");
    let modal_footer = $("<div class='modal-footer'></div>");

    // Add content to modal
    modal_header.append("<h5 class='modal_title'>Detalle Recurso</h5>");

    let data_form = buildModalForm();
    modal_body.append(data_form);

    modal_footer.append("<input type='submit' form='recurso_form' class='btn btn-secondary' value='Guardar Cambios'>")
        .append("<button type='button' class='btn btn-secondary' data-dismiss='modal'>Cancelar</button>");

    // Build modal
    modal_content.append(modal_header)
        .append(modal_body)
        .append(modal_footer);

    modal_dialog.append(modal_content);

    modal.append(modal_dialog);
    return modal;
}

function buildModalForm() {
    // TODO Options should come from server
    let options = ["Opcion 1", "Opcion 2", "Opcion 3"];

    let form = $("<form onsubmit='handleSubmit();return false;' id='recurso_form'></form>");
    let error_field = $("<div id='form_error_field'></div>")
    let titulo_field = $("<div class='form-group form-inline'></div>");
    let tipo_field = $("<div class='form-group form-inline'></div>");
    let descripcion_field = $("<div class='form-group form-inline'></div>");
    let ubicacion_field = $("<div class='form-group form-inline'></div>");

    // Add content to form
    titulo_field.append("<label for='recipient-name' class='col-form-label col-md-3'>Titulo:</label>")
        .append("<input type='text' class='form-control col-md-9' id='recipient-name' autocomplete='nope'>");


    let tipo_select = $("<select class='select form-control col-md-9'></select>")
        .append("<option value='' disabled selected>---------</option>");

    for(var i = 0; i < options.length; i++) {
        let option = options[i];
        tipo_select.append("<option value='" + option + "'>" + option + "</option>");
    }

    tipo_field.append("<label for='recipient-name' class='col-form-label col-md-3'>Tipo:</label>")
        .append(tipo_select);

    descripcion_field.append("<label for='recipient-name' class='col-form-label col-md-3'>Descripción:</label>")
        .append("<textarea class='form-control col-md-9' id='recipient-name' autocomplete='nope'></textarea>");

    let file_dialog_button = $("<button class='load_file_button btn-secondary'>Cargar</button>")
        .click(function() {
            $("#form_file").click();
            return false;
        });

    let path_field = $("<div class='col-md-9 row input_container_row'></div>")
        .append("<input type='text' class='form-control col-md-12' id='load_file_name_input' autocomplete='nope'>")
        .append("<input type='file' id='form_file' class='load_file_button btn-secondary' onchange='handleFileSelected(this);'>")
        .append(file_dialog_button);

    ubicacion_field.append("<label for='recipient-name' class='col-form-label col-md-3'>Ubicación:</label>")
        .append(path_field);


    // Build form
    form.append(error_field)
        .append(titulo_field)
        .append(tipo_field)
        .append(descripcion_field)
        .append(ubicacion_field);

    return form;
}

// Submit helpers
function handleSubmit() {
    console.log("Handle Submit");
}

// File helpers
function handleFileSelected(input) {
    let files = input.files;
    if(files.length <= 0) return;
    $("#load_file_name_input").val(files[0].name);
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