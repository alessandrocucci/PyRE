(function() {

	// Share Buttons
	var fb_button = document.querySelector('.btn-fb-share'),
		tw_button = document.querySelector('.btn-tw-share'),
		li_button = document.querySelector('.btn-li-share'),
		gplus_button = document.querySelector('.btn-gplus-share');

	fb_button.onclick = function(){
		window.open("https://www.facebook.com/sharer/sharer.php?u=www.pyre.it");
	};
	tw_button.onclick = function(){
		window.open("https://twitter.com/home?status=www.pyre.it");
	};
	li_button.onclick = function(){
		window.open("https://www.linkedin.com/shareArticle?mini=true&url=www.pyre.it&title=Python%20Reggio%20Emilia&summary=Iscriviti%20e%20partecipa%20agli%20eventi%20del%20Python%20Reggio%20Emilia%20User%20Group&source=");
	};
	gplus_button.onclick = function(){
		window.open("https://plus.google.com/share?url=www.pyre.it");
	};

	// Link al repo github
	$(window).scroll(function() {
		if ($(window).scrollTop() >= (($(document).height() - $(window).height()) - $('.call-to-action').innerHeight())) {
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
			toastr.success('Scopri come abbiamo sviluppato il nostro sito!', 'How it is made');
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





	// Switch on and off modals
	// $('#myModal').modal('toggle');
})();
