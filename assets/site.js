(() => {
  const year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();

  if (document.body.classList.contains("home-page")) return;

  document.body.classList.add("subpage");

  const script = document.currentScript;
  const stylesheetUrl = script
    ? new URL("subpages.css", script.src).href
    : new URL("/assets/subpages.css", window.location.origin).href;

  const alreadyLoaded = Array.from(document.querySelectorAll('link[rel="stylesheet"]'))
    .some((link) => link.href === stylesheetUrl);

  if (!alreadyLoaded) {
    const link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = stylesheetUrl;
    document.head.appendChild(link);
  }

  const identity = document.querySelector(".site-header .identity");
  if (identity) identity.remove();

  const obsoleteHashes = new Set(["profil", "arastirma", "profile", "research"]);
  document.querySelectorAll(".site-header .nav a").forEach((link) => {
    const href = link.getAttribute("href") || "";
    const hash = href.includes("#") ? href.split("#").pop() : "";
    if (obsoleteHashes.has(hash)) {
      link.remove();
      return;
    }

    try {
      const url = new URL(link.href, document.baseURI);
      if (url.pathname === window.location.pathname && !url.hash) {
        link.setAttribute("aria-current", "page");
      }
    } catch (_) {
      // Ignore malformed navigation URLs without affecting the page.
    }
  });
})();
