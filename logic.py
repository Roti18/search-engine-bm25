# append(gabungkan isi)
# list = []
# item = apa yang ingin di gabung
def gabung(list, item):
  list += [item]
  return list

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

# any(Mengembalikan True jika minimal satu elemen dalam iterable bernilai True.)
def ada(n):
  for i in n:
    if i:
      return True
  return False
# print(ada([0,0,0]))

# all(Mengembalikan True hanya jika semua elemen dalam iterable bernilai True.)
def allTrue(n):
  for i in n:
    if not i:
      return False
  return True
# print(allTrue([0,1,1,1]))

# map(Menerapkan fungsi ke setiap elemen dalam iterasi.)
def applyAll(func, n):
    return [func(i) for i in n]
# angka = [1, 2, 3]
# hasil = applyAll(lambda x: x * 2, angka)
# print(hasil)


# filter(Menyaring elemen dalam iterable berdasarkan kondisi fungsi yang diberikan (mengembalikan True))
def saring(func, n):
    hasil = []
    for i in n:
        if func(i):
            gabung(hasil, i)
    return hasil
# angka = [1, 2, 3, 4, 5]
# genap = saring(lambda x: x % 2 == 0, angka)
# print(genap)


# enumerate(Memberikan indeks dan nilai dari iterasi)
def index(n):
  i = 0
  result = []
  for item in n:
    gabung(result,(i, item))
    i+=1
  return result
# buah = ['apel', 'jeruk', 'mangga']
# for i, nama in index(buah):
#     print(i, nama)


# zip(Menggabungkan dua atau lebih iterable secara berpasangan (sejajar))
def collabLoop(func, n):
    result = []
    i = 0
    while i < semua(func):
      while i < semua(n):
        result.append((func[i], n[i]))
        i += 1
    return result
# nama = ['Ani', 'Budi']
# nilai = [80, 90]
# gabung = collabLoop(nama, nilai)
# print(gabung)
