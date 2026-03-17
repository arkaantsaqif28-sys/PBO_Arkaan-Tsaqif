# meminta pengguna memasukkan nama
nama = input("Masukkan nama anda: ")

# membuka file guest.txt dalam mode write
with open("guest.txt", "w") as file:
    file.write(nama)

print("Nama berhasil disimpan ke file guest.txt")