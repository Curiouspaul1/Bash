let storyInfoArr = [];
let newsLetterArr = [];


const addStory = (e) =>{
    e.preventDefault();

    let storyDetails = {
        story_title: document.getElementById('new-story__title').value,
        story_pictures: storyPics(),
        story:CKEDITOR.instances['story-info'].getData(),
    }
    storyInfoArr.push(storyDetails);
    document.querySelector('form').reset();
    CKEDITOR.instances['story-info'].setData('');
    return JSON.stringify(storyInfoArr);
}

const addNewsLetter = (e) =>{
    e.preventDefault();

    let newsletterDetails = {
        newsletter_title: document.getElementById('newsletter__title'),
        newsletter: CKEDITOR.instances['newsletter-content'].getData(),
    }

    newsLetterArr.push(newsletterDetails);
    document.querySelector('form').reset();
    CKEDITOR.instances['newsletter-content'].setData('');
    return JSON.stringify(newsLetterArr);
}

function storyPics() {
    let picsArr = [];
    const pics = document.getElementsByClassName('new-story__photo');

    for (let i = 0; i < photosDiv.childElementCount; i++) {
        picsArr.push(pics[i].value);
    }

    console.log(picsArr)
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('.btn-submit-story').addEventListener('click', addStory);
    document.querySelector('.btn-send-newsletter').addEventListener('click', addNewsLetter);
});