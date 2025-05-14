# get title news from newsapi
# import requests
# import json

# api_key = "d339770793d34aa4908f2bf6609a3c9b"
# url = f"https://newsapi.org/v2/everything?q=berita&language=id&pageSize=100&apiKey={api_key}"

# response = requests.get(url)
# data = response.json()

# with open("berita.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)

# print(f"Berhasil menyimpan {len(data.get('articles', []))} artikel ke 'berita.json'")



documents = [
    "Marketing: 4 Langkah Penting Menjangkau Generasi C yang Sulit Dipahami",
    "Berita Hampir Tepat Masa:  5 Contoh Transformasi AI (2025-04-27)",
    "Berita Hampir Tepat Masa:  Cara Membuat Spot 30 Saat dengan AI (2025-05-11)",
    "Almost Timely News: Apakah Kandungan Sebuah Bengkel AI? (2025-05-04)",
    "ensemble-hoax-news-detector 0.1",
    "Axi Meraikan Dua Pedagang Axi Select yang Menerima Pembiayaan sebanyak $1 Juta di Sydney, Australia",
    "ensemble-hoax-news-detector added to PyPI",
    "AI-Media Melancarkan LEXI Voice di NAB Show 2025 - Global Reach dengan Terjemahan Suara Secara Langsung yang Dikuasakan oleh AI",
    "AI-Media Menampilkan LEXI Voice di NAB Show 2025 - Jangkauan Global dengan Penerjemahan Suara Langsung yang Didukung AI",
    "KACAU! Rapper AS Sebut Indonesia 'Tempat Sampah Dunia' - Vlix.id",
    "Ingredion Incorporated Melaporkan Keputusan Suku Pertama Yang Kukuh dan Menambah Baik Unjuran Sepanjang Tahun",
    "[Kolom Pakar] Prof Tjandra Yoga: Uji Klinik Vaksin Tuberkulosis yang Sedang Jadi Berita",
    "Duka Selebritas Indonesia Mengiringi Kepergian Paus Fransiskus: Rest in Love, Pope",
    "Rendah Lemak dan Cocok Untuk Menu Diet Sehat, Gunakan Resep Ini Jika Ingin Diet Berhasil",
    "Polisi Ungkap Kronologi Penangkapan Fachri Albar",
    "Sebelum Meninggal, Hotma Sitompul Koma 2 Bulan Lalu",
    "PIK 2 (PANI) Kantongi Marketing Sales Rp466 Miliar per Kuartal I/2025",
    "Ekonomi Suram: Pengembang Meradang, Digital Marketing Jadi Solusi Pemasaran",
    "Rocketindo: Lebih dari Sekadar Marketing Agency, Penyedia Layanan Omni Channel yang Mendorong Kesuksesan Brand di Indonesia",
    "Keras! Ketum PWI Hendry Ch Bangun Keluarkan Pernyataan Resmi Terkait Penangkapan Direktur Pemberitaan JAKTV",
    "Ketum PWI Pusat Hendry Ch Bangun: Kasus Direktur JAKTV Harusnya Lewat Dewan Pers, Bukan Ditangkap",
    "Rapat Paripurna DPRD Balikpapan, Dua Raperda Disahkan",
    "Transmart Pontianak Tutup Permanen Mulai 30 April 2025",
    "Sambangi Rumah Korban Pemukulan OTK, Jenal Mutaqin Minta Pelaku Ditindak",
    "DPRD Ketapang Anggarkan Hampir Rp 1,7 Miliar Untuk Biaya Makan dan Minum Rapat Sepanjang 2025",
    "Warga Minta Dinas PUPR Tanjab Barat Percepat Pengerjaan Galian Turap dan Pelebaran Jalan Senangin",
    "Diduga Menjadi Penyebab Banjir, PHPS Genengsari Diminta Ditinjau Ulang",
    "Tiga Bangunan Ludes Terbakar di Pontianak Barat, Salah Satunya Rumah Wartawan Senior",
    "Wabup Juli Suryadi Sambut Baik Pembentukan Pokja PWI Mempawah",
    "Diskominfo Pontianak Susun Rencana Strategis Kebijakan 2025 - 2029",
    "Banjir Rendam Puluhan Rumah di Kecamatan Beduai, Kapolsek Imbau Warga Waspada dan Siaga Evakuasi",
    "Wujud Kepedulian, Jurnalis KKU Bagikan Bansos kepada Kaum Dhuafa",
    "Kepala Kantor BPN Kubu Raya Dilaporkan ke Polda Kalbar",
    "Babinsa Koramil 0826-06 Pademawu Sinergi Bersama Petani Panen Padi di Desa Bunder",
    "Di Balik Asap Turbin, Dugaan Kelalaian K3 di PLTU Sukabangun Ketapang Sebabkan Nyawa Karyawan Melayang",
    "Jual Miras Ilegal ke Jongkong, 9 Warga Hulu Gurung Diamankan Unsur Muspika Jongkong",
    "Warga RT 17 Keluhkan Kabel Listrik Menjuntai dan Bertiang Kayu di Kampung Nelayan",
    "Bappeda Sumenep Gelar Musrenbang, Sinkronkan Arah Pembangunan 5 Tahun ke Depan",
    "Ketum PWI Pusat Hendry Ch Bangun: Kasus Direktur JAKTV Harusnya Lewat Dewan Pers, Bukan Ditangkap",
    "Kasus Pelecehan oleh Guru Karate di Pontianak, Edi Kamtono: Perlu Pengawasan Ketat Kegiatan Sekolah",
    "KPPAD Kalbar Ungkap Pencabulan Oknum Sensei Karate di Pontianak, 7 Anak Jadi Korban",
    "Revitalisasi Makam Kesultanan Rampung, Wali Kota Pontianak Ajak Warga Rawat Bersama",
    "KPK Geledah Dinas PU Mempawah, Wagub Krisantus: Saya Tidak Tau",
    "Berita Gembira, SK CPNS dan PPPK Tahap I 2024 Kapuas Hulu Diserahkan Pertengahan Mei 2025",
    "Pertama Kali Muncul ke Publik, Alan Pimpinan Islam Sejati Bantah Sebar Ajaran Sesat",
    "Ketua Umum PWI Pusat Hendry Ch Bangun Harap Wartawan Manfaatkan Program Rumah Subsidi",
    "Seorang Lansia Ditemukan Meninggal Dunia di Rumahnya di Blora",
]


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












def kecilKan(documents):
    hasil = []
    # Kamus konversi huruf besar ke huruf kecil
    konversi = {
        'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e',
        'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j',
        'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o',
        'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't',
        'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'
    }
    for dokumen in documents:
        dokumen_kecil = ""
        for karakter in dokumen:
            # Cek apakah karakter ada di kamus konversi
            if karakter in konversi:
                dokumen_kecil += konversi[karakter]
            else:
                dokumen_kecil += karakter
        gabung(hasil, dokumen_kecil)
    return hasil

kecil = kecilKan(documents)
# # print(kecil)




def pisah(kalimat):
    kata = ""
    hasil = []
    for huruf in kalimat:
        if huruf != " ":
            kata += huruf.lower()
        else:
            if kata:
                gabung(hasil, kata)
                kata = ""
    if kata:
        hasil.append(kata)
    return hasil


for i in range(semua(documents)):
    daftar_kata = pisah(kecil[i])
    print(daftar_kata)
