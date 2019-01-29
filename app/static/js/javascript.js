var slider = document.getElementById("Scale1");
var output = document.getElementById("val1");
output.innerHTML = slider.value;

slider.oninput = function() {
  output.innerHTML = document.getElementById("Scale1").value;
}
