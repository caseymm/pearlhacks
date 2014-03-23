var Marker = L.AwesomeMarkers.icon({
  icon: 'book', 
  color: 'blue',
  labelAnchor: [7, -33]
})

var Alabama = L.marker([33.2094,-87.5415], {icon: Marker}).bindPopup("<a href='/1'>Alabama</a>");
Alaska = L.marker([64.8589,-147.8356], {icon: Marker}).bindPopup("<a href='/2'>Alaska</a>");
Arizona = L.marker([32.2317,-110.9519], {icon: Marker}).bindPopup("<a href='/3'>Arizona</a>");
California = L.marker([34.0500,-110.9519], {icon: Marker}).bindPopup("<a href='/4'>California</a>");
Colorado = L.marker([40.0176,-105.2797], {icon: Marker}).bindPopup("<a href='/5'>Colorado</a>");
Connecticut = L.marker([41.8083,-72.2494], {icon: Marker}).bindPopup("<a href='/6'>Connecticut</a>");
Delaware = L.marker([39.6792,-75.7581], {icon: Marker}).bindPopup("<a href='/7'>Delaware</a>");
Florida = L.marker([29.6520,-82.3250], {icon: Marker}).bindPopup("<a href='/8'>Florida></a>");
Georgia = L.marker([33.9500,-83.3833], {icon: Marker}).bindPopup("<a href='/9'>Georgia</a>");
Hawaii = L.marker([21.2970,-157.8170], {icon: Marker}).bindPopup("<a href='/10'>Hawaii</a>");
Idaho = L.marker([29.6520,-116.2040], {icon: Marker}).bindPopup("<a href='/11'>Idaho</a>");
Illinois = L.marker([40.1105,-88.2284], {icon: Marker}).bindPopup("<a href='/12'>Illinois</a>");
Indiana = L.marker([39.1768,-116.2040], {icon: Marker}).bindPopup("<a href='/11'>Indiana</a>");
Idaho = L.marker([29.6520,-86.5197], {icon: Marker}).bindPopup("<a href='/12'>Idaho</a>");
Iowa = L.marker([41.6500,-91.5333], {icon: Marker}).bindPopup("<a href='/13'>Iowa</a>");
Kansas = L.marker([38.9581,-95.2478], {icon: Marker}).bindPopup("<a href='/14'>Kansas</a>");
kentucky = L.marker([38.0297,-84.4947], {icon: Marker}).bindPopup("<a href='/15'>Kentucky</a>");
Louisiana = L.marker([30.4145,-91.1783], {icon: Marker}).bindPopup("<a href='/16'>Louisiana</a>");
Maine = L.marker([44.1056,-70.2042], {icon: Marker}).bindPopup("<a href='/17'>Maine</a>");
Maryland = L.marker([38.9875,-76.9400], {icon: Marker}).bindPopup("<a href='/18'>Maryland</a>");
Massachusetts = L.marker([42.3744,-71.1169], {icon: Marker}).bindPopup("<a href='/19'>Massachusetts</a>");
Michigan = L.marker([42.7230,-84.4810], {icon: Marker}).bindPopup("<a href='/20'>Michigan</a>");
minnesota = L.marker([44.9753,-93.2342], {icon: Marker}).bindPopup("<a href='/22'>minnesota</a>");
mississippi = L.marker([34.3663,-89.5368], {icon: Marker}).bindPopup("<a href='/23'>mississippi</a>");
missouri = L.marker([39.0335,-94.5756], {icon: Marker}).bindPopup("<a href='/24'>missouri</a>");
montana = L.marker([46.8600,-113.9853], {icon: Marker}).bindPopup("<a href='/25'>montana</a>");
nebraska = L.marker([40.8097,-96.6753], {icon: Marker}).bindPopup("<a href='/26'>nebraska</a>");
nevada = L.marker([39.5458,-119.8167], {icon: Marker}).bindPopup("<a href='/27'>nevada</a>");
newhampshire = L.marker([43.1356,-70.9333], {icon: Marker}).bindPopup("<a href='/28'>New Hampshire</a>");
newjersey = L.marker([40.3571,-74.6702], {icon: Marker}).bindPopup("<a href='/29'>new jersey</a>");
newmexico = L.marker([35.0839,-106.6186], {icon: Marker}).bindPopup("<a href='/30'>New Mexico</a>");
newyork = L.marker([42.3482,-75.1890], {icon: Marker}).bindPopup("<a href='/31'>New York</a>");
northcarolina = L.marker([35.9083,-79.0500], {icon: Marker}).bindPopup("<a href='/32'>North Carolina</a>");
northdakota = L.marker([46.8916,-96.8003], {icon: Marker}).bindPopup("<a href='/33'>North Dakota</a>");
Ohio = L.marker([40.0000,-83.0145], {icon: Marker}).bindPopup("<a href='/34'>Ohio</a>");
Oklahoma = L.marker([36.1322,-97.0808], {icon: Marker}).bindPopup("<a href='/35'>oklahoma</a>");
Oregon = L.marker([44.0440,-123.0757], {icon: Marker}).bindPopup("<a href='/36'>oregon</a>");
Pennsylvania = L.marker([40.7961,-77.8628], {icon: Marker}).bindPopup("<a href='/37'>Pennsylvania</a>");
RhodeIsland = L.marker([41.8262,-71.4032], {icon: Marker}).bindPopup("<a href='/38'>Rhode Island</a>");
SouthCarolina = L.marker([34.0008,-81.0353], {icon: Marker}).bindPopup("<a href='/39'>South Carolina</a>");
SouthDakota = L.marker([42.7811,-96.9269], {icon: Marker}).bindPopup("<a href='/40'>South Dakota</a>");
Tennessee = L.marker([36.1667,-86.7833], {icon: Marker}).bindPopup("<a href='/41'>Tennessee</a>");
Texas = L.marker([30.2500,-97.7500], {icon: Marker}).bindPopup("<a href='/42'>Texas</a>");
Utah = L.marker([40.7500,-111.8833], {icon: Marker}).bindPopup("<a href='/43'>Utah</a>");
Vermont = L.marker([44.4758,-73.2119], {icon: Marker}).bindPopup("<a href='/44'>Vermont</a>");
Virginia = L.marker([38.0299,-78.4790], {icon: Marker}).bindPopup("<a href='/45'>Virginia</a>");
Washington = L.marker([46.7333,- 117.1667], {icon: Marker}).bindPopup("<a href='/46'>Washington</a>");
WestVirginia = L.marker([39.6336,-79.9506], {icon: Marker}).bindPopup("<a href='/47'>West Virginia</a>");
Wisconsin = L.marker([43.0667, -89.4000], {icon: Marker}).bindPopup("<a href='/48'>Wisconsin</a>");
Wyoming = L.marker([41.3167, -105.5833], {icon: Marker}).bindPopup("<a href='/49'>Wyoming</a>");
								   
//var all = L.layerGroup([Wyoming]);
var all = L.layerGroup([Alabama, Alaska, Arizona, California, Colorado, Connecticut, Delaware, Florida, Georgia, Hawaii, Idaho, Illinois, Indiana, Idaho, Iowa, Kansas, kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, minnesota, mississippi, missouri, montana, nebraska, nevada, newhampshire, newjersey, newmexico, newyork, northcarolina, northdakota, Ohio, Oklahoma, Oregon, Pennsylvania, RhodeIsland, SouthCarolina, SouthDakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, WestVirginia, Wisconsin, Wyoming]);

    
var cmAttr = 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
    cmUrl = 'http://{s}.tile.cloudmade.com/825c6664ffdf4e619e51fb7dd3b47005/98490/256/{z}/{x}/{y}.png';

var regular   = L.tileLayer(cmUrl, {styleId: 997, attribution: cmAttr});

		var map = L.map('map', {
			center: new L.LatLng(39.8282,-98.5795),
			zoom:3,
			layers: [regular, all],
		});


L.tileLayer('http://{s}.tile.cloudmade.com/825c6664ffdf4e619e51fb7dd3b47005/98490/256/{z}/{x}/{y}.png', {
                        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
                        maxZoom: 16
                        }).addTo(map);

var baseLayers = {};

var overlayMaps = {
    
    "Schools": all
};

L.control.layers(baseLayers, overlayMaps).addTo(map);
    
//var marker = L.marker([33.751748,-84.391479]).bindLabel('Look revealing label!').addTo(map);
    
//var popup = L.popup()
    //.setLatLng([33.751748,-84.491479])
    //.setContent("I am a standalone popup.")
    //.openOn(map);