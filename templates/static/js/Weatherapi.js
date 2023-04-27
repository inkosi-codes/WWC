function getDateInfo(){
  const dayForWidget = new Date().toLocaleDateString('en-us', { weekday:"long", year:"numeric", month:"short", day:"numeric"}) ;
  return dayForWidget

}

function displayWeather(current) {
  console.log(current);
  var weatherdesc = current.weather[0].description;
  var weatherIcon = current.weather[0].icon;
  var weatherTemp = Math.round(current.temp);

  let desc = document.getElementById('description')
  desc.append(weatherdesc.toUpperCase())

  let temp = document.getElementById('weatherTemp')
  let degIcon = document.createElement('span')

  degIcon.innerHTML = '&#176;'
  temp.append('Temp: ' + weatherTemp + ' F')
  temp.appendChild(degIcon)

  let imgLocation = document.getElementById('weatherIcon');
  let imgElement = document.createElement('img')

  imgElement.src = 'https://openweathermap.org/img/wn/'+ weatherIcon + '@2x.png'
  imgElement.alt = 'current weather icon'
  imgLocation.append(imgElement)

  weatherDay = getDateInfo();
  document.getElementById('currentDay').append(weatherDay)
}

function weatherWidget(lat, lon) {
  var key = "913d4cee4b20ad1ce85825ce4a942bb7";
  fetch(
    "https://api.openweathermap.org/data/3.0/onecall?lat=" +
      lat +
      "&lon=" +
      lon +
      "&units=imperial&exclude=hourly,daily,minutely&appid=" +
      key
  )
    .then(function (resp) {
      return resp.json();
    }) // Convert data to json
    .then(function (data) {
      displayWeather(data.current);
      // console.log(data)
    })
    .catch(function () {
      // catch any errors
    });
}

function setVariables(geo){

  let lat = geo.coords.latitude
  let lon = geo.coords.longitude

  weatherWidget(lat,lon)
}

function getCoords() {

  if (window.navigator.geolocation) {
    window.navigator.geolocation.getCurrentPosition(setVariables);
  }
}

window.onload = function () {
  getCoords();
};