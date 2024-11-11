const age = prompt("Enter your age:");

if (!isNaN(age) && age !== null && age !== "") {
    const ageNum = Number(age);
    
    if (ageNum >= 18) {
        console.log("You're an adult");
    } else if (ageNum >= 0) {
        console.log("You're a child");
    } else {
        console.log("The age cannot be negative");
    }
} else {
    console.log("You have entered an invalid value");
}

