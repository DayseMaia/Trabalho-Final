fetch('/static/data.json')
    .then(response => {
        return response.json();
    })
    .then(data => {
        country = data;
    })

window.onload = function () {
    //writing state and city data in text fields
    var selState = document.getElementById('state');
    var selCity = document.getElementById('city');
    var selValue = document.getElementById('sunHours');
    for (var state in country) {
        selState.options[selState.options.length] = new Option(state, state);
    }
    selState.onchange = function () {
        selCity.options[0] = new Option("", "", true, true);
        selCity.options[0].disabled = true;
        selCity.length = 1;
        selValue.innerHTML = "Solar Irradiance: 0";
        selectedCity = this.value;
        if (this.selectedIndex < 1) return;
        for (var city in country[selectedCity]) {
            selCity.options[selCity.options.length] = new Option(city, city);
        }
    }
    selState.onchange();

    selCity.onchange = function () {
        sunLightHours = country[selectedCity][this.value];
        selValue.innerHTML = "Solar Irradiance: " + sunLightHours;
    }
}

var adjustSlider = function (sliderId, minValue, maxValue, stepValue = 1) {
    var element = document.getElementById(sliderId).getElementsByTagName("input")[0];
    element.min = minValue;
    element.max = maxValue;
    element.value = minValue;
    element.step = stepValue;
    element.style.display = "block";
    element.style.marginTop = "3rem";

    var sliderOutput = document.getElementById(sliderId).getElementsByTagName("output")[0];
    sliderOutput.innerHTML = minValue;
}

document.getElementById("systemConstrain").onclick = function () {
    requirement = parseFloat(document.getElementById('requirement').value);
    console.log(requirement + " " + sunLightHours);
}

document.getElementById("batteryBackup").onclick = function () {
    voltage = parseInt(document.getElementById('voltage').value);
    autonomy = parseInt(document.getElementById('autonomy').value);
    console.log(voltage);
    console.log(autonomy);
}

document.getElementById("solarPanel").onclick = function () {
    var typeOfPanel = document.getElementsByName("g3");
    if (typeOfPanel[0].checked) {
        panelEfficiency = 0.15;
        temperatureCoefficient = 0.5;
    } else if (typeOfPanel[1].checked) {
        panelEfficiency = 0.2;
        temperatureCoefficient = 0.45;
    } else if (typeOfPanel[2].checked) {
        panelEfficiency = 0.13;
        temperatureCoefficient = 0.3;
    }
    rating = parseInt(document.getElementById("rv3").value);
}

function calculate() {
    acPowerToLoad = requirement / sunLightHours;
    inverterInput = acPowerToLoad / (1 - parseFloat(document.getElementById('inverterLoss').value) / 100);
    inverterRating = inverterInput / (1 - parseFloat(document.getElementById('safety-factor').value) / 100);
    arrayOutput = inverterInput / (1 - parseFloat(document.getElementById('cableLoss').value) / 100);
    operatingLosses = parseFloat(document.getElementById('mismatchLoss').value) + parseFloat(document.getElementById('soilingLoss').value)
        + (parseFloat(document.getElementById('opTemp').value) - 25) * temperatureCoefficient;
    finalArrayCapacity = arrayOutput / (1 - operatingLosses / 100);
    numberOfModules = finalArrayCapacity * 1000 / rating;
    areaRequired = finalArrayCapacity / panelEfficiency;
    var dod = parseFloat(document.getElementById('dod').value) / 100;
    var batteryCapacity = (inverterInput * 1000) / (parseFloat(document.getElementById('batteryEfficiency').value) / 100);
    var finalbatteryCapacity = (batteryCapacity * autonomy) / (dod * voltage);
    var cost = (finalArrayCapacity * 1000) * 75;
    var finalResult = [finalArrayCapacity, acPowerToLoad, areaRequired, rating, numberOfModules, finalbatteryCapacity, inverterRating, cost, cost * 0.7];
    var result = document.getElementsByClassName('final-result');
    for (let index = 0; index < result.length; index++) {
        result[index].innerHTML = Math.ceil(finalResult[index]);
    }
}