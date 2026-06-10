import"../../admin.bundle-BD84ghkN.js";/* empty css          *//* empty css      *//* empty css    */import"../../main-dpGOw9z9.js";const l=""+new URL("../../images/product-01.webp",import.meta.url).href,u=""+new URL("../../images/product-03.webp",import.meta.url).href,m=""+new URL("../../images/product-09.webp",import.meta.url).href,p=""+new URL("../../images/product-06.webp",import.meta.url).href,y=document.getElementById("timeToLeftPage");let a=300;const g=setInterval(function(){const t=Math.floor(a/60),e=a%60;y.textContent=`${t}:${e<10?"0":""}${e}`,a--,a<0&&(clearInterval(g),window.location.href="apps-ecommerce-products-list.html")},1e3),c=[{id:1,category:"Woman's Fashion",categoryColor:"primary",title:"Tie-Up Neck Top",image:l,price:22.12,originalPrice:29.49,discount:25,quantity:1,selectedSize:"S",selectedColor:"White"},{id:2,category:"Footwear",title:"Elegantly Rounded Shoes",image:u,price:71.56,quantity:2,selectedSize:"6",selectedColor:"Light Blue"},{id:3,category:"Men's Fashion",title:"Oversize Cotton Graphic T-Shirt",image:m,price:44.49,quantity:1,selectedSize:"XL",selectedColor:"Gray"},{id:4,category:"Woman's Fashion",title:"Slim Fit Printed Top",image:p,price:67.99,quantity:1,selectedSize:"L",selectedColor:"Black"}];function b(){const t=document.getElementById("cartProductList");t.innerHTML="",c.forEach(e=>{const s=(e.price*e.quantity).toFixed(2),i=document.createElement("div");i.className="card mb-0",i.setAttribute("data-id",e.id),i.innerHTML=`
        <div class="card-body">
            <div class="row g-5">
                <div class="col-md-2">
                    <img src="${e.image}" loading="lazy" alt="Product Image" class="img-fluid rounded-2">
                </div>
                <div class="col-md-10">
                    <div class="row h-100">
                    <div class="col-lg-6 col-xl-12 col-xxl-6">
                        <h6 class="mt-2 fs-16"><a href="#!" class="text-body">${e.title}</a></h6>
                        <p class="text-muted mb-2">Category: <span class="fw-medium">${e.category}</span></p>
                        <p class="text-muted mb-2">Color: <span class="fw-medium">${e.selectedColor}</span></p>
                        <p class="text-muted mb-2">Size: <span class="fw-medium">${e.selectedSize}</span></p>
                        <p class="text-muted">Price: <span class="fw-medium">$${e.price}</span> per item</p>
                    </div>   
                    <div class="col-lg-6 col-xl-12 col-xxl-6">
                        <div class="d-flex flex-column align-items-end h-100">
                            <h6 class="fs-16 mb-0">$${s}</h6>
                            <div class="mt-auto d-flex align-items-center gap-2">
                                <div class="input-spin-group input-borderless p-1 border rounded">
                                    <button type="button" aria-label="Minus" class="input-spin-minus btn bg-primary-subtle text-primary px-2 border-0 size-8 d-flex justify-content-center align-items-center" data-id="${e.id}"><i class="mgc_minimize_line"></i></button>
                                    <input type="text" class="input-spin form-control text-center border-0 h-8 quantity-display" readonly value="${e.quantity}">
                                    <button type="button" aria-label="Plus" class="input-spin-plus btn bg-primary-subtle text-primary px-2 border-0 size-8 d-flex justify-content-center align-items-center" data-id="${e.id}"><i class="mgc_add_line"></i></button>
                                </div>
                                <button type="button" aria-label="Wishlist" class="btn btn-icon btn-sub-dark"><i class="mgc_heart_line"></i></button>
                                <button type="button" aria-label="Remove" class="btn btn-icon btn-sub-danger remove-item"><i class="mgc_close_line"></i></button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
      `,t.appendChild(i)}),f()}function f(){document.querySelectorAll(".input-spin-minus").forEach(t=>{t.addEventListener("click",()=>{const e=+t.dataset.id,s=c.find(i=>i.id===e);if(s.quantity>1){s.quantity--;const i=t.closest(".card");i.querySelector(".quantity-display").value=s.quantity,i.querySelector(".price-display").textContent=`$${(s.price*s.quantity).toFixed(2)}`,d()}})}),document.querySelectorAll(".input-spin-plus").forEach(t=>{t.addEventListener("click",()=>{const e=+t.dataset.id,s=c.find(n=>n.id===e);s.quantity++;const i=t.closest(".card");i.querySelector(".quantity-display").value=s.quantity,i.querySelector(".price-display").textContent=`$${(s.price*s.quantity).toFixed(2)}`,d()})}),document.querySelectorAll(".remove-item").forEach(t=>{t.addEventListener("click",()=>{const e=t.closest(".card"),s=+e.dataset.id,i=c.findIndex(n=>n.id===s);i!==-1&&(c.splice(i,1),e.remove(),d())})}),document.querySelectorAll(".size-option").forEach(t=>{t.addEventListener("click",()=>{const e=+t.dataset.id,s=t.dataset.size,i=c.find(o=>o.id===e);i.selectedSize=s,t.closest(".card").querySelectorAll(".size-option").forEach(o=>{o.classList.remove("text-success"),o.classList.add("text-muted")}),t.classList.add("text-success"),t.classList.remove("text-muted")})}),document.querySelectorAll(".color-option").forEach(t=>{t.addEventListener("click",()=>{const e=+t.dataset.id,s=t.dataset.color,i=c.find(o=>o.id===e);i.selectedColor=s,t.closest(".card").querySelectorAll(".color-option").forEach(o=>{o.classList.remove("border","border-dark")}),t.classList.add("border","border-dark")})})}function d(){const t=c.reduce((o,r)=>o+r.price*r.quantity,0),e=t*.06,s=t*.1,i=35,n=t+e+i-s;document.getElementById("subtotal").textContent=t.toFixed(2),document.getElementById("vat").textContent=e.toFixed(2),document.getElementById("discount").textContent=s.toFixed(2),document.getElementById("shipping").textContent=i.toFixed(2),document.getElementById("total").textContent=n.toFixed(2)}document.addEventListener("DOMContentLoaded",()=>{b(),d()});
