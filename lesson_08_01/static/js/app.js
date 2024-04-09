var data = [];
var type = '';

async function fetchData(api) {
    try {
        const response = await fetch(api);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        data = await response.json();
        type = api;
        renderData();
    } catch (error) {
        console.error('Error fetching data', error);
    }
}

function renderData() {
    var list = document.getElementById('list');
    list.innerHTML = '';
    data.forEach((item, index) => {
        var listItem = document.createElement('li');
        listItem.className = 'list-group-item';
        listItem.textContent = type === '/api/books/' ? item.title : item.name;
        list.appendChild(listItem);
    });
}

var app = document.getElementById('app');

var booksButton = document.createElement('button');
booksButton.className = 'btn btn-primary m-2';
booksButton.textContent = 'Books';
booksButton.onclick = function() { fetchData('/api/books/'); };
app.appendChild(booksButton);

var authorsButton = document.createElement('button');
authorsButton.className = 'btn btn-primary m-2';
authorsButton.textContent = 'Authors';
authorsButton.onclick = function() { fetchData('/api/authors/'); };
app.appendChild(authorsButton);

var list = document.createElement('ul');
list.id = 'list';
list.className = 'list-group mt-4';
app.appendChild(list);