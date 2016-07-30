/* Javascript for TermsXBlock. */
function TermsXBlock(runtime, element) {

    function updateCount(result) {
        //Функция, которая берет из поля для ввода текстовую информацию и запихивает в массив exampleList
        $('.exampleListOfTerms', element).text(result.exampleList);
        $('.thisIsTest', element).text(result.test);
    }

    var handlerUrl = runtime.handlerUrl(element, 'termsListCheck'); //increment_ount - привязываем данный "элемент" к скрипту increment_count и генерируем URL
    var autocompleteUrl = runtime.handlerUrl(element, 'termsListCheck');
   
    $(function() {
        console.log("Here 1");
        $( "#term" ).autocomplete({
           source: function( request, response ) {
                console.log("Here 2");
                $.ajax({
                    type: "POST",
                    url: autocompleteUrl,
                    data: JSON.stringify({"term": document.getElementById("term").value}),
                    success: function(res) {
                        console.log("Here 3");
                        alert(res);
                        response(
                            return res
                        );
                    }
                });
            }
        });
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
