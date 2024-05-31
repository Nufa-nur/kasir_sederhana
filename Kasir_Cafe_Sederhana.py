pilihan = "Y"
while pilihan == "Y":
    print("\nCAFE SEDERHANA")
    print(("Daftar Menu Cafe Sederhana"))
    kd1= {"Kode" : "A\t|", "Menu" : "Teh Tarik\t|", "Harga" : "Rp 12.000\t"}
    kd2= {"Kode" : "B\t|", "Menu" : "Boba Milk Tea\t|", "Harga" : "Rp 10.000\t"}
    kd3= {"Kode" : "C\t|", "Menu" : "Es Capucino\t|", "Harga" : "Rp 8.000\t"}
    kd4= {"Kode" : "D\t|", "Menu" : "Es Americano\t|", "Harga" : "Rp 14.000\t"}
    print("="*35)
    print("Kode \t|", "Menu\t\t|", "Harga\t|")
    print("="*35)
    print(kd1["Kode"], kd1["Menu"], kd1["Harga"])
    print(kd2["Kode"], kd2["Menu"], kd2["Harga"])
    print(kd3["Kode"], kd3["Menu"], kd3["Harga"])
    print(kd4["Kode"], kd4["Menu"], kd4["Harga"])
    print("="*35)
    pesan = str(input("\nMasukkan Kode Menu\t: "))
    jumlahpesan = int(input("Masukkan Jumlah Pesanan : "))
    if pesan == "A":
        Menu = kd1["menu"]
        harga = (12000*jumlahpesan)
        ppn= int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga*0.2)
            totalharga = int(harga-diskon+ppn)
        else:
            diskon = 0
            totalharga = int(harga+ppn)
    elif pesan == "B":
        Menu = "Boba Milk Tea"
        harga = (10000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga = int(harga-diskon+ppn)
        else:
            diskon = 0
            totalharga = int(harga+ppn)
    elif pesan == "C":
        Menu = "ES Capucino"
        harga = int(8000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon = 0
        totalharga = int(harga+ppn)
    elif pesan == "D":
        Menu = "ES Americano"
        harga = int(14000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon = 0
        totalharga = int(harga+ppn)
    else:
        Menu = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        totalharga = "-"
        pilihan = input("Menu Tidak Tersedia, Silahkan Masukkan Abjad Menu Yang Tersedia, Silahkan Ulangi Kembali Y/N : ") 
    print("-"*30)
    print("Cafe Sederhana")
    print("-"*30)
    print("Menu\t\t:", Menu)
    print("Jumlah Pesan\t:", jumlahpesan)
    print("Harga\t\t:", harga)
    print("Diskon\t\t:", diskon)
    print("PPN\t\t:", ppn)
    print("-"*30)
    print("Total Bayar\t:", totalharga)
    print("-"*30)
    pilihan = input("Apakah Anda Ingin Order Kembali Y/N : ")