import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# =====================================================
# === JUDUL & DESAIN DASAR ============================
# =====================================================
st.set_page_config(page_title="Kalkulator Bunga Efektif & Nominal 💰", layout="centered")
st.title("💰 Kalkulator Bunga Efektif & Nominal")
st.markdown("---")

# =====================================================
# === INPUT PENGGUNA ==================================
# =====================================================
col1, col2 = st.columns(2)
with col1:
    P = st.number_input("Modal Awal (Rp)", min_value=0.0, value=1000000.0, step=100000.0)
    tahun = st.number_input("Lama Investasi (tahun)", min_value=1, value=5, step=1)
with col2:
    i_nom = st.number_input("Bunga Nominal (%)", min_value=0.0, value=10.0, step=0.1)
    i_eff = st.number_input("Bunga Efektif (%)", min_value=0.0, value=0.0, step=0.1)
    m = st.selectbox("Frekuensi Kapitalisasi", ["1 - Tahunan", "2 - Semesteran", "4 - Triwulanan", "12 - Bulanan", "365 - Harian"])

m = int(m.split()[0])

# =====================================================
# === FUNGSI PERHITUNGAN ==============================
# =====================================================
def hitung_bunga_efektif(P, i_nom, m, tahun):
    i_eff = (1 + i_nom / (100 * m)) ** m - 1
    FV = P * (1 + i_eff) ** tahun
    bunga_total = FV - P
    return i_eff, FV, bunga_total

def hitung_bunga_nominal(P, i_eff, m, tahun):
    i_nom = m * ((1 + i_eff / 100) ** (1 / m) - 1)
    FV = P * (1 + i_eff / 100) ** tahun
    bunga_total = FV - P
    return i_nom, FV, bunga_total

def analisis_otomatis(persen, tipe, tahun):
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
        return f"📊 Analisis: Bunga efektif {persen:.2f}% tergolong {kategori} untuk investasi {durasi}."
    else:
        return f"📊 Analisis: Bunga nominal {persen:.2f}% tergolong {kategori} untuk investasi {durasi}."

# =====================================================
# === TOMBOL & HASIL ==================================
# =====================================================
colA, colB = st.columns(2)

with colA:
    if st.button("📈 Hitung Efektif"):
        i_eff, FV, bunga_total = hitung_bunga_efektif(P, i_nom, m, tahun)
        st.success(f"💡 Bunga Efektif: {i_eff * 100:.4f}%")
        st.info(f"💰 Bunga Total: Rp{bunga_total:,.2f}")
        st.info(f"📊 Nilai Akhir (FV): Rp{FV:,.2f}")
        st.markdown(analisis_otomatis(i_eff * 100, "efektif", tahun))

        # === Grafik ===
        tahun_list = np.arange(1, tahun + 1)
        nilai = P * (1 + i_eff) ** tahun_list
        plt.figure(figsize=(6, 4))
        plt.plot(tahun_list, nilai, marker='o', color="#1565C0")
        plt.title("Grafik Pertumbuhan Modal (Efektif)")
        plt.xlabel("Tahun ke-")
        plt.ylabel("Nilai Modal (Rp)")
        plt.grid(True, linestyle='--', alpha=0.6)
        st.pyplot(plt)

with colB:
    if st.button("💹 Hitung Nominal"):
        i_nom, FV, bunga_total = hitung_bunga_nominal(P, i_eff, m, tahun)
        st.success(f"💡 Bunga Nominal: {i_nom * 100:.4f}%")
        st.info(f"💰 Bunga Total: Rp{bunga_total:,.2f}")
        st.info(f"📊 Nilai Akhir (FV): Rp{FV:,.2f}")
        st.markdown(analisis_otomatis(i_nom * 100, "nominal", tahun))

        tahun_list = np.arange(1, tahun + 1)
        nilai = P * (1 + i_eff / 100) ** tahun_list
        plt.figure(figsize=(6, 4))
        plt.plot(tahun_list, nilai, marker='o', color="#2E7D32")
        plt.title("Grafik Pertumbuhan Modal (Nominal)")
        plt.xlabel("Tahun ke-")
        plt.ylabel("Nilai Modal (Rp)")
        plt.grid(True, linestyle='--', alpha=0.6)
        st.pyplot(plt)

# =====================================================
# === FITUR TAMBAHAN ==================================
# =====================================================
st.markdown("---")
if st.button("📝 Simpan Hasil"):
    with open("hasil_kalkulator.txt", "a", encoding="utf-8") as f:
        f.write(f"Modal={P}, Bunga Nominal={i_nom}%, Efektif={i_eff}%, Tahun={tahun}\n")
    st.success("✅ Hasil disimpan ke file 'hasil_kalkulator.txt'.")

if st.button("🚪 Tutup Aplikasi"):
    st.warning("Aplikasi ditutup (di versi web, hanya menutup sesi pengguna).")

# =====================================================
# === FOOTER ==========================================
# =====================================================
st.markdown("---")
st.markdown("<h4 style='text-align:center;color:#555;'>Kelompok Bunga 🌸 | Proyek Matematika Keuangan</h4>", unsafe_allow_html=True)



