

let id;
let target;
let options;


function exit(pos){
  const crd = pos.coords;

  if (target.latitude === crd.latitude && target.longitude === crd.longitude) {
    console.log('Lleagaste a tu destino entrega el pedido');
    navigator.geolocation.clearWatch(id);
  }
}

function error(err){
  console.error(`ERROR(${err.code}): ${err.message}`);
}

terget = {
  latitude : 0,
  longitude: 0
};

options = {
  enableHighAccuracy: false,
  timeout: 5000,
  maximumAge: 0
};

id = navigator.geolocation.watchPosition(success,
error, options);


function iniciarMap(){
    var coord = {lat:-34.5956145 ,lng: -58.4431949};
    var map = new google.maps.Map(document.getElementById('map'),{
      zoom: 10,
      center: coord
    });
    var marker = new google.maps.Marker({
      position: coord,
      map: map
    });
}
