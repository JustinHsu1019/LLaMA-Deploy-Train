$(document).ready(function () {
    var socket = io.connect('http://127.0.0.1:9640');

    // 以 check_res 判斷是否為第一筆
    var check_res = 0;

    function sendRequest() {
        const userInput = $("#userInput").val();
        const outputBox = $("#outputBox");

        // 判斷是否為第一筆，同時切分每一次對話 (response不斷接收會無法切分對話)
        if (check_res == 0) {
            outputBox.val(outputBox.val() + "User: " + userInput + "\nLLama: ");
        } else {
            outputBox.val(outputBox.val() + "\nUser: " + userInput + "\nLLama: ");
        }
        check_res = 1;

        $("#userInput").val('');
        socket.emit('generate', { user_input: userInput });
    }

    // 接收 response
    socket.on('response', function (data) {
        const outputBox = $("#outputBox");
        if (data.error) {
            outputBox.val(outputBox.val() + "Error: " + data.error);
        } else {
            outputBox.val(outputBox.val() + data.data);
        }
    });

    // Enter 送出, Shift + Enter 換行
    $("#userInput").keydown(function (e) {
        if (e.key === 'Enter') {
            if (!e.shiftKey) {
                sendRequest();
                e.preventDefault();
            }
        }
    });

    // 送出事件 --> sendRequest()
    $("#sendButton").click(sendRequest);
});
