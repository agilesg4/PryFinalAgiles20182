$(document).ready(function() {
    fetchRecursos();
});

// Api data
function fetchRecursos() {
    $.getJSON('/polls/api/recursosPorTipo').done(function (data) {
        $.each(data, function (tipoName, recursos) {
            addTipoContainer(tipoName, recursos);
        });
    });
}