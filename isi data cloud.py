import json
import os

FILE_BACKUP = "data_mki.json"

if os.path.exists(FILE_BACKUP):
    with open(FILE_BACKUP, 'r') as f:
        MKI = json.load(f)
    print(">>> Backup ditemukan, data dimuat!")
else:
    MKI = {
        "MKI-001": {
            "judul": "Manajemen Strategis",
            "status": "Aktif"
        }
    }
    print(">>> File baru dibuat.")
while True:
    print("\n[1] Lihat Data | [2] Tambah Data | [3] Keluar")
    pilih = input("Pilih: ")

    if pilih == "1":
        # Nampilin data yang ada di RAM (variabel MKI)
        for k, v in MKI.items():
            print(f"ID: {k} | Judul: {v['judul']} | Status: {v['status']}")

    elif pilih == "2":
        # Masukin data baru ke RAM
        id_baru = input("ID Baru: ").upper()
        judul = input("Judul: ")
        status = input("Status: ")
        MKI[id_baru] = {"judul": judul, "status": status}

        with open(FILE_BACKUP, 'w') as f:
            json.dump(MKI, f, indent=4)
        print(">>> Berhasil! Data sudah terkunci di file JSON.")

    elif pilih == "3":
        break