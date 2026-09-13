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
  // draw each mark in as its tile arrives; icons are already correct without this
  if (window.IntersectionObserver) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('ic-in');
        io.unobserve(e.target);
      });
    }, { rootMargin: '0px 0px -10% 0px' });
    document.querySelectorAll('.card, .feature').forEach(function (el) { io.observe(el); });
  }

  var year = document.querySelectorAll('[data-year]');
  year.forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
