function adjustTextareaHeight(element) {
    element.style.height = element.scrollHeight + 'px';
}

function moveCursorToStart(element) {
    element.focus();
    element.setSelectionRange(0, 0);
}

/*document.getElementsByClassName("add-field-btn").addEventListener("click", function() { 
    console.log('click');
    const formContainer = document.getElementById("orders-create-block"); 
    const inputField = document.createElement("tr"); 
    inputField.classList.add("input-field"); 
    inputField.innerHTML = '<input type="text" name="field[]" />'; 
    formContainer.appendChild(inputField); 
});*/


document.addEventListener("DOMContentLoaded", function() {
    const addFieldBtn = document.querySelector(".add-field-btn");
    const RemoveFieldBtn = document.querySelector(".remove-field-btn");
    const formContainer = document.getElementById("orders-create-block"); 
    const orderPosition = document.querySelector("order-position");
    let idNumberNewField = 2;

    addFieldBtn.addEventListener("click", () => {
        const table = document.querySelector('tbody'); // Выбираем таблицу
        const newRow = document.createElement('tr'); // Создаем новую строку

        newRow.id = 'orders-create-block';
        

        // Получаем содержимое существующей строки
        const existingRow = document.querySelector('#orders-create-block');
        /*existingRow.lastElementChild.id = `number_${idNumberNewField}`;*/
        
        const rowContent = existingRow.innerHTML;

        newRow.innerHTML = rowContent; // Копируем содержимое в новую строку
        const textarea = newRow.querySelector('textarea');
        textarea.style.height = '18px';
        /*newRow.style.height = '';*/
        
        table.appendChild(newRow); // Добавляем новую строку в таблицу
        const newTextArea = newRow.querySelector('.order-position');
        const newInputField = newRow.querySelector('.order-quantity');
        const newUnitSelect = newRow.querySelector('.select-order');
        newTextArea.value = '';
        newTextArea.setAttribute('name', `textarea_${idNumberNewField}`);
        newInputField.setAttribute('name', `quantity_${idNumberNewField}`);
        newUnitSelect.setAttribute('name', `unit_${idNumberNewField}`);
        moveCursorToStart(newTextArea);
        newRow.firstElementChild.id = `number_${idNumberNewField}`;
        document.getElementById(`number_${idNumberNewField}`).textContent = idNumberNewField + '.';
        idNumberNewField++;
    });

    RemoveFieldBtn.addEventListener("click", () => {
        const table = document.querySelector('tbody'); // Выбираем таблицу
        if (table.childElementCount > 2) {
            table.removeChild(table.lastElementChild);
            idNumberNewField--; 
        }
    });

  });


