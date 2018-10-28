$(document).ready(function() {
    fetchRecursosPorTipo();
});

// Api data
function fetchRecursosPorTipo() {
    let urlParts = window.location.href.split("/");
    // TODO Cambiar si local
    let id = urlParts[5];
    $.getJSON('/polls/api/proyectos/' + id + '/recursosPorTipo').done(function (data) {
        $.each(data, function (tipoName, recursos) {
            addTipoContainer(tipoName, recursos);
        });
    });
}
