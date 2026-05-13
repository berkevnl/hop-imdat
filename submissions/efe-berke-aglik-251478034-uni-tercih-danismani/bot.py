from data import *
import socket
from functools import lru_cache

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

# Socket oluşturma
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Sunucuya bağlanma
client_socket.connect(('localhost', 65432))

# Uzman önerilerinin tekrardan aynı mesajın yazılabilme ihtimaline karşı kaydedileceği sözlük
kayitli_mesajlar = {}

# Ana döngü: öğrenci girdisini al, uygun yanıtı ver
while True:
    mesaj = input("Öğrenci: ")
    mevcut_anahtar, minimum = en_yakin_anahtari_bul(mesaj, data.keys())
    if minimum == 0:
        print(f"Bot: {data[mevcut_anahtar]}")
    elif minimum <= 3:
        print(f"Bot: Bunu mu demek istediniz '{mevcut_anahtar}'?")
    elif kayitli_mesajlar.get(mesaj):  # Mesaj önceden kaydedilmiş mi kontrol et
        print(f"Bot: {kayitli_mesajlar[mesaj]}")
    else:
        talep = f"[BOT] '{mesaj}' girdisiyle eşleşen bir veri bulamadım. Öğrenciye nasıl yanıt vermeliyim?"
        client_socket.sendall(talep.encode('utf-8'))  # Bot talebini istemciden sunucuya gönder
        yanit = client_socket.recv(1024)  # Sunucudan gelen yanıtı al
        kayitli_mesajlar[mesaj] = yanit.decode('utf-8')  # Tekrar aynı mesaj gelirse yanıtlanabilmesi için kaydet
        if yanit:
            print(f"Bot: {yanit.decode('utf-8')}")
        else:
            print(f"Mesajınızı tam olarak anlayamadım.")

client_socket.close()

    

