// map refers to a <div> element with the ID map
// examples.map-4l7djmvo is the ID of a map on Mapbox.com

/*$.ajax({
type: "GET",
url: "colleges_clean.json",
dataType: "json",
success: function(xml) {
    parseXML4 (xml);
}
});*/ //close ajax


$.ajax({
    crossDomain: false,
    type:"GET",
    contentType: "application/json; charset=utf-8",
    async:true,
    url: "colleges_clean.json",
    success: data,
    dataType: "json",                
    jsonpCallback: 'fnsuccesscallback'
    });

$( document ).ready(function() {            
    function data(json) {
        console.log(json);
        $.each( json.state, function( i, state ) {
            state = state.state;
            console.log(state);
            });
    };
});

var map = L.mapbox.map('map', 'anniedaniel.hjfkd6ef')
    .setView([40, -74.50], 9);
