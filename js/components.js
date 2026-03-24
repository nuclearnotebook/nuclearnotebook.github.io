/* ═══════════════════════════════════════════════
   SHARED NAV + FOOTER INJECTOR
   Called on every page via: loadComponents()
   ═══════════════════════════════════════════════ */

(function () {
  /* ── Determine root path ── */
  const depth = (function () {
    const p = window.location.pathname;
    const segs = p.replace(/\/+$/, '').split('/').filter(Boolean);
    // Count how many folders deep we are (0 = root)
    let d = 0;
    if (segs.length > 0) {
      const last = segs[segs.length - 1];
      if (last.includes('.')) d = segs.length - 1;
      else d = segs.length;
    }
    return d;
  })();

  const root = depth === 0 ? './' : '../'.repeat(depth);

  /* ── Nav HTML ── */
  const navHTML = `
<nav id="navbar">
  <div class="nav-inner">

    <a href="${root}index.html" class="nav-logo">
      <div class="logo-mark">
        <svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="20" cy="20" r="18" stroke="#00d4ff" stroke-width="1.5" stroke-dasharray="4 2"/>
          <circle cx="20" cy="20" r="10" stroke="#7b2fff" stroke-width="1.5"/>
          <circle cx="20" cy="20" r="3" fill="#00d4ff"/>
          <ellipse cx="20" cy="20" rx="18" ry="7" stroke="#00d4ff" stroke-width="0.8" stroke-dasharray="2 2" opacity="0.4"/>
          <line x1="20" y1="2" x2="20" y2="10" stroke="#00d4ff" stroke-width="1.5" opacity="0.6"/>
          <line x1="20" y1="30" x2="20" y2="38" stroke="#00d4ff" stroke-width="1.5" opacity="0.6"/>
        </svg>
      </div>
      <div class="logo-text">
        <span class="logo-title">QuantumAtlas</span>
        <span class="logo-tagline">Physics Universe</span>
      </div>
    </a>

    <ul class="nav-links" id="nav-links">
      <li><a href="${root}index.html">Home</a></li>
      <li>
        <a href="${root}theory.html" class="has-dropdown">Theories ▾</a>
        <div class="nav-dropdown">
          <a href="${root}branches/classical-mechanics.html">Classical Mechanics</a>
          <a href="${root}branches/quantum-mechanics.html">Quantum Mechanics</a>
          <a href="${root}branches/thermodynamics.html">Thermodynamics</a>
          <a href="${root}branches/electromagnetism.html">Electromagnetism</a>
          <a href="${root}branches/relativity.html">Relativity</a>
          <a href="${root}branches/astrophysics.html">Astrophysics</a>
          <a href="${root}theory.html">All Branches →</a>
        </div>
      </li>
      <li><a href="${root}about.html">About</a></li>
      <li><a href="${root}contact.html">Contact</a></li>
      <li><a href="${root}theory.html" class="nav-cta">Explore Physics</a></li>
    </ul>

    <button class="nav-toggle" id="nav-toggle" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </button>

  </div>
</nav>`;

  /* ── Footer HTML ── */
  const footerHTML = `
<footer id="footer">
  <div class="footer-top">
    <div class="footer-brand">
      <a href="${root}index.html" class="nav-logo" style="margin-bottom:0">
        <div class="logo-mark">
          <svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="20" cy="20" r="18" stroke="#00d4ff" stroke-width="1.5" stroke-dasharray="4 2"/>
            <circle cx="20" cy="20" r="10" stroke="#7b2fff" stroke-width="1.5"/>
            <circle cx="20" cy="20" r="3" fill="#00d4ff"/>
          </svg>
        </div>
        <div class="logo-text">
          <span class="logo-title">QuantumAtlas</span>
          <span class="logo-tagline">Physics Universe</span>
        </div>
      </a>
      <p class="footer-desc">
        Your comprehensive guide to the fundamental laws governing our universe.
        From classical mechanics to quantum fields — explore physics at every scale.
      </p>
      <div class="footer-social">
        <a href="#" class="social-btn" title="Twitter">𝕏</a>
        <a href="#" class="social-btn" title="YouTube">▶</a>
        <a href="#" class="social-btn" title="GitHub">⌥</a>
        <a href="#" class="social-btn" title="RSS">◉</a>
      </div>
    </div>

    <div>
      <p class="footer-col-title">Physics</p>
      <ul class="footer-links">
        <li><a href="${root}branches/classical-mechanics.html">Classical Mechanics</a></li>
        <li><a href="${root}branches/quantum-mechanics.html">Quantum Mechanics</a></li>
        <li><a href="${root}branches/thermodynamics.html">Thermodynamics</a></li>
        <li><a href="${root}branches/electromagnetism.html">Electromagnetism</a></li>
        <li><a href="${root}branches/relativity.html">Relativity</a></li>
        <li><a href="${root}branches/astrophysics.html">Astrophysics</a></li>
      </ul>
    </div>

    <div>
      <p class="footer-col-title">More Physics</p>
      <ul class="footer-links">
        <li><a href="${root}branches/optics.html">Optics</a></li>
        <li><a href="${root}branches/nuclear-physics.html">Nuclear Physics</a></li>
        <li><a href="${root}branches/particle-physics.html">Particle Physics</a></li>
        <li><a href="${root}branches/condensed-matter.html">Condensed Matter</a></li>
        <li><a href="${root}branches/biophysics.html">Biophysics</a></li>
        <li><a href="${root}branches/plasma-physics.html">Plasma Physics</a></li>
      </ul>
    </div>

    <div>
      <p class="footer-col-title">Site</p>
      <ul class="footer-links">
        <li><a href="${root}about.html">About Us</a></li>
        <li><a href="${root}contact.html">Contact</a></li>
        <li><a href="${root}privacy.html">Privacy Policy</a></li>
        <li><a href="${root}terms.html">Terms & Conditions</a></li>
        <li><a href="${root}theory.html">All Branches</a></li>
      </ul>
    </div>
  </div>

  <div class="footer-bottom container">
    <p class="footer-copy">
      © <span id="footer-year"></span> <span>QuantumAtlas</span> — Physics Universe. All rights reserved.
    </p>
    <div class="footer-legal">
      <a href="${root}privacy.html">Privacy</a>
      <a href="${root}terms.html">Terms</a>
      <a href="${root}contact.html">Contact</a>
    </div>
  </div>
</footer>`;

  /* ── Inject ── */
  function inject() {
    // Nav
    const navTarget = document.getElementById('nav-placeholder');
    if (navTarget) navTarget.outerHTML = navHTML;
    else document.body.insertAdjacentHTML('afterbegin', navHTML);

    // Footer
    const ftTarget = document.getElementById('footer-placeholder');
    if (ftTarget) ftTarget.outerHTML = footerHTML;
    else document.body.insertAdjacentHTML('beforeend', footerHTML);

    // Footer year
    const fy = document.getElementById('footer-year');
    if (fy) fy.textContent = new Date().getFullYear();

    initNav();
  }

  /* ── Nav behaviour ── */
  function initNav() {
    const navbar  = document.getElementById('navbar');
    const toggle  = document.getElementById('nav-toggle');
    const links   = document.getElementById('nav-links');

    // Scroll effect
    window.addEventListener('scroll', () => {
      navbar.classList.toggle('scrolled', window.scrollY > 40);
    }, { passive: true });

    // Mobile toggle
    toggle && toggle.addEventListener('click', () => {
      toggle.classList.toggle('open');
      links.classList.toggle('open');
      document.body.style.overflow = links.classList.contains('open') ? 'hidden' : '';
    });

    // Dropdown: tap on mobile
    document.querySelectorAll('.has-dropdown').forEach(a => {
      a.addEventListener('click', e => {
        if (window.innerWidth <= 900) {
          e.preventDefault();
          a.closest('li').classList.toggle('dd-open');
        }
      });
    });

    // Active link
    const cur = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('#nav-links a').forEach(a => {
      const href = a.getAttribute('href').split('/').pop();
      if (href === cur) a.classList.add('active');
    });

    // Close on outside click
    document.addEventListener('click', e => {
      if (links && !navbar.contains(e.target) && links.classList.contains('open')) {
        toggle.classList.remove('open');
        links.classList.remove('open');
        document.body.style.overflow = '';
      }
    });
  }

  /* ── Scroll reveal ── */
  function initReveal() {
    const obs = new IntersectionObserver((entries) => {
      entries.forEach(el => {
        if (el.isIntersecting) {
          el.target.classList.add('visible');
          obs.unobserve(el.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll('.reveal').forEach(el => obs.observe(el));
  }

  /* ── Star field canvas ── */
  window.initStars = function (canvasId, count = 180) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    function resize() {
      canvas.width  = canvas.offsetWidth;
      canvas.height = canvas.offsetHeight;
    }
    resize();
    window.addEventListener('resize', resize);

    const stars = Array.from({ length: count }, () => ({
      x: Math.random(),
      y: Math.random(),
      r: Math.random() * 1.4 + 0.3,
      a: Math.random(),
      speed: Math.random() * 0.0003 + 0.0001
    }));

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      stars.forEach(s => {
        s.a += s.speed;
        const alpha = (Math.sin(s.a) + 1) / 2 * 0.8 + 0.1;
        ctx.beginPath();
        ctx.arc(s.x * canvas.width, s.y * canvas.height, s.r, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(200,220,255,${alpha})`;
        ctx.fill();
      });
      requestAnimationFrame(draw);
    }
    draw();
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => { inject(); initReveal(); });
  } else {
    inject(); initReveal();
  }
})();
