$(document).ready(function () {
  $(".collapsible").collapsible();
  $("select").material_select();
  $(".button-collapse").sideNav();


/* fixes issues that requires t clicks for dropdown to work https://mdbootstrap.com/support/jquery/dropdown-needs-2-clicks-to-activate/ */
$('.dropdown').click(e => e.stopPropagation()); 

});

