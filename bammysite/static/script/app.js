const menu = document.querySelector('.menu');
const navHidden = document.querySelector(".nav-overlay");
const back = document.querySelector(".backBtn");
const hamburger = document.querySelector('.hidden-menu');
const mobileNav = document.querySelector('.menubar');
const news_container = document.getElementById('news-container');
const menuSan = () => {
    // console.log("menuuuuu")
    navHidden.classList.add("show")
}

menu.addEventListener("click", menuSan);


const backSan = () => {
    // console.log("backkkk")
    navHidden.classList.remove("show")
}

hamburger.addEventListener('click', () => {

 })

back.addEventListener("click", backSan)


// latest news


fetch('/feeds')
.then((response) => {
    return response.json()
})
.then((res)=>{
    console.log(res)
    newArray = [res[0],res[1],res[2]];
    return newArray;
})
.then((res)=>{
    console.log(res);
    res.forEach(res => {
        let news = document.createElement('div');
        news.className = 'news';
        let news_header = document.createElement('div');
        news_header.className = 'news-header';
        news_header.innerHTML = res.title;
        let mob_view = document.createElement('div');
        mob_view.className = 'mobile-view-div';
        let news_imgContainer = document.createElement('div')
        news_imgContainer.className = 'news-image-container';
        let news_img = document.createElement('img');
        news_img.className = 'news-image';
        news_img.src = Flask.url_for('static', {'filename': `uploads/${res.img_data}`});
        let news_body = document.createElement('p');
        news_body.innerHTML = res.body;
        let readmore = document.createElement('a');
        news_body.appendChild(readmore);
        news_imgContainer.appendChild(news_img);
        mob_view.appendChild(news_imgContainer);
        mob_view.appendChild(news_body);
        news.appendChild(news_header);
        news.appendChild(mob_view);
        news_container.appendChild(news);
    })
});
