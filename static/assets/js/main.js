// =================== Show Menu ======================
const navMenu = document.getElementById('nav-menu'),
      navToggle =  document.getElementById('nav-toggle'),
      navClose = document.getElementById('nav-close')

// =================== Menu Show ======================
// Validate if constant exists
if(navToggle){
    navToggle.addEventListener('click',() => {
        navMenu.classList.add('show-menu')
    })
}

// =================== Menu Hidden ====================
// Validate if constant exists
if(navClose){
    navClose.addEventListener('click',() => {
        navMenu.classList.remove('show-menu')
    })
}

// =================== Remove Menu Mobile ==================
const navlink = document.querySelectorAll('.nav__link')

const linkAction = () => {
    const navMenu = document.getElementById('nav-menu')
    // when we click on each nav__link, we remove the show-menu click
    navMenu.classList.remove('show-menu')
}
navlink.forEach(n => n.addEventListener('click',linkAction))