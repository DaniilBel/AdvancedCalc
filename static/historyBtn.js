const historyBtn = document.getElementById('open-history');
const panel = document.getElementById('history');

const panelState = localStorage.getItem('panelState');

if (panelState === 'opened') {
    panel.classList.add('opened');
}

historyBtn.addEventListener('click', function() {
    panel.classList.toggle('opened');

    if (panel.classList.contains('opened')) {
        localStorage.setItem('panelState', 'opened');
    } else {
        localStorage.setItem('panelState', 'closed');
    }
});
