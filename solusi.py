# azzammuhyala - Bro

baris = int(input())
lagu = [input().split() for _ in range(baris)]

# buat nyari jumlah lirik tiap penyanyi
# pakek dict (kamus)
frekuensi = {} # {nama: jumlah_lirik}
for lirik in lagu:
    nama = lirik[0]
    if nama not in frekuensi:
        frekuensi[nama] = 1
    else:
        frekuensi[nama] += 1

# pakek sorted()
# urutan = sorted(lagu, key=lambda lirik : frekuensi[lirik[0]], reverse=True)

# pakek method .sort() dari list
# urutan = lagu
# urutan.sort(key=lambda lirik : frekuensi[lirik[0]], reverse=True)

# manual (bubble sort)
urutan = lagu
for i in range(len(urutan)):
    for j in range(len(urutan) - 1):
        if frekuensi[urutan[j][0]] < frekuensi[urutan[j + 1][0]]:
            urutan[j], urutan[j + 1] = urutan[j + 1], urutan[j]

print('OUTPUT'.center(50, '=')) # boleh di apus cuma jadi separator aja antar input ama output
# tampilin hasil
for lirik in urutan:
    print(' '.join(lirik))
