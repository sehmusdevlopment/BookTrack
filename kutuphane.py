def kitap_ekle(kitaplar):
    isim = input("Kitap adı: ")
    yazar = input("Yazar: ")
    yayinevi = input("Yayınevi: ")
    kitaplar.append({"isim": isim, "yazar": yazar, "yayinevi": yayinevi})
    print("Kitap eklendi.")

def kitaplari_listele(kitaplar):
    if not kitaplar:
        print("Kütüphaneniz boş.")
        return
    for i, kitap in enumerate(kitaplar, 1):
        print(f"{i}. {kitap['isim']} - {kitap['yazar']} - {kitap['yayinevi']}")

def kitap_ara(kitaplar):
    arama = input("Aramak istediğiniz kitap adı veya yazar: ").lower()
    bulunanlar = [k for k in kitaplar if arama in k['isim'].lower() or arama in k['yazar'].lower()]
    if bulunanlar:
        for kitap in bulunanlar:
            print(f"{kitap['isim']} - {kitap['yazar']} - {kitap['yayinevi']}")
    else:
        print("Kitap bulunamadı.")

def kitap_sil(kitaplar):
    kitaplari_listele(kitaplar)
    try:
        sira = int(input("Silmek istediğiniz kitabın numarasını girin: "))
        if 1 <= sira <= len(kitaplar):
            silinen = kitaplar.pop(sira - 1)
            print(f"{silinen['isim']} silindi.")
        else:
            print("Geçersiz numara.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

def dosyaya_kaydet(kitaplar, dosya_adi="kutuphane.txt"):
    with open(dosya_adi, "w", encoding="utf-8") as dosya:
        for kitap in kitaplar:
            dosya.write(f"{kitap['isim']}|{kitap['yazar']}|{kitap['yayinevi']}\n")

def dosyadan_oku(dosya_adi="kutuphane.txt"):
    kitaplar = []
    try:
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            for satir in dosya:
                isim, yazar, yayinevi = satir.strip().split("|")
                kitaplar.append({"isim": isim, "yazar": yazar, "yayinevi": yayinevi})
    except FileNotFoundError:
        pass
    return kitaplar

def main():
    kitaplar = dosyadan_oku()
    while True:
        print("\n--- KİŞİSEL KÜTÜPHANE TAKİP ---")
        print("1- Kitap Ekle")
        print("2- Kitapları Listele")
        print("3- Kitap Ara")
        print("4- Kitap Sil")
        print("5- Çıkış")
        secim = input("Seçiminiz: ")
        if secim == "1":
            kitap_ekle(kitaplar)
        elif secim == "2":
            kitaplari_listele(kitaplar)
        elif secim == "3":
            kitap_ara(kitaplar)
        elif secim == "4":
            kitap_sil(kitaplar)
        elif secim == "5":
            dosyaya_kaydet(kitaplar)
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    main()
