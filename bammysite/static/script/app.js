const news_container = document.getElementById('news-container');
const navHidden = document.querySelector(".mobile-nav")
const hamburger = document.querySelector('#spinner-form');

const menuSan = () => {
    navHidden.classList.toggle("nav-out")
}

hamburger.addEventListener("click", menuSan);
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
        readmore.innerHTML = 'Read_more'
        news_body.innerHTML = news_body.innerHTML.substr(0, 200).replace('/\w*$/,')+'....' + readmore;
        news_body.appendChild(readmore);
        news_imgContainer.appendChild(news_img);
        mob_view.appendChild(news_imgContainer);
        mob_view.appendChild(news_body);
        news.appendChild(news_header);
        news.appendChild(mob_view);
        news_container.appendChild(news);
    })
});
