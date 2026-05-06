// Tiny script: hamburger toggle + footer year
(function () {
  var btn = document.querySelector('.menu-toggle');
  var links = document.querySelector('.nav-links');
  if (btn && links) {
    btn.addEventListener('click', function () {
      links.classList.toggle('open');
    });
  }
  var year = document.querySelectorAll('[data-year]');
  year.forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
