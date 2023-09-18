document.addEventListener("DOMContentLoaded", function() {
    const historyItems = document.querySelectorAll(".history-item");


    historyItems.forEach(function (item) {
        item.addEventListener("click", function () {
            const result = item.getAttribute("data-result");
            document.getElementsByName("display")[0].value = result;
        });
    });
});