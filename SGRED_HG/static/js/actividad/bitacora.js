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
                        //window.location = "/polls/recurso/";
                    },

                });
                console.log(formData)
                });

function mySubmitFunction(e)
{
  e.preventDefault();
   var formData = new FormData($("#formbitacora")[0]);

        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: formData,
            cache: false,
            contentType: false,
            processData: false,
            success: function () {
                window.location = "/polls/bitacora/";
            },
        });
        console.log(formData)
 }