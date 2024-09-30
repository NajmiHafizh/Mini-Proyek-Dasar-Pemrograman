User = str(input("Masukkan Nama: "))
Password = int(input("Masukkan NIM: "))

Selamat_Datang = f"Selamat Datang di Market, {User}^^ NIM Anda {Password}."
print(Selamat_Datang)

while True: 
    Harga_Barang = int(input("Masukkan Harga Barang: Rp"))
    Jumlah_Barang = int(input("Masukkan Jumlah Barang: "))
    Total_Harga = Harga_Barang * Jumlah_Barang
    print(Total_Harga)

    if Total_Harga > 250000:
        Diskon = 0.25 * Total_Harga
        Total_Belanjaan = float(f"{Total_Harga - Diskon}")
        print("Total Belanja anda diatas 250000, Anda Mendapatkan Diskon 25%")
        print(Total_Belanjaan)

    else:
        print("Total Belanja anda dibawah 250000, Anda Tidak Mendapatkan Diskon")
        Total_Tanpa_Diskon = f"Total Harga Belanja adalah {Total_Harga}"
        print(Total_Tanpa_Diskon)

    Selanjutnya = input("Apakah Anda Ingin Menghitung ulang Lagi? (y/t): ")
    if Selanjutnya.lower()!= 'y':
        print("Terima kasih Telah Berbelanja di Market")
        break 