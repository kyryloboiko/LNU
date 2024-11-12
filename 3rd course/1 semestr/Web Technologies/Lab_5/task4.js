const shape = prompt(
    "Enter the shape type (1 - rectangle, 2 - triangle, 3 - circle, 4 - trapezoid, 5 - rhombus, or 6 - parallelogram):"
).toLowerCase();

function isValidNumber(value) {
    return !isNaN(value) && value !== null && value !== "" && Number(value) > 0;
}

switch (shape) {
    case 1:
        const length = prompt("a:");
        const width = prompt("b:");

        if (isValidNumber(length) && isValidNumber(width)) {
            const rectangleArea = Number(length) * Number(width);
            alert(`Area of the rectangle: ${rectangleArea.toFixed(2)}`);
        } else {
            alert("Invalid input values");
        }
        break;

    case 2:
        const base = prompt("a:");
        const height = prompt("h:");

        if (isValidNumber(base) && isValidNumber(height)) {
            const triangleArea = (Number(base) * Number(height)) / 2;
            alert(`Area of the triangle: ${triangleArea.toFixed(2)}`);
        } else {
            alert("Invalid input values");
        }
        break;

    case 3:
        const radius = prompt("r:");

        if (isValidNumber(radius)) {
            const circleArea = Math.PI * Math.pow(Number(radius), 2);
            alert(`Area of the circle: ${circleArea.toFixed(2)}`);
        } else {
            alert("Invalid input value");
        }
        break;

    case 4:
        const a = prompt("a:");
        const b = prompt("b:");
        const h = prompt("h:");

        if (isValidNumber(a) && isValidNumber(b) && isValidNumber(h)) {
            const trapezoidArea = ((Number(a) + Number(b)) * Number(h)) / 2;
            alert(`Area of the trapezoid: ${trapezoidArea.toFixed(2)}`);
        } else {
            alert("Invalid input values");
        }
        break;

    case 5:
        const d1 = prompt("a diagonal:");
        const d2 = prompt("b diagonal:");

        if (isValidNumber(d1) && isValidNumber(d2)) {
            const rhombusArea = (Number(d1) * Number(d2)) / 2;
            alert(`Area of the rhombus: ${rhombusArea.toFixed(2)}`);
        } else {
            alert("Invalid input values");
        }
        break;

    case 6:
        const base_p = prompt("a:");
        const height_p = prompt("h:");

        if (isValidNumber(base_p) && isValidNumber(height_p)) {
            const parallelogramArea = Number(base_p) * Number(height_p);
            alert(`Area of the parallelogram: ${parallelogramArea.toFixed(2)}`);
        } else {
            alert("Invalid input values");
        }
        break;

    default:
        alert("You've entered incorrect value.");
}