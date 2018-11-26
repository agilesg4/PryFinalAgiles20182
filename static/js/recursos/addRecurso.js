$('form').submit(function (e){

        var formData = new FormData($("#formRecurso")[0]);
        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: formData,
            cache: false,
            contentType: false,
            processData: false,
            success: function () {
             //window.location = "polls/create_TPPLAN";
            },
        });
        e.preventDefault();
        console.log(formData)
        return false


    });


