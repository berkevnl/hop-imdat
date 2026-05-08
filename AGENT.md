# HOOP-İMDAT — Repository Agent Instructions

> İnsan Müdahale Devri Aktarım Tetikleyicisi
> Sıkışan AI ajanları için insan-döngülü kurtarma protokolü.

## Repo Amacı

Samsun Üniversitesi Yazılım Mühendisliği 2. sınıf **Programlama 2** dersi öğrencilerinin **"Which Language?"** araştırma projesi kapsamındaki dönemlik mini-projelerini topladığı paylaşımlı çalışma alanı.

Her öğrenci kürate edilmiş bir mini-proje şablonu seçer (mini-todo, mini-notes, mini-contacts vb.) ve **specification-first** yaklaşımla `v0` (Hafta 5) → `v6` (Hafta 13–14) artımlı sürümler halinde geliştirir.

## Gönderim Düzeni

Bütün öğrenci çalışmaları `submissions/` altında yer alır. Her öğrenci **tam olarak bir** klasöre sahiptir.

### Klasör Adlandırma

```
submissions/<ad>-<soyad>-<numara>-<proje-kisa-ad>/
```

**Kurallar:**
- Sadece ASCII, küçük harf. Türkçe karakter yok.
- Dönüştürme: `ı→i, ç→c, ğ→g, ö→o, ş→s, ü→u, İ→i`
- Segmentler ve kelime araları arasında tire (`-`)
- `<numara>`: öğrenci numarası, sadece rakam
- `<proje-kisa-ad>`: `mini-todo`, `mini-notes`, `mini-contacts` gibi kısa slug

**Geçerli:**
```
submissions/ahmet-yilmaz-200110123-mini-todo/
submissions/zeynep-ozturk-200110456-mini-contacts/
submissions/can-sahin-200110789-mini-notes/
```

**Geçersiz:**
```
submissions/Ahmet-Yılmaz-200110123-mini-todo/   ← büyük harf + Türkçe karakter
submissions/ahmet_yilmaz_200110123_mini-todo/   ← alt çizgi
submissions/ahmet-yilmaz-mini-todo/             ← numara eksik
submissions/ahmet-200110123-mini-todo/          ← soyad eksik
```

### Klasör İçeriği

**Hafta 5 — Ödev 3 minimum:**
- `IDEA.md` — Karpathy tarzı idea file (motivasyon, kapsam, başarı kriterleri)
- `SPEC.txt` — Mini-projenin spesifikasyonu (`templates/SPEC-v1.txt`'i temel al)
- `README.md` — (opsiyonel) tanıtım, problem ifadesi, haftalık ilerleme

**Dönem sonuna doğru:**
- `v0/` … `v6/` — her hafta yeni dil kavramı geldikçe artımlı sürümler
- `tests/` — doctest / pytest dosyaları
- `notes/` — "Which Language?" araştırması için gözlemler (opsiyonel)

## Gönderim Akışı (Fork → PR)

1. Bu repoyu kendi GitHub hesabına **fork**'la.
2. Forku lokalde **clone**'la.
3. `submissions/` altında yukarıdaki kurallara uygun **kendi klasörünü oluştur**.
4. Dosyalarını ekle. **Kendi klasörün dışındaki hiçbir dosyayı değiştirme.**
5. Forkuna **commit + push**.
6. `seyyah/hoop-imdat:main`'e **Pull Request** aç.

PR başlık formatı:
```
[Hafta-X] <ad soyad numara> <proje-kisa-ad>
```

Örnek:
```
[Hafta-5] Ahmet Yılmaz 200110123 mini-todo
```

## LLM Ajanları İçin Sıkı Kurallar (Claude Code, Codex, OpenCode vb.)

Bir öğrencinin gönderim klasöründe çalışan LLM ajanı **ZORUNLU**:

- `submissions/<bu-ogrenci>/` dışındaki hiçbir dosyayı değiştirmemeli
- Diğer öğrencilerin klasörlerine dokunmamalı
- Kök seviye dosyalara (`AGENT.md`, `.github/`, `templates/`, `README.md`) dokunmamalı
- Yeni klasör oluşturmadan önce isimlendirme kurallarını valide etmeli
- Geçerli haftanın dil/özellik kapsamı dışına çıkmamalı (Hafta 6 öncesi loop/list/file I/O yok)

## Otomatik Doğrulama

`.github/workflows/check-submission.yml` her PR'da kontrol eder:
- Klasör adı pattern'e uyuyor mu
- PR sadece **tek** bir submission klasörünü mü değiştiriyor
- `submissions/` dışına dokunulmuş mu

Doğrulamayı geçmeyen PR merge edilemez.

---

**Ders sorumlusu:** Seyyah
**Ders:** Programlama 2 — Samsun Üniversitesi, Yazılım Mühendisliği
