import streamlit as st
import matplotlib.pyplot as plt

# -------------------------------
# Konfigurasi halaman
# -------------------------------
st.set_page_config(page_title="Kalkulator Bunga Efektif & Nominal", page_icon="💰", layout="centered")
st.title("💰 Kalkulator Bunga Efektif & Nominal")
st.markdown("### 📊 Simulasi Pertumbuhan Modal dan Analisis Hasil")
st.markdown("---")

# -------------------------------
# Input Pengguna
# -------------------------------
col1, col2 = st.columns(2)
with col1:
    modal_awal = st.number_input("💵 Modal Awal (Rp)", min_value=0.0, value=1000000.0, step=100000.0)
    bunga_nominal = st.number_input("📈 Bunga Nominal (% per tahun)", min_value=0.0, value=10.0, step=0.1)
with col2:
    frekuensi = st.selectbox("🔁 Frekuensi Kapitalisasi", ["Tahunan (1x)", "Semester (2x)", "Kuartalan (4x)", "Bulanan (12x)"])
    tahun_simulasi = st.slider("⏳ Lama Investasi (tahun)", 1, 30, 10)

# -------------------------------
# Hitung Bunga Efektif & Hasil Akhir
# -------------------------------
frekuensi_dict = {
    "Tahunan (1x)": 1,
    "Semester (2x)": 2,
    "Kuartalan (4x)": 4,
    "Bulanan (12x)": 12
}

m = frekuensi_dict[frekuensi]
i_nom = bunga_nominal / 100
i_eff = (1 + i_nom/m)**m - 1
nilai_akhir = modal_awal * (1 + i_eff)**tahun_simulasi

# -------------------------------
# Tampilkan Hasil
# -------------------------------
st.markdown("### 🧮 Hasil Perhitungan")
col3, col4 = st.columns(2)
with col3:
    st.metric(label="Bunga Efektif per Tahun", value=f"{i_eff*100:.2f}%")
with col4:
    st.metric(label=f"Total Modal setelah {tahun_simulasi} tahun", value=f"Rp {nilai_akhir:,.2f}")

# -------------------------------
# Analisis Otomatis
# -------------------------------
st.markdown("### 📈 Analisis Otomatis")
if i_eff < 0.05:
    analisis = "Tingkat bunga sangat rendah — pertumbuhan investasi lambat."
elif i_eff < 0.10:
    analisis = "Bunga tergolong sedang — cocok untuk simpanan konservatif."
elif i_eff < 0.20:
    analisis = "Bunga cukup tinggi — investasi memberikan pertumbuhan baik."
else:
    analisis = "Bunga sangat tinggi — pastikan risikonya dapat diterima."

st.info(analisis)

# -------------------------------
# Grafik Pertumbuhan Modal
# -------------------------------
tahun_range = list(range(1, tahun_simulasi + 1))
nilai_tahunan = [modal_awal * (1 + i_eff)**t for t in tahun_range]

fig, ax = plt.subplots()
ax.plot(tahun_range, nilai_tahunan, marker="o", linewidth=2)
ax.set_xlabel("Tahun")
ax.set_ylabel("Nilai Modal (Rp)")
ax.set_title("Grafik Pertumbuhan Modal")
st.pyplot(fig)

# -------------------------------
# Tombol Tutup Aplikasi
# -------------------------------
st.markdown("---")
if st.button("❌ Tutup Aplikasi"):
    st.warning("Aplikasi ditutup. Terima kasih telah menggunakan kalkulator ini!")

# -------------------------------
# Kredit
# -------------------------------
st.markdown("""
<hr>
<p style='text-align:center'>
<b>Kelompok Bunga</b><br>
Proyek Jurnal — Kalkulator Bunga Efektif & Nominal
</p>
""", unsafe_allow_html=True)
