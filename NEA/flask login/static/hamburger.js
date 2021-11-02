const hamburger = document.querySelector('.hamburger');

hamburger.addEventListener('click', function() {
    this.classList.toggle('is-active')
});

const navbar = document.querySelector('nav');

hamburger.addEventListener('click', function() {
    navbar.classList.toggle('active')
});



