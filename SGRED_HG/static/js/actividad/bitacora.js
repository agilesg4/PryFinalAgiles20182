$(document).ready(function() {
        $('#summernote').summernote();
        alert('submit');



    });


$('form').submit(function (e){
        e.preventDefault();
        console.log("voy a hacer submit")



    });