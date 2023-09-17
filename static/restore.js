document.addEventListener("DOMContentLoaded", function() {
    const historyItems = document.querySelectorAll(".history-item");


    historyItems.forEach(function (item) {
        item.addEventListener("click", function () {
            const result = item.getAttribute("data-result");
            document.getElementsByName("display").value = result;
            alert(document.getElementsByName("display").value);

            // fetch('/calculate', {
            //     method: 'POST',
            // }).then(data => {
            //     window.location.reload();
            // })
            // .catch(error => {
            //     console.log(error);
            // });
        });
    });
});