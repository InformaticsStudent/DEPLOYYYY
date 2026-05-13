akses_server = {"Andi", "Budi", "Citra", "Doni"}
akses_db = {"Budi", "Doni", "Eka", "Fajar"}
akses_api = {"Citra", "Doni", "Fajar", "Gilang"}

#1 BARIS CODE PAKAI |
hasil = ((akses_server & akses_db) | (akses_db & akses_api) | (akses_server & akses_api)) - (akses_server & akses_db & akses_api)
print(hasil)