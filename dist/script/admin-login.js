const backBtn = document.getElementById('back-btn');
const mobileNav = document.getElementById('mobile-nav');
const hiddenNav = document.querySelector('.hidden-menu');
const mask = document.getElementById('mask');

hiddenNav.addEventListener('click', () => {
    console.log("hey")
    mobileNav.style.display = 'block';
    mask.style.display = 'block';
});

backBtn.addEventListener('click', () => {
    mask.style.display = 'none';
    mobileNav.style.display = 'none';
});


mask.addEventListener('click', () => {
    mask.style.display = 'none';
    mobileNav.style.display = 'none';
});
