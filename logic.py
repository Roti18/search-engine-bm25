  # sorted() – Jika butuh urutkan elemen (misal, urutkan angka atau string).
  # any() dan all() – Berguna untuk mengecek kondisi di dalam list atau koleksi.
  # map() dan filter() – Berguna untuk transformasi atau filtering koleksi.
  # enumerate() – Berguna ketika kamu perlu mengakses indeks dan nilai sekaligus.
  # zip() – Untuk menggabungkan dua atau lebih list secara paralel, sering dipakai di tugas-tugas data.

# any() → has_any
# all() → has_all
# map() → apply
# filter() → select
# enumerate() → index
# zip() → combine

# len(membaca berapa elemen yang ada di suatu list)
def semua(n):
  count = 0
  for i in n:
    count += 1
  return count
  # print(semua("testing hallo"))

# sum(menghitung semua elemen angka)
def count(n):
  result = 0
  for i in n:
    result += i
  return result
# print(count([18,29,79]))

# max(mencari nilai tertinggi)
def findMax(n):
  big = n[0]
  for i in n:
    if i > big:
      big = i
  return big
# print(findMax([18,78,10]))

def findMin(n):
  low = n[0]
  for i in n:
    if i < low:
      low = i
  return low
# print(findMin([18,78,10]))

# sorted(Mengurutkan angka dari terkecil ke terbesar)
def sort(n):
    ada_penukaran = True
    while ada_penukaran:
        ada_penukaran = False
        i = 0
        panjang = semua(n)
        while i < panjang - 1:
            if n[i] > n[i + 1]:
                n[i], n[i + 1] = n[i + 1], n[i]
                ada_penukaran = True
            i += 1
    return n
# print(sort([19,8,3]))