// NAVBAR
$(document).ready(function() {
        $(window).scroll(function() {
          if($(this).scrollTop()) {
              $('.navbar').addClass('solid');
          } else {
              $('.navbar').removeClass('solid');
          }
        });
});