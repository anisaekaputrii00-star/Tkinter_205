import tkinter as tk
import tkinter.messagebox as mg

# 1. Membuat Jendela Utama (GUI)
top = tk.Tk()
top.title("Aplikasi Prediksi Prodi Pilihan")
top.geometry("350x550")

# 2. Label Judul Aplikasi
L_judul = tk.Label(top, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 12, "bold"))
L_judul.pack(pady=10)

# 3. 10 Input Nilai Mata Pelajaran (Menggunakan Label sesuai contoh Anda)
L1 = tk.Label(top, text="Nilai Matematika: 85")
L1.pack()
L2 = tk.Label(top, text="Nilai Bahasa Indonesia: 90")
L2.pack()
L3 = tk.Label(top, text="Nilai Bahasa Inggris: 88")
L3.pack()
L4 = tk.Label(top, text="Nilai Fisika: 82")
L4.pack()
L5 = tk.Label(top, text="Nilai Kimia: 80")
L5.pack()
L6 = tk.Label(top, text="Nilai Biologi: 85")
L6.pack()
L7 = tk.Label(top, text="Nilai Sejarah: 87")
L7.pack()
L8 = tk.Label(top, text="Nilai Geografi: 84")
L8.pack()
L9 = tk.Label(top, text="Nilai Ekonomi: 86")
L9.pack()
L10 = tk.Label(top, text="Nilai Sosiologi: 88")
L10.pack()

# 5. Label Luaran Hasil Prediksi (Awalnya kosong)
L_hasil = tk.Label(top, text="", font=("Arial", 11, "bold"), fg="blue")

# Fungsi untuk tombol ketika diklik (Hasil Prediksi)
def helloCallBack():
    # Menuliskan prodi Teknologi Informasi pada label luaran sesuai soal
    L_hasil.config(text="Prodi Prediksi: Teknologi Informasi")
    
    # Menampilkan info box seperti gaya contoh kodingan Anda
    mg.showinfo("Hasil Prediksi", "Hasil Prediksi Anda: Teknologi Informasi")

# 4. Button bertuliskan "Hasil Prediksi"
w1 = tk.Button(top, text="Hasil Prediksi", command=helloCallBack)
w1.pack(pady=15)

# Meletakkan label luaran di bawah tombol
L_hasil.pack()

# Menjalankan Aplikasi
top.mainloop()