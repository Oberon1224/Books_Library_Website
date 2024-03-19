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
