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
]


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

# ===============================================================================================
# ================================= START STEP 1 ================================================
# ===============================================================================================

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

# sorted(mengatur angka dari besar ke kecil)
def sortir(data):
  n = semua(data)
  tukar = True
  while tukar:
      tukar = False
      i = 0
      while i < n - 1:
          if data[i][1] < data[i + 1][1]:  # descending
              data[i], data[i + 1] = data[i + 1], data[i]
              tukar = True
          i += 1
  return data



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

# split (pisah perkalimat)
def splt(kalimat):
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
    gabung(hasil, kata)
  return hasil

# memecah dictionary utnuk di tampilkan
def loop_dict(kamus_data):
  daftar_pasangan = []
  for kunci in kamus_data:
      nilai = kamus_data[kunci]
      pasangan = (kunci, nilai)
      gabung(daftar_pasangan, pasangan)
  return daftar_pasangan


pemnghubung = [
  "nya", "dan", "atau", "tetapi", "melainkan", "maupun", "serta", "bahkan",
  "karena", "sebab", "oleh", "itu", "sehingga", "agar", "supaya", "jika", "apabila",
  "kalau", "kalaupun", "seandainya", "meskipun", "biarpun", "walaupun", "kendati",
  "selama", "sejak", "sesudah", "setelah", "sebelum", "tatkala", "ketika", "sementara",
  "asal", "kecuali", "maka", "kemudian", "lalu", "hingga", "sampai", "justru", "malah",
  "seperti", "ibarat", "bagaikan", "bak", "yang", "untuk", "dengan", "ini", "itu", "ke",
  "di", "yang", "to", "pem", "an", "per", "jadi"
]

def kecilKan(documents):
  hasil = []
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
        if karakter in konversi:
            dokumen_kecil += konversi[karakter]
        else:
            dokumen_kecil += karakter
    gabung(hasil, dokumen_kecil)
  return hasil

# hapus tanda baca  
def hapus_tandabaca(teks):
  tanda = [",", ".", ":", ";", "!", "?", "-", "(", ")", "'", "[", "]", "$", "/"]
  hasil = ""
  for i in range(semua(teks)):
    cocok = 0
    for j in range(semua(tanda)):
        if teks[i] == tanda[j]:
            cocok = 1
    if cocok == 0:
        hasil = hasil + teks[i]
  return hasil

def hapus_penghubung(daftar_kata):
  hasil = []
  for i in range(semua(daftar_kata)):
      cocok = 0
      for j in range(semua(pemnghubung)):
          if daftar_kata[i] == pemnghubung[j]:
              cocok = 1
      if cocok == 0:
          gabung(hasil, daftar_kata[i])
  return hasil


# ===============================================================================================
# ======================================== END STEP 1 ===========================================
# ===============================================================================================




# ===============================================================================================
# ======================================== START STEP 2 ===========================================
# ===============================================================================================

# hitung tf
def tf(terms, doc):
    tf_per_document = []
    for doc_index, doc_words in index(doc):
        current_doc_tf = {}
        for term in terms:
            current_doc_tf[term] = 0
        for term in terms:
            for word_in_doc in doc_words:
                if term == word_in_doc:
                    current_doc_tf[term] += 1
        gabung(tf_per_document, current_doc_tf)
    return tf_per_document

def log_10(x):
    if x <= 0:
        return -1
    hasil = 0
    while x >= 10:
        x = x / 10
        hasil += 1
    while x < 1:
        x = x * 10
        hasil -= 1
    step = 0.1
    for i in range(4):
        while x >= 10 ** step:
            x = x / (10 ** step)
            hasil += step
        step = step / 10
    return hasil

def idft(n, df):
    rasio = (n - df + 0.5) / (df + 0.5)
    return log_10(rasio) + 1

def df(term, tf_doc):
    jumlah = 0
    for i, doc in index(tf_doc):
        if doc[term] > 0:
            jumlah += 1
    return jumlah

def panjang_semua(dok_list):
    total = 0
    for doc in dok_list:
        for _ in doc:
            total += 1
    return total

def avgdl(semua_doc):
    return panjang_semua(semua_doc) / semua(semua_doc)

def hitung_df(term, semua_doc):
    jumlah = 0
    for doc in semua_doc:
        ada = 0
        for kata in doc:
            if kata == term:
                ada = 1
        jumlah += ada
    return jumlah

def bm25_score_per_doc(query_terms, satu_doc, semua_doc):
    total_score = 0
    n = semua(semua_doc)
    average = avgdl(semua_doc)
    panjang_doc = semua(satu_doc)

    k1 = 1.5
    b = 0.75

    idx = 0
    while idx < semua(query_terms):
        term = query_terms[idx]

        tf = 0
        i = 0
        while i < semua(satu_doc):
            if satu_doc[i] == term:
                tf += 1
            i += 1

        df_term = hitung_df(term, semua_doc)
        idf = log_10((n - df_term + 0.5) / (df_term + 0.5)) + 1

        if tf > 0:
            atas = tf * (k1 + 1)
            bawah = tf + k1 * (1 - b + b * (panjang_doc / average))
            skor = idf * (atas / bawah)
            total_score += skor

        idx += 1
    return total_score


# =====================================================================================

while True:
    query = input("\nMasukkan query: ")
    if query == "":
       False

    kecil_document = kecilKan(documents)
    del_pnghbng_tnd = []
    for teks in kecil_document:
        teks_bersih = hapus_tandabaca(teks)
        daftar_kata = splt(teks_bersih)
        hasil_bersih = hapus_penghubung(daftar_kata)
        gabung(del_pnghbng_tnd, hasil_bersih)

    split_query = hapus_penghubung(splt(kecilKan([query])[0]))
    tf_doc = tf(split_query, del_pnghbng_tnd)

    print("\n========================================= TF TIAP DOKUMEN")
    print("-" * 100)
    total_kata_query = {}
    for idx, tf_data in index(tf_doc):
        ori_doc = documents[idx]
        print(f"Dokumen {idx+1} ('{ori_doc}'):")
        kosong = True
        for term, count in loop_dict(tf_data):
            if count > 0:
                print(f"  - '{term}': {count} kali")
                kosong = False
                if term in total_kata_query:
                    total_kata_query[term] += count
                else:
                    total_kata_query[term] = count
        if kosong:
            print("  Tidak ada kata kunci kueri yang ditemukan.")
        print("-" * 100)

    print("\n========================================= IDF SCORE SETIAP KATA DALAM DOKUMEN")
    jumlah_dokumen = semua(tf_doc)
    for term in split_query:
        doc_freq = df(term, tf_doc)
        skor_idf = idft(jumlah_dokumen, doc_freq)
        print(f"  - '{term}': IDF = {skor_idf:.4f} (DF = {doc_freq})")

    print("\n========================================= BM25 Score Tiap DOKUMEN")
    list_score = []
    for i in range(semua(del_pnghbng_tnd)):
        skor = bm25_score_per_doc(split_query, del_pnghbng_tnd[i], del_pnghbng_tnd)
        print(f"Dokumen {i+1}: Skor BM25 = {skor:.4f}")
        if skor > 0:
            gabung(list_score, (i+1, skor))

    print("\n========================================= PERANGKINGAN DOCUMENT")
    ranking = sortir(list_score)
    for rank_idx, skor in ranking:
        print(f"Dokumen {rank_idx} ('{documents[rank_idx - 1]}') ==> Skor BM25 = {skor:.4f}")
        print("-"*100)
    
