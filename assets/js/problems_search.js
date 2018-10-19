$(window).load(function() {
    $("#search").bind('input', function(evt){
        var val = $("#search").val();
        console.log(val);
        $("#links a").filter(function (index) {
            if (val && $(this).data('topic').toLowerCase().indexOf(val.toLowerCase()) < 0) {
                $(this).parent().hide();
            } else {
                $(this).parent().show();
            }
        })
    });
});