/**
* Функция добавление нового элемента option в select со значением из другого option
    * @function add_in_list
    * @param {string} id элемента из которого копируются данные
    * @param {string} id элемента куда копируются данные
*/
function add_in_list(id_from, id_to){
 //создание элемента option    
  const newDiv = document.createElement("option");

   //получения выбранного option из select
  var value = $(id_from).text();
  //помещение текста в option
  const newContent = document.createTextNode(value);

  //установка новому option свойство selected
  newDiv.setAttribute('selected','selected')

  //добавление текста в option
  newDiv.appendChild(newContent);

  //Получение select для добавления нового тега 
  const currentDiv = document.getElementById(id_to);
  currentDiv.append(newDiv);
};


/**
* ajax запрос добавления нового тэга
	 * @param {string} type - метод POST
	 * @param {string} url - маршрут flask для добавления нового тэга
    * @param {string} tag - название нового тэга
*/
$(document).ready(function() {
   $('#new_tag').click(function(event) {
      event.preventDefault();
      $.ajax({
         type: 'POST',
         url: '/add_new_tag',
         data: {tag:$('#new_tag_book_id').val()},
         success: function() {
            alert('Тэг добавлен!');
         }
      });
   });
});


/**
* ajax запрос добавления нового автора
	 * @param {string} type - метод POST
	 * @param {string} url - маршрут flask для добавления нового автора
    * @param {string} surname - фамилия нового автора
    * @param {string} name - имя нового автора
    * @param {string} patronymic - отчество нового автора
*/
$(document).ready(function() {
   $('#btn_new_author').click(function(event) {
      event.preventDefault();
      $.ajax({
         type: 'POST',
         url: '/add_new_author',
         data: {surname:$('#surname_author_id').val(), name:$('#name_author_id').val(), patronymic:$('#patronymic_author_id').val()},
         success: function() {
            alert('Автор добавлен!');
         }
      });
   });
});


/**
* ajax запрос добавления новой книги
	 * @param {string} type - метод POST
	 * @param {string} url - маршрут flask для добавления новой книги
    * @param {html} tags - список тэгов для новой книги
    * @param {html} authors - список авторов для новой книги
    * @param {string} title - название новой книги
    * @param {number} page - количество страниц новой книги
    * @param {string} path_book - путь к файлу новой книги
    * @param {string} path_image - путь к изображению новой книги
    * @param {string} category - категория новой книги
    * @param {string} language - язык новой книги
    * @param {string} year - год издания новой книги
    * @param {string} year - описание новой книги
*/
$(document).ready(function() {
   $('#btn_add_file').click(function(event) {
      event.preventDefault();
      $.ajax({
         type: 'POST',
         url: '/add_file',
         data: {tags:$('#selected_tags').html(), authors:$('#selected_authors_list').html(), title: $('#title_book').val(),
               page: $('#count_pages').val(), path_book: $('#path_file_book').val(), path_image: $('#path_image_book').val(),
               category: $('#category_book').val(), language: $('#language_book').val(), year: $('#year_book').val(), 
               description: $('#description_book_id').val()
         },
         success: function() {
            alert('Книга добавлена!');
         }
      });
   });
});

