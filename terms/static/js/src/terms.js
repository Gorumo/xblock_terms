/* Javascript for TermsXBlock. */
function TermsXBlock(runtime, element) {

    function updateList(result) {
        //Получили count и next_one из скрипта-обработчика increment_count
        $('.exampleListOfTerms', element).text(result.exampleList);
    }

    var handlerUrl = runtime.handlerUrl(element, 'termsListCheck'); //increment_ount - привязываем данный "элемент" к скрипту increment_count и генерируем URL
    var handler2 = runtime.handler2(element, 'aad');
    $('.halo', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"term": document.getElementById("term").value}), //Запечатываем массив (hello => "world" и hello2 => "check")
            success: updateList //Вызов функции updateList(result) при успехе, где result - объект, который мы передали из (П) функции increment_count
        });
    });
  $('.ad', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handler2,
            data: JSON.stringify({"term": document.getElementById("term").value}),
            success: updateList //Вызов функции updateList(result) при успехе, где result - объект, который мы передали из (П) функции increment_count
        });
    });
    $(function ($) {
        //Тут действия при загрузке страницы
    });
}
