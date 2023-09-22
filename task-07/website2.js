
var inputval = document.querySelector('#cityinput')
var btn = document.querySelector('#add');
var city = document.querySelector('#cityoutput')
var descrip = document.querySelector('#description')
var temp = document.querySelector('#temp')
var wind = document.querySelector('#wind')
apik = "ebdc273af541d30735dc7c4ac0407927"
function convertion(val)
{
    return (val - 273).toFixed(2)
}

btn.addEventListener('click', function()
{
  fetch('https://api.openweathermap.org/data/2.5/weather?q='+inputval.value+'&appid='+apik)
  .then(res => res.json())


  .then(data => 
  {
    var name = data['name']
    var desc = data['weather']['0']['description']
    var tempature = data['main']['temp']
    var wspd = data['wind']['speed']

    city.innerHTML=`Weather of <span>${name}<span>`
    temp.innerHTML = `Temperature: <span>${ convertion(tempature)} C</span>`
    description.innerHTML = `Sky Conditions: <span>${desc}<span>`
    wind.innerHTML = `Wind Speed: <span>${wspd} km/h<span>`

  })

  .catch(err => alert('Wrong city name,Try Again'))
})