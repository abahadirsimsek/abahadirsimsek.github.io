
(() => {
  const KEY = "abs-site-language";
  const getInitial = () => {
    const saved = localStorage.getItem(KEY);
    if (saved === "tr" || saved === "en") return saved;
    return "tr";
  };

  const applyLanguage = (lang) => {
    window.siteLanguage = lang;
    document.documentElement.lang = lang;

    document.querySelectorAll("[data-tr][data-en]").forEach((el) => {
      const value = el.dataset[lang];
      if (value !== undefined) el.textContent = value;
    });

    document.querySelectorAll("[data-ph-tr][data-ph-en]").forEach((el) => {
      el.placeholder = lang === "tr" ? el.dataset.phTr : el.dataset.phEn;
    });

    document.querySelectorAll("[data-lang-toggle]").forEach((button) => {
      const current = button.querySelector(".lang-current");
      const other = button.querySelector(".lang-other");
      if (current) current.textContent = lang.toUpperCase();
      if (other) other.textContent = lang === "tr" ? "EN" : "TR";
      button.setAttribute(
        "aria-label",
        lang === "tr" ? "Switch language to English" : "Dili Türkçeye değiştir"
      );
    });

    document.title = (() => {
      const path = location.pathname;
      if (path.endsWith("publications.html")) {
        return lang === "tr"
          ? "Yayınlar | Ahmet Bahadır Şimşek"
          : "Publications | Ahmet Bahadır Şimşek";
      }
      if (path.endsWith("tools.html")) {
        return lang === "tr"
          ? "Akademik Araçlar | Ahmet Bahadır Şimşek"
          : "Academic Tools | Ahmet Bahadır Şimşek";
      }
      return lang === "tr"
        ? "Ahmet Bahadır Şimşek | Akademik Profil"
        : "Ahmet Bahadır Şimşek | Academic Profile";
    })();

    window.dispatchEvent(new CustomEvent("languagechange", { detail: { lang } }));
  };

  document.querySelectorAll("[data-lang-toggle]").forEach((button) => {
    button.addEventListener("click", () => {
      const next = window.siteLanguage === "tr" ? "en" : "tr";
      localStorage.setItem(KEY, next);
      applyLanguage(next);
    });
  });

  const year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();

  applyLanguage(getInitial());
})();
