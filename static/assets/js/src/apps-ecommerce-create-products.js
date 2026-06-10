import"../../admin.bundle-BD84ghkN.js";/* empty css                               *//* empty css          *//* empty css      *//* empty css    */import"../../main-dpGOw9z9.js";document.addEventListener("DOMContentLoaded",function(){f(),B(),y(),I(),m(),v(),window.resetForm=p,window.saveAsDraft=L,window.removeImagePreview=w});function f(){const t=document.getElementById("productCreateForm");if(t){t.addEventListener("submit",b);const e=document.getElementById("productName"),s=document.getElementById("productDescription"),n=document.getElementById("productMetaTitle"),a=document.getElementById("productMetaDescription");e&&n&&e.addEventListener("input",function(){n.value||(n.value=this.value,d(n,60-this.value.length,60,"metaTitleCount"))}),s&&a&&s.addEventListener("input",function(){a.value||(a.value=this.value.substring(0,160),d(a,160-this.value.length,160,"metaDescCount"))})}}function m(){const t=document.getElementById("productCreateForm"),e=document.querySelector(".progress-bar"),s=document.getElementById("progressText");if(t&&e&&s){let o=function(){let i=0;n.forEach(l=>{l.value.trim()!==""&&i++});const r=Math.round(i/a*100);e.style.width=r+"%",s.textContent=r+"% Complete",r<25?e.className="progress-bar bg-danger":r<50?e.className="progress-bar bg-warning":r<75?e.className="progress-bar bg-info":e.className="progress-bar bg-success"};const n=t.querySelectorAll("[required]"),a=n.length;n.forEach(i=>{i.addEventListener("input",o),i.addEventListener("change",o)}),o()}}function v(){document.querySelectorAll(".upload-area").forEach(e=>{e.addEventListener("dragover",function(s){s.preventDefault(),this.style.borderColor="#007bff",this.style.backgroundColor="#f8f9fa"}),e.addEventListener("dragleave",function(s){s.preventDefault(),this.style.borderColor="",this.style.backgroundColor=""}),e.addEventListener("drop",function(s){s.preventDefault(),this.style.borderColor="",this.style.backgroundColor="";const n=s.dataTransfer.files;if(n.length>0){const a=this.closest("label").querySelector('input[type="file"]');a&&(a.files=n,a.dispatchEvent(new Event("change")))}})})}function b(t){if(t.preventDefault(),h()){const e=new FormData(t.target),s=Object.fromEntries(e.entries());s.productFeatured=document.getElementById("productFeatured").checked,s.productFreeShipping=document.getElementById("productFreeShipping").checked;const n=t.target.querySelector('button[type="submit"]'),a=n.innerHTML;n.innerHTML='<i class="mgc_loading_4_line me-2"></i>Creating Product...',n.disabled=!0,setTimeout(()=>{k(s),n.innerHTML=a,n.disabled=!1},2e3)}}function h(){const t=["productName","productCategory","productDescription","productPrice","productStock","productMainImage"];let e=!0;t.forEach(o=>{const i=document.getElementById(o);i&&!i.value.trim()?(c(i,"This field is required"),e=!1):i&&u(i)});const s=document.getElementById("productPrice"),n=document.getElementById("productSalePrice");s&&n&&s.value&&n.value&&parseFloat(n.value)>=parseFloat(s.value)&&(c(n,"Sale price must be less than regular price"),e=!1);const a=document.getElementById("productStock");return a&&a.value<0&&(c(a,"Stock quantity cannot be negative"),e=!1),e}function c(t,e){u(t),t.classList.add("is-invalid");const s=document.createElement("div");s.className="invalid-feedback",s.textContent=e,t.parentNode.appendChild(s)}function u(t){t.classList.remove("is-invalid");const e=t.parentNode.querySelector(".invalid-feedback");e&&e.remove()}function y(){const t=document.getElementById("productMainImage"),e=document.getElementById("productGallery");t&&t.addEventListener("change",function(s){E(this,"mainImagePreview")}),e&&e.addEventListener("change",function(s){x(this,"galleryPreview")})}function E(t,e){if(t.files&&t.files[0]){const s=new FileReader;s.onload=function(n){let a=document.getElementById(e);a||(a=document.createElement("div"),a.id=e,a.className="mt-3",t.closest("label").appendChild(a)),a.innerHTML=`
                <div class="position-relative d-inline-block">
                    <img src="${n.target.result}" class="img-thumbnail shadow-sm" style="max-width: 200px; max-height: 200px; object-fit: cover;">
                    <button type="button" class="btn btn-sm btn-danger position-absolute top-0 end-0 rounded-circle" 
                            onclick="removeImagePreview('${e}')" style="margin: 5px; width: 30px; height: 30px;">
                        <i class="mgc_close_line"></i>
                    </button>
                    <div class="position-absolute bottom-0 start-0 w-100 bg-dark bg-opacity-75 text-white p-2">
                        <small>${t.files[0].name}</small>
                    </div>
                </div>
            `;const o=t.closest("label").querySelector(".upload-area");o&&(o.innerHTML=`
                    <span class="avatar size-12 bg-success-subtle rounded-circle mx-auto mb-3">
                        <i class="mgc_check_line text-success fs-5"></i>
                    </span>
                    <span class="d-block text-success mt-2 mb-1">Image uploaded successfully!</span>
                    <small class="text-muted">Click to change image</small>
                `)},s.readAsDataURL(t.files[0])}}function x(t,e){if(t.files&&t.files.length>0){let s=document.getElementById(e);s||(s=document.createElement("div"),s.id=e,s.className="mt-3",t.closest("label").appendChild(s)),s.innerHTML="",Array.from(t.files).forEach((a,o)=>{const i=new FileReader;i.onload=function(r){const l=document.createElement("div");l.className="position-relative d-inline-block me-3 mb-3",l.innerHTML=`
                    <img src="${r.target.result}" class="img-thumbnail shadow-sm" style="max-width: 150px; max-height: 150px; object-fit: cover;">
                    <button type="button" class="btn btn-sm btn-danger position-absolute top-0 end-0 rounded-circle" 
                            onclick="removeImagePreview('${e}', ${o})" style="margin: 5px; width: 30px; height: 30px;">
                        <i class="mgc_close_line"></i>
                    </button>
                    <div class="position-absolute bottom-0 start-0 w-100 bg-dark bg-opacity-75 text-white p-2">
                        <small>${a.name}</small>
                    </div>
                `,s.appendChild(l)},i.readAsDataURL(a)});const n=t.closest("label").querySelector(".upload-area");n&&(n.innerHTML=`
                <span class="avatar size-12 bg-success-subtle rounded-circle mx-auto mb-3">
                    <i class="mgc_check_line text-success fs-5"></i>
                </span>
                <span class="d-block text-success mt-2 mb-1">${t.files.length} images uploaded!</span>
                <small class="text-muted">Click to add more images</small>
            `)}}function w(t,e=null){const s=document.getElementById(t);if(s){if(e!==null){const a=s.querySelectorAll(".position-relative");a[e]&&a[e].remove()}else s.remove();const n=s.closest("label").querySelector('input[type="file"]');if(n){n.value="";const a=n.closest("label").querySelector(".upload-area");a&&(n.id==="productMainImage"?a.innerHTML=`
                        <span class="avatar size-12 bg-primary-subtle rounded-circle mx-auto mb-3">
                            <i class="mgc_upload_2_line text-primary fs-5"></i>
                        </span>
                        <span class="d-block text-muted mt-2 mb-1">Click to upload main image</span>
                        <small class="text-muted">Recommended: 1:1 pixels, JPG/PNG</small>
                    `:a.innerHTML=`
                        <span class="avatar size-12 bg-primary-subtle rounded-circle mx-auto mb-3">
                            <i class="mgc_upload_2_line text-primary fs-5"></i>
                        </span>
                        <span class="d-block text-muted mt-2 mb-1">Click to upload multiple images</span>
                        <small class="text-muted">Drag & drop or click to select</small>
                    `)}}}function I(){const t=document.getElementById("productName"),e=document.getElementById("productSKU");t&&e&&t.addEventListener("input",function(){if(!e.value){const s=C(this.value);e.value=s}})}function C(t){if(!t)return"";const e=Date.now().toString().slice(-4);return`${t.toUpperCase().replace(/[^A-Z0-9]/g,"").substring(0,6)}${e}`}function k(t){console.log("Creating product:",t),g("🎉 Product created successfully!","success"),p()}function L(){const t=document.getElementById("productCreateForm");if(t){const e=new FormData(t),s=Object.fromEntries(e.entries());s.productStatus="draft",s.productFeatured=document.getElementById("productFeatured").checked,s.productFreeShipping=document.getElementById("productFreeShipping").checked,g("💾 Product saved as draft!","success")}}function p(){const t=document.getElementById("productCreateForm");if(t){t.reset();const e=document.getElementById("mainImagePreview"),s=document.getElementById("galleryPreview");e&&e.remove(),s&&s.remove(),t.querySelectorAll(".is-invalid").forEach(a=>{a.classList.remove("is-invalid")}),t.querySelectorAll(".invalid-feedback").forEach(a=>{a.remove()}),t.querySelectorAll(".upload-area").forEach((a,o)=>{o===0?a.innerHTML=`
                    <span class="avatar size-12 bg-primary-subtle rounded-circle mx-auto mb-3">
                        <i class="mgc_upload_2_line text-primary fs-5"></i>
                    </span>
                    <span class="d-block text-muted mt-2 mb-1">Click to upload main image</span>
                    <small class="text-muted">Recommended: 1:1 pixels, JPG/PNG</small>
                `:a.innerHTML=`
                    <span class="avatar size-12 bg-primary-subtle rounded-circle mx-auto mb-3">
                        <i class="mgc_upload_2_line text-primary fs-5"></i>
                </span>
                    <span class="d-block text-muted mt-2 mb-1">Click to upload multiple images</span>
                    <small class="text-muted">Drag & drop or click to select</small>
                `}),m()}}function g(t,e="info"){const s=document.createElement("div");s.className=`alert alert-${e} alert-dismissible fade show position-fixed`,s.style.cssText="top: 20px; right: 20px; z-index: 9999; min-width: 350px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);",s.innerHTML=`
        <div class="d-flex align-items-center">
            <div class="me-3">
                ${e==="success"?"🎉":e==="warning"?"⚠️":e==="danger"?"❌":"ℹ️"}
            </div>
            <div class="flex-grow-1">
                ${t}
            </div>
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `,document.body.appendChild(s),setTimeout(()=>{s.parentNode&&s.remove()},5e3)}function B(){const t=document.getElementById("productPrice"),e=document.getElementById("productSalePrice");t&&e&&[t,e].forEach(a=>{a.addEventListener("input",function(){t.value&&e.value&&(parseFloat(e.value)>=parseFloat(t.value)?c(e,"Sale price must be less than regular price"):u(e))})});const s=document.getElementById("productMetaTitle"),n=document.getElementById("productMetaDescription");s&&s.addEventListener("input",function(){const a=60-this.value.length;d(this,a,60,"metaTitleCount")}),n&&n.addEventListener("input",function(){const a=160-this.value.length;d(this,a,160,"metaDescCount")})}function d(t,e,s,n){const a=document.getElementById(n);if(a){const o=e<0?"text-danger":e<10?"text-warning":"text-muted";a.className=`text-muted ${o}`,a.textContent=`${Math.max(0,e)}/${s}`,e<0?t.classList.add("is-invalid"):t.classList.remove("is-invalid")}}
