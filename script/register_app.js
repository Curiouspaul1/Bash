const siblingsData = document.querySelector('.siblings');

const numberOfSiblings = document.getElementById('number-of-siblings');

const yesRadio = document.getElementById('yes_radio');

const noRadio = document.getElementById('no_radio');

const defectsList = document.getElementById('defects_list');

const mobileNav = document.getElementById('mobile-nav');

const mask = document.getElementById('mask');

const backBtn = document.getElementById('back-btn');

const hiddenNav = document.querySelector('.hidden-menu');

const siblingInfoString = `<div class="siblings-data">
    <h3 class="title__subtitle">Siblings Data</h3>
    <hr class="underline">
    <div class="siblings-input">
        <label for="S_name">Full Name:</label>
        <input type="text" name="S_name" class="S_name">
    </div>
    <div class="siblings-input">
        <label for="S_class">Class:</label>
        <input type="text" name="S_class" class="S_class">
    </div>
    <div class="siblings-input">
        <label for="S_year">Year:</label>
        <input type="text" name="S_year" class="S_year">
    </div>
    <hr>
    </div>`;

//Event Listeners
yesRadio.addEventListener('click', () => {
    defectsList.style.display = 'block';
});

noRadio.addEventListener('click', () => {
    defectsList.style.display = 'none';
});



numberOfSiblings.addEventListener('change', () => {
    if(siblingsData.childElementCount > numberOfSiblings.value){
        siblingsData.innerHTML = '';
    }
    const numberOfForms = numberOfSiblings.value - siblingsData.childElementCount;
    for(let i=0; i < numberOfForms; i++){
        const siblingInfoEl = new DOMParser().parseFromString(siblingInfoString, "text/html").firstChild;
        siblingsData.appendChild(siblingInfoEl);
    }
});


hiddenNav.addEventListener('click', () => {
    mobileNav.style.display= 'block';
    mask.style.display = 'block';
});

backBtn.addEventListener('click', () =>{
    mask.style.display = 'none';
    mobileNav.style.display = 'none';
});

mask.addEventListener('click', () => {
    mask.style.display = 'none';
    mobileNav.style.display = 'none';
});

