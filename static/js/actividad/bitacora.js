$(document).ready(function() {
        $("#summernote").summernote();

        document.getElementById("fakeid").value= window.location.pathname.split("/")[3];

    });


  $("form").submit(function (e) {
              e.preventDefault();

               var formData = new FormData($("#formbitacora")[0]);
               console.log(formData);
                $.ajax({
                    url: $(this).attr('action'),
                    type: $(this).attr('method'),
                    data: formData,
                    cache: false,
                    contentType: false,
                    processData: false,
                    success: function () {
                        window.location = "/polls/lista_actividades/";
                    },

                });
                console.log(formData)
                });

