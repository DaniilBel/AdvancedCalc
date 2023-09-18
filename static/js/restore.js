document.addEventListener("DOMContentLoaded", function() {
    const historyItems = document.querySelectorAll(".history-item");


    historyItems.forEach(function (item) {
        item.addEventListener("click", function () {
            document.getElementsByName("display")[0].value = item.getAttribute("data-result");
        });
    });
});