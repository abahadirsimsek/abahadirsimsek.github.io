from pathlib import Path
import json, html, re

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "publications.json"

def esc(s):
    return html.escape(str(s), quote=True)

def source(p, lang):
    return p["source_tr"] if lang == "tr" else p["source_en"]

def summary(p, lang):
    return p["summary_tr"] if lang == "tr" else p["summary_en"]

def type_label(p, lang):
    if p["type"] == "article":
        return "Makale" if lang == "tr" else "Article"
    return "Kitap bölümü" if lang == "tr" else "Book chapter"

def citation(p, lang):
    link = f"https://doi.org/{p['doi']}" if p.get("doi") else p["url"]
    return f"{p['authors']} ({p['year']}). {p['title']}. {source(p, lang)} {link}"

def card(p, lang):
    search_blob = " ".join([
        p["title"], p["authors"], p["source_tr"], p["source_en"],
        str(p["year"]), p.get("doi",""), type_label(p,lang)
    ]).lower()
    show = "Özeti göster" if lang=="tr" else "Show summary"
    copy = "Künyeyi kopyala" if lang=="tr" else "Copy citation"
    label = "Kısa özet" if lang=="tr" else "Summary"
    link_label = f"DOI {p['doi']}" if p.get("doi") else ("Yayın kaydı" if lang=="tr" else "Publication record")
    return f"""<article class="pub-card" data-pub-card data-type="{esc(p['type'])}" data-year="{p['year']}" data-search="{esc(search_blob)}" tabindex="0">
  <div class="pub-topline"><span class="pub-type">{esc(type_label(p,lang))}</span><span class="pub-year-small">{p['year']}</span></div>
  <h3 class="pub-title"><a href="{esc(p['url'])}" target="_blank" rel="noopener noreferrer">{esc(p['title'])}</a></h3>
  <p class="pub-authors">{esc(p['authors'])}</p>
  <p class="pub-source">{esc(source(p,lang))}</p>
  <div class="pub-actions">
    <a href="{esc(p['url'])}" target="_blank" rel="noopener noreferrer">{esc(link_label)}</a>
    <button class="summary-toggle" type="button" aria-expanded="false">{show}</button>
    <button class="copy-citation" type="button" data-citation="{esc(citation(p,lang))}">{copy}</button>
  </div>
  <div class="summary-panel"><span class="summary-label">{label}:</span> <span>{esc(summary(p,lang))}</span></div>
</article>"""

def group_html(publications, lang):
    years = sorted({p["year"] for p in publications}, reverse=True)
    chunks = []
    for year in years:
        cards = "\n".join(card(p,lang) for p in publications if p["year"]==year)
        chunks.append(f'<section class="year-group" data-year-group="{year}"><h2 class="year-heading">{year}</h2>\n{cards}\n</section>')
    return "\n".join(chunks)

FEATURED_DOIS = [
    "10.4018/979-8-3693-8789-4.ch009",
    "10.4018/979-8-3373-8546-4.ch010",
    "10.1080/01605682.2025.2577774",
    "10.35379/cusosbil.1643022",
]

def featured_html(publications, lang):
    by_doi = {p.get("doi"):p for p in publications}
    rows = []
    for doi in FEATURED_DOIS:
        p = by_doi[doi]
        rows.append(f"""<article class="featured-item">
  <span class="featured-year">{p['year']}</span>
  <div>
    <h3 class="featured-title"><a href="{esc(p['url'])}" target="_blank" rel="noopener noreferrer">{esc(p['title'])}</a></h3>
    <p class="featured-meta">{esc(p['authors'])} · {esc(source(p,lang))}</p>
  </div>
  <span class="type-badge">{esc(type_label(p,lang))}</span>
</article>""")
    return "\n".join(rows)

def replace_region(text, name, content):
    pattern = rf"<!-- GENERATED:{name}:START -->.*?<!-- GENERATED:{name}:END -->"
    replacement = f"<!-- GENERATED:{name}:START -->\n{content}\n<!-- GENERATED:{name}:END -->"
    updated, n = re.subn(pattern, replacement, text, flags=re.S)
    if n != 1:
        raise RuntimeError(f"{name} bölgesi bulunamadı veya birden fazla bulundu.")
    return updated

def update_file(path, lang, publications):
    text = path.read_text(encoding="utf-8")
    if "GENERATED:PUBLICATIONS:START" in text:
        text = replace_region(text, "PUBLICATIONS", group_html(publications,lang))
    if "GENERATED:FEATURED:START" in text:
        text = replace_region(text, "FEATURED", featured_html(publications,lang))
    path.write_text(text, encoding="utf-8")

def main():
    publications = json.loads(DATA.read_text(encoding="utf-8"))
    required = {"year","type","title","authors","source_tr","source_en","url","summary_tr","summary_en"}
    for i,p in enumerate(publications,1):
        missing = sorted(required - set(p))
        if missing:
            raise ValueError(f"Kayıt {i}: eksik alanlar {missing}")
        if p["type"] not in {"article","chapter"}:
            raise ValueError(f"Kayıt {i}: geçersiz type={p['type']}")
        if not str(p["url"]).startswith("http"):
            raise ValueError(f"Kayıt {i}: geçersiz URL")

    update_file(ROOT/"index.html","tr",publications)
    update_file(ROOT/"publications.html","tr",publications)
    update_file(ROOT/"en"/"index.html","en",publications)
    update_file(ROOT/"en"/"publications.html","en",publications)
    print(f"{len(publications)} kayıtla statik yayın sayfaları güncellendi.")

if __name__ == "__main__":
    main()
