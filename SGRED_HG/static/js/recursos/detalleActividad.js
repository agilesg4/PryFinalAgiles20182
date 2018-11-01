$(document).ready(function() {
    fetchActividadPorId();
});

function fetchActividadPorId() {
    let urlParts = window.location.href.split("/");
    let id = urlParts[5];
    $.getJSON('/polls/rest_actividades_id/' + id ).done(function (data) {
        $.each(data, function (i, item) {
                $("#form_detalle").prepend('' +
                        '<p id="tituloactividad">' + item.fields.nombre + '</p>' +
                        '<p id="descripcion">' + item.fields.descripcion + '</p>' +
                        '<p id="tipoactividad">' + item.fields.tipoact + '</p>' +
                        '<p id="fase">' + item.fields.id_fase + '</p>' +
                        '<p id="periodicidad">' + item.fields.periodicidad + '</p>' +
                        '<p id="fechainicio">' + item.fields.fecha_inicio + '</p>'
                );
        });
    });
}

