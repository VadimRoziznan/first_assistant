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

    /* Получаем Номер цеха(корпуса) */
 /*   const selectElement = document.getElementById('factory_number');

    selectElement.addEventListener('change', function() {
        const selectedOption = selectElement.options[selectElement.selectedIndex].value;
        console.log(selectedOption);
        fetch('/create-order/')
        .then(response => {
            // Обработка полученного ответа
            return response;
          })
        .then(console.log(response))
    });*/


    /*const selectElement = document.getElementById('factory_number');
    selectElement.addEventListener('change', function () {
        const selectedOption = selectElement.options[selectElement.selectedIndex].value;
        console.log(selectedOption);
        fetch('/create-order/')
          .then(response => {
            return response;
          })
      });*/


      /*const selectElement = document.getElementById('factory_number');
      selectElement.addEventListener('change', function () {
          const selectedOption = selectElement.options[selectElement.selectedIndex].value;
          console.log(selectedOption);
      
          // Создаем объект FormData и добавляем выбранную опцию
          const formData = new FormData();
          formData.append('selectedOption', selectedOption);
      
          // Отправляем запрос на сервер с использованием метода POST и передаем данные formData
          fetch('/create-order/', {
              method: 'POST',
              body: formData
          })
          .then(response => {
              return response; // Возвращает ответ сервера
          })
      });*/



      const selectElement = document.getElementById('factory_number');
      selectElement.addEventListener('change', function () {
          const selectedOption = selectElement.options[selectElement.selectedIndex].value;
          console.log(selectedOption);
      
          // Получаем CSRF-токен из куки
          const csrftoken = getCookie('csrftoken');
      
          // Создаем объект FormData и добавляем выбранную опцию
          const formData = new FormData();
          formData.append('selectedOption', selectedOption);

          const data = {
            factory_number: selectedOption
          };
          
          const jsonData = JSON.stringify(data);
      
          // Отправляем запрос на сервер с использованием метода POST, устанавливаем заголовок X-CSRFToken
          fetch('/create-order/', {
              method: 'PUT',
              body: jsonData,
              headers: {
                  'X-CSRFToken': csrftoken
              }
          })
          .then(response => {
              return response; // Возвращает ответ сервера
          })
      });
      
      // Функция для получения CSRF-токена из куки
      function getCookie(name) {
          let cookieValue = null;
          if (document.cookie && document.cookie !== '') {
              const cookies = document.cookie.split(';');
              for (let i = 0; i < cookies.length; i++) {
                  const cookie = cookies[i].trim();
                  // Находим куку с именем name
                  if (cookie.substring(0, name.length + 1) === (name + '=')) {
                      cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                      break;
                  }
              }
          }
          return cookieValue;
      }

    

    

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








