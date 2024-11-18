// Оновлення дати і часу
function updateDateTime() {
    const now = new Date();
    const options = {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: false
    };
    document.getElementById('datetime').textContent = now.toLocaleString('uk-UA', options);
}

// Оновлюємо час кожну секунду
setInterval(updateDateTime, 1000);
updateDateTime();

// Робота з локальним сховищем для адміністратора
const adminNameInput = document.getElementById('adminName');

// Завантаження імені адміністратора при завантаженні сторінки
adminNameInput.value = localStorage.getItem('adminName') || '';

// Збереження імені адміністратора при зміні
adminNameInput.addEventListener('input', (e) => {
    localStorage.setItem('adminName', e.target.value);
});

// Валідація форми
const form = document.getElementById('participantForm');
const nameRegex = /^[А-ЩЬЮЯҐЄІЇа-щьюяґєії'-]+$/;
const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
const phoneRegex = /^\+?[0-9]{7,15}$/;

function validateForm(formData) {
    let isValid = true;
    const errors = {};

    // Валідація імені
    if (!formData.firstName || formData.firstName.length < 3 || !nameRegex.test(formData.firstName)) {
        errors.firstName = 'Ім\'я має містити мінімум 3 символи та лише українські літери';
        isValid = false;
    }

    // Валідація прізвища
    if (!formData.lastName || formData.lastName.length < 3 || !nameRegex.test(formData.lastName)) {
        errors.lastName = 'Прізвище має містити мінімум 3 символи та лише українські літери';
        isValid = false;
    }

    // Валідація email
    if (!formData.email || !emailRegex.test(formData.email)) {
        errors.email = 'Введіть коректну email адресу';
        isValid = false;
    }

    // Валідація телефону
    if (!formData.phone || !phoneRegex.test(formData.phone)) {
        errors.phone = 'Введіть коректний номер телефону (мінімум 7 цифр)';
        isValid = false;
    }

    return { isValid, errors };
}

function showErrors(errors) {
    // Очищення попередніх помилок
    document.querySelectorAll('.error').forEach(error => error.textContent = '');
    document.querySelectorAll('input').forEach(input => input.classList.remove('error'));

    // Відображення нових помилок
    Object.keys(errors).forEach(key => {
        const errorElement = document.getElementById(`${key}Error`);
        const inputElement = document.getElementById(key);
        if (errorElement && errors[key]) {
            errorElement.textContent = errors[key];
            inputElement.classList.add('error');
        }
    });
}

// Обробка відправки форми
form.addEventListener('submit', (e) => {
    e.preventDefault();

    const formData = {
        firstName: document.getElementById('firstName').value,
        lastName: document.getElementById('lastName').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value
    };

    const { isValid, errors } = validateForm(formData);

    if (isValid) {
        addParticipant(formData);
        form.reset();
    } else {
        showErrors(errors);
    }
});

// Додавання учасника
function addParticipant(participant) {
    const participantsList = document.getElementById('participantsList');
    const participantCard = document.createElement('div');
    participantCard.className = 'participant-card';
    
    const registrationDate = new Date().toLocaleString('uk-UA');
    
    participantCard.innerHTML = `
        <h3>${participant.firstName} ${participant.lastName}</h3>
        <p>Email: ${participant.email}</p>
        <p>Телефон: ${participant.phone}</p>
        <p>Дата реєстрації: ${registrationDate}</p>
        <div class="attendance-buttons">
            <button class="btn btn-visited">Відвідано</button>
            <button class="btn btn-not-visited">Не відвідано</button>
            <button class="btn btn-delete">Видалити</button>
        </div>
    `;

    // Обробка кнопок відвідування
    participantCard.querySelector('.btn-visited').addEventListener('click', () => {
        participantCard.className = 'participant-card participant-visited';
    });

    participantCard.querySelector('.btn-not-visited').addEventListener('click', () => {
        participantCard.className = 'participant-card participant-not-visited';
    });

    // Обробка кнопки видалення
    participantCard.querySelector('.btn-delete').addEventListener('click', () => {
        participantCard.remove();
    });

    participantsList.appendChild(participantCard);
}