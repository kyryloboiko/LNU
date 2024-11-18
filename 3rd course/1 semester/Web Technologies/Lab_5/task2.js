const age = prompt("Enter your age:");

if (!isNaN(age) && age !== null && age !== "") {
    if (age >= 18) {
        console.log("You're old enough to smoke sigarettes");
    } else if (age >= 0) {
        console.log("Unfortunately, I can't stop you from doing that");
    } else if (age < 0) {
        console.log("Hey man, you're not even born yet");
    } else {
        console.log("What are you doing here?");
    }
} else {
    console.log("What have you just entered?");
}

