function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

var call_form = document.forms["callforpapers-form"];
$(document).on('submit', call_form, function(e) {
    e.preventDefault();
    var fields = ["nome", "cognome", "email", "argomento", "tipologia"];
    fields.forEach(function(field) {
        var parent = call_form[field].parentNode;
        if (!call_form[field].value || ((field == 'email') && !validateEmail(call_form[field].value))){
                parent.classList.remove("has-error");
                parent.classList.add("has-error");
        }
        else {
            parent.classList.remove("has-error");

        }
    });
    toastr.options = {
        "closeButton": true,
        "positionClass": "toast-bottom-right",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
    };
    $.ajax({
        url: '/send_call_mail',
        data: $('form').serialize(),
        type: 'POST',
        success: function(response) {
            response = JSON.parse(response);
            if (response['status'] == 'OK') {
                toastr.success(response['message']);
            }
            else if (response['message'] && response['message'] instanceof Object){
                // Errori nella validazione del form...

                // rimuovo i vecchi (se e' la seconda volta che li commette)
                $(".help-inline").remove();
                for (var k in response['message']){
                    if (response['message'].hasOwnProperty(k)) {
                         contact_form[k].parentNode.innerHTML += '<span class="help-inline">' + response['message'][k] + '</span>';
                    }
                }
            }
            else {
                toastr.error(response['message']);
            }
        },
        error: function(error) {
		    toastr.error("Non e' stato possibile inviare la mail");
        }
    });

});
