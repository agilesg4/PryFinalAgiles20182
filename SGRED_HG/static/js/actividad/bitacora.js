$(document).ready(function() {
        $("#summernote").summernote();
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

