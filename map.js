

var points = [
                ["Dublin", 53.35, -6.26],
                ["Cebu", 10.3157, 123.8854],
                ["El Nido", 11.2097, 119.4623],
                ["Bangkok", 13.7563, 100.5018],
                ["Chiang Mai", 18.7953, 98.9620],
                ["Hanoi", 21.0278, 105.8342],
                ["Ho Chi Minh", 10.8231, 106.6297],
                ["Budapest", 47.4979, 19.0402],
                ["Vancouver", 49.2827, -123.1207],
                ["Orlando", 28.5383, -81.3792],
                ["Madrid", 40.4168, -3.7038],
                ["Oberstdorf", 47.4099, 10.2797],
                ["Berlin", 52.5200, 13.4050],
                ["Amsterdam", 52.3680, 4.9036],
                ["Vienna", 48.2082, 16.3738],
                ["Ljubljana", 46.0569, 14.5058],
                ["Prague",50.0755, 14.4378],
                ["Rome", 41.9028, 12.4964],
                ["Bilbao", 43.2630, -2.9350],
                ["Marrakech", 31.6295, -7.9811],
                ["Zagreb", 45.8150, 15.9819],
                ["Mallorca", 39.6953, 3.0176],
                ["Rosslare", 52.2513, -6.3415],
                ["Westport", 53.8021, -9.5143],
                ["Killarney", 52.0599, -9.5044],
                ["Paris", 48.8566, 2.3522],
                ["Glasgow",55.8642,-4.2518],
                ["Isle of Man", 54.2361, -4.5481]
                //Lisbon 
            ];

//create map object and set default positions and zoom level
var map = L.map('map', {minZoom:2}).setView([20, 0], 2);
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'}).addTo(map);

var markerClusters = L.markerClusterGroup();
for (var i=0; i < points.length; i++){
    var popup = points[i][0];
    var m = L.marker(new L.LatLng(points[i][1], points[i][2])).bindPopup(popup);

    m.on('mouseover', function(event) {
        //open popup;
        this.openPopup();
    });      

    m.on('mouseout', function(event) {
        //close popup;
        this.closePopup();
    }); 

    markerClusters.addLayer(m);
}
map.addLayer(markerClusters);