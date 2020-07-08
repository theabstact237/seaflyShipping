let $map = document.querySelector("#map");
let key = 'AIzaSyDqds4AcbBtmntJedcFGT9ZVbZ6OuFDa5Q';
class GoogleMap {
    /**
     * Charge la carte sur un élément
     * @param element
     */
    load (element){
        $script('https://maps.googleapis.com/maps/api/js?key=' + key + '&callback=initMap', function(){
            let center = {lat: 13.7771722, lng: 100.5760527},
            map = new google.maps.Map(element, {
              center: center,
              zoom: 15
            });
            let marker = new google.maps.Marker({
                position: center,
                map: map
            })
        })
    }
}

if (map != null){
    let map = new GoogleMap();
    map.load($map);
}