const shape = prompt(
    "Enter the shape type (rectangle, triangle, circle, trapezoid, rhombus, or parallelogram):"
).toLowerCase();

function isValidNumber(value) {
    return !isNaN(value) && value !== null && value !== "" && Number(value) > 0;
}

switch (shape) {
    case "rectangle":
        const length = prompt("Enter the length of the rectangle:");
        const width = prompt("Enter the width of the rectangle:");

        if (isValidNumber(length) && isValidNumber(width)) {
            const rectangleArea = Number(length) * Number(width);
            alert(`Area of the rectangle: ${rectangleArea.toFixed(2)}`);
        } else {
            alert("Invalid input values");
        }
        break;

    case "triangle":
        const base = prompt("Enter the base of the triangle:");
        const height = prompt("Enter the height of the triangle:");

        if (isValidNumber(base) && isValidNumber(height)) {
            const triangleArea = (Number(base) * Number(height)) / 2;
            alert(`Area of the triangle: ${triangleArea.toFixed(2)}`);
        } else {
            alert("Invalid input values");
        }
        break;

    case "circle":
        const radius = prompt("Enter the radius of the circle:");

        if (isValidNumber(radius)) {
            const circleArea = Math.PI * Math.pow(Number(radius), 2);
            alert(`Area of the circle: ${circleArea.toFixed(2)}`);
        } else {
            alert("Invalid input value");
        }
        break;

    case "trapezoid":
        const a = prompt("Enter the length of the first base of the trapezoid:");
        const b = prompt("Enter the length of the second base of the trapezoid:");
        const h = prompt("Enter the height of the trapezoid:");

        if (isValidNumber(a) && isValidNumber(b) && isValidNumber(h)) {
            const trapezoidArea = ((Number(a) + Number(b)) * Number(h)) / 2;
            alert(`Area of the trapezoid: ${trapezoidArea.toFixed(2)}`);
        } else {
            alert("Invalid input values");
        }
        break;

    case "rhombus":
        const d1 = prompt("Enter the length of the first diagonal of the rhombus:");
        const d2 = prompt("Enter the length of the second diagonal of the rhombus:");

        if (isValidNumber(d1) && isValidNumber(d2)) {
            const rhombusArea = (Number(d1) * Number(d2)) / 2;
            alert(`Area of the rhombus: ${rhombusArea.toFixed(2)}`);
        } else {
            alert("Invalid input values");
        }
        break;

    case "parallelogram":
        const base_p = prompt("Enter the base of the parallelogram:");
        const height_p = prompt("Enter the height of the parallelogram:");

        if (isValidNumber(base_p) && isValidNumber(height_p)) {
            const parallelogramArea = Number(base_p) * Number(height_p);
            alert(`Area of the parallelogram: ${parallelogramArea.toFixed(2)}`);
        } else {
            alert("Invalid input values");
        }
        break;

    default:
        alert("Unknown shape type. Please choose from the provided options.");
}