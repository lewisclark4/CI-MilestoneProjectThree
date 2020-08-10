$(document).ready(function () {
// Initialise Materialize components
  $(".collapsible").collapsible();
  $("select").material_select();
  $(".button-collapse").sideNav();
   $('.modal').modal();


// fixes issues that requires t clicks for dropdown to work 
$('.dropdown').click(e => e.stopPropagation()); 

// Add ingredient element into recipe form
 var ingredientCount = $('.ingredients').length
$("#add-ingredient").on("click", function () {
    $('.ingredients:first').clone().insertBefore('#add-ingredient').find("input[type='text'], select, textarea").val("")
    ingredientCount += 1;
});

// Remove ingredient element from recipe form
$("#remove-ingredient").on("click", function () {
    if (ingredientCount > 1) {
        $(".ingredients:last").remove();
        ingredientCount-= 1;
    }
});

// Add Preparation element into recipe form
var prepCount = $('.preparation').length
$("#add-prep").on("click", function () {
    $('.preparation:first').clone().insertBefore('#add-prep').find("input[type='text'], select, textarea").val("");
    prepCount += 1;
});

// Remove Preparation element from recipe form
$("#remove-prep").on("click", function () {
    if (prepCount > 1) {
        $(".preparation:last").remove();
        prepCount-= 1;
    }
});

});