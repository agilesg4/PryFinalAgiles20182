$('form').submit(function (e){
        e.preventDefault();
        var formData = new FormData($("#formRecurso")[0]);
        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: formData,
            cache: false,
            contentType: false,
            processData: false,
            success: function () {
                window.location = "polls/recurso/list";
            },

        });
        console.log(formData)

    });