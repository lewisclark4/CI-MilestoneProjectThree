$(document).ready(function () {
  $(".collapsible").collapsible();
  $("select").material_select();
  $(".button-collapse").sideNav();


// fixes issues that requires t clicks for dropdown to work 
$('.dropdown').click(e => e.stopPropagation()); 


// Add & Remove Ingredients/ Preparations 

 var ingredientCount = 1;
$("#addingredient").on("click", function () {
    $('.ingredients:first').clone().insertBefore('#addingredient').find("input[type='text'], select, textarea").val("")
    ingredientCount += 1;
});

$("#removeingredient").on("click", function () {
    if (ingredientCount > 1) {
        $(".ingredients:last").remove();
        ingredientCount-= 1;
    }
});


var prepCount = 1;
$("#addprep").on("click", function () {
    $('.preparation:first').clone().insertBefore('#addprep').find("input[type='text'], select, textarea").val("");
    prepCount += 1;
});

$("#removeprep").on("click", function () {
    if (prepCount > 1) {
        $(".preparation:last").remove();
        prepCount-= 1;
    }
});

});

