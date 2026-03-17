print("Silakan masukkan nama tamu. Ketik 'stop' jika anda telah selesai memasukkannya.")

while True:
    nama = input("Masukkan nama: ")

    if nama.lower() == "stop":
        break

    try:
        with open("guest_book.txt", "a") as file:
            file.write(nama + "\n")
        print("Nama telah terdaftar.")
    
    except OSError:
        print("Terjadi kesalahan saat menyimpan file.")