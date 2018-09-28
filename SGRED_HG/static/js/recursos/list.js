$(document).ready(function() {
    fetchRecursosPorTipo();
});

// Api data
function fetchRecursosPorTipo() {
    $.getJSON('/polls/api/recurso/listByTipo').done(function (data) {
        $.each(data, function (tipoName, recursos) {
            addTipoContainer(tipoName, recursos);
        });
    });
}

// Listeners
function onClickRecurso(e) {
    e.preventDefault();
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
    let tipoCellContainer = $("<div class='tipoCellContainer col-md-3'></div>")
        .click({data: recurso}, onClickRecurso);
    let image = $("<img/>")
        .attr("src", "https://assets.dryicons.com/uploads/icon/svg/5915/80072f4d-46ea-4c63-bd9a-f0c946c25c60.svg")
        .attr("alt", "photoshop file icon")
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