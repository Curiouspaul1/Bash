//Selectors for all
const addPhoto = document.getElementById('add-photo');
const photosDiv = document.querySelector('.new-story__input-images');
// const mask =  document.querySelector('#mask');
const logoutBtn = document.querySelector('.logoutBtn');
const confirmDiv = document.getElementById('confirm-logout');
const yesLogout = document.getElementById('yes_logout');
const noLogout = document.getElementById('no_logout');
const newPhotoDiv = document.querySelectorAll('new-story__input-image');
const deleteImageBtn = document.querySelector('.deleteImage');
const storyTextBox = document.getElementById('story-info');
const storySubmit = document.querySelector('.btn-submit-story')
const newsLetterTextBox = document.getElementById('newsletter-content');
const newsLetterSubmit = document.querySelector('.btn-send-newsletter');
const backBtn = document.getElementById('back-btn');
const mobileNav = document.getElementById('mobile-nav');
const hiddenNav = document.querySelector('.hidden-menu');
const mask = document.getElementById('mask');



addPhoto.addEventListener('click', () => {
    let newPhoto = document.createElement('div');
    newPhoto.className = 'new-story__input-image';
    let picInput = document.createElement('input');
    picInput.setAttribute('type','file');
    picInput.setAttribute('accept', 'image/*');
    picInput.setAttribute('name','new-story__photo');
    picInput.className = 'new-story__photo';
    newPhoto.appendChild(picInput);
    let deleteBtn = document.createElement('button');
    deleteBtn.className = 'deleteImage';
    deleteBtn.innerHTML = '&#10060;';
    deleteBtn.after(newPhoto);
    newPhoto.appendChild(deleteBtn);
    photosDiv.appendChild(newPhoto);
    
})


storySubmit.addEventListener('click', (e) =>{
    e.preventDefault();

    let text = CKEDITOR.instances['story-info'].getData();
    return JSON.stringify(text);
})

newsLetterSubmit.addEventListener('click', (e) =>{
    e.preventDefault();

    let text = CKEDITOR.instances['newsletter-content'].getData();
    return JSON.stringify(text);
})

logoutBtn.addEventListener('click', () =>{
    mask.style.display = 'block';
    confirmDiv.style.display = 'block';
})

yesLogout.addEventListener('click', () =>{
    mask.style.display = 'none';
    confirmDiv.style.display = 'none';
})

noLogout.addEventListener('click', () =>{
    mask.style.display = 'none';
    confirmDiv.style.display = 'none';  
})

photosDiv.addEventListener("click", (e) => {
    if (e.target.classList.contains('deleteImage')){
        e.preventDefault()
        e.target.parentNode.parentNode.removeChild(e.target.parentNode)
    }
})

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
