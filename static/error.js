const element = document.getElementById('error');

if (element.textContent.trim() === '') {
    element.style.display = 'none';
} else {
    element.style.display = 'block';
}