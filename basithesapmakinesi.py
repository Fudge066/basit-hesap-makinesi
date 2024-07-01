print("""
1- Toplama İşlemi
2- Çıkarma İşlemi
3- Çarpma işlemi
4- Bölme işlemi
5- Mod alma
9- Çıkış
""")

while True:
    islem = input("Yapılacak işlemi seçin (çıkış için '9'a basın): ")
    if islem == '9':
        print("Çıkış yapılıyor...")
        break
    elif islem == '1':
        sayi1 = float(input("sayı1 giriniz: "))
        sayi2 = float(input("sayi2 giriniz: "))
        print("{} + {} = {}".format(sayi1, sayi2, sayi1 + sayi2))
    elif islem == '2':
        sayi1 = float(input("sayi1 giriniz: "))
        sayi2 = float(input("sayi2 giriniz: ")) 
        print("{} - {} = {}".format(sayi1, sayi2, sayi1 - sayi2))  
    elif islem == '3':
        sayi1 = float(input("sayi1 giriniz: "))
        sayi2 = float(input("sayi2 giriniz: "))
        print("{} * {} = {}".format(sayi1, sayi2, sayi1 * sayi2))
    elif islem == '4':
        sayi1 = float(input("sayi1 giriniz: "))
        sayi2 = float(input("sayi2 giriniz: "))
        if sayi2 > sayi1:
            print("Bölen sayı bölünenden büyük olamaz!")
        else:
            try:
                print("{} / {} = {}".format(sayi1, sayi2, sayi1 / sayi2))
            except ZeroDivisionError:
                print("Bölme işleminde ikinci sayı 0 olamaz!")
    elif islem == '5':
        sayi1 = int(input("sayi1 giriniz: "))
        sayi2 = int(input("sayi2 giriniz: "))
        if sayi2 <= 0:
            print("Mod alma işlemi için ikinci sayı pozitif ve sıfırdan farklı olmalıdır!")
        else:
            print("{} % {} = {}".format(sayi1, sayi2, sayi1 % sayi2))
    else:
        print("Geçersiz işlem seçtiniz")
