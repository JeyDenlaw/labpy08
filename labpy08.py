class DaftarNilai:
    def __init__(self):
        self.daftar_nilai = {}

    def tambah(self):
        nama = input("Masukkan nama mahasiswa: ")
        nilai = int(input("Masukkan nilai mahasiswa: "))
        self.daftar_nilai[nama] = nilai
        print("Data berhasil ditambahkan.")

    def tampilkan(self):
        if self.daftar_nilai:
            print("=======================")
            print("Daftar Nilai Mahasiswa:")
            print("=======================")
            for nama, nilai in self.daftar_nilai.items():
                print("----------------------")
                print(f"{nama} : {nilai}")
            print("----------------------")    
        else:
            print("Daftar nilai masih kosong.")

    def hapus(self, nama):
        if nama in self.daftar_nilai:
            del self.daftar_nilai[nama]
            print(f"Data {nama} berhasil dihapus.")
        else:
            print(f"Data {nama} tidak ditemukan.")

    def ubah(self, nama):
        if nama in self.daftar_nilai:
            nilai_baru = int(input("Masukkan nilai baru: "))
            self.daftar_nilai[nama] = nilai_baru
            print(f"Data {nama} berhasil diubah.")
        else:
            print(f"Data {nama} tidak ditemukan.")

daftar_nilai = DaftarNilai()

while True:
    print("\nMenu:")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == '1':
            daftar_nilai.tambah()
            while True:
                lagi = input("Apakah Anda ingin menambahkan data lagi? (y/n): ")
                if lagi.lower() == 'y':
                    daftar_nilai.tambah()
                elif lagi.lower() == 'n':
                    break
                else:
                    print("Input tidak valid.")
    elif pilihan == '2':
        daftar_nilai.tampilkan()
    elif pilihan == '3':
        nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
        daftar_nilai.hapus(nama)
    elif pilihan == '4':
        nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
        daftar_nilai.ubah(nama)
    elif pilihan == '5':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")