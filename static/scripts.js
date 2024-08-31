document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        document.querySelector(".loader").style.display = "none";
        document.querySelector(".content").style.display = "block";
        setTimeout(function() {
            document.querySelector(".content").style.opacity = "1";
        }, 100);
    }, 2000); 
});
// BookApp/static/BookApp/scripts.js
document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        document.querySelector(".loader").style.display = "none";
        document.querySelector(".content").style.display = "block";
        setTimeout(function() {
            document.querySelector(".content").style.opacity = "1";
            applyAdditionalAnimations();
        }, 100); // Задержка для плавного появления контента
    }, 2000); // Увеличенная задержка для загрузчика
});

function applyAdditionalAnimations() {
    // Применим анимации к заголовкам
    document.querySelectorAll("h1").forEach(function(element) {
        element.style.animation = "bounceIn 1.5s ease-out";
    });

    // Применим анимации к навигационным ссылкам
    document.querySelectorAll("nav a").forEach(function(element, index) {
        element.style.animation = `rotateIn ${1 + index * 0.2}s ease-out forwards`;
    });

    // Применим анимации к элементам списка
    document.querySelectorAll("ul li").forEach(function(element, index) {
        element.style.animation = `fadeInUp ${1.5 + index * 0.3}s ease-out forwards`;
    });
}
