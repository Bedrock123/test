//  Controls navigation state on scroll
// $(window).scroll(function(event) {
//     if ($(document).scrollTop() > 100) {
//         if ($(window).width() < 660) {
//             $(".sub-navigation ").slideUp(100, function() {});
//             $("#nav-search-bar ").slideUp(100, function() {});
//             $(".main-navigation-1").slideDown(100, function() {
//                 $("#main-nav-2").addClass('main-navigation-2-scrolled ');
//             });
//         } else {
//             $("#nav-search-bar ").slideUp(100, function() {});
//             $(".main-navigation-1").slideUp(100, function() {
//                 $("#main-nav-2").addClass('main-navigation-2-scrolled ');
//             });
//             $(".sub-navigation ").slideUp(100, function() {});
//             $('#enter-your-address-button').removeClass("sky-blue");
//         }
//     }
//     if ($(document).scrollTop() < 100) {
//         if ($(window).width() < 650) {
//             $("#main-nav-2").removeClass('main-navigation-2-scrolled ');
//             $(".sub-navigation ").slideUp(100, function() {});
//             $("#nav-search-bar ").slideUp(100, function() {});
//             $(".main-navigation-1").slideDown(100, function() {});
//             $('#enter-your-address-button').removeClass("sky-blue");
//
//         } else {
//             $("#main-nav-2").removeClass('main-navigation-2-scrolled ');
//             $(".main-navigation-1").slideDown(100, function() {});
//             $(".sub-navigation ").slideDown(100, function() {});
//         }
//     }
// });

// //  Controls navigation state on screen resize
// $(window).resize(function() {
//
//     if ($(window).width() < 600) {
//         if ($(document).scrollTop() > 100) {
//             $(".main-navigation-1").slideDown(100, function() {});
//         }
//     }
// });

// Opens & Closes The Navigation Search bar
$(document).ready(function() {
    $("#nav-search-bar ").slideUp(50, function() {});
    $("#search").focusin(function() {
        $('#nav-search-bar').toggleClass("sky-blue-background");
        $('#nav-search-bar').toggleClass("white-background");
        $('#search-bar-map-icon').removeClass("white-text ");
    });
    $("#search").focusout(function() {
        $('#nav-search-bar').toggleClass("sky-blue-background");
        $('#nav-search-bar').toggleClass("white-background");
        $('#search-bar-map-icon').addClass("white-text ");
    });
});

$('#enter-your-address-button').click(function() {
    $("#nav-search-bar ").slideToggle()
    $("#search").focus();
    $(this).toggleClass("sky-blue");

});

// Puts focus on the address bar in the mobile menu
$('#mobile-map-icon').click(function() {
    $("#mobile-search").focus();

});

$('#left-arrow').click(function() {
    $('.carousel').carousel('prev');

});

$('#right-arrow').click(function() {
    $('.carousel').carousel('next');

});



(function($){
  $(function(){
    $('.button-collapse').sideNav({
      edge: 'right', // Choose the horizontal origin
      closeOnClick: true // Closes side-nav on <a> clicks, useful for Angular/Meteor
    });
  });
})(jQuery);
$(document).ready(function(){
    $('.slider').slider({full_width: true});
});
// Main Page Weather Pop up
$(document).ready(function(){
    $('#weatherModal').modal();
});
$(document).ready(function(){
    $('#cart').modal();
});

// Runs all of the parallex inits
(function($){
  $(function(){
    $('.parallax').parallax();
  });
})(jQuery);
$(document).ready(function() {
    $('select').material_select();
});
  $('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15 // Creates a dropdown of 15 years to control year
  });
  $(document).ready(function(){
    $('.collapsible').collapsible();
  });
  $(document).ready(function(){
    // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
    $('.modal').modal();
  });
 $('.carousel.carousel-slider').carousel({full_width: true});
