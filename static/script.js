window.addEventListener('scroll', function() {
    const header = document.querySelector('.header');
    if (window.scrollY > 50) {
    header.classList.add('shrink');
    } else {
    header.classList.remove('shrink');
    }
    adjustHeroPadding(); // Keep hero aligned with new height
});


// Set initial button state
document.addEventListener('DOMContentLoaded', function() {
  const btn = document.querySelector('.btn');
  btn.classList.add('btn-light');
});

function adjustHeroPadding() {
    const header = document.querySelector('.header');
    const hero = document.querySelector('.hero');

    if (header && hero) {
    const headerHeight = header.offsetHeight;
    hero.style.paddingTop = `${headerHeight + 20}px`; // +20 breathing space
    }
}

// Run on page load
document.addEventListener('DOMContentLoaded', adjustHeroPadding);

// Run again if window resizes
window.addEventListener('resize', adjustHeroPadding);