# Menghitung sigma (5i+2) dari 13 sampai 17
hasil = 0
n = 17
for i in range(13, n+1):
    hasil = hasil + (5*i) + 2
print(hasil)        #hasil bernilai 385


# Menghitung sigma (n^2 + 2n - 1) dari 5 sampai 10
hasil2 = 0
n2 = 10
for m in range(5, n2+1):
    hasil2 = hasil2 + (m*m) + (2*m) - 1
print(hasil2)       #hasil bernilai 439


# Menghitung notasi Pi (i-3) dari 4 sampai 8
hasil3 = 1
n3 = 8
for k in range(4, n3+1):
    hasil3 = hasil3 * (k-3)
print(hasil3)       #hasil bernilai 120