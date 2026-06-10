$(document).ready(function () {

    /* ============================================================
       1. HIDE PRELOADER
    ============================================================ */
    $("#de-loader").fadeOut(600);

    /* ============================================================
       2. STICKY HEADER ON SCROLL
    ============================================================ */
    $(window).on("scroll", function () {
        if ($(this).scrollTop() > 100) {
            $("header").addClass("header-scroll");
        } else {
            $("header").removeClass("header-scroll");
        }
    });

    /* ============================================================
       3. MOBILE MENU TOGGLE
    ============================================================ */
    $("#menu-btn").on("click", function () {
        $(this).toggleClass("active");
        $("#mainmenu").slideToggle(300);
    });

    /* ============================================================
       4. OWL CAROUSEL — 2 column (packages)
    ============================================================ */
    if ($(".owl-2-cols").length) {
        $(".owl-2-cols").owlCarousel({
            loop: true,
            margin: 24,
            nav: false,
            dots: false,
            autoplay: true,
            autoplayTimeout: 4000,
            autoplayHoverPause: true,
            responsive: {
                0:    { items: 1 },
                768:  { items: 1 },
                1024: { items: 2 },
            }
        });
    }

    /* ============================================================
       5. OWL CAROUSEL — single with dots (testimonials)
    ============================================================ */
    if ($(".owl-single-dots").length) {
        $(".owl-single-dots").owlCarousel({
            loop: true,
            margin: 0,
            items: 1,
            nav: false,
            dots: true,
            autoplay: true,
            autoplayTimeout: 5000,
            autoplayHoverPause: true,
            animateOut: "fadeOut",
        });
    }

    /* ============================================================
       6. CUSTOM CAROUSEL NAV BUTTONS
    ============================================================ */
    $(".de-custom-nav").each(function () {
        var target = $(this).data("target");
        $(this).find(".d-prev").on("click", function () {
            $(target).trigger("prev.owl.carousel");
        });
        $(this).find(".d-next").on("click", function () {
            $(target).trigger("next.owl.carousel");
        });
    });

    /* ============================================================
       7. WOW ANIMATIONS
    ============================================================ */
    if (typeof WOW !== "undefined") {
        var wow = new WOW({
            boxClass:     "wow",
            animateClass: "animated",
            offset:       80,
            mobile:       false,
            live:         true,
        });
        wow.init();
    }

    /* ============================================================
       8. JARALLAX PARALLAX
    ============================================================ */
    if (typeof jarallax !== "undefined") {
        jarallax(document.querySelectorAll(".jarallax"), {
            speed: 0.5,
        });
    }

    /* ============================================================
       9. ACCORDION
    ============================================================ */
    $(".accordion-section-title").on("click", function () {
        var target = $(this).data("tab");
        if ($(target).is(":visible")) {
            $(target).slideUp(300);
            $(this).removeClass("active");
        } else {
            $(".accordion-section-content").slideUp(300);
            $(".accordion-section-title").removeClass("active");
            $(target).slideDown(300);
            $(this).addClass("active");
        }
    });

    /* ============================================================
       10. BACK TO TOP
    ============================================================ */
    $("#back-to-top").on("click", function (e) {
        e.preventDefault();
        $("html, body").animate({ scrollTop: 0 }, 600);
    });

    $(window).on("scroll", function () {
        if ($(this).scrollTop() > 300) {
            $("#back-to-top").addClass("show");
        } else {
            $("#back-to-top").removeClass("show");
        }
    });

    /* ============================================================
       11. GALLERY LIGHTBOX
    ============================================================ */
    $(".zpk-item-box img").on("click", function () {
        var src = $(this).attr("src");
        $(".jtr-popup-img").attr("src", src);
        $(".rvx-light-mask").fadeIn(300);
    });

    $(".fnp-close-btn, .rvx-light-mask").on("click", function (e) {
        if ($(e.target).hasClass("rvx-light-mask") || $(e.target).hasClass("fnp-close-btn")) {
            $(".rvx-light-mask").fadeOut(300);
        }
    });

    /* ============================================================
       12. DATA BACKGROUND COLOR
    ============================================================ */
    $("[data-bgcolor]").each(function () {
        $(this).css("background-color", $(this).data("bgcolor"));
    });

    /* ============================================================
       13. DATA BACKGROUND IMAGE
    ============================================================ */
    $("[data-bgimage]").each(function () {
        $(this).css("background-image", $(this).data("bgimage"));
    });

    /* ============================================================
       14. SPLIT TEXT ANIMATION (heading split effect)
    ============================================================ */
    $(".split").each(function () {
        var text = $(this).text();
        var words = text.split(" ");
        var wrapped = words.map(function (word) {
            return '<span class="word">' + word + "</span>";
        });
        $(this).html(wrapped.join(" "));
    });

    /* ============================================================
       15. FX-SLIDE BUTTON HOVER EFFECT
    ============================================================ */
    $(".fx-slide span").each(function () {
        var text = $(this).text();
        $(this).closest("a").attr("data-text", text);
    });

    /* ============================================================
       16. SMOOTH SCROLL FOR ANCHOR LINKS
    ============================================================ */
    $('a[href*="#"]').not('[href="#"]').on("click", function (e) {
        var target = $(this.hash);
        if (target.length) {
            e.preventDefault();
            $("html, body").animate(
                { scrollTop: target.offset().top - 80 },
                600
            );
        }
    });

});