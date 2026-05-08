# hoop-imdat
Intelligent Manual Decision Assist Trigger / İnsan Müdahaleli Denetim ve Aksiyon Tetikleyicisi

Bu repo Python ders odevi icin kurgulanmistir.

## "AI Çağında Kim Çağırır Kimi?": Kendi A2P Senaryonu Tasarla

**Ders:** Programlama 2 · **Hafta:** 11 (Modüller ve Dosyalar) · **Süre:** 1 hafta · **Bireysel**

---

## 0. Bağlam (5 dk oku)

YC'nin (Y Combinator) son partilerinden iki şirket aynı şeyi söylüyor:
**"AI agent'lar her şeyi yapamıyor — takıldıklarında bir insan lazım."**

- **HireAHuman.ai** — *"AI agents can't step outside, but you can."* AI agent'ı **fiziksel dünyada** bir insan kiralar. (Birisi kapıya gitsin, fotoğraf çeksin, refakat etsin, vs.)
- **Humwork.ai** (YC P26) — *"AI agents call verified human experts when they get stuck."* AI agent'ı **dijital uzmanlığa** çağırır. Kod, hukuk, tasarım, tıp. Ortalama cevap süresi 2 dakikadan az.

Bu mimariye **A2P (Agent-to-Person)** deniyor. Geçen hafta sınıfta gördüğün **HOOTL / HITL / HOTL** modlarının doğrudan endüstriyel uygulaması.

Bu ödevde, **kendi seçeceğin gerçek bir senaryo** üzerinden bu üç modu kodlayacaksın.

---

## 1. Saha Araştırması (zorunlu — rapora gidecek)

İki siteyi de ziyaret et, ekran görüntüsü al (`arastirma/` klasörüne koy):

- https://hireahuman.ai
- https://humwork.ai

Cevaplaman gereken **üç soru**:

1. Bu iki şirket hangi noktada **AI'a güvenmediklerini** söylüyor? (Kendi cümlelerinle.)
2. "İnsan devreye girer" derken **nereden devreye girer**? HireAHuman ile Humwork arasındaki temel fark ne?
3. Senin seçeceğin senaryoya hangi şirket daha yakın? Niye?

> Sayfalar maintenance'a girebilir. Maintenance görüyorsan **iki ekran görüntüsü** + LinkedIn'deki launch post'unun ekran görüntüsünü ekle.

---

## 2. Senaryo Seç

Aşağıdaki **Senaryo Kataloğu**'ndan birini seç **veya** kendi senaryonu yaz.

Kurallar:
- Aynı senaryoyu **en fazla 3 öğrenci** seçebilir (ilk yorumlayan alır).
- Classroom yorumuna **"S## numaralı senaryoyu alıyorum"** yaz.
- Kendi senaryon ise **eğitmenden onay al** (Classroom yorumu ile).

Kullanım hikayesi 1-2 cümle olmalı. Örnek:

> *"Kargo takip botu: kullanıcı sipariş numarasını yazar, bot durumu söyler veya operatöre yönlendirir."*
> *"Görme engelliye yer tarifi: kullanıcı 'metroya nasıl giderim' yazar, bot temel rotayı söyler veya gönüllüye bağlar."*
> *"Yazılımcı desteği: kullanıcı hata mesajını yazar, bot bilinen çözümleri sunar veya senior'a yönlendirir."*
> *"Ayakkabı bağcığı bağlama rehberi: motor güçlüğü olan kullanıcı sorar, bot adımları söyler veya fizyoterapiste bağlar."*

---

## 3. Spesifikasyon (`SPEC.md`)

`SPEC.md` adında bir markdown dosyasında şunları yaz:

1. **Senaryo adı** ve 2-3 cümlelik kullanım hikayesi.
2. **Hedef kullanıcı** kim? (Kim, ne zaman, niye kullanır?)
3. **HOOTL** modunda bot ne yapar? Hangi tip soruda doğru cevap verir, hangi tipte yanlış cevap verir?
4. **HITL** modunda **operatör kim**? (Müşteri temsilcisi? Doktor? Aile üyesi? Gönüllü?)
5. **HOTL** modunda hangi tip soruda insana havale gider? **NİYE?** *Bu en kritik tasarım kararı, en yüksek puanlı bölüm.*
6. **bilgi.txt** içeriğinin taslağı (en az 12 satır, senaryona uygun).

---

## 4. Kodla

Geçen haftaki yapıyı kullan (lab oturumunda gördün):

| Dosya | Görev |
|---|---|
| `bilgi.txt` | `anahtar\|cevap` formatında, ≥12 satır |
| `bot.py` | `python3 bot.py [hootl\|hitl\|hotl]` — üç mod tek dosyada |
| `operator.py` | Ayrı terminalde, kuyruğu izler |

Senaryona özgü **en az 5 farklı kullanıcı girdisi** ile her üç modu da test et. Ekran görüntülerini rapora ekle.

---

## 5. Rapor (`rapor.pdf`, 2 sayfa)

1. **Saha araştırması** (~3 paragraf) — Adım 1'in cevapları.
2. **Senaryom ve tasarım kararlarım** (~1 sayfa) — Özellikle: HOTL'da "ne zaman insana havale" kuralını niye o şekilde seçtin?
3. **Test çıktıları** — 5 girdinin 3 modda davranışı (ekran görüntüsü tablosu).
4. **Düşünme sorusu** (1 paragraf): *"Senin senaryonu HireAHuman mı, Humwork mu satabilirdi? Niye?"*

---

## 6. Yasaklar

- ❌ LLM API yok. `requests`, `openai`, `groq`, `httpx` **yasak**.
- ❌ Sözlük (`dict`) yok. (Hafta 13'te göreceğiz.)
- ❌ AI'a "tüm ödevi yaz" yasak. AI'a "şu hatayı bul" / "şu kavramı açıkla" serbest.
- ✅ Kod yorumları **Türkçe**, kendi cümlelerinle.

---

## 7. Teslim

| Klasör/Dosya | Açıklama |
|---|---|
| `SPEC.md` | Senaryon ve tasarım kararları |
| `bilgi.txt` | ≥12 satır |
| `bot.py` | Üç mod, tek dosya |
| `operator.py` | Bağımsız süreç |
| `rapor.pdf` | 2 sayfa |
| `arastirma/` | HireAHuman + Humwork ekran görüntüleri |

**Platform:** Google Classroom · **Son tarih:** [GÜN/AY/YIL, 23:59]

**Değerlendirme (100):**
- Saha araştırması (15)
- SPEC kalitesi — özellikle HOTL kuralı (15)
- Çalışan kod, üç mod (40)
- Test örnekleri (10)
- Rapor + düşünme sorusu (20)

---

## EK A — Senaryo Kataloğu

Aynı senaryoyu en fazla 3 kişi seçebilir. Classroom yorumuna **"S## alıyorum"** yaz.

### Erişilebilirlik (HireAHuman ruhu)
- **S01** — Görme engelliye yer/rota tarifi (metro, otobüs, yaya)
- **S02** — Görme engelliye ürün/raf tanıma desteği
- **S03** — Tekerlekli sandalye için engelsiz rota
- **S04** — İşitme engelliye telefon görüşmesi tercümesi
- **S05** — Demanslı kişi için "neredeyim, kim olduğum" anchor
- **S06** — Otizmli birey için sosyal etkileşim provası
- **S07** — Motor güçlüğü olan için günlük yaşam rehberi (bağcık, düğme, kıyafet)
- **S08** — Yaşlı kişi için ilaç saati ve doz onayı

### Acil & Güvenlik
- **S09** — Kapı kilitlendi: yakındaki çilingir + ne yapmalı
- **S10** — Yalnız yürüyen kişi için güvenli rota + acil paylaşım
- **S11** — Doğal afet: yakındaki toplanma alanı
- **S12** — Yangın/gaz kaçağı: ilk 60 saniye protokolü
- **S13** — Trafik kazası: tutanak rehberi + tarafların hakları
- **S14** — Çocuk kayboldu: hızlı eylem listesi

### Yaşam & Yer
- **S15** — Veterinere gitmeden: evcil hayvan acil mi?
- **S16** — Yabancı şehirde dil + yer tarifi
- **S17** — Restoran menüsü çevirisi (özellikle alerjen)
- **S18** — Pazarda ürün tazeliği / fiyat kontrolü
- **S19** — Eve gelen tamircinin işini ön kontrol
- **S20** — Kayıp eşya: sistemli geri sorgulama

### Müşteri Hizmetleri
- **S21** — Kargo takip
- **S22** — Sipariş iadesi süreci
- **S23** — Banka kart kayıp/şifre/itiraz
- **S24** — Telekom fatura itirazı
- **S25** — Restoran rezervasyon asistanı
- **S26** — Otel check-in/out asistanı
- **S27** — Uçak/otobüs bileti değişikliği

### Dijital Uzmanlık (Humwork ruhu)
- **S28** — Yazılımcı desteği: hata ayıklama (error → çözüm)
- **S29** — Kod review asistanı (basit lint kuralları)
- **S30** — Hukuki sözleşme: bu maddeyi imzalamalı mıyım?
- **S31** — Vergi beyannamesi: hangi indirim
- **S32** — Sigorta tazminatı süreç rehberi
- **S33** — Akademik makale: dilbilgisi/üslup
- **S34** — CV/özgeçmiş geri bildirim
- **S35** — Diploma/yurt dışı denklik

### Sağlık (yönlendirme — tıbbi tavsiye değil)
- **S36** — Belirti ön tarama: acil mi, randevu mu?
- **S37** — İlaç etkileşimi ön sorgu
- **S38** — Aşı takvimi (çocuk/yetişkin)
- **S39** — Ruh sağlığı destek hattı yönlendirme
- **S40** — Beslenme/diyet temel ilkeler

### Eğitim
- **S41** — Matematik problemi adım adım yardım
- **S42** — Dil öğrenme: cümle örneği + telaffuz ipucu
- **S43** — Sınav stresi yönetimi (öğrenci destek)
- **S44** — Üniversite tercih danışmanı
- **S45** — Akademik kaynak bulma asistanı

### Resmi & Hukuki (yönlendirme)
- **S46** — e-Devlet hizmet bulucu
- **S47** — Dilekçe örneği (konuya göre şablon)
- **S48** — Belediye/SGK randevu yönlendirme
- **S49** — Tüketici hakları: nereye şikayet, nasıl?

### Yaratıcı / Eğlence
- **S50** — Düğün davetiyesi metin yardımı
- **S51** — Doğum günü/mezuniyet konuşması taslağı
- **S52** — Aşk mektubu / barışma mesajı düzenleme
- **S53** — Tinder/eş arama profili düzenleme
- **S54** — Sosyal medya gönderi danışmanı
- **S55** — Resmi şikayet/teşekkür mektubu üslup ayarı

### Hayvan & Doğa
- **S56** — Köpek davranış problemi rehberi
- **S57** — Kedi yemek/davranış sorunları
- **S58** — Akvaryum bakımı (suda problem belirtileri)
- **S59** — Bitki bakımı (yaprakları sarardı, ne yapayım?)
- **S60** — Bahçe takibi (mevsim göre)

### Hobi & Beceri
- **S61** — Yemek tarifi adım adım rehber
- **S62** — DIY ev tamiri (musluk, sigorta, badana)
- **S63** — El işi & örgü model takibi
- **S64** — Müzik enstrümanı pratik takibi
- **S65** — Fitness antrenman düzeltici
- **S66** — Kahve demleme rehberi (yöntem bazlı)

### Meta
- **S67** — **Kendi senaryon** — eğitmen onayı şart

---

## EK B — HOTL "Ne Zaman İnsan?" Tasarım İpuçları

HOTL modunda en kritik karar: *"Bot ne zaman insana havale eder?"* Üç tipik strateji:

| Strateji | Tetik | Örnek senaryo |
|---|---|---|
| **Eşleşme yok** | bilgi.txt'de bulunamadı | Müşteri hizmetleri (basit) |
| **Risk kelimesi** | "iade", "şikayet", "acil" geçiyor | Banka, sağlık |
| **Belirsizlik** | Birden fazla eşleşme var | Tıbbi/hukuki |

Senin senaryona en uygun stratejiyi seç. Raporda **niye** o stratejiyi seçtiğini açıkla. Kötü bir HOTL kuralı, ödevin geri kalanı kusursuz olsa bile düşük puan getirir.

---

## EK C — Sık Sorulan Sorular

**S: Ben S03'ü seçtim ama 3 kişi olmuş. Ne yapayım?**
C: Aynı kategoriden başka bir senaryo seç veya S67 ile kendi senaryonu öner.

**S: Senaryom çok hassas (sağlık, hukuk). Sorumluluk nasıl?**
C: bilgi.txt'in başına ve bot başlangıç ekranına **"Bu bot tıbbi/hukuki tavsiye vermez. Ciddi durumlarda profesyonele başvurun."** uyarısı ekle. Bu zorunlu.

**S: HireAHuman ya da Humwork çalışmıyor (maintenance).**
C: Ekran görüntüsü al, "maintenance görüldü" notu düş, LinkedIn launch post'una bak.

**S: bot.py'imde sadece 2 mod çalışıyor.**
C: Sıfır puan. Üç modu da test ettiğinden emin ol.
