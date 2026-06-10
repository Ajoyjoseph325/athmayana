const de_swiper = new Swiper('.swiper', {

  autoplay: {
     delay: 3000,
     disableOnInteraction: false
   },

  // Optional parameters
  effect: "slide", // cards, coverflow, cube, fade, flip, slide 
  slidesPerView: 1,
  loop: true,
  speed: 1200,
  mousewheel: false,
  watchSlidesProgress: true,
  parallax: true,
  spaceBetween: -1,

  // If we need pagination
   pagination: {
      el: ".swiper-pagination",
      type: "fraction",
    },

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },

  watchSlidesProgress: true

});

const galleryItems = document.querySelectorAll(".zpk-item-box img");
const lightbox = document.querySelector(".rvx-light-mask");
const popupImage = document.querySelector(".jtr-popup-img");
const closeBtn = document.querySelector(".fnp-close-btn");

galleryItems.forEach(item => {

    item.addEventListener("click", function(){

        popupImage.src = this.src;

        lightbox.classList.add("active-pop");

    });

});

closeBtn.addEventListener("click", ()=>{

    lightbox.classList.remove("active-pop");

});

lightbox.addEventListener("click", function(e){

    if(e.target===this){

        lightbox.classList.remove("active-pop");

    }

});