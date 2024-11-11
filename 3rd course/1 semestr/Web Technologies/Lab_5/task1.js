const number = prompt("Enter a number to check if it's even or odd:");

if (!isNaN(number) && number !== null && number !== "") {
    if (number % 2 === 0) {
        console.log(`${number} is even`);
    } else {
        console.log(`${number} is odd`);
    }
} else {
    console.log("You have entered an invalid value.");
}

