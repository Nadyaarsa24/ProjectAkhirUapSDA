import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import *
import csv

# Nama file CSV
CSV_FILE = 'datatiketbus.csv'

class Tiket:
    def __init__(self, root):
        # <----------------- Inisialisasi variabel ----------------->
        self.root = root
        self.root.title("Aplikasi Pemesanan Tiket")
        self.root.geometry("1540x900+0+0")

        # <----------------- Label untuk judul aplikasi ----------------->
        lbtitle = Label(self.root, text="Aplikasi Pemesanan Tiket Bus Sugeng Rahayu", bd=10, relief=GROOVE, font=("times new roman", 25, "bold"), bg="white", fg="red")
        lbtitle.pack(side=TOP, fill=X)

        # <----------------- Frame untuk data pemesan ----------------->
        DataFrame = Frame(self.root, bd=10, relief=RIDGE, padx=20, bg="light grey")
        DataFrame.place(x=0, y=50, width=1525, height=400)

        DataFrameLeft = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, bg="white", text="Data Pemesan", font=("times new roman", 20, "bold"))
        DataFrameLeft.place(x=0, y=5, width=600, height=300)

        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, pady=10, bg="white", text="Invoice", font=("times new roman", 20, "bold"))
        DataFrameRight.place(x=850, y=5, width=600, height=300)

        # <----------------- Label untuk menampilkan listbox ----------------->
        DataFrameDown = tk.Frame(self.root, bd=10, relief=RIDGE, padx=20, bg="light grey")
        DataFrameDown.place(x=0, y=400, width=1525, height=300)

        # <----------------- Kolom Tabel CSV ----------------->
        columns = ("Nama", "Asal", "Tujuan", "Tanggal", "Jumlah Kursi", "Kelas", "Harga", "Sisa Kursi")
        self.tree = ttk.Treeview(DataFrameDown, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(fill=tk.BOTH, expand=1)
        
        skroll_bar = tk.Scrollbar(DataFrameDown, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=skroll_bar.set)
        skroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # <----------------- Label, Entry dan Dropdown ----------------->

        # <----------------- Label dan entry untuk entry nama ----------------->
        self.nama_label = Label(DataFrameLeft, text="Nama", font=("times new roman", 10, "bold"), bg="light grey")
        self.nama_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.nama_entry = Entry(DataFrameLeft, font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        self.nama_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # <----------------- Label dan Entry untuk Asal ----------------->
        self.asal_label = Label(DataFrameLeft, text="Asal", font=("times new roman", 10, "bold"), bg="light grey")
        self.asal_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.asal_entry = ttk.Combobox(DataFrameLeft, font=("times new roman", 10, "bold"), state='readonly')
        self.asal_entry['values'] = ["Lampung", "Jakarta", "Bandung", "Jogja"]
        self.asal_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.asal_entry.bind("<<ComboboxSelected>>", self.set_destination)

        # <----------------- Label dan Entry untuk Tujuan ----------------->
        self.destination_label = Label(DataFrameLeft, text="Tujuan", font=("times new roman", 10, "bold"), bg="light grey")
        self.destination_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.destination_entry = ttk.Combobox(DataFrameLeft, font=("times new roman", 10, "bold"), state='readonly')
        self.destination_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # <----------------- Label dan Entry untuk Tanggal ----------------->
        self.tanggal_label = Label(DataFrameLeft, text="Tanggal Keberangkatan", font=("times new roman", 10, "bold"), bg="light grey")
        self.tanggal_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.tanggal_entry = Entry(DataFrameLeft, font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        self.tanggal_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # <----------------- Label dan Dropdwon untuk Kelas ----------------->
        self.kelas_label = Label(DataFrameLeft, text="Kelas", font=("times new roman", 10, "bold"), bg="light grey")
        self.kelas_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.kelas_entry = ttk.Combobox(DataFrameLeft, font=("times new roman", 10, "bold"), state='readonly')
        self.kelas_entry['values'] = ["Bisnis", "Eksekutif"]
        self.kelas_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        self.kelas_entry.bind("<<ComboboxSelected>>", self.set_kursi)

        # <----------------- Label dan Dropdown untuk Jumlah Kursi ----------------->
        self.jumlah_kursi_label = Label(DataFrameLeft, text="Jumlah Kursi", font=("times new roman", 10, "bold"), bg="light grey")
        self.jumlah_kursi_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.jumlah_kursi_entry = ttk.Combobox(DataFrameLeft, font=("times new roman", 10, "bold"), state='readonly')
        self.jumlah_kursi_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        # <----------------- Label dan Dropdown untuk Pengurutan ----------------->
        self.sort_label = Label(DataFrameLeft, text="Urutkan berdasarkan", font=("times new roman", 10, "bold"), bg="light grey")
        self.sort_label.grid(row=9, column=0, padx=10, pady=5, sticky="w")
        self.sort_by_entry = ttk.Combobox(DataFrameLeft, font=("times new roman", 10, "bold"), state='readonly')
        self.sort_by_entry.bind("<<ComboboxSelected>>", self.sort_data)
        self.sort_by_entry['values'] = ["Nama", "Asal", "Tujuan", "Tanggal", "Jumlah Kursi", "Kelas"]
        self.sort_by_entry.grid(row=9, column=1, padx=10, pady=5, sticky="w")
        self.sort_by = StringVar()

        # <---------- Label dan Entry untuk Pencarian Data ------------>
        self.search_label = Label(DataFrameLeft, text="Cari Data", font=("times new roman", 10, "bold"), bg="light grey")
        self.search_label.grid(row=10, column=0, padx=10, pady=5, sticky="w")
        self.search_entry = Entry(DataFrameLeft, font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        self.search_entry.grid(row=10, column=1, padx=10, pady=5, sticky="w")

        # <------------ Label untuk keluaran harga tiket ------------>
        self.harga_label = Label(DataFrameRight, text="Harga Tiket", font=("times new roman", 10, "bold"), bg="light grey")
        self.harga_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")

        # <------------- Label untuk invoice ----------------->
        self.nama_Label = Label(DataFrameRight, text="Nama", font=("times new roman", 10, "bold"), bg="light grey")
        self.nama_Label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.asal_Label = Label(DataFrameRight, text="Asal", font=("times new roman", 10, "bold"), bg="light grey")
        self.asal_Label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.tujuan_Label = Label(DataFrameRight, text="Tujuan", font=("times new roman", 10, "bold"), bg="light grey")
        self.tujuan_Label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.tanggal_Label = Label(DataFrameRight, text="Tanggal", font=("times new roman", 10, "bold"), bg="light grey")
        self.tanggal_Label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.jumlah_kursi_Label = Label(DataFrameRight, text="Jumlah Kursi", font=("times new roman", 10, "bold"), bg="light grey")
        self.jumlah_kursi_Label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.kelas_Label = Label(DataFrameRight, text="Kelas", font=("times new roman", 10, "bold"), bg="light grey")
        self.kelas_Label.grid(row=6, column=0, padx=10, pady=5, sticky="w")


        # <----------------- Tombol untuk menginput data ----------------->

        btnFrame = Frame(self.root, bd=10, relief=RIDGE, padx=20, bg="white")
        btnFrame.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

        self.save_btn = Button(btnFrame, text="Simpan", command=self.save_data, font=("times new roman", 15, "bold"), bg="green", fg="white")
        self.save_btn.grid(row=2, column=0, padx=15, pady=15)
        self.update_btn = Button(btnFrame, text="Update Data", command=self.update_data, font=("times new roman", 15, "bold"), bg="orange", fg="white")
        self.update_btn.grid(row=2, column=1, padx=10, pady=10)
        self.clear_btn = Button(btnFrame, text="Hapus Data", command=self.clear_data, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        self.clear_btn.grid(row=2, column=2, padx=10, pady=10)
        self.tampil_btn = Button(btnFrame, text="Tampilkan Data", command=self.load_data, font=("times new roman", 15, "bold"), bg="yellow", fg="black")
        self.tampil_btn.grid(row=2, column=3, padx=10, pady=10)
        self.sort_btn = Button(btnFrame, text="Urutkan Data", command=self.sort_data, font=("times new roman", 15, "bold"), bg="purple", fg="white")
        self.sort_btn.grid(row=2, column=4, padx=10, pady=10)
        self.search_btn = Button(btnFrame, text="Cari Data", command=self.search_data, font=("times new roman", 15, "bold"), bg="brown", fg="white")
        self.search_btn.grid(row=2, column=6, padx=10, pady=10)
        self.exit_btn = Button(btnFrame, text="Keluar", command=root.quit, font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.exit_btn.grid(row=2, column=5, padx=10, pady=10)

        self.load_data()

    # <------------ Fungsi untuk menentukan tujuan berdasarkan asal ------------>
    def set_destination(self, event):
        asal = self.asal_entry.get()
        destination = ["Lampung", "Jakarta", "Bandung", "Jogja"]

        if asal in destination:
            destination.remove(asal)
        self.destination_entry['values'] = destination
        if destination:
            self.destination_entry.set(destination[0])
    
    # <-------------- Fungsi untuk memilih kursi berdasarkan kelas ---------------->
    def set_kursi(self, event):
        kelas = self.kelas_entry.get()
        if kelas == "Bisnis":
            self.jumlah_kursi_entry['values'] = [i for i in range(1, 37)]  # 36 seats
        elif kelas == "Eksekutif":
            self.jumlah_kursi_entry['values'] = [i for i in range(1, 27)]  # 26 seats
        else:
            self.jumlah_kursi_entry['values'] = []
        self.jumlah_kursi_entry.set('')

    # <-------------- Fungsi untuk melihat sisa kursi yang tersedia ---------------->

    def sisa_kursi(self, asal, tujuan, kelas, tanggal):
        selected = self.tree.selection()
        bisnis = 36
        eksekutif = 26
        with open(CSV_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == asal and row[2] == tujuan and row[5] == kelas and row[3] == tanggal:
                    if kelas == "Bisnis":
                        bisnis -= int(row[4])
                    elif kelas == "Eksekutif":
                        eksekutif -= int(row[4])
        return bisnis if kelas == "Bisnis" else eksekutif

    # <---------------- Fungsi untuk membaca data CSV ------------------------>
    def load_data(self):
        self.tree.delete(*self.tree.get_children())
        try:
            with open(CSV_FILE, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    row = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], self.sisa_kursi(row[1], row[2], row[5], row[3])]
                    self.tree.insert('', 'end', values=row)
        except FileNotFoundError:
            with open(CSV_FILE, 'w') as file:
                pass

    # <--------------------- Fungsi untuk menampilkan data yang sudah disimpan ------------------------>
    def tampilkan_data(self):
        with open(CSV_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    # <---------------------- Fungsi untuk menyimpan data ------------------------>
    def save_data(self):
        nama = self.nama_entry.get()
        asal = self.asal_entry.get()
        tujuan = self.destination_entry.get()
        tanggal = self.tanggal_entry.get()
        jumlah_kursi = self.jumlah_kursi_entry.get()
        kelas = self.kelas_entry.get()
        harga = self.hitung_harga_tiket(asal, tujuan, kelas, int(jumlah_kursi))
        sisa_kursi = self.sisa_kursi(asal, tujuan, kelas, tanggal)
        if nama == "" or asal == "" or tujuan == "" or tanggal == "" or jumlah_kursi == "" or kelas == "":
            messagebox.showerror("Error", "Semua kolom harus diisi")
        else:
            if int(sisa_kursi) == 0:
                messagebox.showinfo("Alert", "Kursi sudah penuh")
                return
            with open(CSV_FILE, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([nama, asal, tujuan, tanggal, jumlah_kursi, kelas, harga])
            messagebox.showinfo("Berhasil", "Data berhasil disimpan")
            self.load_data()
            self.clear_entries()
            self.nama_Label.config(text=f"Nama: {nama}")
            self.asal_Label.config(text=f"Asal: {asal}")
            self.tujuan_Label.config(text=f"Tujuan: {tujuan}")
            self.tanggal_Label.config(text=f"Tanggal: {tanggal}")
            self.jumlah_kursi_Label.config(text=f"Jumlah Kursi: {jumlah_kursi}")
            self.kelas_Label.config(text=f"Kelas: {kelas}")
            self.harga_label.config(text=f"Harga Tiket: Rp {harga}")
            self.sisa_kursi.config(text=f"Sisa Kursi: {sisa_kursi}")

    # <--------------------- Fungsi untuk menghapus data ------------------------>
    def clear_data(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            with open(CSV_FILE, mode='r') as file:
                reader = list(csv.reader(file))
            reader.pop(index)
            with open(CSV_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(reader)
            self.load_data()
        else:
            messagebox.showwarning("Selection Error", "Pilih item yang ingin dihapus")

    # <------------------------ Fungsi untuk mengupdate data ------------------------>
    def update_data(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Pilih data yang ingin diupdate")
            return
        data = [self.nama_entry.get(), self.asal_entry.get(), 
                self.destination_entry.get(), self.tanggal_entry.get(), 
                self.jumlah_kursi_entry.get(), self.kelas_entry.get(), 
                self.hitung_harga_tiket(self.asal_entry.get(), 
                self.destination_entry.get(), self.kelas_entry.get(), 
                int(self.jumlah_kursi_entry.get()))]
        if '' in data:
            messagebox.showerror("Error", "Semua kolom harus diisi")
            return
        try:
            with open(CSV_FILE, newline='') as file:
                reader = list(csv.reader(file))
            selected_index = self.tree.index(selected_item[0])
            reader[selected_index] = data
            with open(CSV_FILE, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(reader)
            self.load_data()
            messagebox.showinfo("Sukses", "Data berhasil diupdate")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan saat mengupdate data: {e}")

    # <------------------------- Fungsi untuk menghitung harga tiket bus ------------------------>
    def hitung_harga_tiket(self, asal, tujuan, kelas, jumlah_kursi):
        prices = {
            ("Lampung", "Jakarta", "Bisnis"): 200000,
            ("Lampung", "Jakarta", "Eksekutif"): 300000,
            ("Lampung", "Bandung", "Bisnis"): 250000,
            ("Lampung", "Bandung", "Eksekutif"): 350000,
            ("Lampung", "Jogja", "Bisnis"): 150000,
            ("Lampung", "Jogja", "Eksekutif"): 250000,
            ("Jakarta", "Lampung", "Bisnis"): 200000,
            ("Jakarta", "Lampung", "Eksekutif"): 300000,
            ("Jakarta", "Bandung", "Bisnis"): 80000,
            ("Jakarta", "Bandung", "Eksekutif"): 100000,
            ("Jakarta", "Jogja", "Bisnis"): 300000,
            ("Jakarta", "Jogja", "Eksekutif"): 350000,
            ("Bandung", "Lampung", "Bisnis"): 250000,
            ("Bandung", "Lampung", "Eksekutif"): 300000,
            ("Bandung", "Jakarta", "Bisnis"): 80000,
            ("Bandung", "Jakarta", "Eksekutif"): 100000,
            ("Bandung", "Jogja", "Bisnis"): 150000,
            ("Bandung", "Jogja", "Eksekutif"): 200000,
            ("Jogja", "Lampung", "Bisnis"): 400000,
            ("Jogja", "Lampung", "Eksekutif"): 450000,
            ("Jogja", "Jakarta", "Bisnis"): 300000,
            ("Jogja", "Jakarta", "Eksekutif"): 350000,
            ("Jogja", "Bandung", "Bisnis"): 200000,
            ("Jogja", "Bandung", "Eksekutif"): 250000,
        }

        harga = prices.get((asal, tujuan, kelas), 0) * jumlah_kursi
        return harga

    # <------------------- Fungsi untuk mengosongkan entry ------------------->
    def clear_entries(self):
        self.nama_entry.delete(0, END)
        self.asal_entry.set('')
        self.destination_entry.set('')
        self.tanggal_entry.delete(0, END)
        self.jumlah_kursi_entry.set('')
        self.kelas_entry.set('')

    # <-------------------- Fungsi untuk menangani pemilihan item di Treeview dan menampilkan data di entry --------------------->
    def on_tree_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            row = item['values']
            self.nama_entry.delete(0, END)
            self.nama_entry.insert(0, row[0])
            self.asal_entry.set(row[1])
            self.destination_entry.set(row[2])
            self.tanggal_entry.delete(0, END)
            self.tanggal_entry.insert(0, row[3])
            self.jumlah_kursi_entry.set(row[4])
            self.kelas_entry.set(row[5])
            self.harga_label.config(text=f"Harga Tiket: Rp {row[6]}")
            self.sisa_kursi.config(text=f"Sisa Kursi: {self.sisa_kursi(row[1], row[2], row[5])}")


    # <------------------ Fungsi untuk mengurutkan data berdasarkan kolom ------------------->
    def sort_data(self, event=None):
        sort_by = self.sort_by_entry.get()
        if sort_by:
            col_index = ["Nama", "Asal", "Tujuan", "Tanggal", "Jumlah Kursi", "Kelas"].index(sort_by)
            data = [(self.tree.set(child, sort_by), child) for child in self.tree.get_children('')]
            data.sort(reverse=False)
            for index, (val, child) in enumerate(data):
                self.tree.move(child, '', index)
        else:
            messagebox.showwarning("Sort Error", "Pilih kolom yang ingin diurutkan")

    # <------------------- Fungsi untuk mencari data berdasarkan Nama ------------------->
    def search_data(self):
        search_value = self.search_entry.get().lower()
        if not search_value:
            messagebox.showwarning("Search Error", "Please enter a search value")
            return
        self.sort_treeview()
        items = list(self.tree.get_children())
        left, right = 0, len(items) - 1
        while left <= right:
            mid = (left + right) // 2
            item = items[mid]
            item_value = self.tree.item(item)["values"][0].lower()
            if item_value == search_value:
                self.tree.selection_set(item)
                self.tree.focus(item)
                self.tree.see(item)
                return
            elif item_value < search_value:
                left = mid + 1
            else:
                right = mid - 1
        messagebox.showwarning("Search Error", "Data not found")

    def sort_treeview(self):
        items = [(self.tree.item(child)["values"][0].lower(), child) for child in self.tree.get_children('')]
        items.sort()
        for index, (val, child) in enumerate(items):
            self.tree.move(child, '', index)

# <--- Main Program --->
if __name__ == "__main__":
    root = tk.Tk()
    app = Tiket(root)
    root.mainloop()
