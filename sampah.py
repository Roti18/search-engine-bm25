# Data Dokumen
my_list1 = ['Penampakan Tipisnya Samsung Galaxy S25 Edge']
my_list2 = ['Waspada VajraSpy Susupi 12 Aplikasi Android Ini']
my_list3 = ['Google Akan Cabut Lisensi Android Smartphone Huawei']
my_list4 = ['Google Pamerkan HP Flagship Pixel 9 Pro dan HP Lipat Pixel 9 Pro Fold']
my_list5 = ['Review Realme 13+ 5G: Tampilan Casual, Tapi Performa Gaming Banget']
my_list6 = ['Sesetia Apa sih Pengguna Android ?']
my_list7 = ['Pasang Anti Gores Bikin Layar HP Kurang Sensitif, Emang Iya']
my_list8 = ['5 Besar Merek Smartphone di Indonesia Kuartal I-2025 Versi Canalys, Xiaomi Teratas']
my_list9 = ['Infinix Note 30 VIP Meluncur dengan RAM 12 GB dan Wireless Charging 50 Watt']
my_list10 = ['Apa Itu Qualcomm Snapdragon, Sponsor Utama di Jersey MU Terbaru']

# Fungsi menghitung panjang list atau string
def hitung_panjang(data):
    panjang = 0
    for dt in data:
        panjang += 1
    return panjang

# Fungsi mengubah teks menjadi huruf kecil tanpa fungsi/metode bawaan
def ke_huruf_kecil(teks):
    hasil = ""
    abjad_besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    abjad_kecil = "abcdefghijklmnopqrstuvwxyz"
    
    for char in teks:
        ditemukan = False
        for i in range(26):  
            if char == abjad_besar[i]: 
                hasil += abjad_kecil[i]  
                ditemukan = True
                break
        if not ditemukan: 
            hasil += char
    return hasil

# Fungsi pemisah kata
def pemisah_kata(teks):
    teks = ke_huruf_kecil(teks)  
    hasil = [""] * 100  
    indeks_hasil = 0
    kata = ""
    i = 0
    while i < hitung_panjang(teks):
        if teks[i] != " ":
            kata += teks[i]
        else:
            if kata != "":
                hasil[indeks_hasil] = kata
                indeks_hasil += 1
                kata = ""
        i += 1
    if kata != "":
        hasil[indeks_hasil] = kata
        indeks_hasil += 1
    return [hasil[j] for j in range(indeks_hasil)]

# Fungsi gabungkan banyak list tanpa duplikasi
def gabungkan_banyak_list_tanpa_duplikasi(list1):
    hasil = []
    for lst in list1:
        for elemen in lst:
            elemen = ke_huruf_kecil(elemen)  
            sudah_ada = False
            for item in hasil:
                if elemen == item:
                    sudah_ada = True
                    break
            if not sudah_ada:
                hasil += [elemen]
    return hasil

# Fungsi hapus stop words
def hapus_stop_word(kata_kata, stop_words):
    hasil = []
    for kata in kata_kata:
        is_stop_word = False
        for stop_word in stop_words:
            if kata == ke_huruf_kecil(stop_word):
                is_stop_word = True
                break
        if not is_stop_word:
            hasil += [kata]
    return hasil

# Fungsi hapus tanda/karakter unik
def hapus_karakter_unik(kata_kata, karakter_unik):
    hasil1 = []
    for kata in kata_kata:
        is_karakter_unik = False
        for ch_unik in karakter_unik:
            if kata == ke_huruf_kecil(ch_unik):
                is_karakter_unik = True
                break
        if not is_karakter_unik:
            hasil1 += [kata]
    return hasil1

# Fungsi log manual
def log_manual(x):
    if x <= 0:
        return 0
    n = 100
    x = (x - 1) / (x + 1)
    result = 0
    for i in range(n):
        result += (1 / (2 * i + 1)) * (x ** (2 * i + 1))
    return 2 * result

# Fungsi menghitung TF
def hitung_tf(dokumen, semua_kata):
    tf = [0] * hitung_panjang(semua_kata)
    total_kata = hitung_panjang(dokumen)
    for kata in dokumen:
        for i in range(hitung_panjang(semua_kata)):
            if kata == semua_kata[i]:
                tf[i] += 1
    for i in range(hitung_panjang(tf)):
        tf[i] = tf[i] / total_kata
    return tf

# Fungsi menghitung IDF
def hitung_idf(dokumen_list, semua_kata):
    idf = [0] * hitung_panjang(semua_kata)
    total_dokumen = hitung_panjang(dokumen_list)
    for i in range(hitung_panjang(semua_kata)):
        count = 0
        for dokumen in dokumen_list:
            for kata in dokumen:
                if semua_kata[i] == kata:
                    count += 1
                    break
        idf[i] = 1 + log_manual(total_dokumen / (1 + count))
    return idf

# Fungsi menghitung TF-IDF
def hitung_tfidf(dokumen, semua_kata_bersih, idf):
    tf = hitung_tf(dokumen, semua_kata_bersih)
    tfidf = [0] * hitung_panjang(semua_kata_bersih)
    for i in range(hitung_panjang(tf)):
        tfidf[i] = tf[i] * idf[i]
    return tfidf

# Fungsi hitung panjang dokumen
def panjang_dokumen(dokumen):
    return hitung_panjang(dokumen)

# Fungsi menghitung IDF untuk BM25
def hitung_idf_bm25(semua_dokumen, semua_kata):
    N = hitung_panjang(semua_dokumen)
    idf_bm25 = [0] * hitung_panjang(semua_kata)
    for i in range(hitung_panjang(semua_kata)):
        df = 0
        for dokumen in semua_dokumen:
            if semua_kata[i] in dokumen:
                df += 1
        rasio = (N - df + 0.5) / (df + 0.5)
        if rasio <= 0:
            idf_bm25[i] = 0
        else:
            idf_bm25[i] = log_manual(rasio)
    return idf_bm25

# Fungsi menghitung skor BM25
def hitung_bm25(dokumen, query, semua_kata, idf_bm25, avgdl):
    skor = 0
    b = 0.75
    k1 = 1.5
    panjang_doc = panjang_dokumen(dokumen)
    for kata in query:
        for i in range(hitung_panjang(semua_kata)):
            if semua_kata[i] == kata:
                f = 0
                for token in dokumen:
                    if token == kata:
                        f += 1
                denom = f + k1 * (1 - b + b * (panjang_doc / avgdl))
                skor += idf_bm25[i] * ((f * (k1 + 1)) / denom)
                break
    return skor

# PROSES 
stop_words = ["dan", "di", "ke", "dari", "yang", "adalah", "untuk", "dengan", "ini", "itu", "pada", "seperti", "-"]
karakter_unik = '+-=_\}{/*#@!`%$)(?:;'

dokumen_list = [
    pemisah_kata(my_list1[0]),
    pemisah_kata(my_list2[0]),
    pemisah_kata(my_list3[0]),
    pemisah_kata(my_list4[0]),
    pemisah_kata(my_list5[0]),
    pemisah_kata(my_list6[0]),
    pemisah_kata(my_list7[0]),
    pemisah_kata(my_list8[0]),
    pemisah_kata(my_list9[0]),
    pemisah_kata(my_list10[0]),
]

semua_kata = gabungkan_banyak_list_tanpa_duplikasi(dokumen_list)
semua_kata_bersih = hapus_stop_word(semua_kata, stop_words)
semua_kata_bersih1 = hapus_karakter_unik(semua_kata_bersih, karakter_unik)

idf = hitung_idf(dokumen_list, semua_kata_bersih1)
idf_bm25 = hitung_idf_bm25(dokumen_list, semua_kata_bersih1)

total_panjang_dokumen = 0
for d in dokumen_list:
    total_panjang_dokumen += panjang_dokumen(d)
avgdl = total_panjang_dokumen / hitung_panjang(dokumen_list)

# Fungsi proses query
def input_query(query, stop_words, karakter_unik):
    query_kecil = [ke_huruf_kecil(k) for k in query]
    query_bersih = hapus_stop_word(query_kecil, stop_words)
    query_bersih1 = hapus_karakter_unik(query_bersih, karakter_unik)
    return query_bersih1, []


kondisi = True
while kondisi:
    query = pemisah_kata(input("Masukkan query pencarian: "))
    query_bersih1, _ = input_query(query, stop_words, karakter_unik)

    bm25_scores = []
    for i in range(hitung_panjang(dokumen_list)):
        skor = hitung_bm25(dokumen_list[i], query_bersih1, semua_kata_bersih1, idf_bm25, avgdl)
        bm25_scores += [(i, skor)]

    for i in range(hitung_panjang(bm25_scores) - 1):
        for j in range(hitung_panjang(bm25_scores) - i - 1):
            if bm25_scores[j][1] < bm25_scores[j + 1][1]:
                bm25_scores[j], bm25_scores[j + 1] = bm25_scores[j + 1], bm25_scores[j]

    print("\nDokumen Paling Relevan (BM25):")
    for i in range(panjang_dokumen(dokumen_list)):
        if i >= hitung_panjang(bm25_scores):
            break
        indeks, skor = bm25_scores[i]
        judul_awal = eval(f"my_list{indeks + 1}[0]")
        if skor > 0:
            print(f"Dokumen {indeks + 1} : {judul_awal} (Skor BM25: {skor})")

    user = input('Masukkan query lagi? (y/n) : ').lower()
    if user == 'n':
        kondisi = False