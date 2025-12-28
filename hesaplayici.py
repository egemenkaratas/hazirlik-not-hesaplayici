def ortalama_hesapla():
    # Sınav isimleri ve ağırlıkları
    sinavlar = {
        "Quiz 1": 0.10,
        "Quiz 2": 0.10,
        "In Class Writing 1": 0.075,
        "In Class Writing 2": 0.075,
        "MidTerm 1": 0.20,
        "MidTerm 2": 0.20,
        "Video Task": 0.05,
        "Paralı Kitap": 0.10,
        "Speaking Exam": 0.10

    }
    toplam_puan = 0

    print("--- Hazırlık Ortalama Hesaplama Sistemine Hoş Geldiniz ---")

    for sınav, agırlık in sinavlar.items():
        try:
            # Kullanıcıdan notu alma
            not_degeri = float(input(f"{sınav} notunu giriniz: "))
            # Ağırlıklı notu hesaplayıp toplama ekliyoruz
            toplam_puan += not_degeri * agırlık
        except ValueError :
            print("Lütfen geçerli bir sayı giriniz")
            return
        
     # Sonuçları ekrana yazdırıyoruz
    print(f"\n1. Dönem Ortalamanız :{toplam_puan:.2f}")

    gecme_notu = 120 - toplam_puan
    if gecme_notu > 100:
        print("UYARI: Sınıfı geçmek için 2. dönem imkansız bir not almanız gerekir!")
    elif gecme_notu <= 0:
        print("Tebrikler! Şimdiden geçmeyi garantilediniz.")
    else:
        print(f"Sınıfı geçmek için 2. dönem almanız gereken minimum not: {gecme_notu:.2f}")

if __name__ == "__main__":
    ortalama_hesapla()
    input("\nKapatmak için Enter'a basınız...")
    





