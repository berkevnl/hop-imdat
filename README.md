# hop-imdat

> **HOP-İMDAT** — İnsan Müdahale Devri Aktarım Tetikleyicisi
> Sıkışan AI ajanları için insan-döngülü kurtarma protokolü.

Samsun Üniversitesi Yazılım Mühendisliği 2. sınıf **Programlama 2** dersi öğrencilerinin **"Which Language?"** araştırma projesi kapsamındaki dönemlik mini-projelerini topladığı paylaşımlı çalışma alanı.

## Hızlı Başlangıç

1. Projenin fikir dokümanı ve ödev detayları → **[IDEA.md](IDEA.md)**
2. LLM ajanları ve gönderim kuralları → **[AGENT.md](AGENT.md)**
3. Gönderimler → `submissions/` klasörü

## Gönderim Akışı

1. Bu repoyu kendi GitHub hesabına **fork**'la.
2. Forku lokalde **clone**'la.
3. `submissions/` altında kendi klasörünü oluştur (bkz. [AGENT.md](AGENT.md)).
4. Dosyalarını ekle. **Kendi klasörün dışındaki dosyalara dokunma.**
5. Forkuna **commit + push**.
6. `seyyah/hop-imdat:main`'e **Pull Request** aç.

PR başlık formatı: `[Hafta-X] <ad soyad numara> <proje-kisa-ad>`

## Otomatik Doğrulama

Her PR'da `.github/workflows/check-submission.yml` çalışır:
- Klasör adı pattern kontrolü
- Tek submission klasörü değişikliği kontrolü
- `submissions/` dışına dokunulmamış mı kontrolü

---

**Ders sorumlusu:** Seyyah
**Ders:** Programlama 2 — Samsun Üniversitesi, Yazılım Mühendisliği
