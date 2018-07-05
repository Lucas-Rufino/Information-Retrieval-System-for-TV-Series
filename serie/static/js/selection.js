$(document).ready(function() {
    $(".js-example-placeholder-multiple").select2({
        placeholder: "Genres - ex: history, gameshow, music"
    });
});
function isNumberKey(evt){
    var charCode = (evt.which) ? evt.which : event.keyCode
    if (charCode > 31 && (charCode < 48 || charCode > 57))
        return false;
    return true;
}