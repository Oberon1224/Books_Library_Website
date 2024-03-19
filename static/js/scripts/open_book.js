
/**
*Функция открытия и закрытие окна закладки
	* @param {boolean} marker_state - состояния окна (false - закрыто, true - открыто)
*/
$(document).ready(function(){
    var marker_state=false;
    $("#btn_show_marker").click(function(){
        if (!marker_state)
        {
            $('.container_marker').css('visibility','visible');
            marker_state = true;
        }
        else
        {
            $('.container_marker').css('visibility','hidden');
            marker_state = false;
        }
    });
});


/**
*Функция открытия и закрытие окна заметок
	* @param {boolean} notes_state - состояния окна (false - закрыто, true - открыто)
*/
$(document).ready(function(){
    var notes_state=false;
    $("#show_notes").click(function(){
        if (!notes_state)
        {
            $('.container_notes').css('visibility','visible');
            notes_state = true;
        }
        else
        {
            $('.container_notes').css('visibility','hidden');
            notes_state = false;
        }
    });
});


/**
*Функция отображения книги во весь экран
*/
$(document).ready(function(){
    $("#scale_size").click(function(){
      $("#menu_book_id").css("top","-1940px");
      $("#book_window").css("left","0px");
      $("#book_window").css("top","-905px");
      $("#book_window").css("width","2220px");
      $("#book_window").css("height","888px");
      $("#frame_book").css("height","1888px");
      $("#frame_book").css("width","2220px");
    });
});


/**
*Функция свернуть окно книги
*/
$(document).ready(function(){
  $("#return_size").click(function(){
    $("#menu_book_id").css("top","-770px");
    $("#book_window").css("left","375px");
    $("#book_window").css("top","-585px");
    $("#book_window").css("width","1150px");
    $("#book_window").css("height","888px");
    $("#frame_book").css("height","720px");
    $("#frame_book").css("width","1150px");
  });
});


/**
*ajax запрос изменения страницы закладки
	* @param {string} type - метод POST
	* @param {string} url - маршрут flask для изменения страницы закладки
    * @param {string} new_page - новый страница закладки
    * @param {number} id_book - id книги
*/
$(document).ready(function() {
    $('#btn_change_marker').click(function(event) {
       event.preventDefault();
       $.ajax({
          type: 'POST',
          url: '/change_page_marker',
          data: {new_page: $('#value_marker').val(), id_book: id_book},
          success: function() {
             alert('Страница закладки изменена!');
          }
       });
    });
 });


/**
*ajax запрос добавления заметки
	* @param {string} type - метод POST
	* @param {string} url - маршрут flask для изменения страницы закладки
    * @param {string} text_note - текст новой заметки
    * @param {number} id_book - id книги
*/
$(document).ready(function() {
    $('#add_note_button').click(function(event) {
       $.ajax({
          type: 'POST',
          url: '/add_note',
          data: {text_note: $('#input_field_note').val(), id_book: id_book},
          success: function() {
             alert('Заметка добавлена!');
          }
       });
    });
 });
