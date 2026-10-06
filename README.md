# Studi_Kasus_6_Abdul-Azis-Zulkarnain

**Nama**: Abdul Azis Zulkarnain

**NIM** : 2609116051

**Kelas** : B

<img width="502" height="160" alt="Screenshot 2026-10-06 214936" src="https://github.com/user-attachments/assets/038d02b1-a5f3-44ed-9195-33030727e72e" />

while True: membuat program terus berjalan sampai user memilih keluar, print("Menu:") menampilkan pilihan menu, input("Pilih menu...") menerima pilihan dari user

<img width="342" height="157" alt="Screenshot 2026-10-06 220533" src="https://github.com/user-attachments/assets/2708d0d1-ac13-4d0a-b43a-f892d93e147f" />

if pilihan == "1": menjalankan menu untuk menambah data mahasiswa, nim = input(...) memasukkan NIM mahasiswa, nama = input(...) memasukkan nama mahasiswa, nilai = input(...) memasukkan nilai mahasiswa, data_baru = {...} membuat data baru dalam bentuk dictionary.

<img width="458" height="157" alt="Screenshot 2026-10-06 220725" src="https://github.com/user-attachments/assets/65ae5e3b-8d84-41ed-9fee-b83b3404516d" />

with open(..., 'r') membuka file JSON untuk membaca data yang sudah ada, json.load(file) mengambil data dari file JSON ke Python, data.append(data_baru) menambahkan data mahasiswa baru ke data yang sudah ada, with open(..., 'w') membuka file untuk menulis atau memperbarui data, json.dump(data, file, indent=4) menyimpan data ke file JSON dengan format yang rapi.

<img width="663" height="102" alt="Screenshot 2026-10-06 221235" src="https://github.com/user-attachments/assets/2ca292a6-8c99-412a-aec0-5faf6131786c" />

elif pilihan == "2": menjalankan menu untuk menampilkan semua data, for item in data: mengulang setiap data mahasiswa, print(f"...") menampilkan nama, NIM, dan nilai mahasiswa.

<img width="443" height="105" alt="Screenshot 2026-10-06 221403" src="https://github.com/user-attachments/assets/ddc9897e-4358-474d-9e3e-800598c7bf11" />

elif pilihan == "3": menjalankan menu keluar, break menghentikan perulangan while, else: dijalankan kalau user memasukkan pilihan selain 1, 2, atau 3.




