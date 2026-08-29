// Subtle reveal for sections as they scroll into view.
// Respects prefers-reduced-motion (see CSS) — this only toggles a class,
// no motion is added if the user has reduced motion set.
(function () {
  if (!('IntersectionObserver' in window)) return;

  const targets = document.querySelectorAll('section, .tl-item, .product-card, .process-card');
  targets.forEach((el) => { el.style.opacity = 0; el.style.transform = 'translateY(12px)'; el.style.transition = 'opacity .5s ease, transform .5s ease'; });

  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = 1;
        entry.target.style.transform = 'none';
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  targets.forEach((el) => io.observe(el));
})();
