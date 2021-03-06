let current_page = 1;
let records_per_page = 5;
const mainNewsContainer = document.querySelector('.news-section');
const menu = document.querySelector('.menu');
//const navHidden = document.querySelector(".nav-overlay");
const back = document.querySelector(".backBtn");
//const hamburger = document.querySelector('.hidden-menu');
const mobileNav = document.querySelector('.menubar');
const news_container = document.getElementById('news-container');
const navHidden = document.querySelector(".mobile-nav")
const hamburger = document.querySelector('#spinner-form');

const menuSan = () => {
    navHidden.classList.toggle("nav-out")
}

hamburger.addEventListener("click", menuSan);

fetch('/news')
.then((req) => {
   return req.json()
})
.then((res)=>{
    console.log(res);
    res.forEach(article => {
        let newsContainer = document.createElement('div');
        newsContainer.className = 'news';
        let newsHeading = document.createElement('div');
        newsHeading.className ='news-heading';
        let newsTitle = document.createElement('h4');
        newsTitle.innerHTML = article.title;
        let newsDate = document.createElement('i');
        let dateObj = new Date(article.date_created);
        newsDate.innerHTML = `${dateObj.toLocaleDateString()}`;
        let newsImg = document.createElement('img');
        newsImg.src = Flask.url_for('static', {'filename': `uploads/${article.img_data}`});
        newsImg.className = 'news-img';
        let newsContent = document.createElement('div');
        newsContent.innerHTML = article.body;
        newsContent.className = 'news-content';
        let newsBody = document.createElement('div');
        newsBody.className = 'news-body';
        newsHeading.appendChild(newsTitle);
        newsHeading.appendChild(newsDate);
        newsBody.appendChild(newsImg);
        newsBody.appendChild(newsContent);
        newsContainer.appendChild(newsHeading);
        newsContainer.appendChild(newsBody);
        mainNewsContainer.appendChild(newsContainer);
    });
    
})


// function prevPage()
// {
//     if (current_page > 1) {
//         current_page--;
//         changePage(current_page);
//     }
// }

// function nextPage()
// {
//     if (current_page < numPages()) {
//         current_page++;
//         changePage(current_page);
//     }
// }
    
// function changePage(page)
// {
//     var btn_next = document.getElementById("btn_next");
//     var btn_prev = document.getElementById("btn_prev");
//     var listing_table = document.getElementById("listingTable");
//     var page_span = document.getElementById("page");
 
//     // Validate page
//     if (page < 1) page = 1;
//     if (page > numPages()) page = numPages();

//     listing_table.innerHTML = "";

//     for (var i = (page-1) * records_per_page; i < (page * records_per_page) && i < objJson.length; i++) {
//         listing_table.innerHTML += objJson[i].adName + "<br>";
//     }
//     page_span.innerHTML = page + "/" + numPages();

//     if (page == 1) {
//         btn_prev.style.visibility = "hidden";
//     } else {
//         btn_prev.style.visibility = "visible";
//     }

//     if (page == numPages()) {
//         btn_next.style.visibility = "hidden";
//     } else {
//         btn_next.style.visibility = "visible";
//     }
// }

// function numPages()
// {
//     return Math.ceil(objJson.length / records_per_page);
// }

// window.onload = function() {
//     changePage(1);
// };
