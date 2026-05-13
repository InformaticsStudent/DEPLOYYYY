# Database Dictionary dengan format menurun (vertikal) agar mudah dibaca
MKI = {
    "MKI-001": {
        "judul": "Manajemen Strategis",
        "deskripsi": "Proses perumusan, implementasi, dan evaluasi keputusan lintas fungsional.",
        "leader": "Melvin Rahma Sayuga Subroto, S.Pd., M.Acc.",
        "anggota": 48,
        "status": "Aktif"
    },
    "MKI-002": {
        "judul": "Smart Logistics System",
        "leader": "Siti Aminah",
        "anggota": 3,
        "status": "Tahap Riset"
    }
}

while True:
    print("\n" + "="*50)
    print("   SISTEM MANAJEMEN KEPEMIMPINAN & INOVASI   ")
    print("="*50)
    print("1. Lihat Data | 2. Cari Detail | 3. Keluar")
    pilihan = input("Pilih menu (1-3): ")

    if pilihan == '1':
        # Menampilkan ringkasan semua data
        print(f"\n{'ID':<10} | {'JUDUL':<20} | {'LEADER'}")
        print("-" * 60)
        for k, v in MKI.items():
            # Gunakan f-string agar teks rapi sejajar
            print(f"{k:<10} | {v['judul'][:18]:<20} | {v['leader'][:20]}")

    elif pilihan == '2':
        # Menampilkan SEMUA TEKS secara menurun
        id_cari = input("\nMasukkan ID yang dicari: ").upper()
        data = MKI.get(id_cari)
        if data:
            print(f"\n--- DETAIL LENGKAP PROYEK {id_cari} ---")
            # Loop ini akan memunculkan semua isi teks yang ada di dictionary
            for kunci, nilai in data.items():
                print(f"{kunci.capitalize():<15}: {nilai}")
        else:
            print("ID tidak ditemukan.")

    elif pilihan == '3':
        print("Program selesai.")
        break