// Показывает уведомленеи об ошибке, которое исчезает после обновления или вычисления результата
const element = document.getElementById('error');

if (element.textContent.trim() === '') {
    element.style.display = 'none';
} else {
    element.style.display = 'block';
}