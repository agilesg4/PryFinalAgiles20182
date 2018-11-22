$(document).ready(function() {
    getRecurso();
});

// HTTP
function getRecurso() {
    let id = getId();
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
    let id = parts[parts.length-2];
    return id;
}