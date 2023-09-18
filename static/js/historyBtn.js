const historyBtn = document.getElementById('open-history');
const panel = document.getElementById('history');
const image = historyBtn.querySelector('img');

const panelState = localStorage.getItem('panelState');
const imageRotation = localStorage.getItem('imageRotation');

if (imageRotation) {
    image.style.transform = `rotate(${imageRotation}deg)`;
}

if (panelState === 'opened') {
    panel.classList.add('opened');
}

// Запоминаем текущее вращение в кнопке, чтобы после перезапуска страницы оно не сбрасывалось
historyBtn.addEventListener('click', () => {
    const currentRotation = getRotationValue(image);
    const newRotation = currentRotation + 180;

    image.style.transform = `rotate(${newRotation}deg)`;

    localStorage.setItem('imageRotation', newRotation);
})

// Открытие/закрытие панели истории с запоминанием состояния
historyBtn.addEventListener('click', () => {
    panel.classList.toggle('opened');

    if (panel.classList.contains('opened')) {
        localStorage.setItem('panelState', 'opened');
    } else {
        localStorage.setItem('panelState', 'closed');
    }
});

// chatgpt)
function getRotationValue(element) {
    const style = window.getComputedStyle(element);
    const matrix = style.getPropertyValue('transform');
    if (matrix && matrix !== 'none') {
        const values = matrix.split('(')[1].split(')')[0].split(',');
        const a = values[0];
        const b = values[1];
        return Math.round(Math.atan2(b, a) * (180 / Math.PI));
    }
    return 0;
}