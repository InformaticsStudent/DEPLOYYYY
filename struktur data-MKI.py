import json
import os

if os.path.exists("data_mki.json"):
    with open("data_mki.json", "r") as f:
        MKI = json.load(f)
else:

    MKI = {
        "MKI-001": {
            "judul": "Manajemen Strategis",
            "isi data": ("Proses perumusan, implementasi, dan evaluasi keputusan lintas fungsional "
                        "yang memungkinkan organisasi mencapai tujuannya."),
            "dosen": "Melvin Rahma Sayuga Subroto, S.Pd., M.Acc.",
            "mahasiswa": 48,
            "status": "Aktif"
        }
    }

while True:
    print("\n" + "="*50)
    print("    MANAJEMEN KEPEMIMPINAN DAN INOVASI    ")
    print("="*50)
    print("1. Lihat Semua Data")
    print("2. Tambah Data Baru")
    print("3. Cari Detail Proyek")
    print("4. Keluar")
    print("="*50)
    
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == '1':
        print(f"\n{'ID':<10} | {'JUDUL':<20} | {'DOSEN'}")
        print("-" * 60)
        for k, v in MKI.items():
            print(f"{k:<10} | {v['judul'][:18]:<20} | {v['dosen'][:20]}")

    elif pilihan == '2':
        print("\n--- INPUT DATA INOVASI BARU ---")
        id_baru = input("Masukkan ID Proyek (Contoh: MKI-002): ").upper()
        
        if id_baru in MKI:
            print("Peringatan: ID sudah ada dalam database!")
        else:
            judul = input("Masukkan Judul Data: ")
            desk = input("Masukkan Isi Data Sesuai Keinginan Kalian: ")
            dsn = input("Masukkan Nama Dosen: ")
            mhs = input("Masukkan Jumlah Mahasiswa: ")
            stat = input("Masukkan Status (Aktif/Riset/Selesai): ")

            MKI[id_baru] = {
                "judul": judul,
                "isi data": desk,
                "dosen": dsn,
                "mahasiswa": mhs,
                "status": stat
            }
            
            # --- SIMPAN KE JSON (BIAR KEHUBUNG) ---
            with open("data_mki.json", "w") as f:
                json.dump(MKI, f, indent=4)
            
            print("\n>>> Sukses! Data tersimpan di Dictionary & File JSON.")

    elif pilihan == '3':
        id_cari = input("\nMasukkan ID yang dicari: ").upper()
        data = MKI.get(id_cari)
        if data:
            print(f"\n--- DETAIL LENGKAP PROYEK {id_cari} ---")
            for kunci, nilai in data.items():
                print(f"{kunci.capitalize():<15}: {nilai}")
        else:
            print("ID tidak ditemukan.")

    elif pilihan == '4':
        print("Analisis selesai.")
        break