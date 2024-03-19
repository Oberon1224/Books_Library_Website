/**
*ajax запрос изменения названия книги
	 * @param {string} type - метод POST
	 * @param {string} url - маршрут flask для изменения названия книги
    * @param {string} title - новое название книги
    * @param {number} id_book - id книги
*/
$(document).ready(function() {
    $('#change_name_book').click(function(event) {
       event.preventDefault();
       $.ajax({
          type: 'POST',
          url: '/change_title',
          data: {title: $('#title_book').val(), id_book: id_book},
          success: function() {
             alert('Название изменено!');
          }
       });
    });
 });


/**
*ajax запрос изменения количества страниц книги
	 * @param {string} type - метод POST
	 * @param {string} url - маршрут flask для изменения количества страниц книги
    * @param {number} page - новое количество страниц книги
    * @param {number} id_book - id книги
*/
 $(document).ready(function() {
    $('#change_page_book').click(function(event) {
       event.preventDefault();
       $.ajax({
          type: 'POST',
          url: '/change_page',
          data: {page: $('#count_pages').val(), id_book: id_book},
          success: function() {
             alert('Количество страниц изменено!');
          }
       });
    });
 });


/**
*ajax запрос изменения пути к файлу книги
	 * @param {string} type - метод POST
	 * @param {string} url - маршрут flask для изменения пути к файлу книги
    * @param {string} path_book - новый путь к файлу книги
    * @param {number} id_book - id книги
*/
 $(document).ready(function() {
    $('#change_path_book').click(function(event) {
       event.preventDefault();
       $.ajax({
          type: 'POST',
          url: '/change_path_book',
          data: {path_book: $('#path_file_book').val(), id_book: id_book},
          success: function() {
             alert('Путь к файлу книги изменен!');
          }
       });
    });
 });


/**
*ajax запрос изменения пути к изображению книги
	 * @param {string} type - метод POST
	 * @param {string} url - маршрут flask для изменения пути к изображению книги
    * @param {string} path_image - новый путь к изображнию книги
    * @param {number} id_book - id книги
*/
 $(document).ready(function() {
    $('#change_path_image_book').click(function(event) {
       event.preventDefault();
       $.ajax({
          type: 'POST',
          url: '/change_path_image',
          data: {path_image: $('#path_image_book').val(), id_book: id_book},
          success: function() {
             alert('Путь к изображению книги изменен!');
          }
       });
    });
 });


/**
*ajax запрос изменения категории книги
	 * @param {string} type - метод POST
	 * @param {string} url - маршрут flask для изменения категории книги
    * @param {string} category - новая категория книги
    * @param {number} id_book - id книги
*/
 $(document).ready(function() {
    $('#change_category_book').click(function(event) {
       event.preventDefault();
       $.ajax({
          type: 'POST',
          url: '/change_category',
          data: {category: $('#category_book').val(), id_book: id_book},
          success: function() {
             alert('Категория книги изменена!');
          }
       });
    });
 });


 /**
*ajax запрос изменения языка книги
	 * @param {string} type - метод POST
	 * @param {string} url - маршрут flask для изменения языка книги
    * @param {string} language - новый язык книги
    * @param {number} id_book - id книги
*/
 $(document).ready(function() {
    $('#change_language_book').click(function(event) {
       event.preventDefault();
       $.ajax({
          type: 'POST',
          url: '/change_language',
          data: {language: $('#language_book').val(), id_book: id_book},
          success: function() {
             alert('Язык книги изменен!');
          }
       });
    });
 });


 /**
*ajax запрос изменения года издания книги
	 * @param {string} type - метод POST
	 * @param {string} url - маршрут flask для изменения года издания книги
    * @param {number} year - новый год издания книги
    * @param {number} id_book - id книги
*/
 $(document).ready(function() {
    $('#change_year_book').click(function(event) {
       event.preventDefault();
       $.ajax({
          type: 'POST',
          url: '/change_year',
          data: {year: $('#year_book').val(), id_book: id_book},
          success: function() {
             alert('Год издания книги изменен!');
          }
       });
    });
 });


/**
*ajax запрос изменения описания книги
	 * @param {string} type - метод POST
	 * @param {string} url - маршрут flask для изменения описания книги
    * @param {string} description - новое описание книги
    * @param {number} id_book - id книги
*/
 $(document).ready(function() {
    $('#btn_change_description').click(function(event) {
       event.preventDefault();
       $.ajax({
          type: 'POST',
          url: '/change_description',
          data: {description: $('#description_book_id').val(), id_book: id_book},
          success: function() {
             alert('Описание книги изменено!');
          }
       });
    });
 });



/**
*ajax запрос добавления автора/авторов к книге
	 * @param {string} type - метод POST
	 * @param {string} url - маршрут flask для добавления автора/авторов к книге
    * @param {html} authors - автор/авторы 
    * @param {number} id_book - id книги
*/
 $(document).ready(function() {
    $('#btn_add_list_authors').click(function(event) {
       event.preventDefault();
       $.ajax({
          type: 'POST',
          url: '/change_add_author',
          data: {authors: $('#selected_authors_list').html(), id_book: id_book},
          success: function() {
             alert('Автор/авторы добавлены к книге!');
          }
       });
    });
 });


/**
*ajax запрос добавления тэга/тэгов к книге
	 * @param {string} type - метод POST
	 * @param {string} url - маршрут flask для добавления тэга/тэгов к книге
    * @param {html} tags - тэг/тэги
    * @param {number} id_book - id книги
*/
$(document).ready(function() {
   $('#change_list_tags').click(function(event) {
       event.preventDefault();
       $.ajax({
          type: 'POST',
          url: '/change_add_tag',
          data: {tags: $('#selected_tags').html(), id_book: id_book},
          success: function() {
             alert('Тэг/тэги добавлены к книге!');
          }
       });
    });
 });