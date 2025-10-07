import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt

# =====================================================
# === FUNGSI UTAMA ====================================
# =====================================================

def hitung_bunga_efektif():
    try:
        i_nom = float(entry_nominal.get()) / 100
        m = int(combo_m.get().split()[0])
        P = float(entry_modal.get())
        tahun = int(entry_tahun.get())

        # Rumus bunga efektif
        i_eff = (1 + i_nom / m) ** m - 1
        FV = P * (1 + i_eff) ** tahun
        bunga_total = FV - P

        hasil = (
            f"💡 Tingkat Bunga Efektif: {i_eff * 100:.4f}% per tahun\n"
            f"💰 Bunga Total ({tahun} tahun): Rp{bunga_total:,.2f}\n"
            f"📈 Nilai Akhir (FV): Rp{FV:,.2f}"
        )
        label_hasil.config(text=hasil)

        analisis = analisis_otomatis(i_eff, "efektif", tahun)
        label_analisis.config(text=analisis)

        tampilkan_grafik(P, i_eff, tahun, "efektif")

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan:\n{e}")

def hitung_bunga_nominal():
    try:
        i_eff = float(entry_efektif.get()) / 100
        m = int(combo_m.get().split()[0])
        P = float(entry_modal.get())
        tahun = int(entry_tahun.get())

        # Rumus bunga nominal
        i_nom = m * ((1 + i_eff) ** (1 / m) - 1)
        FV = P * (1 + i_eff) ** tahun
        bunga_total = FV - P

        hasil = (
            f"💡 Tingkat Bunga Nominal: {i_nom * 100:.4f}% per tahun\n"
            f"💰 Bunga Total ({tahun} tahun): Rp{bunga_total:,.2f}\n"
            f"📈 Nilai Akhir (FV): Rp{FV:,.2f}"
        )
        label_hasil.config(text=hasil)

        analisis = analisis_otomatis(i_nom, "nominal", tahun)
        label_analisis.config(text=analisis)

        tampilkan_grafik(P, i_eff, tahun, "nominal")

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan:\n{e}")

# =====================================================
# === FUNGSI TAMBAHAN =================================
# =====================================================

def tampilkan_grafik(P, i_eff, tahun_total, tipe):
    tahun = list(range(1, tahun_total + 1))
    FV_tahunan = [P * ((1 + i_eff) ** t) for t in tahun]

    plt.figure(figsize=(6, 4))
    plt.plot(tahun, FV_tahunan, marker='o', linewidth=2, color='#0D47A1')
    plt.title(f"📊 Pertumbuhan Modal ({tahun_total} Tahun) - Bunga {tipe.capitalize()}", fontsize=12)
    plt.xlabel("Tahun ke-")
    plt.ylabel("Nilai Modal (Rp)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def analisis_otomatis(i, tipe, tahun):
    persen = i * 100
    if persen < 5:
        kategori = "rendah"
    elif persen < 10:
        kategori = "sedang"
    else:
        kategori = "tinggi"

    if tahun <= 3:
        durasi = "jangka pendek"
    elif tahun <= 7:
        durasi = "menengah"
    else:
        durasi = "jangka panjang"

    if tipe == "efektif":
        return (f"📊 Analisis: Tingkat bunga efektif sebesar {persen:.2f}% termasuk kategori {kategori}.\n"
                f"Untuk investasi {durasi}, potensi keuntungan meningkat signifikan bila bunga efektif di atas 8%.")
    else:
        return (f"📊 Analisis: Bunga nominal {persen:.2f}% tergolong {kategori}. "
                f"Untuk periode {durasi}, nilai efektif riil akan memengaruhi hasil aktual investasi.")

def reset():
    entry_modal.delete(0, tk.END)
    entry_nominal.delete(0, tk.END)
    entry_efektif.delete(0, tk.END)
    entry_tahun.delete(0, tk.END)
    entry_tahun.insert(0, "5")
    combo_m.set("12 - Bulanan")
    label_hasil.config(text="")
    label_analisis.config(text="")

def info():
    messagebox.showinfo("Info", 
        "💰 Kalkulator ini membantu menghitung hubungan antara bunga nominal dan bunga efektif.\n\n"
        "Bunga Efektif → bunga sesungguhnya setelah kapitalisasi.\n"
        "Bunga Nominal → suku bunga tahunan dari bank.\n"
        "Hasil mencakup nilai akhir investasi dan grafik pertumbuhan modal berdasarkan lama investasi.")

def simpan_hasil():
    teks = label_hasil.cget("text") + "\n" + label_analisis.cget("text")
    if teks.strip():
        with open("hasil_kalkulator.txt", "a", encoding="utf-8") as f:
            f.write(teks + "\n\n")
        messagebox.showinfo("Berhasil", "✅ Hasil berhasil disimpan ke file 'hasil_kalkulator.txt'")
    else:
        messagebox.showwarning("Peringatan", "Tidak ada hasil untuk disimpan.")

def tutup_aplikasi():
    root.destroy()

# =====================================================
# === GUI DESAIN ======================================
# =====================================================
root = tk.Tk()
root.title("Kalkulator Bunga Efektif dan Nominal")
root.geometry("820x680")
root.configure(bg="#E3F2FD")

judul_font = ("Helvetica", 20, "bold")
label_font = ("Helvetica", 12)
entry_font = ("Helvetica", 12)

tk.Label(root, text="💰 Kalkulator Bunga Efektif & Nominal", font=judul_font, fg="#0D47A1", bg="#E3F2FD").pack(pady=20)

frame = tk.Frame(root, bg="#E3F2FD")
frame.pack(pady=5)

# === Input Fields ===
tk.Label(frame, text="Modal Awal (P)", font=label_font, bg="#E3F2FD").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_modal = tk.Entry(frame, font=entry_font, width=20)
entry_modal.grid(row=0, column=1)

tk.Label(frame, text="Bunga Nominal (%)", font=label_font, bg="#E3F2FD").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_nominal = tk.Entry(frame, font=entry_font, width=20)
entry_nominal.grid(row=1, column=1)

tk.Label(frame, text="Bunga Efektif (%)", font=label_font, bg="#E3F2FD").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_efektif = tk.Entry(frame, font=entry_font, width=20)
entry_efektif.grid(row=2, column=1)

tk.Label(frame, text="Frekuensi Kapitalisasi", font=label_font, bg="#E3F2FD").grid(row=3, column=0, padx=10, pady=5, sticky="e")
combo_m = ttk.Combobox(frame,
                       values=["1 - Tahunan", "2 - Semesteran", "4 - Triwulanan", "12 - Bulanan", "365 - Harian"],
                       width=18, font=entry_font)
combo_m.set("12 - Bulanan")
combo_m.grid(row=3, column=1)

tk.Label(frame, text="Lama Investasi (tahun)", font=label_font, bg="#E3F2FD").grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry_tahun = tk.Entry(frame, font=entry_font, width=20)
entry_tahun.grid(row=4, column=1)
entry_tahun.insert(0, "5")

# === Tombol ===
btn_frame = tk.Frame(root, bg="#E3F2FD")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Hitung Efektif", font=("Helvetica", 11, "bold"),
          bg="#4CAF50", fg="white", width=14, command=hitung_bunga_efektif).grid(row=0, column=0, padx=10)

tk.Button(btn_frame, text="Hitung Nominal", font=("Helvetica", 11, "bold"),
          bg="#2196F3", fg="white", width=14, command=hitung_bunga_nominal).grid(row=0, column=1, padx=10)

tk.Button(root, text="Reset", font=("Helvetica", 11, "bold"),
          bg="#f44336", fg="white", width=12, command=reset).pack(pady=5)

tk.Button(root, text="ℹ Info", font=("Helvetica", 11, "bold"),
          bg="#FFC107", fg="black", width=12, command=info).pack(pady=3)

tk.Button(root, text="Simpan Hasil", font=("Helvetica", 11, "bold"),
          bg="#795548", fg="white", width=14, command=simpan_hasil).pack(pady=5)

tk.Button(root, text="🚪 Tutup Aplikasi", font=("Helvetica", 11, "bold"),
          bg="#9E9E9E", fg="white", width=15, command=tutup_aplikasi).pack(pady=8)

# === Label Hasil ===
frame_hasil = tk.Frame(root, bg="#BBDEFB", bd=2, relief="groove")
frame_hasil.pack(pady=15, padx=20, fill="x")
label_hasil = tk.Label(frame_hasil, text="", font=("Helvetica", 12, "bold"),
                       fg="#0D47A1", bg="#BBDEFB", wraplength=760, justify="center")
label_hasil.pack(pady=10)

# === Analisis Otomatis ===
label_analisis = tk.Label(root, text="", font=("Helvetica", 11, "italic"),
                          fg="#0D47A1", bg="#E3F2FD", wraplength=760, justify="center")
label_analisis.pack(pady=5)

# === Footer ===
tk.Label(root, text="Kelompok Bunga 🌸 | Aplikasi Proyek Matematika Keuangan", 
         font=("Helvetica", 11, "italic"), bg="#E3F2FD", fg="#555").pack(side="bottom", pady=10)

root.mainloop()
