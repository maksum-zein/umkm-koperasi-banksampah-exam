class UMKMSystem:
    def __init__(self, nama_umkm):
        self.nama_umkm = nama_umkm
        self.anggota = []
        self.dana_pinjaman = 50000000

    def tambah_anggota(self, nama, pinjaman):
        anggota = {
            "nama": nama,
            "pinjaman": pinjaman
        }
        self.anggota.append(anggota)

    def hitung_pengembalian(self, nama, tahun):
        for anggota in self.anggota:
            if anggota["nama"] == nama:
                pinjaman = anggota["pinjaman"]
                bunga = 0.05 * tahun * pinjaman
                return pinjaman + bunga
        return None

class Koperasi(UMKMSystem):
    def __init__(self, nama_umkm):
        super().__init__(nama_umkm)
        self.transaksi = []

    def catat_transaksi(self, nama, jenis, jumlah):
        transaksi = {
            "nama": nama,
            "jenis": jenis,
            "jumlah": jumlah
        }
        self.transaksi.append(transaksi)

    def hitung_keuntungan(self):
        keuntungan = 0
        for transaksi in self.transaksi:
            if transaksi["jenis"] == "jual":
                keuntungan += transaksi["jumlah"]
            elif transaksi["jenis"] == "beli":
                keuntungan -= transaksi["jumlah"]
        return keuntungan

class BankSampah(UMKMSystem):
    def __init__(self, nama_umkm):
        super().__init__(nama_umkm)
        self.data_sampah = {}

    def catat_sampah(self, nama, jenis_sampah, jumlah_kg):
        if nama not in self.data_sampah:
            self.data_sampah[nama] = {}
        if jenis_sampah not in self.data_sampah[nama]:
            self.data_sampah[nama][jenis_sampah] = 0
        self.data_sampah[nama][jenis_sampah] += jumlah_kg

    def hitung_nilai_tukar(self, nama):
        nilai_per_kg = {
            "plastik": 5000,
            "kertas": 2000
        }
        total = 0
        if nama in self.data_sampah:
            for jenis, jumlah in self.data_sampah[nama].items():
                harga = nilai_per_kg.get(jenis, 0)
                total += jumlah * harga
        return total

    def pesan_edukasi(self, nama):
        total_kg = 0
        if nama in self.data_sampah:
            for jumlah in self.data_sampah[nama].values():
                total_kg += jumlah

        if total_kg >= 100:
            return "Luar biasa! Anda adalah pahlawan lingkungan!"
        elif total_kg >= 50:
            return "Hebat! Terus kumpulkan dan daur ulang!"
        elif total_kg > 0:
            return "Ayo tingkatkan partisipasi untuk bumi yang lebih bersih!"
        else:
            return "Yuk mulai kumpulkan sampah dan peduli lingkungan!"

def menu_koperasi(koperasi):
    while True:
        print("\n--- MENU KOPERASI ---")
        print("1. Tambah Anggota")
        print("2. Catat Transaksi")
        print("3. Kembali ke Menu Utama")
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            nama = input("Nama anggota: ")
            pinjaman = int(input("Jumlah pinjaman (Rp): "))
            koperasi.tambah_anggota(nama, pinjaman)
        elif pilihan == "2":
            nama = input("Nama anggota: ")
            jenis = input("Jenis transaksi (beli/jual): ")
            jumlah = int(input("Jumlah (Rp): "))
            koperasi.catat_transaksi(nama, jenis, jumlah)
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid!")

def menu_bank_sampah(bank_sampah):
    while True:
        print("\n--- MENU BANK SAMPAH ---")
        print("1. Catat Sampah")
        print("2. Kembali ke Menu Utama")
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            nama = input("Nama anggota: ")
            jenis = input("Jenis sampah (plastik/kertas): ")
            jumlah = float(input("Jumlah (kg): "))
            bank_sampah.catat_sampah(nama, jenis, jumlah)
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid!")

def menu_laporan(koperasi, bank_sampah):
    print("\n--- LAPORAN UMKM ---")
    for anggota in koperasi.anggota:
        nama = anggota["nama"]
        pinjaman = anggota["pinjaman"]
        pengembalian = koperasi.hitung_pengembalian(nama, tahun=1)
        nilai_tukar = bank_sampah.hitung_nilai_tukar(nama)
        pesan = bank_sampah.pesan_edukasi(nama)

        print(f"\nNama: {nama}")
        print(f"- Pinjaman: Rp{pinjaman}")
        print(f"- Pengembalian (1 tahun): Rp{pengembalian}")
        print(f"- Nilai Tukar Sampah: Rp{nilai_tukar}")
        print(f"- Pesan Edukasi: {pesan}")

    print("\nTotal Keuntungan Koperasi: Rp", koperasi.hitung_keuntungan())

def main():
    print("=== SISTEM UMKM, KOPERASI, & BANK SAMPAH ===")
    nama_umkm = input("Masukkan nama UMKM: ")

    koperasi = Koperasi(nama_umkm)
    bank_sampah = BankSampah(nama_umkm)

    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Modul Koperasi")
        print("2. Modul Bank Sampah")
        print("3. Tampilkan Laporan UMKM")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            menu_koperasi(koperasi)
        elif pilihan == "2":
            menu_bank_sampah(bank_sampah)
        elif pilihan == "3":
            menu_laporan(koperasi, bank_sampah)
        elif pilihan == "4":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
