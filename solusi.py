# @azzammuhyala - Bro

input = "LVIII"

map = {
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

sum = 0

for i in range(len(input)):
    bobot = map[input[i]]
    selanjutnya = i + 1
    #  +-- ini buat cek apakah indeks selanjutnya lebih kecil dari panjkang input biar gak terjadi error (IndexError)
    #  |                            +--> bandingin nilai bobot karakter di indeks i sekarang dengan karakter indeks selanjutnya
    #  |                            |    (aturannya)
    #  vvvvvvvvvvvvvvvvvvvvvvvv     vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv 
    if selanjutnya < len(input) and bobot < map[input[selanjutnya]]:
        sum -= bobot # kalo semua kondisi di atas True (benar) maka kurangi bobot karakter sekarang
    else:
        sum += bobot # kalo gak ya jumlahin aja

print(sum)
