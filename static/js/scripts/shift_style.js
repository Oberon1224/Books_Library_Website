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