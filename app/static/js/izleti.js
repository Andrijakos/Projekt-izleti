
   $(window).on('load',function(){
        $('#modal2').modal('show');
    });
jQuery.featherlight(jQuery('#modal'), {
        closeOnClick:false,
});
 function toggler(divId) {
    $("#" + divId).toggle();
}



