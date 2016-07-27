/* Javascript for TermsXBlock. */
function TermsXBlock(runtime, element) {

    function updateCount(result) {
        //Функция, которая берет из поля для ввода текстовую информацию и запихивает в массив exampleList
        $('.exampleListOfTerms', element).text(result.exampleList);
        $('.thisIsTest', element).text(result.test);
    }

    var handlerUrl = runtime.handlerUrl(element, 'termsListCheck'); //increment_ount - привязываем данный "элемент" к скрипту increment_count и генерируем URL
	
	
	
	var autoUrl = runtime.handlerUrl(element, 'getTerms');
	$( "#tags" ).autocomplete({
    source: function (request, response) {
        $.ajax({
            type: "POST",
            url: autoUrl,
            data: JSON.stringify({ query: request.term }),
            success: function (data) {
                var transformed = $.map(data, function (el) {
                    return {
                        label: el.phrase,
                        value: el.id
                    };
                });
                alert(transformed);
                response(transformed);
            },
            error: function () {
                response([]);
            }
        });
    }        
	});        


	

    $('.halo', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"term": document.getElementById("term").value, "id": document.getElementById("id").value}), //Запечатываем массив (hello => "world" и hello2 => "check")
            success: updateCount //Вызов функции updateCount(result) при успехе, где result - объект, который мы передали из (П) функции increment_count
        });
    });
}
