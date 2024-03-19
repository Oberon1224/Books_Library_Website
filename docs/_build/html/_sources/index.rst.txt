.. Library books documentation master file, created by
   sphinx-quickstart on Sat Mar 16 00:34:29 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Документация
============

.. toctree::
   :maxdepth: 25

   main
   settings
   database
   modules
   blueprints
   
   
JavaScript код
==============

add_file.js
--------------

	..  code-block:: javascript

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

	..  code-block:: javascript
	
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

	..  code-block:: javascript
	
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

	..  code-block:: javascript
	
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


change_file.js
--------------

	..  code-block:: javascript
	
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

	..  code-block:: javascript

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

	..  code-block:: javascript
	
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

	..  code-block:: javascript

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

	..  code-block:: javascript
	
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

	..  code-block:: javascript

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

	..  code-block:: javascript
	
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

	..  code-block:: javascript

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

	..  code-block:: javascript

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

	..  code-block:: javascript

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
   
   
change_state.js
---------------

	..  code-block:: javascript
   
		/**
		*ajax запрос добавления книги в избранное
			* @param {string} type - метод POST
			* @param {string} url - маршрут flask для добавления книги в избранное
			* @param {string} login - логин пользователя
			* @param {string} id_book - id книги
		*/
		function change_state_favorite(login, id_book)
		{
			$(document).ready(function() {
				$('#favorite'+id_book).click(function(event) {
					event.preventDefault();
					$.ajax({
					type: 'POST',
					url: '/' + login + '/change_on_favorite/' + id_book,
					success: function(){ 
							alert('Книга добавлена в избранное');
						}
					});
				});
			});
		}
		
	..  code-block:: javascript
	
		/**
		*ajax запрос добавления книги на чтение
			* @param {string} type - метод POST
			* @param {string} url - маршрут flask для добавления книги на чтение
			* @param {string} login - логин пользователя
			* @param {string} id_book - id книги
		*/
		function change_state_in_read(login, id_book)
		{
			$(document).ready(function() {
				$('#in_read'+id_book).click(function(event) {
					event.preventDefault();
					$.ajax({
					type: 'POST',
					url: '/' + login + '/change_in_read/' + id_book,
					success: function(){ 
							alert('Книга добавлена на чтение');
						}
					});
				});
			});
		}

	..  code-block:: javascript
	
		/**
		*ajax запрос добавления книги в прочитанное
			* @param {string} type - метод POST
			* @param {string} url - маршрут flask для добавления книги в прочитанное
			* @param {string} login - логин пользователя
			* @param {string} id_book - id книги
		*/
		function change_state_end_read(login, id_book)
		{
			$(document).ready(function() {
				$('#end_read'+id_book).click(function(event) {
					event.preventDefault();
					$.ajax({
					type: 'POST',
					url: '/' + login + '/change_end_read/' + id_book,
					success: function(){ 
							alert('Книга перенесена в прочитанное');
						}
					});
				});
			});
		}   
   
filter_scripts.js
-----------------

	..  code-block:: javascript
	
		/**
		*Функция открытия и закрытие окна фильтра
			* @param {boolean} filter_state - состояния окна (false - закрыто, true - открыто)
		*/
		$(document).ready(function(){
			var filter_state = false;
			$("#button_filter_id").click(function(){
				if (!filter_state)
				{
					$(".button_filter").css('visibility', 'visible');
					$(".select_filter").css('visibility', 'visible');
					$("#filter_main_window").css('visibility', 'visible');
					filter_state = true;
				}
				else
				{
					$(".button_filter").css('visibility', 'hidden');
					$(".select_filter").css('visibility', 'hidden');
					$("#filter_main_window").css('visibility', 'hidden');
					filter_state = false;
				}
			});
		});
		
		
main_scripts.js
-----------------

	..  code-block:: javascript		
		
		/**
		*Функция изменения расположение элементов при нажатии кнопки скрыть
		*/
		$(document).ready(function(){
		  $("#button_hide_id").click(function(){
			$("#button_show_id").show();
			$("#button_show_id").css("visibility","visible");
			$(".menu_button").hide()
			$(this).hide();
			$(".main_window_library").css("position","absolute");
			$(".main_window_library").css("left","0px");
			$(".main_window_library").css("top","-155px");
			$("#menu_style").css("top","-5px");
			$("#button_style1").css("top","250px");
			$("#button_style2").css("top","250px");
			$("#button_style3").css("top","250px");
			$("#button_style4").css("top","250px");
			$("#button_style5").css("top","250px");
		  });
		});


	..  code-block:: javascript
	
		/**
		*Функция изменения расположение элементов при нажатии кнопки показать
		*/
		$(document).ready(function(){
		  $("#button_show_id").click(function(){
			$("#button_hide_id").show();
			$(".menu_button").show();//++
			$(this).hide();//++
			$(".main_window_library").css("position","absolute");
			$(".main_window_library").css("left","0px");
			$(".main_window_library").css("top","0px");
			$("#menu_style").css("top","150px");
			$("#button_style1").css("top","250px");
			$("#button_style2").css("top","250px");
			$("#button_style3").css("top","250px");
			$("#button_style4").css("top","250px");
			$("#button_style5").css("top","250px");
		  });
		});

	..  code-block:: javascript

		/**
		*Функция динамичного повяления и исчезновения кнопок для изменения стилей
		*/
		$(document).ready(function(){
		  $(".button_style").hover(
			function(){
			  $(".button_style_position1").css("visibility","visible");
			  $(".button_style_position2").css("visibility","visible");
			  $(".button_style_position3").css("visibility","visible");
			  $(".button_style_position4").css("visibility","visible");
			  $(".button_style_position5").css("visibility","visible");
			},
			function(){
			  $(".button_style_position1").css("visibility","hidden");
			  $(".button_style_position2").css("visibility","hidden");
			  $(".button_style_position3").css("visibility","hidden");
			  $(".button_style_position4").css("visibility","hidden");
			  $(".button_style_position5").css("visibility","hidden");
			}); 
		});

	..  code-block:: javascript

		/**
		*Функция передвижения меню пользователя в процессе скроллинга
		*/
		window.addEventListener('scroll', function() {
		  $(document).ready(function(){
			var elemValueScroll = 320;
			var valueScroll = String (window.pageYOffset+elemValueScroll);
			var setValueScroll = valueScroll + "px";
			$(".user_menu").css("top",setValueScroll); 
		  });
		});


open_book.js
-----------------

	..  code-block:: javascript		 
			
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

	..  code-block:: javascript	
	
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

	..  code-block:: javascript	
	
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

	..  code-block:: javascript	
	
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

	..  code-block:: javascript	
	
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

	..  code-block:: javascript	

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

			
shift_style.js
--------------

	..  code-block:: javascript					
			
		/**
		* ajax запрос для стиля 1
			 * @param {string} type - метод POST
			 * @param {string} url - маршрут flask для изменения стиля сайта
		*/
		$(document).ready(function() {
		  $('#button_style1').click(function() {
			 $.ajax({
				type: 'POST',
				url: '/style1'
			 });
		  });
		});

	..  code-block:: javascript		
	
		/**
		* ajax запрос для стиля 2
			 * @param {string} type - метод POST
			 * @param {string} url - маршрут flask для изменения стиля сайта
		*/
		$(document).ready(function() {
		  $('#button_style2').click(function() {
			 $.ajax({
				type: 'POST',
				url: '/style2'
			 });
		  });
		});

	..  code-block:: javascript		
	
		/**
		* ajax запрос для стиля 3
			 * @param {string} type - метод POST
			 * @param {string} url - маршрут flask для изменения стиля сайта
		*/
		$(document).ready(function() {
		  $('#button_style3').click(function() {
			 $.ajax({
				type: 'POST',
				url: '/style3'
			 });
		  });
		});

	..  code-block:: javascript		
	
		/**
		* ajax запрос для стиля 4
			 * @param {string} type - метод POST
			 * @param {string} url - маршрут flask для изменения стиля сайта
		*/
		$(document).ready(function() {
		  $('#button_style4').click(function() {
			 $.ajax({
				type: 'POST',
				url: '/style4'
			 });
		  });
		});

	..  code-block:: javascript		
	
		/**
		* ajax запрос для стиля 5
			 * @param {string} type - метод POST
			 * @param {string} url - маршрут flask для изменения стиля сайта
		*/
		$(document).ready(function() {
		  $('#button_style5').click(function() {
			 $.ajax({
				type: 'POST',
				url: '/style5'
			 });
		  });
		});

	..  code-block:: javascript		

		/**
		* Функция изменения задания стиля 1
			* @function style1
			* Меняет стиль некоторых элементов сайта.
		*/
		function style1(){
		   // Класс кнопок low_button (все кнопки кроме верхник и кнопок меню пользователя)
		   $(".low_button").css("color","rgb(22, 22, 22)");  
		   $(".low_button").css("background-color","rgb(255,174,66)");     
		   $(".low_button").css("box-shadow","0px 0px 0px 0px rgb(44, 7, 7),0px 6px 12px 0px" +
											"rgba(44, 7, 7, 0.98),1px 23px 23px 0px rgba(44, 7, 7, 0.85)," + 
											"2px 51px 31px 0px rgba(44, 7, 7, 0.5),4px 90px 36px 0px" + 
											"rgba(44, 7, 7, 0.15),6px 141px 40px 0px rgba(44, 7, 7, 0.02)");     
		   //Фильтр
		   $(".filter_window").css("background-color","rgb(244,159,47)");  
		   $(".container_selected_attributes").css("background-color","rgb(237,118,14)");  
		   $(".select_filter").css("background-color","rgb(244,159,47)");  
		   //Кнопка найти
		   $(".button_search_class").css("box-shadow","0px 0px 0px 0px rgb(44, 7, 7),0px 6px 12px 0px rgba(44, 7, 7, 0.98)," + 
													 "1px 23px 23px 0px rgba(44, 7, 7, 0.85),2px 51px 31px 0px rgba(44, 7, 7, 0.5)," + 
													 "4px 90px 36px 0px rgba(44, 7, 7, 0.15),6px 141px 40px 0px rgba(44, 7, 7, 0.02)");         
		   $(".button_search_class").css("background","rgb(244,159,47)"); 
		   $(".button_search_class").css("color","black");    

		   //Добавление и изменение информации о файле (Добавить, Изменить)
		   $(".add_file_class").css("background-color","rgb(244,159,47)"); 
		   $(".div_add_information_book").css("background-color","rgb(237,118,14)"); 
		   $(".add_book_author").css("background-color","rgb(237,118,14)"); 
		   $(".add_book_tags").css("background-color","rgb(237,118,14)"); 
		   $(".description_book").css("background-color","rgb(237,118,14)"); 

		   //Заметки (Открыть)
		   //Задний фон окна заметок
		   $(".container_notes").css("background-color","rgb(255,174,66)"); 
		   //Добавление и изменение (таблица заметок)
		   $(".table_notes").css("background-color","rgb(255,174,66)"); 
		   $(".table_notes").css("color","rgb(0,0,0)"); 

		   //Верхние кнопки
		   $(".menu_button").css("color","rgb(0, 0, 0)");
		   $(".menu_button").css("background-color","rgb(255,174,66)");   

		   //Главное окно сайта
		   $(".main_window_library").css("box-shadow"," 0px 0px 0px 0px rgb(0, 0, 0),12px 12px 37px 0px rgba(0, 0, 0, 0.98)," + 
														"46px 49px 67px 0px rgba(0, 0, 0, 0.85),104px 110px 91px 0px rgba(0, 0, 0, 0.5)," + 
														"185px 195px 108px 0px rgba(0, 0, 0, 0.15),289px 305px 118px 0px rgba(244,159,47, 0.02)");           
		   $(".main_window_library").css("background","rgb(255,174,66)");
		   
		   //Меню пользователя
		   //Задний фон меню пользователя
		   $(".user_menu").css("background-color","rgba(255,174,66, 1)");
		   //Кнопки меню пользователя с подсветкой
		   $("user_icon_name").css("background-color","rgb(0, 0, 0)"); 
		   $("user_icon_name").css("box-shadow","0px 0px 69.36000061035156px rgba(244,159,47, 1)");     
		   //Кнопки меню пользователя с подсветкой
		   $(".button_user_menu").css("background-color","rgb(255,174,66)");  
		   $(".button_user_menu").css("box-shadow","0px 0px 69.36000061035156px rgba(240, 255, 255, 1)");                
		   $(".button_user_menu").css("color","black");  

		   //Блоки книги
		   //Контейнеры тэгов в блоках книг
		   $(".tag_book").css("background-color","rgb(255,111,66)");  
		   $(".tag_book").css("box-shadow","0px 0px 69.36000061035156px rgba(255,174,66, 1)");                
		   $(".tag_book").css("color","white");  
		   //Контейнер описания книги
		   $(".text_book").css("color","black");
		   $(".text_book").css("background-color","rgb(227,146,79)");
		   $(".text_book").css("box-shadow","0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px" + 
											"rgba(127, 107, 107, 0.98),46px 49px 67px 0px " + 
											"rgba(0, 0, 0, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5)," + 
											"185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02)");   
		   //Название книги
		   $(".label_title").css("color","rgb(255, 255, 255)");   
		   $(".label_title").css("background-color","rgb(237,118,14)");
		   $(".label_title").css("box-shadow","0px 0px 69.36000061035156px rgba(244,159,47, 0.8)");
		   //Автор книги
		   $(".label_author").css("color","rgb(255, 255, 255)");           
		   $(".label_author").css("background-color","rgb(244,159,47");
		   $(".label_author").css("background-color","0px 0px 69.36000061035156px rgba(240, 44, 5, 1)");          
		   //Тэги
		   $(".tag_container").css("background-color","rgb(237,118,14)");  
		   $(".tag_container").css("box-shadow","0px 0px 69.36000061035156px rgba(227,146,79, 1)");                
		   $(".tag_container").css("color","black");  
		   //Один блок книги      ^
		   $(".books_block").css("box-shadow","0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px rgba(0, 0, 0, 0.98)," + 
											   "46px 49px 67px 0px rgba(0, 0, 0, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5)," + 
											   "185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02)");         
		   $(".books_block").css("background","rgba(198,97,12, 1)");         
		   //Контейнер информации книги        
		   $(".container_book_info").css("background","rgba(255, 255, 255, 0.45");

		};

	..  code-block:: javascript		

		/**
		* Функция изменения задания стиля 2
			* @function style2
			* Меняет стиль некоторых элементов сайта.
		*/
		function style2(){
		   // Класс кнопок low_button (все кнопки кроме верхник и кнопок меню пользователя)
		   $(".low_button").css("color","rgb(0, 0, 0)");  
		   $(".low_button").css("background-color","rgba(128, 128, 128, 1)");   
		   $(".low_button").css("box-shadow","0px 0px 0px 0px rgb(44, 22, 7),0px 6px 12px 0px" +
											   "rgba(44, 7, 7, 0.2),1px 23px 23px 0px rgba(44, 7, 7, 0.2)," + 
											   "2px 51px 31px 0px rgba(44, 7, 7, 0.5),4px 90px 36px 0px" + 
											   "rgba(44, 7, 7, 0.15),6px 141px 40px 0px rgba(44, 7, 7, 0.02)");   
		   //Фильтр
		   $(".filter_window").css("background-color","rgb(157,161,170)");  
		   $(".container_selected_attributes").css("background-color","rgb(157,161,170)");  
		   $(".select_filter").css("background-color","rgb(222,211,213)");  
		   //Кнопка найти
		   $(".button_search_class").css("box-shadow","0px 0px 0px 0px rgb(44, 7, 7),0px 6px 12px 0px rgba(44, 7, 7, 0.98)," + 
													 "1px 23px 23px 0px rgba(44, 7, 7, 0.85),2px 51px 31px 0px rgba(44, 7, 7, 0.5)," + 
													 "4px 90px 36px 0px rgba(44, 7, 7, 0.15),6px 141px 40px 0px rgba(44, 7, 7, 0.02)");         
		   $(".button_search_class").css("background","rgba(157,161,170, 1)"); 
		   $(".button_search_class").css("color","black"); 

		   //Добавление и изменение информации о файле (Добавить, Изменить)
		   $(".add_file_class").css("background-color","rgb(157,161,170)"); 
		   $(".div_add_information_book").css("background-color","rgba(55,55,55, 1)"); 
		   $(".add_book_author").css("background-color","rgba(55,55,55, 1)"); 
		   $(".add_book_tags").css("background-color","rgba(55,55,55, 1)"); 
		   $(".description_book").css("background-color","rgba(55,55,55, 1)"); 

		   //Заметки (Открыть)
		   //Задний фон окна заметок
		   $(".container_notes").css("background-color","rgb(157,161,170)"); 
		   //Добавление и изменение (таблица заметок)
		   $(".table_notes").css("background-color","rgb(157,161,170)"); 
		   $(".table_notes").css("color","rgb(0, 0, 0)"); 
		   //Верхние кнопки
		   $(".menu_button").css("color","rgb(0, 0, 0)");
		   $(".menu_button").css("background-color","rgb(157,161,170)");
		   //Главное окно сайта
		   $(".main_window_library").css("box-shadow"," 0px 0px 0px 0px rgb(0, 0, 0),12px 12px 37px 0px rgba(0, 0, 0, 0.98)," + 
														"46px 49px 67px 0px rgba(0, 0, 0, 0.85),104px 110px 91px 0px rgba(0, 0, 0, 0.5)," + 
														"185px 195px 108px 0px rgba(0, 0, 0, 0.15),289px 305px 118px 0px rgba(0, 0, 0, 0.02)");           
		   $(".main_window_library").css("background","linear-gradient(to bottom, rgb(123, 115, 110), rgba(100, 100, 100, 0.98)," + 
													 " rgb(55, 55, 55), rgb(45 45 45 / 98%), rgb(65, 65, 65))");
			
		   //Меню пользователя
		   //Задний фон меню пользователя
		   $(".user_menu").css("background-color","rgba(157,161,170, 1)");
		   //Изображение пользователя
		   $(".user_icon_name").css("background-color","rgba(157,161,170, 1)"); 
		   $(".user_icon_name").css("box-shadow","0px 0px 69.36000061035156px rgba(240, 244, 225, 1)");     
		   //Кнопки меню пользователя с подсветкой
		   $(".button_user_menu").css("background-color","rgb(157,161,170)");  
		   $(".button_user_menu").css("box-shadow","0px 0px 69.36000061035156px rgba(240, 255, 255, 1)");                
		   $(".button_user_menu").css("color","black");  

		   //Блоки книги
		   //Контейнеры тэгов в блоках книг
		   $(".tag_book").css("background-color","rgb(55,111,89)");  
		   $(".tag_book").css("box-shadow","0px 0px 69.36000061035156px rgba(33,33,89, 1)");                
		   $(".tag_book").css("color","white");  
		   //Контейнер описания книги
		   $(".text_book").css("color","white");
		   $(".text_book").css("background-color","rgb(111, 111, 111)");
		   $(".text_book").css("box-shadow","0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px" + 
											"rgba(127, 107, 107, 0.98),46px 49px 67px 0px " + 
											"rgba(0, 0, 0, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5)," + 
											"185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02)");   
		   //Название книги
		   $(".label_title").css("color","rgb(0, 0, 0)");     
		   $(".label_title").css("background-color","rgb(157,161,170)");
		   $(".label_title").css("box-shadow","0px 0px 69.36000061035156px rgba(22, 22, 22, 1)");
		   //Автор книги
		   $(".label_author").css("color","rgb(255, 255, 255)");           
		   $(".label_author").css("background-color","rgb(65, 65, 55");
		   $(".label_author").css("box-shadow","0px 0px 69.36000061035156px rgba(22, 22, 22, 1)");        
		   //Тэги
		   $(".tag_container").css("background-color","rgb(33,33,33)");  
		   $(".tag_container").css("box-shadow","0px 0px 69.36000061035156px rgba(240, 255, 255, 1)");                
		   $(".tag_container").css("color","white");  
		   //Один блок книги
		   $(".books_block").css("box-shadow","0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px rgba(0, 0, 0, 0.98)," + 
											   "46px 49px 67px 0px rgba(0, 0, 0, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5)," + 
											   "185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02)");         
		   $(".books_block").css("background","rgba(65, 65, 65, 0.45)");         
		   $(".books_block").css("background-color","rgba(65, 65, 65, 0.45)");           
		   //Контейнер информации книги          ^
		   $(".container_book_info").css("background","rgba(188, 188, 188, 0.45"); 

		};

	..  code-block:: javascript		

		/**
		* Функция изменения задания стиля 3
			* @function style3
			* Меняет стиль некоторых элементов сайта.
		*/
		function style3(){
		   // Класс кнопок low_button (все кнопки кроме верхник и кнопок меню пользователя)
		   $(".low_button").css("color","rgb(255, 255, 255)");  
		   $(".low_button").css("background-color","rgb(49,54,89)");     
		   $(".low_button").css("box-shadow","0px 0px 0px 0px rgb(44, 7, 7),0px 6px 12px 0px" +
											"rgba(44, 7, 7, 0.98),1px 23px 23px 0px rgba(44, 7, 7, 0.85)," + 
											"2px 51px 31px 0px rgba(44, 7, 7, 0.5),4px 90px 36px 0px" + 
											"rgba(44, 7, 7, 0.15),6px 141px 40px 0px rgba(44, 7, 7, 0.02)");     

		   //Фильтр
		   $(".filter_window").css("background-color","rgb(49,54,89)");  
		   $(".container_selected_attributes").css("background-color","rgb(49,54,89)");  
		   $(".select_filter").css("background-color","rgb(222,211,213)");  
		   //Кнопка найти
		   $(".button_search_class").css("box-shadow","0px 0px 0px 0px rgb(44, 7, 7),0px 6px 12px 0px rgba(44, 7, 7, 0.98)," + 
													 "1px 23px 23px 0px rgba(44, 7, 7, 0.85),2px 51px 31px 0px rgba(44, 7, 7, 0.5)," + 
													 "4px 90px 36px 0px rgba(44, 7, 7, 0.15),6px 141px 40px 0px rgba(44, 7, 7, 0.02)");         
		   $(".button_search_class").css("background","rgb(49,54,89)"); 
		   $(".button_search_class").css("color","white"); 

		   //Добавление и изменение информации о файле (Добавить, Изменить)
		   $(".add_file_class").css("background-color","rgb(49,54,89)"); 
		   $(".div_add_information_book").css("background-color","rgb(33,22,42)"); 
		   $(".add_book_author").css("background-color","rgb(33,22,42)"); 
		   $(".add_book_tags").css("background-color","rgb(33,22,42)"); 
		   $(".description_book").css("background-color","rgb(33,22,42)"); 

		   //Заметки (Открыть)
		   //Задний фон окна заметок
		   $(".container_notes").css("background-color","rgb(49,54,89)"); 
		   //Добавление и изменение (таблица заметок)
		   $(".table_notes").css("background-color","rgb(49,54,89)"); 
		   $(".table_notes").css("color","rgb(255,255,255)"); 

		   //Верхние кнопки
		   $(".menu_button").css("color","white");
		   $(".menu_button").css("background-color","rgb(55,66,111)");

		   //Главное окно сайта
		   $(".main_window_library").css("box-shadow"," 0px 0px 0px 0px rgb(0, 0, 0),12px 12px 37px 0px rgba(0, 0, 0, 0.98)," + 
														"46px 49px 67px 0px rgba(49,54,89, 0.85),104px 110px 91px 0px rgba(0, 0, 0, 0.5)," + 
														"185px 195px 108px 0px rgba(49,54,89, 0.15),289px 305px 118px 0px rgba(0, 0, 0, 0.02)");           
		   $(".main_window_library").css("background","linear-gradient(to bottom, rgb(49,54,89), rgba(49,54,89, 0.98),"+" rgb(49,54,89), rgb(49,54,89))");
			 
		   //Меню пользователя
		   //Задний фон меню пользователя
		   $(".user_menu").css("background-color","rgba(55, 111, 111, 1)");
		   //Изображение пользователя
		   $(".user_icon_name").css("background-color","rgb(49,54,89)"); 
		   $(".user_icon_name").css("box-shadow","0px 0px 69.36000061035156px rgba(240, 244, 225, 1)");     
		   //Кнопки меню пользователя с подсветкой
		   $(".button_user_menu").css("background-color","rgb(66,66,89)");  
		   $(".button_user_menu").css("box-shadow","0px 0px 69.36000061035156px rgba(240, 255, 255, 1)");                
		   $(".button_user_menu").css("color","white");  

		   //Блоки книги
		   //Контейнеры тэгов в блоках книг
		   $(".tag_book").css("background-color","rgb(55,111,89)");  
		   $(".tag_book").css("box-shadow","0px 0px 69.36000061035156px rgba(33,33,89, 1)");                
		   $(".tag_book").css("color","white");  
		   //Контейнер описания книги
		   $(".text_book").css("color","white");
		   $(".text_book").css("background-color","rgb(33,33,77)");
		   $(".text_book").css("box-shadow","0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px" + 
											"rgba(127, 107, 107, 0.98),46px 49px 67px 0px " + 
											"rgba(0, 0, 0, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5)," + 
											"185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02)");   
		   //Название книги
		   $(".label_title").css("color","black");     
		   $(".label_title").css("background-color","rgb(211,211,222)");
		   $(".label_title").css("box-shadow","0px 0px 69.36000061035156px rgba(255,216,111, 0.8)");
		   //Автор книги
		   $(".label_author").css("color","white");           
		   $(".label_author").css("background-color","rgb(49,54,89");
		   $(".label_author").css("box-shadow","0px 0px 69.36000061035156px rgba(222, 172, 172, 0.8)");        
		   //Тэги
		   $(".tag_container").css("background-color","rgb(33,33,89)");  
		   $(".tag_container").css("box-shadow","0px 0px 69.36000061035156px rgba(240, 255, 255, 1)");                
		   $(".tag_container").css("color","white");  
		   //Один блок книги
		   $(".books_block").css("box-shadow","0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px rgba(0, 0, 0, 0.98)," + 
											   "46px 49px 67px 0px rgba(0, 0, 0, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5)," + 
											   "185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02)");         
		   $(".books_block").css("background","rgba(49,54,89, 0.45)");         
		   $(".books_block").css("background-color","rgba(49,54,89, 0.45)");         
		   //Контейнер информации книги
		   $(".container_book_info").css("background","rgba(49,54,89, 0.7"); 

		};

	..  code-block:: javascript		

		/**
		* Функция изменения задания стиля 4
			* @function style4
			* Меняет стиль некоторых элементов сайта.
		*/
		function style4(){     
		   // Класс кнопок low_button (все кнопки кроме верхник и кнопок меню пользователя)
		   $(".low_button").css("color","rgb(255, 255, 255)");  
		   $(".low_button").css("background-color","rgba(61,100,45, 1)");  
		   $(".low_button").css("box-shadow","0px 0px 0px 0px rgb(44, 22, 7),0px 6px 12px 0px" +
											"rgba(44, 7, 7, 0.2),1px 23px 23px 0px rgba(44, 7, 7, 0.2)," + 
											"2px 51px 31px 0px rgba(44, 7, 7, 0.5),4px 90px 36px 0px" + 
											"rgba(61,100,45, 0.15),6px 141px 40px 0px rgba(61,100,45, 0.02)");    

		   //Фильтр
		   $(".filter_window").css("background-color","rgb(112,245,41)");  
		   $(".container_selected_attributes").css("background-color","rgb(112,245,41)");  
		   $(".select_filter").css("background-color","rgb(222,211,213)");  
		   //Кнопка найти
		   $(".button_search_class").css("box-shadow","0px 0px 0px 0px rgb(44, 7, 7),0px 6px 12px 0px rgba(44, 7, 7, 0.98)," + 
													 "1px 23px 23px 0px rgba(44, 7, 7, 0.85),2px 51px 31px 0px rgba(44, 7, 7, 0.5)," + 
													 "4px 90px 36px 0px rgba(44, 7, 7, 0.15),6px 141px 40px 0px rgba(44, 7, 7, 0.02)");         
		   $(".button_search_class").css("background","rgb(61,100,45)"); 
		   $(".button_search_class").css("color","black"); 

		   //Добавление и изменение информации о файле (Добавить, Изменить)
		   $(".add_file_class").css("background-color","rgb(61,100,45)"); 
		   $(".div_add_information_book").css("background-color","rgba(112,188,41, 1)"); 
		   $(".add_book_author").css("background-color","rgba(112,188,41, 1)"); 
		   $(".add_book_tags").css("background-color","rgba(112,188,41, 1)"); 
		   $(".description_book").css("background-color","rgba(112,188,41, 1)"); 
				
		   //Заметки (Открыть)
		   //Задний фон окна заметок
		   $(".container_notes").css("background-color","rgb(112,245,41)"); 
		   //Добавление и изменение (таблица заметок)
		   $(".table_notes").css("background-color","rgb(112,245,41)"); 
		   $(".table_notes").css("color","rgb(22,22,22)"); 
			   
		   //Верхние кнопки
		   $(".menu_button").css("color","rgb(255, 255, 255)");
		   $(".menu_button").css("background-color","rgb(61,100,45)");

		   //Главное окно сайта
		   $(".main_window_library").css("box-shadow"," 0px 0px 0px 0px rgb(0, 0, 0),12px 12px 37px 0px rgba(0, 0, 0, 0.98)," + 
													 "46px 49px 67px 0px rgba(0, 0, 0, 0.85),104px 110px 91px 0px rgba(0, 0, 0, 0.5)," + 
													 "185px 195px 108px 0px rgba(0, 0, 0, 0.15),289px 305px 118px 0px rgba(0, 0, 0, 0.02)");           
		   $(".main_window_library").css("background","rgb(61,100,45");
			 
		   //Меню пользователя
		   //Задний фон меню пользователя
		   $(".user_menu").css("background-color","rgba(112,245,41, 1)");
		   //Изображение пользователя
		   $(".user_icon_name").css("background-color","rgb(61,100,45)"); 
		   $(".user_icon_name").css("box-shadow","0px 0px 69.36000061035156px rgba(240, 244, 225, 1)");     
		   //Кнопки меню пользователя с подсветкой
		   $(".button_user_menu").css("background-color","rgb(61,100,45)");  
		   $(".button_user_menu").css("box-shadow","0px 0px 69.36000061035156px rgba(61,100,45, 1)");                
		   $(".button_user_menu").css("color","white");  

		   //Блоки книги
		   //Контейнеры тэгов в блоках книг
		   $(".tag_book").css("background-color","rgb(61,100,45)");  
		   $(".tag_book").css("box-shadow","0px 0px 69.36000061035156px rgba(22,22,22, 1)");                
		   $(".tag_book").css("color","white");  
		   //Контейнер описания книги
		   $(".text_book").css("color","white");
		   $(".text_book").css("background-color","rgb(33,110,67)");
		   $(".text_book").css("box-shadow","0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px" + 
											"rgba(61,100,45, 0.98),46px 49px 67px 0px " + 
											"rgba(61,100,45, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5)," + 
											"185px 195px 108px 0px rgba(61,100,45, 0.15),22px 22px 22px 0px rgba(61,100,45, 0.02)");   
		   //Название книги
		   $(".label_title").css("color","rgb(0, 0, 0)");     
		   $(".label_title").css("background-color","rgb(112,245,41)");
		   $(".label_title").css("box-shadow","0px 0px 69.36000061035156px rgba(210, 111, 30)");
		   //Автор книги
		   $(".label_author").css("color","rgb(14, 14, 14)");           
		   $(".label_author").css("background-color","rgb(112,177,41");
		   $(".label_author").css("box-shadow","0px 0px 69.36000061035156px rgba(177, 122, 35, 1)");      
		   //Тэги
		   $(".tag_container").css("background-color","rgb(96,225,55)");  
		   $(".tag_container").css("box-shadow","0px 0px 69.36000061035156px rgba(22,22,22, 1)");                
		   $(".tag_container").css("color","black");          
		   //Один блок книги
		   $(".books_block").css("box-shadow","0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px rgba(0, 0, 0, 0.98)," + 
											   "46px 49px 67px 0px rgba(0, 0, 0, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5)," + 
											   "185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02)");         
		   $(".books_block").css("background","rgba(61,100,45, 0.45)");    
		   //Контейнер информации книги
		   $(".container_book_info").css("background","rgba(11,111,45, 0.9"); 
		};

	..  code-block:: javascript		

		/**
		* Функция изменения задания стиля 5
			* @function style5
			* Меняет стиль некоторых элементов сайта.
		*/
		function style5(){
		   // Класс кнопок low_button (все кнопки кроме верхник и кнопок меню пользователя)
		   $(".low_button").css("color","rgb(255, 255, 255)");  
		   $(".low_button").css("background-color","rgba(236,65,14, 1)");  
		   $(".low_button").css("box-shadow","0px 0px 0px 0px rgb(44, 22, 7),0px 6px 12px 0px" +
											"rgba(44, 7, 7, 0.2),1px 23px 23px 0px rgba(44, 7, 7, 0.2)," + 
											"2px 51px 31px 0px rgba(44, 7, 7, 0.5),4px 90px 36px 0px" + 
											"rgba(44, 7, 7, 0.15),6px 141px 40px 0px rgba(44, 7, 7, 0.02)");     
		   
		   //Фильтр
		   $(".filter_window").css("background-color","rgb(22, 22, 22)");  
		   $(".container_selected_attributes").css("background-color","rgb(22, 22, 22)");  
		   $(".select_filter").css("background-color","rgb(222,211,213)");   
		   //Кнопка найти      ^
		   $(".button_search_class").css("box-shadow","0px 0px 0px 0px rgb(236,65,14),0px 6px 12px 0px" + 
													 "rgba(44, 7, 7, 0.98),1px 23px 23px 0px rgba(236,65,14, 0.85)," + 
													 "2px 51px 31px 0px rgba(44, 7, 7, 0.5),4px 90px 36px 0px rgba(44, 7, 7, 0.15),6px 141px 40px 0px rgba(44, 7, 7, 0.02)");         
		   $(".button_search_class").css("background","rgb(236,65,14)"); 
		   $(".button_search_class").css("color","white"); 

		   //Добавление и изменение информации о файле (Добавить, Изменить)
		   $(".add_file_class").css("background-color","rgb(22, 22, 22)"); 
		   $(".div_add_information_book").css("background-color","rgba(22,22,22, 1)"); 
		   $(".add_book_author").css("background-color","rgba(22,22,22, 1)"); 
		   $(".add_book_tags").css("background-color","rgba(22,22,22, 1)"); 
		   $(".description_book").css("background-color","rgba(22,22,22, 1)"); 

		   //Заметки (Открыть)
		   //Задний фон окна заметок
		   $(".container_notes").css("background-color","rgb(22, 22, 22)"); 
		   //Добавление и изменение (таблица заметок)
		   $(".table_notes").css("background-color","rgb(22, 22, 22)"); 
		   $(".table_notes").css("color","rgb(255,255,255)"); 

		   //Верхние кнопки
		   $(".menu_button").css("color","rgb(255, 255, 255)");
		   $(".menu_button").css("background-color","rgb(236,65,14)");

		   //Главное окно сайта      ^
		   $(".main_window_library").css("box-shadow"," 0px 0px 0px 0px rgb(0, 0, 0),12px 12px 37px 0px" +
													 "rgba(0, 0, 0, 0.98),46px 49px 67px 0px rgba(0, 0, 0, 0.85)," +
													  "104px 110px 91px 0px rgba(0, 0, 0, 0.5),185px 195px 108px 0px" + 
													 "rgba(0, 0, 0, 0.15),289px 305px 118px 0px rgba(0, 0, 0, 0.02)");           
		   $(".main_window_library").css("background","rgb(22, 22, 22)");
		   
		   //Меню пользователя
		   //Задний фон меню пользователя
		   $(".user_menu").css("background-color","rgba(22, 22, 22, 1)");
		   //Изображение пользователя
		   $(".user_icon_name").css("background-color","rgb(0, 0, 0)"); 
		   $(".user_icon_name").css("box-shadow","0px 0px 69.36000061035156px rgba(236,65,14, 1)");     
		   //Кнопки меню пользователя с подсветкой
		   $(".button_user_menu").css("background-color","rgb(236,65,14)");  
		   $(".button_user_menu").css("box-shadow","0px 0px 69.36000061035156px rgba(22,22,22, 1)");                
		   $(".button_user_menu").css("color","white");  
		 
		   //Блоки книги
		   //Контейнеры тэгов в блоках книг
		   $(".tags_book").css("background-color","rgb(22,22,22)");  
		   $(".tags_book").css("box-shadow","0px 0px 69.36000061035156px rgba(33,33,89, 1)");                
		   $(".tags_book").css("color","white");  
		   //Контейнер описания книги
		   $(".text_book").css("color","white");
		   $(".text_book").css("background-color","rgb(11, 11, 11)");
		   $(".text_book").css("box-shadow","0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px" + 
											"rgba(127, 107, 107, 0.98),46px 49px 67px 0px " + 
											"rgba(0, 0, 0, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5)," + 
											"185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02)");   
		   //Название книги
		   $(".label_title").css("color","rgb(255, 255, 255)");     
		   $(".label_title").css("background-color","rgb(22, 22, 22)");
		   $(".label_title").css("box-shadow","0px 0px 69.36000061035156px rgba(236,65,14, 0.6)");
		   //Автор книги    ^   
		   $(".label_author").css("color","rgb(255, 255, 255)");           
		   $(".label_author").css("background-color","rgb(44, 44, 44)");
		   $(".label_author").css("box-shadow","0px 0px 69.36000061035156px rgba(236,65,14, 0.3)");        
		   //Тэги
		   $(".tag_container").css("background-color","rgb(236,65,14)");  
		   $(".tag_container").css("box-shadow","0px 0px 69.36000061035156px rgba(22, 22, 22, 1)");                
		   $(".tag_container").css("color","black");  
		   //Один блок книги 
		   $(".books_block").css("box-shadow","0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px" + 
											   "rgba(0, 0, 0, 0.98),46px 49px 67px 0px rgba(0, 0, 0, 0.85)," + 
											   "12px 25px 22px 0px rgba(0, 0, 0, 0.5),185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02)");         
		   $(".books_block").css("background","rgba(22,22,22, 1)");         
		   //Контейнер информации книги      ^
		   $(".container_book_info").css("background","rgba(11, 11, 11, 0.7"); 

		};
   
   


CSS код
=======

add_file.css
------------
	..  code-block:: css

		/** 
		* Контейнер добавления файла
		*/
		.add_file_class{
			position: relative;
			top: -805px;
			left: 375px;
			width: 1150px;
			height: 860px;
			background-color: rgb(22, 22, 22); 
			border-color: black; 
			border-width: 1px; 
			border-style: solid;
			box-shadow: 0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px rgba(0, 0, 0, 0.98),46px 49px 67px 0px rgba(0, 0, 0, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5),185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02);
		}

	..  code-block:: css
	
		/** 
		* Контейнер информация о книге
		*/
		.div_add_information_book{
			position: relative;
			top:15px;
			left:35px;
			width: 320px;
			background-color: rgb(22, 22, 22);
			box-shadow: 0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px rgba(0, 0, 0, 0.98),46px 49px 67px 0px rgba(0, 0, 0, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5),185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02);
		}

	..  code-block:: css
	
		/** 
		* Класс текстовых полей добавления файла
		*/
		.input_add_book_class{
		 color: rgb(0, 0, 0);
		 font-size: 26px;
		 width: 300px;
		}

	..  code-block:: css
	
		/** 
		* Класс заголовков текстовых полей добавления файла
		*/
		.label_add_book{
			position: relative;
			font-size: 26px;
			color: rgb(255, 255, 255);
		}

	..  code-block:: css
	
		/**
		* Заголовок названия книги
		*/
		.p_add_title_book{
			top:10px; 
			left: 10px;
		}

	..  code-block:: css
	
		/** 
		* Поле ввода названия книги
		*/
		.input_title_book{
			position: relative;
			top: -15px;
			left: 10px;
		}

	..  code-block:: css
	
		/** 
		* Заголовок количества страниц книги
		*/
		.p_add_page_book{
			top:-20px; 
			left: 10px;
		}

	..  code-block:: css
	
		/** 
		* Поле ввода количества страниц книги
		*/
		.input_page_book{
			position: relative;
			top: -45px;
			left: 10px;
		}

	..  code-block:: css
	
		/**
		* Заголовок путь к книге
		*/
		.p_add_path_book{
			top:-55px; 
			left: 10px;
		}

	..  code-block:: css
	
		/** 
		* Поле ввода пути к файлу книги
		*/
		.input_path_book{
			position: relative;
			top: -80px;
			left: 10px;
		}

	..  code-block:: css
	
		/** 
		* Заголовок путь к изображению книги
		*/
		.p_add_image_book{
			top:-85px; 
			left: 10px;
		}

	..  code-block:: css
	
		/** 
		* Поле ввода к изображению книги
		*/
		.input_image_book{
			position: relative;
			top: -110px;
			left: 10px;
		}

	..  code-block:: css
	
		/** 
		* Класс раскрывающихся списков добавления книги
		*/
		.add_book_combobox{
			position: relative;
			height: 40px;
			font-size: 20px;
			width: 300px;
		}

	..  code-block:: css
	
		/** 
		* Раскрывающий список выбора категории книги
		*/
		.combobox_category{
			top: -75px;
			left: 10px;
		}

	..  code-block:: css
	
		/** 
		* Раскрывающий список выбора языка книги
		*/
		.combobox_language{
			top: -45px;
			left: 10px;
		}
		
	..  code-block:: css
	
		/** 
		* Раскрывающий список выбора языка книги
		*/
		.combobox_year{
			top: -15px;
			left: 10px;
		}

	..  code-block:: css
	
		/** 
		* Контейнер Авторы
		*/
		.add_book_author{
			position: relative;
			left: 395px;
			top:-635px;
			font-size: 26px;
			width: 340px;
			background-color: rgb(22, 22, 22);
			height: 625px;
			box-shadow: 0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px rgba(0, 0, 0, 0.98),46px 49px 67px 0px rgba(0, 0, 0, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5),185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02);

		}

	..  code-block:: css

		/** 
		* Заголовок фамилия автора
		*/
		.surname_author_label{
			position: relative;
			top: 5px;
			left: 15px;
			width: 300px;
		}

	..  code-block:: css

		/** 
		* Текстовое поле фамилии автора
		*/
		.surname_author_input{
			position: relative;
			top: -20px;
			left: 15px;
		}

	..  code-block:: css

		/**
		* Заголовок имени автора
		*/
		.name_author_label{
			position: relative;
			top:-25px;
			left: 15px;
		}

	..  code-block:: css

		/** 
		* Текстовое поле имени автора
		*/
		.name_author_input{
			position: relative;
			top: -50px;
			left: 15px;
		}

	..  code-block:: css

		/**
		* Заголовок отчества автора
		*/
		.patronymic_author_label{
			position: relative;
			top:-55px;
			left: 15px;
		}

	..  code-block:: css

		/** 
		* Текстовое поле отчества автора
		*/
		.patronymic_author_input{
			position: relative;
			top: -80px;
			left: 15px;
		}

	..  code-block:: css

		/** 
		* Кнопка Добавить нового автора
		*/
		.button_add_new_author{
			width: 300px;
			height: 40px;
			font-size: 21px;
			left: 15px;
			top: 355px;
		}

	..  code-block:: css

		/** 
		* Заголовок Список авторов для книги
		*/
		.title_list_authors{
			left: 15px;
			top: -35px;
		}

	..  code-block:: css

		/** 
		* Класс мульти списка добавления книги
		*/
		.field_combobox_add_book{
			position: relative;
			width: 300px;
			height: 60px;
			overflow: auto;
			font-size: 18px;
		}

	..  code-block:: css

		/** 
		* Список авторов для книги
		*/
		.field_authors{
			left: 15px;
			top:-55px;
		}

	..  code-block:: css

		/** 
		* Раскрывающий список авторов
		*/
		.combobox_authors{
			top:-35px;
			left: 15px;
		}

	..  code-block:: css

		/** 
		* Кнопка Добавить автора в список 
		*/
		.button_add_list_author{
			width: 300px;
			height: 40px;
			font-size: 21px;
			left: 15px;
			top: 575px;
		}

	..  code-block:: css

		/** 
		* Тэги книги
		*/
		.add_book_tags{
			position: relative;
			top:-1285px;
			left:780px;
			background-attachment: fixed;
			font-size: 26px;
			width: 340px;
			background-color: rgb(22, 22, 22);
			height: 455px;
			box-shadow: 0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px rgba(0, 0, 0, 0.98),46px 49px 67px 0px rgba(0, 0, 0, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5),185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02);

		}

	..  code-block:: css

		/** 
		* Заголовок Тэги книги, Добавить новый тэг, Название тэга
		*/
		.tag_label{
			position: relative;
			top: 5px;
			left: 15px;
			width: 300px;
		}

	..  code-block:: css

		/** 
		* Поле ввода нового тэга
		*/
		.name_tag_input{
			position: relative;
			top: -20px;
			left: 15px;
		}

	..  code-block:: css

		/** 
		* Кнопка добавления нового тэга
		*/
		.button_new_tag{
			width: 300px;
			height: 40px;
			font-size: 21px;
			left: 15px;
			top: 175px;
		}

	..  code-block:: css

		/** 
		* Заголовок Список тэгов для книги
		*/
		.label_list_tags{
			position: relative;
			top: 25px;
			left: 15px;
			width: 300px;
		}

	..  code-block:: css

		/** 
		* Список тэгов для книги
		*/
		.field_list_tags{
			left: 15px;
			top:5px;
		}

	..  code-block:: css

		/** 
		* Кнопка Добавить тэг в список
		*/
		.button_add_list_tag{
			width: 300px;
			height: 40px;
			font-size: 21px;
			left: 15px;
			top: 395px;
		}

	..  code-block:: css

		/** 
		* Раскрывающий список выбора тэга
		*/
		.combobox_tags{
			top: 20px;
			left: 15px;
		}

	..  code-block:: css

		/** 
		* Описание книги
		*/
		.description_book{
			position: relative;
			top:-1285px;
			left: 780px;
			background-attachment: fixed;
			font-size: 26px;
			width: 340px;
			background-color: rgb(22, 22, 22);
			height: 145px;
			box-shadow: 0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px rgba(0, 0, 0, 0.98),46px 49px 67px 0px rgba(0, 0, 0, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5),185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02);

		}

	..  code-block:: css

		/** 
		* Заголовок Описание книги
		*/
		.description_book_label{
			left:15px;
		}

	..  code-block:: css

		/**
		* Текстовое поле Описание книги
		*/
		.description_book_input{
			white-space: pre-wrap; 
			word-wrap: normal; 
			position: relative;
			width: 300px;
			height: 100px;
			left:15px;
			top:-20px; 
			z-index: 44;
		}

	..  code-block:: css

		/** 
		* Кнопка Добавить книгу
		*/
		.button_create_book{
			position: relative;
			top:-1250px;
			left:870px;
			width: 250px;
		}		
		
book_container.css
------------------

	..  code-block:: css	

		/** 
		* Контейнер со всеми книгами 
		*/
		.all_block_books{
			position: absolute;
			top:0px;
			left:25px;
		}
		
	..  code-block:: css	

		/** 
		* Блок с книгой 
		*/
		.books_block_inside{
			position: absolute;
			width: 1154px;
			height: 422px;
			left: 344px;
			right: 25px;
			top: 322px;
		}

	..  code-block:: css	
	
		/**
		* Блок книги 1 уровня 
		*/
		.books_block{
			width: 1154px;
			height: 420px;
			bottom: 336px;
			box-shadow: 0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px rgba(23, 22, 22, 0.98),46px 49px 67px 0px rgba(0, 0, 0, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5),185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02);
			background: rgba(22, 22, 22, 0.45);
		}

	..  code-block:: css	
	
		/** 
		* Блок описания книги
		*/
		.container_book_info{
			position: fixed;
			width: 570px; 
			height: 310px; 
			background: rgba(11, 11, 11, 0.45);
			box-shadow: 0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px rgba(23, 22, 22, 0.98),46px 49px 67px 0px rgba(0, 0, 0, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5),185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02);
		}

	..  code-block:: css	
	
		/** 
		* Кнопка Открыть
		*/
		.button_container_books1{
			position: relative;
			left: 590px;
			top: -58px;
			width: 200px;
			height: 60px;
			font-size: 26px;
		}

	..  code-block:: css	

		/** 
		* Кнопка Изменить
		*/
		.button_container_books2{
			position: relative;
			left: 590px;
			top: -50px;
			width: 200px;
			height: 60px;
			font-size: 26px;
		}

	..  code-block:: css	

		/** 
		* Кнопка В избранное
		*/
		.button_container_books3{
			position: relative;
			left: 590px;
			top: -42px;
			width: 200px;
			height: 60px;
			font-size: 26px;
		}

	..  code-block:: css	

		/** 
		* Кнопка На чтение
		*/
		.button_container_books4{
			position: relative;
			left: 590px;
			top: -34px;
			width: 200px;
			height: 60px;
			font-size: 26px;
		}

	..  code-block:: css	

		/** 
		* Кнопка В прочитанное
		*/
		.button_container_books5{
			position: relative;
			left: 590px;
			top: -26px;
			width: 200px;
			height: 60px;
			font-size: 26px;
		}

	..  code-block:: css	

		/** 
		* Описание книги
		*/
		.text_book{
			white-space: pre-wrap; 
			word-wrap: normal; 
			overflow: auto; 
			width: 570px; 
			height:220px;
			font-size: 24px;
			color: white;
			background-color: rgb(11, 11, 11);
			box-shadow: 0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px rgba(127, 107, 107, 0.98),46px 49px 67px 0px rgba(0, 0, 0, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5), 185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02);
		}

	..  code-block:: css	

		/** 
		* Заголовок названия книги
		*/
		.label_title{
			white-space: pre-nowrap; 
			overflow-x:auto;
			word-wrap: normal; 
			position: relative;
			color: rgb(255, 255, 255);
			font-family: Inter;
			font-size: 20px;
			letter-spacing: 0px;
			text-align: center;
			font-variant: small-caps;
			width: 570px; 
			height: 43px; 
			background-color: rgb(22, 22, 22); 
			box-shadow: 0px 0px 69.36000061035156px rgba(236,65,14, 0.6);
			line-height: 32px;

		}

	..  code-block:: css	

		/** 
		* Заголовок имени автора
		*/
		.label_author{
			white-space: nowrap; 
			overflow-x:auto;
			word-wrap: normal; 
			position: relative;
			color: rgb(255, 255, 255);
			font-family: Inter;
			font-size: 18px;
			letter-spacing: 0px;
			text-align: center;
			font-variant: small-caps;
			width: 375px; 
			height: 50px; 
			background-color: rgb(44, 44, 44); 
			box-shadow: 0px 0px 69.36000061035156px rgba(236,65,14, 0.3);
			line-height: 32px;
		}

	..  code-block:: css	

		/** 
		* Заголовок языка книги и года издания
		*/
		.label_year_language{
			font-weight:bold ;
			position: absolute;
			left: 420px; 
			top: 45px;
			color: #fffcfc;
		}

	..  code-block:: css	

		/** 
		* Заголовок категории книги 
		*/
		.label_category{
			font-weight:bold ;
			position: absolute;
			left: 400px; 
			top: 312px;
			color: #fffcfc;
		}

	..  code-block:: css	

		/** 
		* Заголовок статуска книги
		*/
		.label_state{
			font-weight:bold ;
			position: absolute;

			top: 312px;
			color: #fffcfc;
		}

	..  code-block:: css	

		/** 
		* Контейнер блоков тэгов книги
		*/
		.tags_book{
			white-space: pre-wrap; 
			word-wrap: normal; 
			overflow: auto; 
			width: 570px; 
			height:90px;
			font-size: 24px;
			color: black;
			scrollbar-width: thin;
			scrollbar-color: hsl(0 0% 50%);
			background-color: 0px 0px 69.36000061035156px rgba(33,33,89, 1);
			box-shadow: r;
		}

	..  code-block:: css	

		/** 
		* Контейнер тэгов
		*/
		.tag_container{
			width: auto;
			height: 44px;
			font-family: Inter;
			font-size: 22px;
			line-height: 41px;
			white-space: nowrap; 
			color: rgb(255, 255, 255);
			text-align: center;
			background-color: rgb(236, 65, 14); 
			border-color: black; 
			border-width: 1px; 
			border-style: solid;
			box-shadow: 0px 0px 69.36000061035156px rgba(22, 22, 22, 1);

		}

	..  code-block:: css	

		/**
		* Дизайн скролла
		*/
		::-webkit-scrollbar {
			height: 12px;
			width: 12px;
			background: #3b280d53;
		}

		::-webkit-scrollbar-thumb {
			background: #c2bab5;
			-webkit-border-radius: 1ex;
			-webkit-box-shadow: 0px 1px 2px rgba(22, 20, 20, 0);
		}

		::-webkit-scrollbar-corner {
			background: #000;
		}	

change_file.css
---------------

	..  code-block:: css	
	
		/** 
		* Класс кнопки изменения информации о книге
		*/
		.change_btn{
			font-size: 16px;
			width: 90px;
			height: 20px;
			line-height: 14px;
		}

	..  code-block:: css	

		/** 
		* Контейнер информации о книге
		*/
		.change_information{
			height: 690px;
		}

	..  code-block:: css	

		/** 
		* Кнопка изменить название книги
		*/
		#change_name_book{
			position: absolute;
			top:145px;
			left: 220px;
		}

	..  code-block:: css	

		/** 
		* Кнопка изменить количество страниц книги
		*/
		#change_page_book{
			position: absolute;
			top:232px;
			left: 220px;
		}

	..  code-block:: css	

		/** 
		* Кнопка изменить путь к файлу книги
		*/
		#change_path_book{
			position: absolute;
			top:315px;
			left: 220px;
		}

	..  code-block:: css	

		/** 
		* Кнопка изменить путь к изображению книги
		*/
		#change_path_image_book{
			position: absolute;
			top:405px;
			left: 220px;
		}

	..  code-block:: css	

		/** 
		* Кнопка изменить категорию книги
		*/
		#change_category_book{
			position: absolute;
			top:495px;
			left: 220px;
		}

	..  code-block:: css	

		/** 
		* Кнопка изменить язык книги
		*/
		#change_language_book{
			position: absolute;
			top:580px;
			left: 220px;
		}

	..  code-block:: css	

		/** 
		* Кнопка изменить год книги
		*/
		#change_year_book{
			position: absolute;
			top:665px;
			left: 220px;
		}

	..  code-block:: css	

		/**
		* Контейнер Авторы
		*/
		.change_author{
			top:-700px;
			height: 690px;
		}

	..  code-block:: css	

		/** 
		* Раскрывающий список авторов
		*/
		.combobox_change_list_authors{
			top:-30px;
		}

	..  code-block:: css	

		/** 
		* Кнопка Добавить автора в список
		*/
		.btn_change_list_authors{
			top: 615px;
		}

	..  code-block:: css	

		/** 
		* Кнопка Добавить авторов из списка
		*/
		#btn_add_list_authors{
			position: absolute;
			top: 515px;
			left: 225px;
		}

	..  code-block:: css	

		/** 
		* Тэги книги
		*/
		.change_tags{
			top:-1415px;
			height: 485px;
		}

	..  code-block:: css	

		/** 
		* Кнопка Добавить тэг в список
		*/
		.change_btn_add_list_tag{
			top: 425px;
		}

	..  code-block:: css	

		/** 
		* Раскрывающий список выбора тэга
		*/
		.change_combobox_tags{
			top: 50px;
		}

	..  code-block:: css	

		/** 
		* Кнопка добавления списка тэгов
		*/
		#change_list_tags{
			position: absolute;
			top:340px;
			left:225px;
		}

	..  code-block:: css	

		/** 
		* Описание книги
		*/
		.change_description{
			top:-1420px;
			height: 185px;
		}

	..  code-block:: css	

		/** 
		* Кнопка изменения описания книги
		*/
		#btn_change_description{
			position: absolute;
			left:220px;
			top:150px;
		}
		
filter_window.css
-----------------

	..  code-block:: css

		/** 
		* Окно фильтра поиска
		*/
		.filter_window{
			visibility: hidden;
			background-color: rgba(22, 22, 22);
			width: 1150px;
			height: 70px;
			z-index: 15;
			position: relative;
			left: 370px;
			top: -630px;
			box-shadow: 0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px rgba(23, 22, 22, 0.98),46px 49px 67px 0px rgba(0, 0, 0, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5),185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02);
		}

	..  code-block:: css

		/** 
		* Класс раскрывающегося списка фильтра поиска
		*/
		.select_filter{
			width: 380px;
			font-size: 21px;
			background-color: rgb(222,211,213);
		}

	..  code-block:: css

		/** 
		* Класс кнопок в окне Фильтр
		*/
		.button_filter{
			height:40px;
			width: 120px;
			font-size: 21px;
		}

	..  code-block:: css

		/** 
		* Кнопка применения фильтра
		*/
		#enter_window_filter{
			position: absolute;
			left:1010px;
			top:30px;
		}

main_book.css
-------------

	..  code-block:: css
	
		/** 
		* класс кнопок верхнего меню
		*/
		.menu_button{
			position: absolute;
			top: 30px;
			width: 214px;
			height: 72px;
			font-family: Inter;
			font-size: 28px;
			font-weight: 800;
			line-height: 34px;
			letter-spacing: 0px;
			color: rgb(255, 255, 255);
			text-align: center;
			font-variant: small-caps;	
			cursor: pointer;
			background-color: rgb(236, 65, 14); 
			border-color: black; 
			border-width: 1px; 
			border-style: solid;
			box-shadow: 0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px rgba(0, 0, 0, 0.98),46px 49px 67px 0px rgba(0, 0, 0, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5),185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02);
			opacity: 0.6;
			transition: 0.3s;
			border-radius: 10%;
		}
		.menu_button:hover {opacity: 1}

	..  code-block:: css
	
		/** 
		* расположение кнопки 1 
		*/
		#menu_button1{
			left: 25px;
		}

	..  code-block:: css

		/** 
		* расположение кнопки 2 
		*/
		#menu_button2
		{
			left: 345px;
		}

	..  code-block:: css

		/** 
		* расположение кнопки 3 
		*/
		#menu_button3{
			left: 672px;
		}

	..  code-block:: css

		/** 
		* расположение кнопки 4 
		*/
		#menu_button4{
			left: 990px;
		}

	..  code-block:: css

		/** 
		* расположение кнопки 5 
		*/
		#menu_button5{
			left: 1310px;
		}

	..  code-block:: css

		/** 
		* Класс для всех кнопок сайта
		*/
		.low_button{
			color: rgb(255, 255, 255);
			font-family: Inter;
			font-size: 28px;
			font-weight: 800;
			line-height: 34px;
			letter-spacing: 0px;
			text-align: center;
			font-variant: small-caps;	
			width: 158px; height: 67px; 
			background-color: rgba(236,65,14, 1);
			border-radius: 9999px; 
			border-color: black; 
			border-width: 1px; 
			border-style: solid;
			position: absolute;
			box-sizing: border-box;
			border: 1px solid rgb(0, 0, 0);
			box-shadow: 0px 0px 0px 0px rgb(44, 22, 7),0px 6px 12px 0px rgba(44, 7, 7, 0.2),1px 23px 23px 0px rgba(44, 7, 7, 0.2), 2px 51px 31px 0px rgba(44, 7, 7, 0.5),4px 90px 36px 0px rgba(44, 7, 7, 0.15),6px 141px 40px 0px rgba(44, 7, 7, 0.02);
			border-radius: 10%;
			opacity: 0.6;
			transition: 0.3s;
			cursor: pointer;
		}
		.low_button:hover {opacity: 1}

	..  code-block:: css

		/** 
		* кнопка скрыть/показать 
		* расположение кнопки показать верхнее меню 
		*/
		.button_hide_class{
			left: 25px;
			top: 150px;
			width: 130px;
			height: 67px;
		}

	..  code-block:: css

		/** 
		* расположение кнопки скрыть верхнее меню 
		*/
		.button_show_class{
			visibility: hidden;
			left: 25px;
			top: 150px;
			width: 130px;
			height: 67px;
		}

	..  code-block:: css

		/** 
		* кнопки изменения стиля сайта
		*/
		.button_style{
			visibility: hidden;
			position: fixed;
			top: 150px;
			left: 175px;
			opacity: 0.6;
			transition: 0.3s;
			cursor: pointer;
		}
		.button_style:hover {opacity: 1}

	..  code-block:: css

		/** 
		* главная кнопка изменения стиля сайта
		*/
		.button_style_visibility_main{
			height: 67px;
			width: 95px;
			visibility: visible;
			border-radius: 10%;
		}

	..  code-block:: css

		/** 
		* расположение кнопки стиля 1
		*/
		.button_style_position1{
			background-color: rgb(214, 129, 24);
			height: 40px;
			width: 35px;
			left: 30px;
			top: 250px;
			border-radius: 100%;
		}

	..  code-block:: css

		/** 
		* расположение кнопки стиля 2
		*/
		.button_style_position2{
			background-color: rgba(158, 181, 181, 0.848);
			height: 40px;
			width: 35px;
			left: 80px;
			top: 250px;
			border-radius: 100%;
		}

	..  code-block:: css

		/** 
		* расположение кнопки стиля 3
		*/
		.button_style_position3{
			background-color: rgb(49,54,89);
			height: 40px;
			width: 35px;
			left: 130px;
			top: 250px;
			border-radius: 100%;
		}

	..  code-block:: css

		/** 
		* расположение кнопки стиля 4
		*/
		.button_style_position4{
			background-color: rgb(112,245,41);
			height: 40px;
			width: 35px;
			left: 180px;
			top: 250px;
			border-radius: 100%;
		}

	..  code-block:: css

		/** 
		* расположение кнопки стиля 5
		*/
		.button_style_position5{
			background-color: rgb(18, 20, 20);
			height: 40px;
			width: 35px;
			left: 230px;
			top: 250px;
			border-radius: 100%; 
		}

	..  code-block:: css

		/** 
		* главный контейнер сайта 
		*/
		.main_window_library{
			position: relative;
			width: 1555px;
			max-height: 2500px;
			height: 2500px; 
			background-attachment: fixed;
			backdrop-filter: blur(22px);
			background: rgb(22, 22, 22);
			box-shadow: 0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px rgba(23, 22, 22, 0.98),46px 49px 67px 0px rgba(0, 0, 0, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5),185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02);
		}

	..  code-block:: css

		/** 
		* класс кнопки фильтр 
		*/
		.button_filter_class{
			width: 158px;
			height: 67px;
			left: 370px;
			top: 150px;
		}

	..  code-block:: css

		/** 
		* поле ввода для поиска 
		*/
		.search_input_class{
			position: absolute;
			width: 971px;
			height: 70px;
			left: 550px;
			top: 150px;
			font-size: 25px;
			box-sizing: border-box;
			border: 1px solid rgb(0, 0, 0);
			box-shadow: 0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px rgba(23, 22, 22, 0.98),46px 49px 67px 0px rgba(0, 0, 0, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5),185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02);
			background: rgb(196, 196, 196);
		}

	..  code-block:: css

		/** 
		* кнопка найти 
		*/
		.button_search_class{
			width: 158px;
			height: 67px;
			left: 1360px;
			top: 150px;
			background: rgb(236,65,14);
			color: white;
		}

	..  code-block:: css

		/** 
		* Контейнер для страниц 
		*/
		.page{
			position: relative;

			top:20px;
			left: 395px;
		}

	..  code-block:: css

		/** 
		* Блок страницы 
		*/
		.page_container{
			width: 125px;
			position: relative;
		}
		
open_book.css
-------------

	..  code-block:: css
	
		/**
		* Контейнер книги
		*/
		.book_window_class{
			position: relative; 
			top: -585px;
			left: 375px; 
			width: 1150px;
		}

	..  code-block:: css

		/** 
		* Документ книги
		*/
		.frame_book_class{
			width: 1150px;
			height: 720px;
		}

	..  code-block:: css

		/**
		* Контейнер меню открытой книги
		*/
		.menu_book_read{
			position: relative; 
			top: -770px; 
			left: 0px
		}

	..  code-block:: css

		/** 
		* Класс меню кнопок открытой книги
		*/
		.book_button_open{
			position:static;
			width: 180px;
			height: 44px;
			font-family: Inter;
			font-size: 22px;
			line-height: 34px;
		}

	..  code-block:: css

		/** 
		* Контейнер закладки
		*/
		.container_marker{
			position: relative;
			visibility: hidden;
		}

	..  code-block:: css

		/** 
		* Поле ввода страницы закладки
		*/
		.input_marker{
			width: 80px;
			height: 44px;
			font-size: 22px;
		}

	..  code-block:: css

		/** 
		* Кнопка изменения страницы закладки
		*/
		.btn_marker{
			left: 80px;
			width: 180px;
			height: 44px;
			font-family: Inter;
			font-size: 22px;
			line-height: 34px;
		}

	..  code-block:: css

		/** 
		* Контейнер заметок
		*/
		.container_notes{
			position: absolute;
			width: 1150px;
			height: 600px;
			top: 50px;
			background-color: rgb(22, 22, 22);
			visibility: hidden;
		}

	..  code-block:: css

		/** 
		* Контейнер таблицы
		*/
		.container_table{
			overflow-y: scroll;
			position: absolute;
			width: 1100px; 
			height: 300px; 
			left: 25px;
		}

	..  code-block:: css

		/** 
		* Таблица заметок
		*/
		.table_notes{
			width: 1080px;
			height: auto;
			background-color: rgb(22, 22, 22);
			color: rgb(255, 255, 255);
			font-size: 26px;
			word-break: break-all;
			position: relative;
			box-shadow: 0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px rgba(23, 22, 22, 0.98),46px 49px 67px 0px rgba(0, 0, 0, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5),185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02);
		}

	..  code-block:: css

		/** 
		* Класс линии границ таблицы
		*/
		.border_tables{
			border: 3px;
			border-color: black;
			border-style:groove;
		}

	..  code-block:: css

		/** 
		* Класс ячейки id
		*/
		.id_note{
			width: 50px;
			height: 20px;
		}

	..  code-block:: css

		/** 
		* Класс ячейки заметки
		*/
		.name_note{
			height: 20px;
			white-space: pre-wrap;
		}

	..  code-block:: css

		/** 
		* Класс записи таблицы заметок
		*/
		.row_table{
			height: 20px;
		}

	..  code-block:: css

		/** 
		* Контейнер добавления заметок
		*/
		.add_notes{
			position: absolute;
			width: 1090px;
			height: 210px;
			top: 320px;
			left: 25px;
			background-color: rgb(213, 213, 229);
			box-shadow: 0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px rgba(23, 22, 22, 0.98),46px 49px 67px 0px rgba(0, 0, 0, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5),185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02);
		}

	..  code-block:: css

		/**
		* Кнопка Добавить заметку
		*/
		.btn_add_note{
			width: 200px;
			height: 44px;
			font-size: 22px;
			position: absolute;
			top: 225px;
			left:900px;
		}

	..  code-block:: css

		/**
		* Поле ввода заметки
		*/
		.field_note{
			position: relative;
			top: -20px;
			width: 1100px;
			height: 220px;
			font-size: 26px;
		}

user_menu.css
-------------

	..  code-block:: css

		/** 
		* меню пользователя 
		*/
		.user_menu
		{
			background-color: rgba(22, 22, 22, 1);
			position: relative;
			width: 317px;
			height: 863px;
			left: 25px;
			right: 1222px;
			top: 320px;
			bottom: -13px;
			box-shadow: 0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px rgba(23, 22, 22, 0.98),46px 49px 67px 0px rgba(0, 0, 0, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5),185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02);
			opacity: 1;
		}

	..  code-block:: css

		/** 
		* икона пользователя в меню пользователя 
		*/
		.user_icon_name
		{	
			background-color: rgb(0, 0, 0);
			box-shadow: 0px 0px 69.36000061035156px rgba(236,65,14, 1);	
			position: absolute;
			width: 317px;
			height: 93px;
			left: 0;
			right: 1206px;
			
		}

	..  code-block:: css

		/** 
		* кнопка меню пользователя 
		*/
		.user_menu_button
		{
			position: absolute;
			left: 40px;
			width: 296px; 
			height: 93px; 
			font-size: 26px; 
			font-weight: 800; 
			line-height: 100%; 
			text-align: center; 
			color: white;
		}

	..  code-block:: css

		/** 
		* кнопки меню пользователя 
		*/
		.button_user_menu{
			position: absolute;
			background-color: rgb(236,65,14);
			box-shadow: 0px 0px 69.36000061035156px rgba(22,22,22, 1);	
			width: 317px;
			height: 90px;
			color: rgb(255, 255, 255);
			font-family: Inter;
			font-size: 20px;
			letter-spacing: 0px;
			text-align: center;
			font-variant: small-caps;
			opacity: 0.6;
			transition: 0.3s;
		}
		.button_user_menu:hover {opacity: 1}

	..  code-block:: css

		/** 
		* распоположение кнопки 1 
		*/
		.button_user_menu_position1
		{
			top:150px;
		}

	..  code-block:: css

		/** 
		* распоположение кнопки 2 
		*/
		.button_user_menu_position2
		{
			top:240px;
		}

	..  code-block:: css

		/** 
		* распоположение кнопки 3 
		*/
		.button_user_menu_position3
		{
			top:330px;
		}

	..  code-block:: css

		/** 
		* распоположение кнопки 4 
		*/
		.button_user_menu_position4
		{
			top:420px;
		}

	..  code-block:: css

		/** 
		* распоположение кнопки 5 
		*/
		.button_user_menu_position5
		{
			top:510px;
		}

	..  code-block:: css

		/** 
		* изображение пользователя
		*/
		.image_user{
			position: absolute;
			left: 0px;
			top: 0px;
			width: 90px; 
			height:95px;
			box-shadow: 0px 0px 0px 0px rgb(0, 0, 0),11px 12px 37px 0px rgba(23, 22, 22, 0.98),46px 49px 67px 0px rgba(0, 0, 0, 0.85),12px 25px 22px 0px rgba(0, 0, 0, 0.5),185px 195px 108px 0px rgba(0, 0, 0, 0.15),22px 22px 22px 0px rgba(0, 0, 0, 0.02);
		}
		
index_book.css
--------------

	..  code-block:: css
	
		/**
		* Главный контейнер страницы авторизации
		*/
		.window{
			position: relative;
			width: 1000x;
			height: 1200px; 
			background-attachment: fixed;
			box-shadow: 0px 0px 0px 0px rgb(0, 0, 0),12px 12px 37px 0px rgba(0, 0, 0, 0.98),46px 49px 67px 0px rgba(0, 0, 0, 0.85),104px 110px 91px 0px rgba(0, 0, 0, 0.5),185px 195px 108px 0px rgba(0, 0, 0, 0.15),119px 305px 118px 0px rgba(0, 0, 0, 0.02);
			backdrop-filter: blur(22px);
			background: linear-gradient(to bottom, rgb(13, 13, 13), rgba(17, 17, 17, 0.98), rgb(8, 7, 7), rgba(24, 22, 22, 0.98), rgb(17, 15, 14));
		}

	..  code-block:: css
	
		/**
		* Класс контейнер для полей ввода логина и пароля
		*/
		.input_lk{
			width: 355px;
			height: 70px;
			box-sizing: border-box;
			border: 1px solid rgb(0, 0, 0);
			box-shadow: 0px 0px 0px 0px rgb(44, 7, 7),0px 6px 12px 0px rgba(44, 7, 7, 0.98),1px 23px 23px 0px rgba(44, 7, 7, 0.85),2px 51px 31px 0px rgba(44, 7, 7, 0.5),4px 90px 36px 0px rgba(44, 7, 7, 0.15),6px 141px 40px 0px rgba(44, 7, 7, 0.02);
			background: rgb(196, 196, 196);
		}

	..  code-block:: css
	
		/**
		* Расположение контейнера ввода логина
		*/
		#login_input{
			position: absolute;
			left: 1123px;
			top: 217px;
		}

	..  code-block:: css

		/**
		* Расположение контейнера ввода пароля
		*/
		#password_input{
			position: absolute;
			left: 1123px;
			top: 417px;
		}

	..  code-block:: css

		/**
		* Класс надписей для окна авторизации
		*/
		.label_auth{
		color:white;
		font-size: 36px;
		}

	..  code-block:: css

		/**
		* Надпись логин
		*/
		#lable_login{
			position: absolute;
			left: 1123px;
			top: 127px;
		}

	..  code-block:: css

		/**
		* Надпись Пароль
		*/
		#label_password{
			position: absolute;
			left: 1123px;
			top: 327px;
		}

	..  code-block:: css

		/**
		* Кнопка войти
		*/
		#button_in{
			position: absolute;
			left: 1123px;
			top: 527px;
			font-size: 36px;
			width: 370px;
			text-align: center;
			color:rgb(0, 0, 0);
			font-family: Arial, Helvetica, sans-serif;
			background-color: rgb(214, 21, 21);
			cursor: pointer;
			border: 1px solid rgb(248, 246, 246);
			box-shadow: 0px 0px 0px 0px rgb(44, 7, 7),0px 6px 12px 0px rgba(44, 7, 7, 0.98),1px 23px 23px 0px rgba(44, 7, 7, 0.85),2px 51px 31px 0px rgba(44, 7, 7, 0.5),4px 90px 36px 0px rgba(44, 7, 7, 0.15),6px 141px 40px 0px rgba(44, 7, 7, 0.02);
		}

	..  code-block:: css

		/**
		* Класс полей для ввода
		*/
		.text_input{
			position: absolute;
			width: 371px;
			height: 70px;
			font-size: 25px;
			box-sizing: border-box;
			border: 1px solid rgb(0, 0, 0);
			box-shadow: 0px 0px 0px 0px rgb(44, 7, 7),0px 6px 12px 0px rgba(44, 7, 7, 0.98),1px 23px 23px 0px rgba(44, 7, 7, 0.85),2px 51px 31px 0px rgba(44, 7, 7, 0.5),4px 90px 36px 0px rgba(44, 7, 7, 0.15),6px 141px 40px 0px rgba(44, 7, 7, 0.02);
			background: rgb(196, 196, 196);
		}
		
		
		
		
		
Стили приложения
================
	
	Страница добавления книги (стиль 1)

	.. image:: /styles/add/add1.jpg
	
|
	
	Страница добавления книги (стиль 2)

	.. image:: /styles/add/add2.jpg

|	
	
	Страница добавления книги (стиль 3)

	.. image:: /styles/add/add3.jpg

|

	Страница добавления книги (стиль 4)

	.. image:: /styles/add/add4.jpg

|

	Страница добавления книги (стиль 5)
	
	.. image:: /styles/add/add5.jpg	

|	
	
	Страница с книгами (стиль 1)

	.. image:: /styles/books/books1.jpg
	
	
	Страница с книгами (стиль 2)

	.. image:: /styles/books/books2.jpg

|	
	
	Страница с книгами (стиль 3)
	
	.. image:: /styles/books/books3.jpg

|

	Страница с книгами (стиль 4)
	
	.. image:: /styles/books/books4.jpg

|

	Страница с книгами (стиль 5)
	
	.. image:: /styles/books/books5.jpg

|

	Страница изменения информации о книге (стиль 1)
	
	.. image:: /styles/change/change1.jpg

|	
	
	Страница изменения информации о книге (стиль 2)
	
	.. image:: /styles/change/change2.jpg

|
	
	Страница изменения информации о книге (стиль 3)
	
	.. image:: /styles/change/change3.jpg

|

	Страница изменения информации о книге (стиль 4)
	
	.. image:: /styles/change/change4.jpg

|

	Страница изменения информации о книге (стиль 5)
	
	.. image:: /styles/change/change5.jpg

|
	
	Окно фильтра (стиль 1)
	
	.. image:: /styles/filters/filter1.jpg

|
	
	Окно фильтра (стиль 2)

	.. image:: /styles/filters/filter2.jpg

|
	
	Окно фильтра (стиль 3)

	.. image:: /styles/filters/filter3.jpg

|

	Окно фильтра (стиль 4)

	.. image:: /styles/filters/filter4.jpg

|

	Окно фильтра (стиль 5)
	
	.. image:: /styles/filters/filter5.jpg

|

	Окно заметок и закладки (стиль 1)

	.. image:: /styles/notes/note1.jpg

|	
	
	Окно заметок и закладки (стиль 2)

	.. image:: /styles/notes/note2.jpg

|
	
	Окно заметок и закладки (стиль 3)

	.. image:: /styles/notes/note3.jpg

|

	Окно заметок и закладки (стиль 4)

	.. image:: /styles/notes/note4.jpg

|

	Окно заметок и закладки (стиль 5)
	
	.. image:: /styles/notes/note5.jpg

|

	Окно чтения во весь экран

	.. image:: /styles/other/big1.jpg

|

	Меню изменения стиля
	
	.. image:: /styles/other/menu_style.jpg