import hashlib
def fitur_himpunan():
    print("--- 1. Analisis Himpunan (Filter Produk) ---")
    keranjang_user = {"iPhone 15", "Charger Type-C", "Casing HP"}
    barang_diskon = {"Casing HP", "Anti Gores", "Powerbank"}
    
    # Irisan (Intersection): Barang di keranjang yang sedang promo
    siap_beli = keranjang_user & barang_diskon 
    
    print(f"Keranjang: {keranjang_user}")
    print(f"Barang Diskon: {barang_diskon}")
    print(f"Hasil (Barang keranjang yang diskon): {siap_beli}\n")


# ==========================================
# 2. RELASI & FUNGSI - Pemetaan Harga & Keamanan
# ==========================================
def fitur_fungsi_dan_relasi(harga_asli):
    print("--- 2. Analisis Relasi & Fungsi (Diskon & Hash) ---")
    
    # Fungsi Matematika f(x) untuk diskon 10%
    # Relasi: Memetakan harga input ke harga output setelah diskon
    f_diskon = lambda x: x - (0.1 * x)
    harga_akhir = f_diskon(harga_asli)
    
    # Fungsi Hash (Relasi One-to-One untuk Keamanan Password)
    password = "password123"
    hash_pw = hashlib.sha256(password.encode()).hexdigest()
    
    print(f"Harga Asli: Rp{harga_asli} -> Harga Diskon (f(x)): Rp{harga_akhir}")
    print(f"Keamanan (Hash Relasi): {hash_pw[:20]}...\n")


# ==========================================
# 3. LOGIKA (LOGIC) - Sistem Verifikasi Pembayaran
# ==========================================
def fitur_logika(saldo_cukup, stok_ada):
    print("--- 3. Analisis Logika (Gerbang Pembayaran) ---")
    
    # Ekspresi Logika: Transaksi sukses JIKA saldo cukup DAN stok ada
    transaksi_sukses = saldo_cukup and stok_ada
    
    if transaksi_sukses:
        print("Status: [TRUE] Transaksi Berhasil.")
    else:
        print("Status: [FALSE] Transaksi Gagal (Cek Saldo/Stok).")
    print("")


# ==========================================
# 4. INDUKSI MATEMATIK - Validasi Biaya Admin
# ==========================================
def simulasi_induksi_biaya(n):
    """
    Membuktikan total biaya admin tetap Rp1.000 per transaksi.
    Jika ada 'n' transaksi, total biaya admin adalah 1000 * n.
    Langkah Induksi:
    1. Basis: n=1, Total = 1000
    2. Langkah Induksi: Jika n=k benar, maka n=k+1 adalah (1000*k) + 1000
    """
    print(f"--- 4. Simulasi Induksi Matematik (Total Biaya Admin {n} Transaksi) ---")
    total = 0
    for i in range(1, n + 1):
        total += 1000
        print(f"Transaksi ke-{i}: Total Biaya Terakumulasi = Rp{total}")
    print(f"Terbukti secara algoritma untuk n={n}.\n")


# ==========================================
# MAIN PROGRAM
# ==========================================
if __name__ == "__main__":
    print("=== SIMULASI MATEMATIKA DISKRIT PADA TOKOPEDIA ===\n")
    
    # Panggil semua materi
    fitur_himpunan()
    fitur_fungsi_dan_relasi(500000)
    fitur_logika(saldo_cukup=True, stok_ada=True)
    simulasi_induksi_biaya(3)
    
    print("==================================================")