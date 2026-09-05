/**
 * HAMZA ABU SALEH — PORTFOLIO v3.0 MOTION ENGINE
 * custom cursor · preloader · smart nav · reveals · counters
 * hero video auto-scroll · role typewriter · marquees · magnetic
 * project index preview · filters · lightbox
 * All effects respect prefers-reduced-motion.
 */
(function () {
    'use strict';

    var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var coarse = window.matchMedia('(hover: none), (pointer: coarse)').matches;

    document.addEventListener('DOMContentLoaded', function () {
        initPreloader();
        initScrollProgress();
        initNavbar();
        initMobileMenu();
        initActiveNav();
        initReveals();
        initCounters();
        initRoleRotator();
        initHeroVideo();
        initMarquees();
        initMagnetic();
        initIndexPreview();
        initFilters();
        initLightbox();
        initSmoothScroll();
    });

    /* ==================== PRELOADER ==================== */
    function initPreloader() {
        var pre = document.getElementById('preloader');
        if (!pre) return;

        var finish = function () {
            pre.classList.add('done');
            setTimeout(function () { pre.remove(); }, 750);
            document.body.classList.remove('is-loading');
        };

        if (reduced || sessionStorage.getItem('booted-v3')) { finish(); return; }
        sessionStorage.setItem('booted-v3', '1');
        document.body.classList.add('is-loading');

        var bar = pre.querySelector('.preloader-bar');
        var count = pre.querySelector('.preloader-count');
        var p = 0;
        var t0 = performance.now();
        var dur = 1200;

        (function step(t) {
            p = Math.min((t - t0) / dur, 1);
            var eased = 1 - Math.pow(1 - p, 2);
            if (bar) bar.style.setProperty('--p', eased);
            if (count) count.textContent = Math.round(eased * 100).toString().padStart(3, '0');
            if (p < 1) requestAnimationFrame(step);
            else setTimeout(finish, 260);
        })(t0);

        setTimeout(finish, 3200); // hard fallback
    }

    /* ==================== SCROLL PROGRESS ==================== */
    function initScrollProgress() {
        var bar = document.getElementById('scroll-progress');
        if (!bar) return;
        var ticking = false;
        var update = function () {
            var max = document.documentElement.scrollHeight - window.innerHeight;
            bar.style.transform = 'scaleX(' + (max > 0 ? window.scrollY / max : 0) + ')';
            ticking = false;
        };
        window.addEventListener('scroll', function () {
            if (!ticking) { requestAnimationFrame(update); ticking = true; }
        }, { passive: true });
        update();
    }

    /* ==================== NAVBAR ==================== */
    function initNavbar() {
        var nav = document.getElementById('navbar');
        if (!nav) return;
        var lastY = window.scrollY;
        window.addEventListener('scroll', function () {
            var y = window.scrollY;
            nav.classList.toggle('scrolled', y > 24);
            var menuOpen = document.querySelector('.nav-links.open');
            if (!menuOpen && y > 340 && y > lastY + 6) nav.classList.add('nav-hidden');
            else if (y < lastY - 4 || y <= 340) nav.classList.remove('nav-hidden');
            lastY = y;
        }, { passive: true });
    }

    /* ==================== MOBILE MENU ==================== */
    function initMobileMenu() {
        var toggle = document.querySelector('.menu-toggle');
        var links = document.querySelector('.nav-links');
        if (!toggle || !links) return;
        toggle.addEventListener('click', function () {
            var open = links.classList.toggle('open');
            toggle.classList.toggle('open', open);
            toggle.setAttribute('aria-expanded', open);
        });
        links.querySelectorAll('a').forEach(function (a) {
            a.addEventListener('click', function () {
                links.classList.remove('open');
                toggle.classList.remove('open');
                toggle.setAttribute('aria-expanded', 'false');
            });
        });
    }

    /* ==================== ACTIVE NAV ==================== */
    function initActiveNav() {
        var path = window.location.pathname;
        document.querySelectorAll('.nav-links a').forEach(function (link) {
            var href = link.getAttribute('href');
            if (!href || link.closest('.nav-cta')) return;
            var clean = href.split('#')[0] || '/';
            if ((clean === '/' && path === '/' && href.indexOf('#') === -1) ||
                (clean !== '/' && path.indexOf(clean) === 0)) {
                link.classList.add('active');
            }
        });
    }

    /* ==================== REVEALS ==================== */
    function initReveals() {
        var items = document.querySelectorAll('[data-reveal]');
        if (!items.length) return;
        if (reduced || !('IntersectionObserver' in window)) {
            items.forEach(function (el) { el.classList.add('in'); });
            return;
        }
        var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (e) {
                if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
            });
        }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
        items.forEach(function (el) { io.observe(el); });
    }

    /* ==================== COUNTERS ==================== */
    function initCounters() {
        var counters = document.querySelectorAll('[data-count]');
        if (!counters.length) return;
        var run = function (el) {
            var target = parseFloat(el.dataset.count);
            var dec = parseInt(el.dataset.decimals || '0', 10);
            if (reduced) { el.textContent = target.toFixed(dec); return; }
            var t0 = performance.now(), dur = 1500;
            (function step(t) {
                var p = Math.min((t - t0) / dur, 1);
                var eased = 1 - Math.pow(1 - p, 3);
                el.textContent = (target * eased).toFixed(dec);
                if (p < 1) requestAnimationFrame(step);
            })(t0);
        };
        var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (e) { if (e.isIntersecting) { run(e.target); io.unobserve(e.target); } });
        }, { threshold: 0.6 });
        counters.forEach(function (c) { io.observe(c); });
    }

    /* ==================== ROLE ROTATOR ==================== */
    function initRoleRotator() {
        var el = document.getElementById('role-rotator');
        if (!el) return;
        var roles;
        try { roles = JSON.parse(el.dataset.roles); } catch (e) { return; }
        if (!roles || roles.length < 2 || reduced) { if (roles) el.textContent = roles[0]; return; }
        var ri = 0, ci = roles[0].length, del = true;
        setTimeout(function tick() {
            var word = roles[ri];
            if (del) {
                ci--; el.textContent = word.slice(0, ci);
                if (ci === 0) { del = false; ri = (ri + 1) % roles.length; return void setTimeout(tick, 240); }
                setTimeout(tick, 24);
            } else {
                var next = roles[ri]; ci++; el.textContent = next.slice(0, ci);
                if (ci === next.length) { del = true; return void setTimeout(tick, 2200); }
                setTimeout(tick, 55);
            }
        }, 2400);
    }

    /* ==================== HERO VIDEO + AUTO-SCROLL ==================== */
    function initHeroVideo() {
        var video = document.getElementById('hero-video');
        var auto = document.getElementById('hero-autoscroll');
        var target = document.getElementById('after-hero');
        if (!video) return;

        // Best-effort autoplay
        var tryPlay = function () {
            var p = video.play();
            if (p && p.catch) p.catch(function () { /* autoplay blocked; poster stays */ });
        };
        if (video.readyState >= 2) tryPlay();
        video.addEventListener('canplay', tryPlay, { once: true });

        if (reduced || !target || !auto) { if (auto) auto.classList.add('hide'); return; }

        var ring = auto.querySelector('.ring');
        var secEl = auto.querySelector('.sec');
        var CIRC = 88;
        var cancelled = false;
        var started = false;
        var t0 = 0, dur = 10000;

        var cancel = function () {
            if (cancelled) return;
            cancelled = true;
            auto.classList.add('hide');
        };

        // Cancel auto-scroll the moment the user takes control
        window.addEventListener('wheel', function () { if (window.scrollY > 20) cancel(); }, { passive: true });
        window.addEventListener('touchmove', cancel, { passive: true });
        window.addEventListener('keydown', function (e) {
            if (['ArrowDown', 'ArrowUp', 'PageDown', 'PageUp', 'Home', 'End', ' '].indexOf(e.key) !== -1) cancel();
        });
        window.addEventListener('scroll', function () { if (window.scrollY > 60) cancel(); }, { passive: true });

        var begin = function () {
            if (started) return;
            started = true;
            dur = (isFinite(video.duration) && video.duration > 1 ? video.duration : 10) * 1000;
            t0 = performance.now();
            (function frame(t) {
                if (cancelled) return;
                var elapsed = t - t0;
                var remain = Math.max(0, dur - elapsed);
                var prog = Math.min(elapsed / dur, 1);
                if (ring) ring.style.strokeDashoffset = (CIRC * (1 - prog)).toFixed(1);
                if (secEl) secEl.textContent = Math.ceil(remain / 1000);
                if (prog >= 1) {
                    if (window.scrollY < 40) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                    auto.classList.add('hide');
                    return;
                }
                requestAnimationFrame(frame);
            })(t0);
        };

        // Start the countdown when the video actually starts playing
        if (video.readyState >= 3 && !video.paused) begin();
        video.addEventListener('playing', begin, { once: true });
        // Fallback: if playback never fires (blocked), still count down from load
        setTimeout(function () { if (!started && !cancelled) begin(); }, 1200);

        // Click the cue to skip immediately
        var cue = document.querySelector('.scroll-cue');
        if (cue) cue.addEventListener('click', function () {
            cancel();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
    }

    /* ==================== MARQUEES ==================== */
    function initMarquees() {
        document.querySelectorAll('[data-marquee]').forEach(function (track) {
            track.innerHTML += track.innerHTML;
        });
    }

    /* ==================== MAGNETIC ==================== */
    function initMagnetic() {
        if (reduced || coarse) return;
        document.querySelectorAll('[data-magnetic]').forEach(function (btn) {
            btn.addEventListener('mousemove', function (e) {
                var r = btn.getBoundingClientRect();
                var x = (e.clientX - r.left - r.width / 2) * 0.25;
                var y = (e.clientY - r.top - r.height / 2) * 0.4;
                btn.style.transform = 'translate(' + x + 'px,' + y + 'px)';
            });
            btn.addEventListener('mouseleave', function () { btn.style.transform = ''; });
        });
    }

    /* ==================== INDEX PREVIEW (cursor-following) ==================== */
    function initIndexPreview() {
        if (coarse) return;
        var rows = document.querySelectorAll('.index-row[data-preview]');
        if (!rows.length) return;

        var preview = document.createElement('div');
        preview.className = 'index-preview';
        document.body.appendChild(preview);

        var px = 0, py = 0, cx = 0, cy = 0, active = false;

        var setContent = function (row) {
            var img = row.getAttribute('data-preview');
            var label = row.getAttribute('data-preview-label') || '';
            if (img) preview.innerHTML = '<img src="' + img + '" alt="">';
            else preview.innerHTML = '<div class="placeholder">' + label + '</div>';
        };

        rows.forEach(function (row) {
            row.addEventListener('mouseenter', function () {
                setContent(row);
                preview.classList.add('show');
                active = true;
            });
            row.addEventListener('mouseleave', function () {
                preview.classList.remove('show');
                active = false;
            });
        });

        window.addEventListener('mousemove', function (e) { px = e.clientX; py = e.clientY; }, { passive: true });
        (function loop() {
            cx += (px - cx) * 0.14;
            cy += (py - cy) * 0.14;
            if (active) preview.style.transform = 'translate(' + cx + 'px,' + cy + 'px) translate(-50%,-50%)';
            requestAnimationFrame(loop);
        })();
    }

    /* ==================== FILTERS ==================== */
    function initFilters() {
        var buttons = document.querySelectorAll('.filter-btn');
        var rows = document.querySelectorAll('.index-row[data-category]');
        if (!buttons.length || !rows.length) return;

        buttons.forEach(function (btn) {
            btn.addEventListener('click', function () {
                var cat = btn.getAttribute('data-category');
                buttons.forEach(function (b) { b.classList.remove('active'); });
                btn.classList.add('active');
                var visible = 0;
                rows.forEach(function (row) {
                    var match = cat === 'All' ||
                        row.getAttribute('data-category') === cat ||
                        (row.getAttribute('data-tags') || '').split(',').indexOf(cat) !== -1;
                    row.classList.toggle('filtered-out', !match);
                    if (match) { visible++; renumber(row, visible); }
                });
            });
        });

        function renumber(row, n) {
            var num = row.querySelector('.index-num');
            if (num) num.textContent = (n < 10 ? '0' : '') + n;
        }
    }

    /* ==================== LIGHTBOX ==================== */
    function initLightbox() {
        var lightbox = document.getElementById('lightbox');
        var shots = document.querySelectorAll('.shot img');
        if (!lightbox || !shots.length) return;

        var img = document.getElementById('lightbox-img');
        var counter = document.getElementById('lightbox-counter');
        var sources = Array.prototype.map.call(shots, function (s) { return s.src; });
        var index = 0;

        var show = function (i) {
            index = (i + sources.length) % sources.length;
            img.src = sources[index];
            counter.textContent = (index + 1) + ' / ' + sources.length;
        };
        var open = function (i) { show(i); lightbox.classList.add('open'); document.body.style.overflow = 'hidden'; };
        var close = function () { lightbox.classList.remove('open'); document.body.style.overflow = ''; };

        document.querySelectorAll('.shot').forEach(function (shot, i) {
            shot.addEventListener('click', function () { open(i); });
        });
        lightbox.querySelector('.lightbox-close').addEventListener('click', close);
        lightbox.querySelector('.lightbox-prev').addEventListener('click', function (e) { e.stopPropagation(); show(index - 1); });
        lightbox.querySelector('.lightbox-next').addEventListener('click', function (e) { e.stopPropagation(); show(index + 1); });
        lightbox.addEventListener('click', function (e) { if (e.target === lightbox) close(); });
        document.addEventListener('keydown', function (e) {
            if (!lightbox.classList.contains('open')) return;
            if (e.key === 'Escape') close();
            if (e.key === 'ArrowLeft') show(index - 1);
            if (e.key === 'ArrowRight') show(index + 1);
        });
    }

    /* ==================== SMOOTH SCROLL ==================== */
    function initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(function (a) {
            a.addEventListener('click', function (e) {
                var id = this.getAttribute('href');
                if (id === '#' || id.length < 2) return;
                var target = document.querySelector(id);
                if (!target) return;
                e.preventDefault();
                target.scrollIntoView({ behavior: reduced ? 'auto' : 'smooth', block: 'start' });
            });
        });
    }

})();
