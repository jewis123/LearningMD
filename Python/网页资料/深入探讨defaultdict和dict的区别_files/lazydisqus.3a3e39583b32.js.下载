(function () {
  var hasLoaded = false;
  var disqusDiv = document.getElementById("disqus_thread");

  window.onDisqusReady = function () {
    if (window.location.hash.includes("#comment-")) {
      disqusDiv.scrollIntoView();
    }
  }

  function loadDisqus() {
    if (hasLoaded) {
      return;
    }

    console.log("Loading Disqus")
    var d = document, s = d.createElement("script");
    s.src = window.disqus_script_url;
    s.setAttribute("data-timestamp", +new Date());
    (d.head || d.body).appendChild(s);

    hasLoaded = true;
  }

  function isInViewport(elem) {
    var bounding = elem.getBoundingClientRect();
    return (
      bounding.top >= 0 &&
      bounding.left >= 0 &&
      bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
      bounding.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
  }

  function shouldLoad() {
    if (hasLoaded) {
      return false;
    }

    if (window.location.hash.includes("#comment-")) {
      return true;
    }

    if (/bot|google|baidu|bing|msn|duckduckgo|slurp|yandex/i.test(navigator.userAgent)) {
      return true;
    }

    if (isInViewport(disqusDiv)) {
      return true;
    }

    return false;
  }

  function throttle(a, b) { var c, d; return function () { var e = this, f = arguments, g = +new Date; c && g < c + a ? (clearTimeout(d), d = setTimeout(function () { c = g, b.apply(e, f) }, a)) : (c = g, b.apply(e, f)) } }

  if (shouldLoad()) {
    loadDisqus();
  }

  function check() {
    if (shouldLoad()) {
      loadDisqus();
    }
    if (hasLoaded) {
      window.removeEventListener("scroll", checkFunc);
      window.removeEventListener("resize", checkFunc);
    }
  }

  var checkFunc = throttle(250, check);
  window.addEventListener("scroll", checkFunc);
  window.addEventListener("resize", checkFunc);
})();
