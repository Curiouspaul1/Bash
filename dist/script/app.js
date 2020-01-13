const navHidden = document.querySelector(".mobile-nav")
const hamburger = document.querySelector('#spinner-form');

const menuSan = () => {
    navHidden.classList.toggle("nav-out")
}

hamburger.addEventListener("click", menuSan);
