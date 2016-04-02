/* Javascript for TermsXBlock. */
function TermsXBlock(runtime, element) {

    function updateCount(result) {
        //Получили count и next_one из скрипта-обработчика increment_count
        $('.count', element).text(result.count); 
        $('.next_one', element).text(result.next_one); //В (П) указан параметр next_one. Мы его получаем в объекте result, а его название - метод
    }

    function updateList(result) {
        $('.next_one', element).text(result.next_one);
    }

    var handlerUrl = runtime.handlerUrl(element, 'increment_count'); //increment_ount - привязываем данный "элемент" к скрипту increment_count и генерируем URL
    var handlerUrl2 = runtime.handlerUrl(element, 'updateList');

    $('.count', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"hello": "world", "hello2" : "check"}), //Запечатываем массив (hello => "world" и hello2 => "check")
            success: updateCount //Вызов функции updateCount(result) при успехе, где result - объект, который мы передали из (П) функции increment_count
        });
    });

    $('.halo', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrl2,
            data: JSON.stringify({"term": document.getElementById("term").value}),
            success: updateList
        });
    });
    /*$('.next_one', element).click(function(eventObject) { //Функция для декрементации
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"hello": "world"}), //Запечатываем массив (hello => "world" и hello2 => "check")
            success: updateCount //Вызов функции updateCount(result) при успехе, где result - объект, который мы передали из (П) функции increment_count
        });
    });*/

    $(function ($) {
        //Тут действия при загрузке страницы
    });
}
