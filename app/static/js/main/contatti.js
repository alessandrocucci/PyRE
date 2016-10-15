var contact_form = document.forms["contact-form"];
	$(document).on('submit', contact_form, function(e) {
        var fields = ["nome", "cognome", "email", "messaggio"];
		fields.forEach(function(field) {
			if (!contact_form[field].value){
				contact_form[field].parentNode.classList.add("has-error");
				e.preventDefault();
			}
		});

	});
