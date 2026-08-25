# Ahmet Bahadır Şimşek — Academic Website

GitHub Pages için hazırlanmış iki dilli (TR/EN), statik akademik kişisel site.

## Dosyalar

- `index.html` — ana akademik profil
- `publications.html` — tam yayın listesi, arama/filtre ve hover/focus özetleri
- `tools.html` — tarayıcı içinde çalışan akademik Python araçları
- `tools.py` — PyScript/Pyodide betimsel istatistik aracı
- `assets/style.css` — ortak tasarım
- `assets/site.js` — TR/EN dil yönetimi
- `assets/publications.js` — yayın verileri ve arayüzü

## Yayın verisi

Bu sürümde 31 yayın kaydı bulunmaktadır. Künye bilgileri kamuya açık DOI,
dergi/yayınevi, DergiPark ve kurumsal kayıtlarla çapraz kontrol edilmiştir.
ORCID kimliği: https://orcid.org/0000-0002-7276-2376

`publications.js` içinde her kayıt şu alanları taşır:

- yıl ve yayın türü
- başlık ve yazarlar
- dergi/kitap, cilt-sayı, sayfa veya makale numarası
- DOI veya doğrudan yayın bağlantısı
- Türkçe ve İngilizce kısa özet

Kısa özetler özgün özetlerin tam metin kopyası değildir; akademik içeriği
kısaca tanımlayan yeniden yazılmış açıklamalardır.

## GitHub'a yükleme

1. ZIP'i açın.
2. `abahadirsimsek.github.io` deponuzda **Add file → Upload files** yolunu açın.
3. Bu klasördeki tüm dosya ve klasörleri yükleyin.
4. `assets` klasör yapısını koruyun.
5. Commit oluşturun. GitHub Pages mevcut `main` / root yayını üzerinden otomatik güncellenir.

## Dil

Varsayılan dil Türkçedir. TR/EN düğmesi kullanıcı tercihini tarayıcıdaki `localStorage`
üzerinde hatırlar.

## Python

`tools.html`, PyScript `2026.7.3` sürümünü CDN üzerinden yükler.
Python ziyaretçinin tarayıcısında çalışır. API anahtarı, parola veya gizli veri
istemci tarafı dosyalarına eklenmemelidir.

## İleride eklenebilecekler

- `cv.pdf`
- doğrulanmış Google Scholar profil bağlantısı
- profesyonel profil fotoğrafı
- güncel dersler ve projeler
- ORCID/Crossref tabanlı otomatik yayın güncelleme iş akışı
