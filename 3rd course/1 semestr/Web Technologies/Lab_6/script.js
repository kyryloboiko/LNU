// Array to hold product objects
let products = [];
// Counter for the product items
let itemCounter = 1;

// Formats a number to two decimal places
function formatNumber(number) {
    return number.toFixed(2);
}

// Converts a price string to a float
function convertPrice(price) {
    return parseFloat(price.replace(',', '.'));
}

// Calculates the price without VAT from the price with VAT
function calculatePriceWithoutVAT(priceWithVAT) {
    return priceWithVAT / 1.2;
}

// Validates if the provided value is a positive number
function isValidNumber(value) {
    return !isNaN(value) && value > 0;
}

// Prompts user to add a product with details like name, price, and quantity
function addProduct() {
    let name = prompt('Введіть назву товару:');
    if (name === null) return false;
    if (name.trim() === '') {
        alert('Назва товару не може бути порожньою!');
        return false;
    }

    let priceInput = prompt('Введіть ціну товару з ПДВ:');
    if (priceInput === null) return false;
    let price = convertPrice(priceInput);
    if (!isValidNumber(price)) {
        alert('Некоректна ціна! Ціна повинна бути більше 0.');
        return false;
    }

    let quantityInput = prompt('Введіть кількість товару:');
    if (quantityInput === null) return false;
    let quantity = parseInt(quantityInput);
    if (!isValidNumber(quantity)) {
        alert('Некоректна кількість! Кількість повинна бути більше 0.');
        return false;
    }

    products.push({
        number: itemCounter++,
        name: name,
        price: price,
        quantity: quantity
    });

    return true;
}

// Formats the current date and time
function formatDate() {
    const now = new Date();
    const date = now.toLocaleDateString();
    const time = now.toLocaleTimeString('uk-UA');
    return { date, time };
}

// Generates and displays a receipt for the added products
function generateReceipt() {
    if (products.length === 0) {
        console.log('Жодного товару не було додано. Чек не може бути сформований.');
        return;
    }

    let totalWithVAT = 0;
    let totalWithoutVAT = 0;

    console.log('Фіскальний касовий чек');
    console.log('-'.repeat(67));
    console.log('Назва товару | Ціна з ПДВ | Кількість | Вартість | Вартість без ПДВ');
    console.log('-'.repeat(67));

    products.forEach(product => {
        const totalPrice = product.price * product.quantity;
        const priceWithoutVAT = calculatePriceWithoutVAT(product.price);
        const totalPriceWithoutVAT = priceWithoutVAT * product.quantity;

        totalWithVAT += totalPrice;
        totalWithoutVAT += totalPriceWithoutVAT;

        console.log(
            `${product.name.padEnd(12)} | ` +
            `${formatNumber(product.price).padStart(9)} | ` +
            `${product.quantity.toString().padStart(9)} | ` +
            `${formatNumber(totalPrice).padStart(8)} | ` +
            `${formatNumber(totalPriceWithoutVAT).padStart(15)}`
        );
    });

    console.log('-'.repeat(67));
    console.log(`Загальна вартість без ПДВ: ${formatNumber(totalWithoutVAT)} грн`);
    
    const VAT = totalWithVAT - totalWithoutVAT;
    console.log(`Сума ПДВ: ${formatNumber(VAT)} грн`);
    console.log(`Загальна вартість з ПДВ: ${formatNumber(totalWithVAT)} грн`);
    console.log('-'.repeat(40));
    console.log(`Кількість артикулів: ${products.length}`);
    console.log('-'.repeat(40));

    // Обробка оплати
    const paymentInput = prompt(`До сплати: ${formatNumber(totalWithVAT)} грн\nВведіть суму оплати:`);
    if (paymentInput !== null) {
        const payment = convertPrice(paymentInput);
        if (isValidNumber(payment) && payment >= totalWithVAT) {
            const change = payment - totalWithVAT;
            console.log(`Сума готівкою: ${formatNumber(payment)} грн`);
            console.log(`Решта: ${formatNumber(change)} грн`);
        } else {
            console.log('Недостатньо коштів для оплати!');
            return;
        }
    }
    
    console.log('-'.repeat(40));
    console.log('Каса: 0001');
    console.log('Касир: Бойко Кирило Романович');
        
    const { date, time } = formatDate();
    console.log(`Дата: ${date}`);
    console.log(`Час: ${time}`);
    console.log('-'.repeat(40));
    console.log('QR-код чеку: [QR-код]');
    console.log('-'.repeat(40));
}

// Main function to control the flow of the program
function main() {
    do {
        const continueAdding = addProduct();
        if (!continueAdding) break;
    } while (confirm('Бажаєте додати ще один товар?'));

    generateReceipt();
}

// Start the program
main();