/* ==========================================================================
   Work Showcase — auto-scroll to the feature video, autoplay it, then cue the
   two walkthroughs with a glow as it finishes.

   Autoplay reality: every current browser blocks autoplay *with sound* until the
   user has interacted with the page. So we try unmuted first, and if the browser
   refuses we fall back to muted playback and surface a "Tap for sound" button.
   Any click/key/tap on the page also unmutes.
   ========================================================================== */
(function () {
    'use strict';

    var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    var theatre = document.getElementById('theatre');       // the whole one-frame panel
    var stage = document.getElementById('feature-stage');
    var video = document.getElementById('feature-video');
    var cue = document.getElementById('auto-cue');
    var soundBtn = document.getElementById('sound-btn');
    var demos = [].slice.call(document.querySelectorAll('[data-cue-target]'));
    if (!video || !stage || !theatre) return;

    var DELAY_MS = 5000;   // wait before taking over
    var GLOW_LEAD = 12;    // seconds before the end to light up the next videos

    /* ---------------- sound handling ---------------- */
    var unmuted = false;

    function unmute() {
        if (unmuted) return;
        unmuted = true;
        video.muted = false;
        video.volume = 1;
        if (soundBtn) soundBtn.classList.add('is-hidden');
        var p = video.play();
        if (p && p.catch) p.catch(function () { });
    }

    function offerSound() {
        if (soundBtn) soundBtn.classList.remove('is-hidden');
    }

    if (soundBtn) {
        soundBtn.addEventListener('click', function (e) {
            e.stopPropagation();
            unmute();
        });
    }
    // any deliberate interaction counts as the gesture browsers want
    ['pointerdown', 'keydown', 'touchstart'].forEach(function (evt) {
        window.addEventListener(evt, function () {
            if (video.muted && !video.paused) unmute();
        }, { once: true, passive: true });
    });

    /* ---------------- play, with a muted fallback ---------------- */
    function playFeature() {
        video.muted = false;
        var p = video.play();
        if (p && p.catch) {
            p.catch(function () {
                // blocked with sound - retry muted, which is always allowed
                video.muted = true;
                var p2 = video.play();
                if (p2 && p2.catch) p2.catch(function () { });
                offerSound();
            });
        }
    }

    /* ---------------- glow cue on the two walkthroughs ---------------- */
    var cued = false;

    function cueNext() {
        if (cued) return;
        cued = true;
        demos.forEach(function (el) { el.classList.add('is-cued'); });
    }

    video.addEventListener('timeupdate', function () {
        if (cued || !isFinite(video.duration)) return;
        if (video.duration - video.currentTime <= GLOW_LEAD) cueNext();
    });
    video.addEventListener('ended', cueNext);

    /* ---------------- the 5s takeover ---------------- */
    if (reduced) {
        if (cue) cue.classList.add('is-hidden');
        return;   // no auto-scroll, no autoplay: let the user drive
    }

    var cancelled = false;
    var fired = false;
    var ring = cue ? cue.querySelector('.ring') : null;
    var secEl = cue ? cue.querySelector('.sec') : null;
    var CIRC = 88;

    function cancel() {
        if (cancelled || fired) return;
        cancelled = true;
        if (cue) cue.classList.add('is-hidden');
    }

    // the user taking control always wins
    window.addEventListener('wheel', function () { if (window.scrollY > 20) cancel(); }, { passive: true });
    window.addEventListener('touchmove', cancel, { passive: true });
    window.addEventListener('scroll', function () { if (window.scrollY > 60) cancel(); }, { passive: true });
    window.addEventListener('keydown', function (e) {
        if (['ArrowDown', 'ArrowUp', 'PageDown', 'PageUp', 'Home', 'End', ' '].indexOf(e.key) !== -1) cancel();
    });
    if (cue) {
        cue.addEventListener('click', function () {
            if (cancelled || fired) return;
            takeover();          // clicking the chip skips the wait
        });
    }

    function takeover() {
        if (cancelled || fired) return;
        fired = true;
        if (cue) cue.classList.add('is-hidden');
        // Scroll to the section's exact top rather than scrollIntoView({block:'center'}).
        // The theatre is exactly one viewport tall, so its top IS the correct
        // resting place; 'center' consistently landed ~38px short and clipped
        // the bottom row of videos.
        window.scrollTo({ top: theatre.offsetTop, behavior: 'smooth' });
        // let the smooth scroll settle before starting playback
        setTimeout(playFeature, 750);
    }

    var t0 = performance.now();
    (function frame(t) {
        if (cancelled || fired) return;
        var elapsed = t - t0;
        var prog = Math.min(elapsed / DELAY_MS, 1);
        if (ring) ring.style.strokeDashoffset = (CIRC * (1 - prog)).toFixed(1);
        if (secEl) secEl.textContent = Math.ceil(Math.max(0, DELAY_MS - elapsed) / 1000);
        if (prog >= 1) return void takeover();
        requestAnimationFrame(frame);
    })(t0);
})();
