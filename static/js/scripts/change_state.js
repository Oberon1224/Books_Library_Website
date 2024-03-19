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