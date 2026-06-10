import"../../admin.bundle-BD84ghkN.js";/* empty css          *//* empty css      *//* empty css    */import{u as o,a as l,b as m}from"../../user-60-BivYOsBf.js";import{u as c,a as u}from"../../user-61-ByeBmVEC.js";import"../../main-dpGOw9z9.js";document.addEventListener("DOMContentLoaded",function(){document.querySelectorAll(".post-text").forEach(function(e){const n=e.getAttribute("data-full");e.getAttribute("data-short");const a=e.querySelector(".see-more");a&&a.addEventListener("click",function(i){i.preventDefault(),e.innerHTML=n})})});const r=[{name:"Edilson De Carvalho",avatar:o,date:"Today",messageBox:!0},{name:"Tommy Beahan",avatar:l,date:"Tomorrow"},{name:"Sheila Parker",avatar:m,date:"19 Feb"},{name:"Peggy Ernser",avatar:c,date:"20 Feb"},{name:"Nora Keebler",avatar:u,date:"21 Feb"}];let t=!1;function d(){const e=document.getElementById("birthdayList"),n=document.getElementById("upcomingSummary");let a="";(t?r:[r[0]]).forEach(s=>{a+=`
      <div class="d-flex align-items-center">
        <img src="${s.avatar}" class="rounded-circle size-10 me-3" alt="">
        <div>
          <h6 class="mb-0">${s.name}</h6>
          <small class="text-muted">${s.date==="Today"?"Birthday today":s.date}</small>
        </div>
      </div>
    `}),e.innerHTML=a,t?n.innerHTML="":n.innerHTML=`
      <div class="d-flex align-items-center bg-light rounded p-2">
        <div class="bg-primary-subtle rounded-circle d-flex align-items-center justify-content-center me-3" style="width: 36px; height: 36px;">
          <i class="mgc_gift_2_line text-primary fs-5"></i>
        </div>
        <div>
          <div class="fw-medium">Upcoming birthdays</div>
          <small class="text-muted">See ${r.length-1} others have upcoming birthdays</small>
        </div>
      </div>
    `,document.getElementById("birthdayMessageBox").style.display=!t&&r[0].messageBox?"flex":"none"}document.addEventListener("DOMContentLoaded",function(){d(),document.getElementById("seeAllBirthdays").addEventListener("click",function(e){e.preventDefault(),t=!t,this.textContent=t?"Show Less":"See All",d()})});
