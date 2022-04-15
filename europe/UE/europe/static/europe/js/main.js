function setCookie(name,value,days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "")  + expires + "; path=/";
    location.reload();
}

function set_filters(){
    var country = $('#form_countries').val();
    var type = $('#form_chart').val();
    console.log(country);
    console.log(type);
    setCookie('country',country,1);
    setCookie('type',type,1);
}

$( document ).ready(function() {
    $("#data_table_wrapper").addClass("col-md-9");
});
