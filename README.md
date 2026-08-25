# Ahmet Bahadır Şimşek — Academic Website v3

GitHub Pages için hazırlanmış statik, iki dilli ve SEO odaklı akademik kişisel site.

## v3 ile gelen değişiklikler

- Türkçe ve İngilizce artık ayrı URL'lerde:
  - `/`
  - `/en/`
- Yayın künyeleri JavaScript ile sonradan üretilmez; HTML içinde **statik** bulunur.
- Arama, tür filtresi, hover/focus özeti ve künye kopyalama JavaScript ile zenginleştirilir.
- `canonical`, `hreflang`, Open Graph ve Twitter metadata eklendi.
- `sitemap.xml` ve `robots.txt` eklendi.
- Ana sayfadaki seçilmiş yayınlar da statik HTML'dir.
- Kurumsal e-posta birincil iletişim kanalı olarak vurgulandı.
- Yayın verisinin tek kaynağı `data/publications.json` dosyasıdır.
- `build_site.py` yayın sayfalarını JSON verisinden yeniden üretir.
- GitHub Actions iş akışı JSON değiştiğinde statik yayın HTML'lerini otomatik güncelleyebilir.
- `404.html` ve `assets/favicon.svg` eklendi.

## Dosya yapısı

```text
/
├── index.html
├── publications.html
├── tools.html
├── tools.py
├── 404.html
├── robots.txt
├── sitemap.xml
├── build_site.py
├── data/
│   └── publications.json
├── en/
│   ├── index.html
│   ├── publications.html
│   └── tools.html
├── assets/
│   ├── style.css
│   ├── site.js
│   ├── publications-ui.js
│   └── favicon.svg
└── .github/
    └── workflows/
        └── build-publications.yml
```

## Yayın verisini güncelleme

`data/publications.json` içindeki bir kaydın yapısı:

```json
{
  "year": 2026,
  "type": "article",
  "title": "Makale başlığı",
  "authors": "Yazarlar",
  "source_tr": "Türkçe künye kaynağı",
  "source_en": "English source citation",
  "doi": "10.xxxx/...",
  "url": "https://doi.org/...",
  "summary_tr": "Kısa Türkçe özet",
  "summary_en": "Short English summary"
}
```

Değişiklikten sonra:

```bash
python build_site.py
```

komutunu çalıştırın. GitHub Actions etkinse `data/publications.json` değişikliğinin ardından bu işlem otomatik de yapılır.

## GitHub'a yükleme

ZIP'i açın ve içindeki dosyaları mevcut `abahadirsimsek.github.io` deposunun köküne yükleyin.
Mevcut dosyaların üzerine yazılmasına izin verin. `en`, `assets`, `data` ve `.github`
klasörlerinin yapısını koruyun.

## Not

Bu v3 paketi, v2'deki 31 doğrulanmış yayın kaydını mimari olarak yeniden düzenler.
Yeni yayın taraması yapılmamıştır. Yeni bir yayın eklenecekse önce DOI/yayınevi kaydıyla doğrulanması önerilir.
