import hashlib

def analisis_matdis_tokopedia():
    print("=== Simulasi Matematika Diskrit pada Tokopedia ===\n")
    print("================== Kelompok 7 ====================\n")

# 1.LOGIKA (Logic)
# Proposisi p: Barang Diskon, q: Rating >= 4
    print("[1] LOGIKA (Filter Pencarian)")
    is_diskon = True  # Proposisi p
    is_high_rating = True  # Proposisi q
    
# Evaluasi Logika: p AND q
    if is_diskon and is_high_rating:
        print("Sistem: Menampilkan produk yang sedang Diskon DAN memiliki Rating 4+.\n")
    else:
        print("Sistem: Produk tidak memenuhi kriteria filter.\n")


# 2.HIMPUNAN (Set)
    print("[2] HIMPUNAN (Kategori Produk)")
    set_kebutuhan = {"Keyboard", "Handphone", "Celana", "Mouse", "Sabun Mandi", "Seblak"}
    set_promo_flash_sale = {"Handphone", "Mouse", "Keyboard", "Celana"}
    
# Operasi Irisan (Intersection)
    irisan_produk = set_kebutuhan.intersection(set_promo_flash_sale)
    print(f"Himpunan Kebutuhan Sekunder: {set_kebutuhan}")
    print(f"Himpunan Flash Sale: {set_promo_flash_sale}")
    print(f"Hasil Filter (Kebutuhan Sekunder n Flash Sale): {irisan_produk}\n")


# 3.RELASI & FUNGSI
    print("[3] RELASI & FUNGSI (Perhitungan Ongkos Kirim)")
    def hitung_ongkir(berat, jarak):
        # f(w, d) = (berat * 5000) + (jarak * 2000)
        return (berat * 5000) + (jarak * 2000)

    berat_barang = 2  # dalam kg
    jarak_tempuh = 15 # dalam km
    biaya = hitung_ongkir(berat_barang, jarak_tempuh)
    print(f"Input: Berat={berat_barang}kg, Jarak={jarak_tempuh}km")
    print(f"Biaya Ongkir (Fungsi Deterministik): Rp {biaya}\n")


# 4.TEORI BILANGAN (Number Theory)
    print("[4] TEORI BILANGAN (Keamanan Transaksi & Modulo)")
    # Simulasi Hashing sederhana (Representasi Kriptografi)
    password_user = "Kelompok7-matdis"
    hash_result = hashlib.sha256(password_user.encode()).hexdigest()
    print(f"Password Asli: {password_user}")
    print(f"Encrypted (Konsep Bilangan Prima/Kriptografi): {hash_result[:20]}...")
    
# Modulo untuk Validasi VA
    nomor_va = 2026
    checksum = nomor_va % 10
    print(f"Validasi Nomor VA (Modulo 10): {checksum}\n")

# 5.INDUKSI MATEMATIK (Mathematical Induction)
    print("[5] INDUKSI MATEMATIK (Verifikasi Algoritma Rekursif)")
    def telusuri_kategori(level):
        if level == 0:
            return "Basis Tercapai: Level Root/Pusat"
        else:
            print(f"Menelusuri Level {level}...")
            return telusuri_kategori(level - 1)

    print(telusuri_kategori(3))
    print("\n=== Simulasi Selesai. Algoritma Terverifikasi. ===")

if __name__ == "__main__":
    analisis_matdis_tokopedia()