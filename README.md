Flowchart :
-
![image](https://github.com/user-attachments/assets/29911265-83d9-410b-9fd4-2b8910a983b6)


Penjelasan Mendetail Program : 
-
Program ini adalah sebuah aplikasi manajemen nilai mahasiswa yang menggunakan konsep OOP (Object-Oriented Programming) dengan kelas DaftarNilai. Program ini memungkinkan pengguna untuk menambah, menampilkan, menghapus, dan mengubah data nilai mahasiswa. 
 - INISIALISASI KELAS (Daftar Nilai)
   Penjelasan: Kelas DaftarNilai diinisialisasi dengan atribut daftar_nilai yang berupa dictionary kosong. Dictionary ini akan digunakan untuk menyimpan data mahasiswa dengan nama sebagai kunci dan nilai sebagai nilai.
 - METODE (tambah)
   Penjelasan:
    - Input Nama : Program meminta pengguna untuk memasukkan nama mahasiswa.
    - Input Nilai : Program meminta pengguna untuk memasukkan nilai mahasiswa.
    - Penyimpanan Data : Data nama dan nilai mahasiswa disimpan dalam dictionary 'daftar_nilai'.
    - Umpan Balik : Program menampilkan pesan bahwa data berhasil ditambahkan.
 - METODE (tampilkan)
   Penjelasan :
    - Cek Isi Dictionary : Program memeriksa apakah ada data di dalam 'daftar_nilai'.
    - Tampilkan Data : Jika ada data, program mencetak daftar nama dan nilai mahasiswa. Jika tidak ada data, program menampilkan pesan bahwa daftar nilai masih kosong.
 - METODE (hapus)
   Penjelasan:
    - Input Nama: Program meminta pengguna untuk memasukkan nama mahasiswa yang ingin dihapus.
    - Cek dan Hapus Data: Program memeriksa apakah nama tersebut ada dalam 'daftar_nilai'. Jika ada, data dihapus dan program menampilkan pesan bahwa data berhasil dihapus. 
      Jika tidak ada, program menampilkan pesan bahwa data tidak ditemukan.
 - METODE (ubah)
   Penjelasan:
    - Input Nama: Program meminta pengguna untuk memasukkan nama mahasiswa yang ingin diubah nilainya.
    - Cek dan Ubah Data: Program memeriksa apakah nama tersebut ada dalam daftar_nilai. Jika ada, program meminta input nilai baru dan mengupdate nilai mahasiswa tersebut. 
      Jika tidak ada, program menampilkan pesan bahwa data tidak ditemukan.
 - MENU UTAMA
   Penjelasan:
    - Inisialisasi Kelas: Membuat objek 'daftar_nilai' dari kelas 'DaftarNilai'.
    - Loop Menu Utama: Menampilkan menu utama dengan pilihan 1 hingga 5.
    - Pilihan Menu:
       - Tambah Data: Memanggil metode tambah untuk menambah data. Setelah menambah data, menanyakan apakah ingin menambah data lagi.
       - Tampilkan Data: Memanggil metode tampilkan untuk menampilkan data.
       - Hapus Data: Meminta input nama mahasiswa yang ingin dihapus dan memanggil metode hapus.
       - Ubah Data: Meminta input nama mahasiswa yang ingin diubah nilainya dan memanggil metode ubah.
       - Keluar: Menampilkan pesan "Terima kasih!" dan keluar dari loop.
       - Pilihan Tidak Valid: Menampilkan pesan bahwa pilihan tidak valid jika input pengguna tidak sesuai dengan pilihan yang tersedia.
     
Tampilan Ketika Program di Running :
-
 - Tampilan ketika Tambah data : 
![Screenshot 2024-12-05 130240](https://github.com/user-attachments/assets/a328a0a4-c8aa-461e-ae6c-d006598644b4)
 - Tampilan Data setelah penambahan data :
![Screenshot 2024-12-05 130324](https://github.com/user-attachments/assets/a2f27082-2259-475d-a37b-d1902e63b221)
 - Tampilan ketika Ubah Data dan Hapus Data
![Screenshot 2024-12-05 130353](https://github.com/user-attachments/assets/a7f6b565-2241-4b78-89f5-2afd3abc89fa)
 - Tampilan Setelah Data dihapus dan diubah
![Screenshot 2024-12-05 130602](https://github.com/user-attachments/assets/87262818-6198-4a3a-8f69-a0bccb81112b)

Terimakasih
-
