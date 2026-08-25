
(() => {
  const lang = window.PUBLICATION_UI_LANG === "en" ? "en" : "tr";
  const cards = [...document.querySelectorAll("[data-pub-card]")];
  const groups = [...document.querySelectorAll("[data-year-group]")];
  const search = document.getElementById("pubSearch");
  const count = document.getElementById("publicationCount");
  const noResults = document.getElementById("noResults");
  let filter = "all";
  let query = "";

  const normalize = (s) => String(s || "").toLocaleLowerCase(lang === "tr" ? "tr-TR" : "en-US");

  function update() {
    let visible = 0;
    cards.forEach((card) => {
      const typeOK = filter === "all" || card.dataset.type === filter;
      const searchOK = !query || normalize(card.dataset.search).includes(normalize(query));
      const show = typeOK && searchOK;
      card.hidden = !show;
      if (show) visible += 1;
    });

    groups.forEach((group) => {
      group.hidden = !group.querySelector("[data-pub-card]:not([hidden])");
    });

    if (count) {
      count.textContent = lang === "tr"
        ? `${visible} yayın`
        : `${visible} publication${visible === 1 ? "" : "s"}`;
    }
    if (noResults) noResults.hidden = visible !== 0;
  }

  search?.addEventListener("input", () => {
    query = search.value.trim();
    update();
  });

  document.querySelectorAll("[data-pub-filter]").forEach((button) => {
    button.addEventListener("click", () => {
      filter = button.dataset.pubFilter;
      document.querySelectorAll("[data-pub-filter]").forEach((b) =>
        b.classList.toggle("active", b === button)
      );
      update();
    });
  });

  document.querySelectorAll(".summary-toggle").forEach((button) => {
    button.addEventListener("click", () => {
      const card = button.closest(".pub-card");
      const open = card.classList.toggle("is-open");
      button.setAttribute("aria-expanded", String(open));
      button.textContent = open
        ? (lang === "tr" ? "Özeti gizle" : "Hide summary")
        : (lang === "tr" ? "Özeti göster" : "Show summary");
    });
  });

  document.querySelectorAll(".copy-citation").forEach((button) => {
    button.addEventListener("click", async () => {
      const original = button.textContent;
      try {
        await navigator.clipboard.writeText(button.dataset.citation || "");
        button.textContent = lang === "tr" ? "Kopyalandı" : "Copied";
      } catch {
        button.textContent = lang === "tr" ? "Kopyalanamadı" : "Could not copy";
      }
      setTimeout(() => button.textContent = original, 1400);
    });
  });

  update();
})();
