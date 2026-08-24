# @azzammuhyala - Bro

# ILMU baru: len(x) itu mendaaptkan panjang string/list, contoh: mau cari berapa banyak/panjang karakter 'LVIII'? len(...) menghasilkan 5

angka_romawi = "LVIII"
mapping_romawi = {
    #    vvvv --> bobot
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
#   ^^^ --> karakter romawi
}

total = 0

for i in range(len(angka_romawi)):
    bobot = mapping_romawi[angka_romawi[i]]
    indeks_selanjutnya = i + 1
    #  +-- ini buat cek apakah indeks selanjutnya lebih kecil dari panjkang input biar gak terjadi error (IndexError)
    #  |                                          +--> bandingin nilai bobot karakter di indeks i sekarang dengan bobot karakter indeks selanjutnya
    #  |                                          |    (aturannya)
    #  vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv     vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    if indeks_selanjutnya < len(angka_romawi) and bobot < mapping_romawi[angka_romawi[indeks_selanjutnya]]:
        total -= bobot # kalo semua kondisi di atas True (benar) maka kurangi bobot karakter sekarang
    else:
        total += bobot # kalo gak ya jumlahin aja

print(total)
