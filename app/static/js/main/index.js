// COOKIE LAW
toastr.options = {
  "closeButton": true,
  "debug": false,
  "newestOnTop": false,
  "progressBar": false,
  "positionClass": "toast-bottom-full-width",
  "preventDuplicates": false,
  "onclick": null,
  "showDuration": "300",
  "hideDuration": "1000",
  "timeOut": "5000",
  "extendedTimeOut": "1000",
  "showEasing": "swing",
  "hideEasing": "linear",
  "showMethod": "fadeIn",
  "hideMethod": "fadeOut"
};
toastr.info('Questo sito NON utilizza Cookie di nessun tipo. Volevamo fartelo sapere  <i class="fa fa-thumbs-o-up" aria-hidden="true"></i>');


// Link al repo github
$(window).scroll(function() {
	if ($(window).scrollTop() >= (($(document).height() - $(window).height()) - $('.call-to-action').innerHeight()) && location.pathname == '/') {
		toastr.options = {
			"closeButton": true,
		    "positionClass": "toast-bottom-right", // toast-top-right / toast-top-left / toast-bottom-right / toast-bottom-left
			"preventDuplicates": true,
		    "showDuration": "7000", // in milliseconds
		    "hideDuration": "1000", // in milliseconds
		    "timeOut": "5000", // in milliseconds
		    "extendedTimeOut": "1000", // in milliseconds
		    "showEasing": "swing",
		    "hideEasing": "linear",
		    "showMethod": "fadeIn",
		    "hideMethod": "fadeOut"
		};
		toastr.options.onclick = function() { window.location.assign("https://github.com/alessandrocucci/PyRE"); };
		toastr.success('Scopri come abbiamo sviluppato questo sito!', 'How it is made');
	  }
});

var login_modal = $("#login");
login_modal.on('show.bs.modal', function(){
	var login_form = document.forms["login-form"];
	$(document).on('submit', login_form, function(e) {
		if (!login_form["email"].value){
			login_form["email"].classList.add("invalid");
			e.preventDefault();
		}
		if (!login_form["password"].value){
			login_form["password"].classList.add("invalid");
			e.preventDefault();
		}
	});
});
