// Tiny script: hamburger toggle + footer year
(function () {
  var btn = document.querySelector('.menu-toggle');
  var links = document.querySelector('.nav-links');
  if (btn && links) {
    btn.addEventListener('click', function () {
      // the class alone told assistive tech nothing about whether the menu was open
      var open = links.classList.toggle('open');
      btn.setAttribute('aria-expanded', String(open));
      btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    });
  }
  var year = document.querySelectorAll('[data-year]');
  year.forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
