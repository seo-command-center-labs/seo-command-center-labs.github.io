# Örnek Bahçe Rehberi (deneme sitesi)

SEO Komuta Merkezi'nin gerçek GitHub üzerindeki uçtan uca değişiklik testi için hazırlanmış nötr bir sitedir. Gerçek bir işletmeye ait değildir, bahis
içeriği yoktur, kişisel veri toplamaz. Bu klasör uygulamanın bir parçası değildir; ayrı bir GitHub deposuna kopyalanıp GitHub Pages ile ücretsiz yayınlanır.

## Yayın
- Depo adı: `seo-command-center-labs.github.io` (organizasyon sitesi kökte yayınlanır: `https://seo-command-center-labs.github.io/`). Başka bir adla
  açılırsa site bir alt yolda yayınlanır; sistem siteyi alan adının kökünde beklediği için bu deneme çalışmaz.
- GitHub Pages organizasyon sitesini `main` dalının kökünden yayınlar (gerekirse Settings → Pages → "Deploy from a branch" → `main` / `(root)`).
- `.nojekyll` nokta klasörünün (`.well-known`) yayınlanması için gerekir.
- Bağlantılar sonda `/` ile yazılır (`/bitkiler/`). Sistem sayfayı `/bitkiler` olarak tanır; GitHub Pages bunu `/bitkiler/` adresine yönlendirir ve
  doğrulama yalnız aynı sitedeki yönlendirmeyi izler (en fazla 3 adım).

## Sahiplik
`.well-known/seo-ownership.txt` dosyasına, panelde bağlantı istendiğinde verilen anahtar yazılır. Anahtar hem depoda hem yayındaki sitede
bulunmalıdır.

## Testler
`.github/workflows/html-check.yml` her pull request'te `scripts/check_html.py .` çalıştırır (yalnız Python standart kütüphanesi). Sistem,
birleştirme onayı istemeden önce bu denetimin geçmesini bekler.

## Bilerek bırakılan küçük eksikler (analiz bunları bulmalı)
- Ana sayfadaki görselin `alt` metni yok.
- `/bitkiler/` sayfasında meta açıklama yok.
