const historyBtn = document.getElementById('open-history');
const panel = document.getElementById('history');

historyBtn.addEventListener('click', function() {
    panel.classList.toggle('opened');
});