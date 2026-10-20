import tkinter as tk
import tkinter.messagebox as mg

top = tk.Tk()
top.title("Aplikasi Prediksi Prodi Pilihan")
top.geometry("350x550")

L_judul = tk.Label(top, text="Aplikasi Prediksi Prodi Pilihan", font=("Times New Roman", 12, "bold"))
L_judul.pack(pady=10)


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
L8 = tk.Label(top, text="Nilai Informatika: 84")
L8.pack()
L9 = tk.Label(top, text="Nilai Ekonomi: 86")
L9.pack()
L10 = tk.Label(top, text="Nilai Pamcasila: 88")
L10.pack()

L_hasil = tk.Label(top, text="", font=("Times New Roman", 12, "bold"), fg="black")

def helloCallBack():
   
    L_hasil.config(text="Prodi Prediksi: Teknologi Informasi")
    mg.showinfo("Hasil Prediksi", "Hasil Prediksi Anda: Teknologi Informasi")


w1 = tk.Button(top, text="Hasil Prediksi", command=helloCallBack)
w1.pack(pady=15)

L_hasil.pack()
top.mainloop()