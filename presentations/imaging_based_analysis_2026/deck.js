// Exported-deck helper: scale the 1280x720 slide to the window; Right/PageDown/Space = next, Left/PageUp = previous.
(function () {
  function fit() {
    var z = Math.min(innerWidth / 1280, innerHeight / 720);
    document.documentElement.style.zoom = z;
    document.body.style.margin = Math.max(0, (innerHeight / z - 720) / 2) + 'px ' + Math.max(0, (innerWidth / z - 1280) / 2) + 'px';
  }
  addEventListener('resize', fit);
  addEventListener('DOMContentLoaded', fit);
  addEventListener('keydown', function (e) {
    if (e.target && /^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName)) return;  // sliders keep their arrow keys
    var next = ['ArrowRight', 'PageDown', ' '].indexOf(e.key) >= 0, prev = ['ArrowLeft', 'PageUp'].indexOf(e.key) >= 0;
    if (!next && !prev) return;
    var a = document.querySelector(next ? 'a[aria-label="Next slide"]' : 'a[aria-label="Previous slide"]');
    if (!next && !a) a = document.querySelector('a[aria-label="Previous slide"]');
    if (next && !a) { var links = document.querySelectorAll('a[href$=".dc.html"]'); a = links[links.length - 1]; }
    if (a) { e.preventDefault(); location.href = a.getAttribute('href'); }
  });
})();
