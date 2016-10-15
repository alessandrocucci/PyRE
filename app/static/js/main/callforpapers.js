function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

var call_form = document.forms["callforpapers-form"];
$(document).on('submit', call_form, function(e) {
    var fields = ["nome", "cognome", "email", "argomento", "tipologia"];
    fields.forEach(function(field) {
        var parent = call_form[field].parentNode;
        if (!call_form[field].value || ((field == 'email') && !validateEmail(call_form[field].value))){
                parent.classList.remove("has-error");
                parent.classList.add("has-error");
            e.preventDefault();
        }
        else {
            parent.classList.remove("has-error");

        }
    });

});
