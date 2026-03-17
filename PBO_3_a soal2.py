print("Silakan masukkan nama tamu.")
print("Ketik 'stop' jika anda telah selesai memasukkannya.\n")

with open("guest_book.txt", "a") as file:
    while True:
        nama = input("Masukkan nama: ")

        if nama == "stop":
            break

        file.write(nama + "\n")

print("Semua nama telah berhasil disimpan.")