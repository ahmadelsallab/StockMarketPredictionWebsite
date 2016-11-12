var zoomSlider = document.getElementById('zoom');
var zoomValue = document.getElementById('zoomvalue');
var map, targetZoom;

var initMap = function() {
  var template = 'http://{S}tile.openstreetmap.org/{Z}/{X}/{Y}.png';
  var subdomains = ['', 'a.', 'b.', 'c.'];
  var provider = new MM.TemplatedLayer(template, subdomains);
      map = new MM.Map('map', provider, null);

	map.setCenterZoom(new MM.Location(37.811530, -122.2666097), 9);

  targetZoom = map.getZoom();
  zoomSlider.onchange = function() {
    var sliderProp = (zoomSlider.value - zoomSlider.min) / (zoomSlider.max - zoomSlider.min);
    targetZoom = sliderProp * 18.0; 
    MM.getFrame(animateToZoom);
  };
  zoomValue.innerHTML = targetZoom;

  map.addCallback('zoomed', function(){
    zoomValue.innerHTML = map.getZoom().toFixed(2);
    zoomSlider.value = map.getZoom() * 1000;
  });
}

var animateToZoom = function() {
  var currentZoom = map.getZoom();
  var nextZoom = currentZoom + (targetZoom - currentZoom) * 0.2;
  if (Math.abs(nextZoom - currentZoom) < 0.001) {
    nextZoom = currentZoom;
  } else {
    MM.getFrame(animateToZoom);
  }
  map.setZoom(nextZoom);
  zoomValue.innerHTML = nextZoom.toFixed(2);
}
