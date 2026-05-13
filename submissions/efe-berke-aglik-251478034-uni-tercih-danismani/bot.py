from data import *
import socket
from functools import lru_cache

# Uzman önerilerinin tekrardan aynı mesajın yazılabilme ihtimaline karşı kaydedileceği sözlük
kayitli_mesajlar = {}

# Levenshtein Mesafe Algoritması (lru_cache ile memoized — O(m×n))
@lru_cache(maxsize=None)
def levenshtein_mesafesi(mesaj, anahtar):
    if not mesaj: return len(anahtar)
    if not anahtar: return len(mesaj)
    if mesaj[0] == anahtar[0]:
        return levenshtein_mesafesi(mesaj[1:], anahtar[1:])
    return 1 + min(
        levenshtein_mesafesi(mesaj[1:], anahtar),    # silme
        levenshtein_mesafesi(mesaj, anahtar[1:]),    # ekleme
        levenshtein_mesafesi(mesaj[1:], anahtar[1:]) # değiştirme
    )

# Verilen mesaja en yakın data anahtarını ve Levenshtein mesafesini döndürür
def en_yakin_anahtari_bul(mesaj, anahtarlar):
    en_yakin, minimum = None, 999
    for anahtar in anahtarlar:
        mesafe = levenshtein_mesafesi(mesaj, anahtar)
        if mesafe < minimum:
            minimum = mesafe
            en_yakin = anahtar
    return en_yakin, minimum

# Bottan (istemci) uzmana (sunucu) mesajı ilet ve yanıtı al
def uzman_bot_iletisim(mesaj, kayitli_mesajlar):
    talep = f"[BOT] '{mesaj}' girdisiyle eşleşen bir veri bulamadım. Öğrenciye nasıl yanıt vermeliyim?"
    client_socket.sendall(talep.encode('utf-8'))  # Bot talebini istemciden sunucuya gönder
    yanit = client_socket.recv(1024)  # Sunucudan gelen yanıtı al
    kayitli_mesajlar[mesaj] = yanit.decode('utf-8')  # Tekrar aynı mesaj gelirse yanıtlanabilmesi için kaydet
    return yanit

# Uzmandan (sunucudan) alınan yanıtın mantıksal kontrolleri
def yanit_kontrol(mesaj, kayitli_mesajlar):
    yanit = uzman_bot_iletisim(mesaj, kayitli_mesajlar)
    if yanit:
        print(f"Bot: {yanit.decode('utf-8')}")
    else:
        print(f"Bot: Şu an için isteğinizi yerine getiremiyorum.")

# Socket oluşturma
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Sunucuya bağlanma
client_socket.connect(('localhost', 65432))

# Ana döngü
try:
    while True:
        minimum = 999
        mesaj = input("Öğrenci: ")
        mevcut_anahtar, minimum = en_yakin_anahtari_bul(mesaj, data.keys())
        if kayitli_mesajlar.get(mesaj):  # Mesaj önceden kaydedilmiş mi kontrol et
            print(f"Bot: {kayitli_mesajlar[mesaj]}")
        elif minimum == 0:
            print(f"Bot: {data[mevcut_anahtar]}")
        elif minimum <= 3:
            while True:
                onay = input(f"Bot: Bunu mu demek istediniz '{mevcut_anahtar}'? [E/H]: ")
                if onay.lower() in ["e", "evet"]:
                    print(f"Bot: {data[mevcut_anahtar]}")
                    break
                elif onay.lower() in ["h", "hayır"]:
                    yanit_kontrol(mesaj, kayitli_mesajlar)  # Öğrenci 'hayır' derse mesajı uzmana ilet
                    break
                else:
                    print(f"Bot: Size yardımcı olabilmem için lütfen doğru şekilde yanıtlayın.")
        else:
            yanit_kontrol(mesaj, kayitli_mesajlar)
except KeyboardInterrupt:
    print("\nBağlantı kapatılıyor...")
finally:
    client_socket.close()

    

