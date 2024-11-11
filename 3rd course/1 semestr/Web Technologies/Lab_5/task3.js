const celsius = prompt("Enter the temperature in Celsius:");

if (!isNaN(celsius) && celsius !== null && celsius !== "") {
    const kelvin = Number(celsius) + 273.15;

    alert(`${celsius}°C = ${kelvin.toFixed(2)}K`);
} else {
    alert("You have entered an invalid value.");
}

