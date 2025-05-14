let page = 1;

function add_data(factsArray) {
    const main = document.getElementById('main');
    factsArray.forEach(text => {
        const p = document.createElement('p');
        p.textContent = '💡 ' + text;
        main.appendChild(p);
    });
}

// ✅ Підхід 1 — fetch (10 запитів паралельно)
function fetchDatabyfetch() {
    const urls = Array.from({ length: 10 }, () =>
        fetch('https://uselessfacts.jsph.pl/api/v2/facts/random?language=en')
            .then(res => res.json())
            .then(data => data.text)
    );

    Promise.all(urls)
        .then(facts => {
            add_data(facts);
            page++;
            setTimeout(fetchDatabyfetch, 5000);
        })
        .catch(console.error);
}

// ✅ Підхід 2 — async/await (10 запитів паралельно)
async function fetchDatabyasync() {
    try {
        const promises = Array.from({ length: 10 }, async () => {
            const res = await fetch('https://uselessfacts.jsph.pl/api/v2/facts/random?language=en');
            const data = await res.json();
            return data.text;
        });

        const facts = await Promise.all(promises);
        add_data(facts);
        page++;
        setTimeout(fetchDatabyasync, 5000);
    } catch (error) {
        console.error(error);
    }
}

// ✅ Підхід 3 — XMLHttpRequest (10 запитів по черзі)
function fetchDatabyXHR() {
    let count = 0;
    const results = [];

    function requestOne() {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', 'https://uselessfacts.jsph.pl/api/v2/facts/random?language=en', true);

        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                const data = JSON.parse(xhr.responseText);
                results.push(data.text);
                count++;
                if (count < 10) {
                    requestOne();
                } else {
                    add_data(results);
                    page++;
                    setTimeout(fetchDatabyXHR, 5000);
                }
            }
        };

        xhr.send();
    }

    requestOne();
}

// ❗ Активуй лише один із трьох варіантів:
fetchDatabyfetch();
// fetchDatabyasync();
// fetchDatabyXHR();
