# Membuat perulangan while
while (True):
    # Mencetak Toko saya
    print()
    print("+++++++++++++++++++++++++")
    print("++ Warung Makan Padang ++")
    print("+++++++++++++++++++++++++")
    print()

    # Mencetak Pilih menu
    print("Pilih Menu : ")

    # Mencetak menu
    print("1. Prekedel      -> Rp. 4000")
    print("2. Gurami        -> Rp. 15000")
    print("3. Ayam Goreng   -> Rp. 7000")
    print("4. Rendang       -> Rp. 8000")

    print()
    # Membuat opsi inputan Pilih menu
    opsi = input("Pilih Menu     : ")

    # Membuat opsi pertama
    if opsi == "1":
        # Memasukan inputan jumlah
        jumlah = int(input("Jumlah         : "))
        # Memasukan inputan Uang kamu
        uangKamu = int(input("Uang Kamu      : "))
        # Membuat variabel Harga
        harga = 4000
        # Membuat variabel total (harga dikali jumlah)
        total = (harga * jumlah)

        # Membuat opsi jumlah pertama
        if jumlah == 1:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah kedua
        elif jumlah == 2:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah ketiga
        elif jumlah == 3:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)


    # Membuat opsi kedua
    elif opsi == "2":
        # Memasukan inputan jumlah
        jumlah = int(input("Jumlah         : "))
        # Memasukan inputan Uang kamu
        uangKamu = int(input("Uang Kamu      : "))
        # Membuat variabel Harga
        harga = 15000
        # Membuat variabel total (harga dikali jumlah)
        total = (harga * jumlah)

        # Membuat opsi jumlah pertama
        if jumlah == 1:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah kedua
        elif jumlah == 2:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah ketiga
        elif jumlah == 3:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)

    # Membuat opsi ketiga
    elif opsi == "3":
        # Memasukan inputan jumlah
        jumlah = int(input("Jumlah         : "))
        # Memasukan inputan Uang kamu
        uangKamu = int(input("Uang Kamu      : "))
        # Membuat variabel Harga
        harga = 7000
        # Membuat variabel total (harga dikali jumlah)
        total = (harga * jumlah)

        # Membuat opsi jumlah pertama
        if jumlah == 1:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah kedua
        elif jumlah == 2:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah ketiga
        elif jumlah == 3:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)

    # Membuat opsi keempat
    elif opsi == "4":
        # Memasukan inputan jumlah
        jumlah = int(input("Jumlah         : "))
        # Memasukan inputan Uang kamu
        uangKamu = int(input("Uang Kamu      : "))
        # Membuat variabel Harga
        harga = 8000
        # Membuat variabel total (harga dikali jumlah)
        total = (harga * jumlah)

        # Membuat opsi jumlah pertama
        if jumlah == 1:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah kedua
        elif jumlah == 2:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)
        # Membuat opsi jumlah ketiga
        elif jumlah == 3:
            print("Uang Kembalian :", uangKamu - total)
            print("Total          :", total)

    # Mencetak Maaf tidak ada pilihan ini, dan menghentikan program dengan break
    else:
        print("Maaf tidak ada pilhan ini ")
        break

    print()
    # Membuat variabel status inputan "apakah masih akan melanjutkan program atau tidak"
    status = input("Apakah masih ada inputan? (y = Ya, n = Tidak)? ")
    # jika y maka program akan berlanjut
    if status == "y":
        print()
        print("Silahkan masukan input data lagi")

    # Jika n maka program akan berhenti dengan break
    elif status == "n":
        break

    # Jika memasukan komentar salah maka program akan berhenti dengan break
    else:
        print("Maaf inputan tidak dikenal \n")
        break 