import"../../admin.bundle-BD84ghkN.js";/* empty css          *//* empty css      *//* empty css    */import"../../main-dpGOw9z9.js";(function(){document.addEventListener("DOMContentLoaded",function(){m(),f()});function m(){const t=document.querySelector('.btn-outline-info[data-action="contact-carrier"]');t&&t.addEventListener("click",function(){s()});const e=document.querySelector('.btn-outline-primary[data-action="edit-order"]');e&&e.addEventListener("click",function(){r()});const o=document.querySelector('.btn-outline-success[data-action="duplicate-order"]');o&&o.addEventListener("click",function(){d()});const n=document.querySelector('.btn-outline-warning[data-action="cancel-order"]');n&&n.addEventListener("click",function(){l()});const i=document.querySelector('.btn-outline-info[data-action="download-invoice"]');i&&i.addEventListener("click",function(){downloadInvoice()})}function f(){setInterval(()=>{u()},3e4),u()}function s(){const t="+1-800-463-3339",e="support@semidash.com",o=`
            <div class="alerts alert-info">
                <h6 class="alert-heading">Semidash Contact Information</h6>
                <p class="mb-2">Phone: <a href="tel:${t}" class="text-white">${t}</a></p>
                <p class="mb-0">Email: <a href="mailto:${e}" class="text-white">${e}</a></p>
            </div>
        `;c(o,"info",!0)}function r(){c("Edit order functionality will open order editing form...","info"),setTimeout(()=>{window.location.href="apps-ecommerce-orders-list.html"},2e3)}function d(){c("Order duplicated successfully! Redirecting to new order...","success"),setTimeout(()=>{window.location.href="apps-ecommerce-orders-list.html"},2e3)}function l(){confirm("Are you sure you want to cancel this order? This action cannot be undone.")&&c("Order cancellation request submitted successfully!","success")}function u(){document.querySelectorAll(".shipment-timeline .timeline-item").forEach((e,o)=>{if(Math.random()>.8){e.classList.remove("completed","active"),e.classList.add("completed");const n=e.querySelector("small");if(n){const i=new Date;n.textContent=`${i.toLocaleDateString()} - ${i.toLocaleTimeString()} • Updated`}}})}function c(t,e="info",o=!1){const n=document.querySelector(".toast-container")||p(),i=`
            <div class="toast align-items-center text-bg-${e} border-0" role="alert" aria-live="assertive" aria-atomic="true">
                <div class="d-flex">
                    <div class="toast-body">
                        ${t}
                    </div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
            </div>
        `;n.insertAdjacentHTML("beforeend",i);const a=n.lastElementChild;new bootstrap.Toast(a).show(),setTimeout(()=>{a.parentNode&&a.remove()},5e3)}function p(){const t=document.createElement("div");return t.className="toast-container position-fixed top-0 end-0 p-3",t.style.zIndex="9999",document.body.appendChild(t),t}window.contactCarrier=s,window.editOrder=r,window.duplicateOrder=d,window.cancelOrder=l})();
