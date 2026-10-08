import json

while True:
    print("Menu:")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        nama = input(":masukkan Nama: ")
        nim = input(":masukkan Nim: ")
        nilai = input("Masukkan Nilai: ")

        data_baru = {
            "nama": nama,
            "nim": nim,
            "nilai": nilai
        }

        with open('data_nilai.json', 'r') as file:
            data = json.load(file)

        data.append(data_baru)

        with open('data_nilai.json', 'w') as file:
            json.dump(data, file, indent=4)

        print("Data berhasil ditambahkan.")

    elif pilihan == "2":
        with open('data_nilai.json', 'r') as file:
            data = json.load(file)

        for item in data:
            print(f"Nama: {item['nama']}, NIM: {item['nim']}, Nilai: {item['nilai']}")

    elif pilihan == "3":
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
