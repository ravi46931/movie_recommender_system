// Get the current URL path
var currentPath = window.location.pathname;
    
// Find all elements with the "nav-link" class
var navLinks = document.querySelectorAll('.nav-link');

// Loop through the elements and check if their data-url attribute matches the current path
navLinks.forEach(function (link) {
  if (link.getAttribute('data-url') === currentPath) {
    link.classList.add('active'); // Apply the "active" class if there is a match
  }
});

function toggleMenu(){
    const menu=document.querySelector(".menu-links");
    const icon=document.querySelector(".hamburger-icon");
    menu.classList.toggle("open");
    icon.classList.toggle("open");
}