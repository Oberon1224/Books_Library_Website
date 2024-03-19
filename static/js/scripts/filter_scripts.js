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