// -----------------------
// Header shrink on scroll
// -----------------------
window.addEventListener('scroll', function () {
  const header = document.querySelector('.header');
  if (window.scrollY > 50) {
    header.classList.add('shrink');
  } else {
    header.classList.remove('shrink');
  }
  adjustHeroPadding(); // Keep hero aligned with new height
});

// -----------------------
// Hero padding adjustment
// -----------------------
function adjustHeroPadding() {
  const header = document.querySelector('.header');
  const hero = document.querySelector('.hero');
  if (header && hero) {
    const headerHeight = header.offsetHeight;
    hero.style.paddingTop = `${headerHeight + 20}px`; // +20 breathing space
  }
}

// Run on load + resize
window.addEventListener('load', adjustHeroPadding);
window.addEventListener('resize', adjustHeroPadding);

// -----------------------
// Main DOMContentLoaded
// -----------------------
document.addEventListener("DOMContentLoaded", () => {
  // --- Alert Box ---
  const params = new URLSearchParams(window.location.search);
  const alertBox = document.getElementById("alert-box");

  function showAlert(message, bgColor, textColor) {
    if (!alertBox) return;
    alertBox.style.display = "block";
    alertBox.style.backgroundColor = bgColor;
    alertBox.style.color = textColor;
    alertBox.textContent = message;

    setTimeout(() => {
      alertBox.style.transition = "opacity 1s ease";
      alertBox.style.opacity = "0";
      setTimeout(() => alertBox.remove(), 1000);
    }, 5000);
  }

  if (params.get("success") === "true") {
    showAlert("✅ Your message has been sent successfully!", "#d4edda", "#155724");
  } else if (params.get("success") === "false") {
    showAlert("❌ Failed to send your message. Please try again.", "#f8d7da", "#721c24");
  }

  // Remove ?success=... from URL
  if (params.has("success") && window.history.replaceState) {
    const newUrl = window.location.origin + window.location.pathname;
    window.history.replaceState({}, document.title, newUrl);
  }

  // --- Mobile Menu Toggle ---
  const menuToggle = document.querySelector('.menu-toggle');
  const navLinks = document.querySelector('.nav-links');
  if (menuToggle && navLinks) {
    menuToggle.addEventListener('click', () => {
      navLinks.classList.toggle('active');
    });

    // Close dropdown after link click
    const links = navLinks.querySelectorAll('a');
    links.forEach(link =>
      link.addEventListener('click', () => {
        navLinks.classList.remove('active');
      })
    );
  }

  // --- Set initial button style ---
  const btn = document.querySelector('.btn');
  if (btn) btn.classList.add('btn-light');

  // --- Update form action based on environment (optional) ---
  const form = document.getElementById("contact-form");
  if (form) {
    if (window.location.hostname.includes("netlify.app") || window.location.hostname.includes("rapttech.com")) {
      form.action = "https://rapttech.netlify.app/contact";
    } else {
      form.action = "/contact"; // Local Flask endpoint
    }
  }
});
