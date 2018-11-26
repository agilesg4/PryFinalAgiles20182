function myFunction() {

    // Declare variables
    var  filtros_activos, i;
    var lista_filtros = [];
    filtros_activos = document.getElementsByTagName('input');

    list_group = document.getElementsByClassName('list-group');

    for (i = 0; i < filtros_activos.length; i++) {
        if (filtros_activos[i].checked == true) {
            lista_filtros.push(filtros_activos[i].name.toUpperCase());
        }
    }
    // Loop through all list items, and hide those who don't match the search query

    for (i = 0; i < list_group.length; i++) {
        if (lista_filtros.indexOf(list_group[i].id.toUpperCase()) == -1) {
            list_group[i].style.display = "none";

        } else {
            list_group[i].style.display = "block";

        }
    }
}