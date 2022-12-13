var map;
var directions;

function initMap() {
  var useragent = navigator.userAgent;
  var mapdiv = document.getElementById("map");
  if (useragent.indexOf('iPhone') != -1 || useragent.indexOf('Android') != -1){
    mapdiv.style.width = '100%';
    mapdiv.style.height = '100%';
  }  

  var opts = {
    zoom: 15,
    center: new google.maps.LatLng(35.778022, 139.720245)
  };

  var map = new google.maps.Map(mapdiv, opts);
  var directions = new GDirections(map, document.getElementById('route'));

  const iconBase =
    "https://developers.google.com/maps/documentation/javascript/examples/full/images/";
  const icons = {
    parking: {
      icon: iconBase + "parking_lot_maps.png",
    },
    library: {
      icon: iconBase + "library_maps.png",
    },
    info: {
      icon: iconBase + "info-i_maps.png",
    },
  };
  const features = [
    {
      position: new google.maps.LatLng(-33.91721, 151.2263),
      type: "info",
    },
    {
      position: new google.maps.LatLng(-33.91539, 151.2282),
      type: "info",
    },

  ];

  // Create markers.
  for (let i = 0; i < features.length; i++) {
    const marker = new google.maps.Marker({
      position: features[i].position,
      icon: icons[features[i].type].icon,
      map: map,
    });
  }
}

function initialize() {
  if (GBrowserIsCompatible()) {
    map = new GMap2(document.getElementById("map_canvas"));
    map.setCenter(new GLatLng(35.681379,139.765577), 13);

    directions = new GDirections(map, document.getElementById('route'));
  }
}

function dispRoute() {
  var from = document.getElementById("from").value;
  var to = document.getElementById("to").value;

  directions.clear();

  str = 'from: ' + from + ' to: ' + to;
  directions.load(str, {locale: 'ja_JP'});
}