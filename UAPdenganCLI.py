# <-- Modul CSV -->
import csv

# <-- Class TiketBus -->
class TiketBus:
    def __init__(self, file_path="datatiketbus.csv"):
        self.file_path = file_path
        self.data = self.unggah_data()

    # <-- Fungsi untuk mengunggah data dari file CSV -->
    def unggah_data(self):
        data = []
        try: 
            with open(self.file_path, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row: 
                        data.append(Tiket(row[0], row[1], row[2], row[3], int(row[4]), row[5]))
        except FileNotFoundError:
            print("File tidak ditemukan")
            with open(self.file_path, "w") as file:
                pass
        return data

    # <-- Fungsi untuk menyimpan data ke file CSV -->
    def simpan_data(self):
        with open(self.file_path, "w", newline="") as file:
            writer = csv.writer(file)
            for tiket in self.data:
                writer.writerow([tiket.nama, tiket.asal, tiket.tujuan, tiket.tanggal, tiket.jumlah_kursi, tiket.kelas])

    # <-- Fungsi untuk mengecek kursi yang tersedia -->
    def kursi_tersedia(self, asal, tujuan, kelas, tanggal=""):
        bisnis = 36
        eksekutif = 26
        for tiket in self.data:
            if tiket.kelas.lower() == "bisnis" and tiket.asal.lower() == asal.lower() and tiket.tujuan.lower() == tujuan.lower() and tiket.tanggal == tanggal.lower():
                bisnis -= tiket.jumlah_kursi
            elif tiket.kelas.lower() == "eksekutif" and tiket.asal.lower() == asal.lower() and tiket.tujuan.lower() == tujuan.lower() and tiket.tanggal == tanggal.lower():
                eksekutif -= tiket.jumlah_kursi
        return bisnis if kelas.lower() == "bisnis" else eksekutif

    # <-- Fungsi untuk menghitung harga tiket -->
    def harga_tiket(self, asal, tujuan, jumlah_kursi, kelas):
        if (kelas == "Bisnis" or "bisnis") and (asal == "Jakarta" or "jakarta") and (tujuan == "Lampung" or "lampung"):
            return 200000 * jumlah_kursi
        elif (kelas == "Eksekutif" or "eksekutif") and (asal == "Jakarta" or "jakarta") and (tujuan == "Lampung" or "lampung"):
            return 300000 * jumlah_kursi
        elif (kelas == "Bisnis" or "bisnis") and (asal == "Lampung" or "lampung") and (tujuan == "Jakarta" or "jakarta"):
            return 200000 * jumlah_kursi
        elif (kelas == "Eksekutif" or "eksekutif") and (asal == "Lampung" or "lampung") and (tujuan == "Jakarta" or "jakarta"):
            return 300000 * jumlah_kursi
        elif (kelas == "Bisnis" or "bisnis") and (asal == "Jakarta" or "jakarta") and (tujuan == "Bandung" or "bandung"):
            return 80000 * jumlah_kursi
        elif (kelas == "Bisnis" or "bisnis") and (asal == "Bandung" or "bandung") and (tujuan == "Jakarta" or "jakarta"):
            return 80000 * jumlah_kursi
        elif (kelas == "Eksekutif" or "eksekutif") and (asal == "Jakarta" or "jakarta") and (tujuan == "Bandung" or "bandung"):
            return 100000 * jumlah_kursi
        elif (kelas == "Eksekutif" or "eksekutif") and (asal == "Bandung" or "bandung") and (tujuan == "Jakarta" or "jakarta"):
            return 100000 * jumlah_kursi
        elif (kelas == "Bisnis" or "bisnis") and (asal == "Bandung" or "bandung") and (tujuan == "Lampung" or "lampung"):
            return 250000 * jumlah_kursi
        elif (kelas == "Bisnis" or "bisnis") and (asal == "Lampung" or "lampung") and (tujuan == "Bandung" or "bandung"):
            return 250000 * jumlah_kursi
        elif (kelas == "Eksekutif" or "eksekutif") and (asal == "Bandung" or "bandung") and (tujuan == "Lampung" or "lampung"):
            return 350000 * jumlah_kursi
        elif (kelas == "Eksekutif" or "eksekutif") and (asal == "Lampung" or "lampung") and (tujuan == "Bandung" or "bandung"):
            return 350000 * jumlah_kursi
        elif (kelas == "Eksekutif" or "eksekutif") and (asal == "Yogyakarta" or "yogyakarta") and (tujuan == "Jakarta" or "jakarta"):
            return 300000 * jumlah_kursi
        elif (kelas == "Eksekutif" or "eksekutif") and (asal == "Jakarta" or "jakarta") and (tujuan == "Yogyakarta" or "yogyakarta"):
            return 300000 * jumlah_kursi
        elif (kelas == "Eksekutif" or "eksekutif") and (asal == "Yogyakarta" or "yogyakarta") and (tujuan == "Lampung" or "lampung"):
            return 400000 * jumlah_kursi
        elif (kelas == "Eksekutif" or "eksekutif") and (asal == "Lampung" or "lampung") and (tujuan == "Yogyakarta" or "yogyakarta"):
            return 400000 * jumlah_kursi
        elif (kelas == "Eksekutif" or "eksekutif") and (asal == "Yogyakarta" or "yogyakarta") and (tujuan == "Bandung" or "bandung"):
            return 250000 * jumlah_kursi
        elif (kelas == "Eksekutif" or "eksekutif") and (asal == "Bandung" or "bandung") and (tujuan == "Yogyakarta" or "yogyakarta"):
            return 250000 * jumlah_kursi
        elif (kelas == "Bisnis" or "bisnis") and (asal == "Yogyakarta" or "yogyakarta") and (tujuan == "Jakarta" or "jakarta"):
            return 250000 * jumlah_kursi
        elif (kelas == "Bisnis" or "bisnis") and (asal == "Jakarta" or "jakarta") and (tujuan == "Yogyakarta" or "yogyakarta"):
            return 250000 * jumlah_kursi
        elif (kelas == "Bisnis" or "bisnis") and (asal == "Yogyakarta" or "yogyakarta") and (tujuan == "Lampung" or "lampung"):
            return 350000 * jumlah_kursi
        elif (kelas == "Bisnis" or "bisnis") and (asal == "Lampung" or "lampung") and (tujuan == "Yogyakarta" or "yogyakarta"):
            return 350000 * jumlah_kursi
        elif (kelas == "Bisnis" or "bisnis") and (asal == "Yogyakarta" or "yogyakarta") and (tujuan == "Bandung" or "bandung"):
            return 200000 * jumlah_kursi
        elif (kelas == "Bisnis" or "bisnis") and (asal == "Bandung" or "bandung") and (tujuan == "Yogyakarta" or "yogyakarta"):
            return 200000 * jumlah_kursi
        else:
            return 0
    
    # <-- Fungsi untuk menambah data -->
    def tambah_data(self, nama, asal, tujuan, tanggal, jumlah_kursi, kelas):
        self.data.append(Tiket(nama, asal, tujuan, tanggal, int(jumlah_kursi), kelas))
        self.simpan_data()
        return self.harga_tiket(asal, tujuan, int(jumlah_kursi), kelas)

    # <-- Fungsi untuk menghapus data -->
    def hapus_data(self, nama):
        initial_length = len(self.data)
        self.data = [tiket for tiket in self.data if tiket.nama != nama]
        self.simpan_data()
        return initial_length != len(self.data)

    # <-- Fungsi untuk mengupdate data -->
    def update_data(self, nama, asal, tujuan, tanggal, jumlah_kursi, kelas):
        for tiket in self.data:
            if tiket.nama == nama:
                tiket.asal = asal
                tiket.tujuan = tujuan
                tiket.tanggal = tanggal
                tiket.jumlah_kursi = int(jumlah_kursi)
                tiket.kelas = kelas
                self.simpan_data()
                return True
        return False

    # <-- Fungsi untuk melihat data -->
    def lihat_data(self):
        for tiket in self.data:
            harga = self.harga_tiket(tiket.asal, tiket.tujuan, tiket.jumlah_kursi, tiket.kelas)
            kursi_tersedia = self.kursi_tersedia(tiket.asal, tiket.tujuan, tiket.kelas, tiket.tanggal)
            print(f"{tiket} - Harga: {harga} - Kursi Tersedia: {kursi_tersedia}")
        return self.data 

    # <-- Fungsi untuk mencari data dengan binary search -->
    def binary_search_by_id(self, nama, lihat_data=False):
        self.data.sort(key=lambda x: x.nama.lower())
        low, high = 0, len(self.data) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.data[mid].nama.lower() == nama.lower():
                return self.data[mid]
            elif self.data[mid].nama.lower() < nama.lower():
                low = mid + 1
            else:
                high = mid - 1
        return None + self.lihat_data() if lihat_data else None

    # <-- Fungsi untuk mengurutkan data menggunakan quick sort -->
    def quick_sort_by(data):
        if len(data) <= 1:
            return data
        else:
            pivot = data[0]
            less = [tiket for tiket in data[1:] if tiket.nama.lower() <= pivot.nama.lower()]
            high = [tiket for tiket in data[1:] if tiket.nama.lower() > pivot.nama.lower()]
            return TiketBus.quick_sort_by(less) + [pivot] + TiketBus.quick_sort_by(high)

class Tiket:
    def __init__(self, nama, asal, tujuan, tanggal, jumlah_kursi, kelas):
        self.nama = nama
        self.asal = asal
        self.tujuan = tujuan
        self.tanggal = tanggal
        self.jumlah_kursi = jumlah_kursi
        self.kelas = kelas

    def __str__(self):
        return f"{self.nama} : {self.asal} ke {self.tujuan} pada {self.tanggal} ({self.jumlah_kursi} kursi, {self.kelas})"

def tampilkan_menu():
    print("\n === Aplikasi Pemesanan Tiket Bus ===")
    print("1. Tambah Pemesanan")
    print("2. Lihat Pemesanan")
    print("3. Update Pemesanan")
    print("4. Hapus Pemesanan")
    print("5. Sortir Pemesanan")
    print("6. Cari Pemesanan")
    print("7. Keluar")

# <-- Fungsi main -->
def main():
    tiket_bus = TiketBus()

    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            nama = input("Masukkan Nama: ")
            print("Asal: Jakarta, Lampung, Bandung, Yogyakarta")
            asal = input("Pilih Asal: ")
            if asal == 'Jakarta' or 'jakarta':
                print("Tujuan: Lampung, Bandung")
            elif asal == 'Lampung' or 'lampung':
                print("Tujuan: Jakarta, Bandung")
            elif asal == 'Bandung' or 'bandung':
                print("Tujuan: Jakarta, Lampung")
            elif asal == 'Yogyakarta' or 'yogyakarta':
                print("Tujuan: Jakarta, Lampung, Bandung")
            tujuan = input("Pilih Tujuan: ")
            tanggal = input("Masukkan Tanggal: ")
            jumlah_kursi = input("Masukkan Jumlah Kursi: ")
            kelas = input("Masukkan Kelas: ")
            total_harga = tiket_bus.tambah_data(nama, asal, tujuan, tanggal, jumlah_kursi, kelas)
            print(f"Total harga: {total_harga}")
        elif pilihan == '2':
            tiket_bus.lihat_data()
        elif pilihan == '3':
            print("")
            nama = input("Masukkan Nama: ")
            asal = input("Masukkan Asal: ")
            tujuan = input("Masukkan Tujuan: ")
            tanggal = input("Masukkan Tanggal: ")
            jumlah_kursi = input("Masukkan Jumlah Kursi: ")
            kelas = input("Masukkan Kelas: ")
            if tiket_bus.update_data(nama, asal, tujuan, tanggal, jumlah_kursi, kelas):
                print("Data berhasil diupdate")
            else:
                print("Data tidak ditemukan")
        elif pilihan == '4':
            nama = input("Masukkan Nama yang akan dihapus: ")
            if tiket_bus.hapus_data(nama):
                print("Data berhasil dihapus")
            else:
                print("Data tidak ditemukan")
        elif pilihan == '5':
            tiket_bus.data = TiketBus.quick_sort_by(tiket_bus.data)
            print("Data telah diurutkan")
        elif pilihan == '6':
            nama = input("Masukkan Nama yang akan dicari: ")
            hasil = tiket_bus.binary_search_by_id(nama)
            if hasil:
                print("Data ditemukan:")
                print(hasil)
            else:
                print("Data tidak ditemukan")
        elif pilihan == '7':
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

main()
