// Listeners
function onClickRecurso(e) {
    e.preventDefault();
    let recurso = e.data.data;
    setModalInfo(recurso);
    $('#recurso_build_modal').modal('toggle');
}

// Manejo del UI
function addTipoContainer(tipoName,recursos) {
    let row = $("<div class='row'></div>");
    let name = $("<div class='tipoName col-md-12'></div>")
        .append(tipoName);

    let tipoContainer = $("<div class='tipoContentContainer col-md-12'></div>");
    let innerContainer = $("<div class='container'></div>");
    let innerRow = $("<div class='row'></div>");

    // Agregar cells
    for(var i = 0; i < recursos.length; i++) {
        addRecursoToTipo(innerRow, recursos[i]);
    }

    // Unir partes
    innerContainer.append(innerRow);
    tipoContainer.append(innerContainer);

    row.append(name)
        .append(tipoContainer);

    // Mostrarlo en div
    $("#tiposList").append(row);
}

function addRecursoToTipo(tipoContainer, recurso) {
    let buttonId = "recurso" + recurso.id_recurso;
    let tipoCellContainer = $("<div class='tipoCellContainer col-md-3' id=" + buttonId + "></div>")
        .click({data: recurso, element: this}, onClickRecurso);
    let image = $("<img/>")
        .attr("src", recurso.tipo.icono)
        .attr("alt", "file type icon")
        .attr("class", "tipoImage");

    let row = $("<div class='row'></div>");
    let tipoTitle = $("<div class='tipoTitle'></div>")
        .append(recurso.titulo);

    // Unir partes
    row.append(tipoTitle);

    tipoCellContainer.append(image);
    tipoCellContainer.append(row);

    // Mostrarlo en tipoContainer
    tipoContainer.append(tipoCellContainer);
}