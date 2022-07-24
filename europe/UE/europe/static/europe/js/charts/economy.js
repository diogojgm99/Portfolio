var line_chart = "Line";
var bar_chart = "Bar";
var map_chart = "Map";
var GDP = "GDP";
var GDP_GROWTH = "GDP_GROWTH";
var GDP_PER_CAPITA = "GDP_PER_CAPITA";

window.onload = function () {
    loadCharts();
}
$(document).ready(function() {
    $('#data_table').DataTable({
        "paging":   true,
        "ordering": true,
        "info": true
    });
} );

var ChartLineBarOptions = {
    responsive: true,
    scales: {
        x: {
            grid: {
                display: false
            }
        },
        y: {
            grid: {
                display: false
            },
            ticks: {
                beginAtZero: true
            },
        },
    }
};

var loadCharts = function(){
    $(".canvasChart").each(
        function(index, element){
            graph_id = $(element).attr("id");
            type_chart = $(element).attr("type_chart");
            report = $(element).attr("report");
            var my_url = "";
            switch(report){
                case GDP:
                    my_url = "/gdp_data/";
                    break;
                case GDP_GROWTH:
                    my_url = "/gdp_growth_data/";
                    break;
                case GDP_PER_CAPITA:
                    my_url = "/gdp_capita_data/";
                    break;
            }
            console.log(report);
            console.log(my_url);
            if (type_chart == line_chart){
                var ChartCanvas = $(element).get(0).getContext("2d");
                my_data = { graph_id };
                $.ajax({
                    type: "GET",
                    url: my_url + window.location.search,
                    data: my_data,
                    success: function (json, data) {
                        var chart = new Chart(ChartCanvas, {
                            type: 'line',
                            data: json,
                            options: ChartLineBarOptions
                        });
                    } 
                })       
            }
    });
}