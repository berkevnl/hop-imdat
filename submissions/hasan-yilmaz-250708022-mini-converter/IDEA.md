IDEA: miniconverter 

Motivasyon
Yapay zeka modelleri (LLM'ler) artık devasa kod blokları üretebiliyor; ancak basit ama kritik mantıksal işlemlerde hala tökezleyebiliyorlar. 
`miniconverter`, modellerin sadece "kod yazma" yeteneğini değil, aynı zamanda doğruluk ve yapısal sağlamlık yeteneklerini ölçmek için tasarlanmış bir deney alanıdır.
Karpathy tarzı bir yaklaşımla: Kodun estetiğinden ziyade, fonksiyonel determinizmi ve hata yönetimini (error handling) standardize etmek istiyorum.

Kapsam
Evrimsel Gelişim (v0 -> v2): Modellerin mevcut kod tabanlarını ne kadar iyi anladığını ve üzerine ne kadar güvenli eklemeler yapabildiğini ölçen aşamalı prompt mühendisliği.
Metrik Odaklı Analiz: Sadece "geçti/kaldı" değil; üretim hızı (TPS), token maliyeti (Cost) ve kod yoğunluğu (LOC) üzerinden derinlemesine inceleme.

Başarı Kriterleri
Tam Doğruluk (100% Pass Rate): Hazırlanan 8 test senaryosunun (edge cases dahil) tamamından sıfır hata ile geçilmesi.
Maliyet/Hız Dengesi: Gemini 1.5 Flash-Lite gibi modellerde, minimum maliyetle maksimum üretim hızı (High TPS) elde edilmesi.
Kalıcı Yapı: Üretilen kodun sadece testi geçmesi değil, `pylint` veya `mypy` gibi araçlardan geçer not alacak yapısal düzgünlükte olması.
Otomasyon: Benchmark sürecinin insan müdahalesi olmadan rapor ve grafik üretebilir hale gelmesi.
