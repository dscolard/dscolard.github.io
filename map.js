

var points = [
                ["Cebu", 10.3157, 123.8854],
                ["El Nido", 11.2097, 119.4623],
                ["Moalboal", 9.9557, 123.4008],
                ["Oslob", 9.5630, 123.4159],
                ["Siquijor", 9.2133, 123.5157],
                ["Bohol", 9.8500, 124.1435],
                ["Puerto Princesa", 9.9672, 118.7855],

                ["Marrakech", 31.6295, -7.9811],

                ["Bangkok", 13.7563, 100.5018],
                ["Chiang Mai", 18.7953, 98.9620],
                ["Koh Tao", 10.0956, 99.8404],
                ["Koh Samui", 9.5120, 100.0136],
                ["Koh Phangan", 9.7319, 100.0136],    
                ["Khao Sok", 8.9155, 98.5284],

                ["Hanoi", 21.0278, 105.8342],
                ["Ho Chi Minh", 10.8231, 106.6297],
                ["Phong Nha", 17.5908, 106.2834],
                ["Ha Long Bay", 20.9101, 107.1839],
                ["Tam Cốc-Bích Động", 20.2158, 105.9114],
                ["Hội An", 15.8801, 108.3380],

                ["Vancouver", 49.2827, -123.1207],
                ["Orlando", 28.5383, -81.3792],

                ["Budapest", 47.4979, 19.0402],
                ["Madrid", 40.4168, -3.7038],
                ["Oberstdorf", 47.4099, 10.2797],
                ["Berlin", 52.5200, 13.4050],
                ["Amsterdam", 52.3680, 4.9036],
                ["Vienna", 48.2082, 16.3738],
                ["Ljubljana", 46.0569, 14.5058],
                ["Prague",50.0755, 14.4378],
                ["Rome", 41.9028, 12.4964],
                ["Bilbao", 43.2630, -2.9350],
                ["Zagreb", 45.8150, 15.9819],
                ["Mallorca", 39.6953, 3.0176],
                ["Paris", 48.8566, 2.3522],
                ["Novalja", 44.5562, 14.8854],
                ["Kandersteg", 46.4947, 7.6744],
                ["Lisbon", 38.7223, -9.1393],

                ["Dublin", 53.35, -6.26],
                ["Rosslare", 52.2513, -6.3415],
                ["Westport", 53.8021, -9.5143],
                ["Killarney", 52.0599, -9.5044],

                ["Glasgow",55.8642,-4.2518],
                ["Isle of Man", 54.2361, -4.5481],
                ["Manchester", 53.4808, -2.2426],
                ["Nottingham", 52.9548, -1.1581]
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