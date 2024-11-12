let number;

do {
    number = prompt("Enter a number you want to bet on the roulette:");
    if (!isNaN(number) && number !== null && number !== "") {
        if (number > 36) {
            console.log("There is no" + number + " on the rullette table. Please enter a number between 1 and 36.");
        } else if (number <= 0) {
            console.log("Please enter a positive number.");
            
        } else if (number % 2 === 0) {
            console.log(number + " is even");
        } else {
        console.log(number + " is odd");
        }
    } else {
        console.log("Invalid input. Please enter a number.");
    }
} while (isNaN(number) || number === null || number === "");