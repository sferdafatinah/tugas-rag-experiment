# RAG Parameter Exploration

Pada eksperimen ini, saya mencoba memahami bagaimana perubahan beberapa parameter pada sistem Retrieval-Augmented Generation (RAG) dapat memengaruhi jawaban yang dihasilkan dari dokumen PDF. Parameter yang saya uji adalah Temperature, TOP_K, Chunk Size, dan Chunk Overlap.

Saya menggunakan dokumen dan dua pertanyaan yang sama selama pengujian agar hasilnya dapat dibandingkan. Dari percobaan ini, saya ingin mengetahui apakah perubahan parameter benar-benar membuat jawaban menjadi berbeda, bagaimana pengaruhnya terhadap jumlah chunk, serta konfigurasi mana yang paling sesuai untuk dokumen yang saya gunakan.

## 1. Informasi Eksperimen

- **Nama PDF:** Alih Wahana Data - kelompok 5 BINDO (5GAMD).pdf

- **Jumlah halaman PDF:** 14 halaman

- **Tujuan Eksprerimen:** Mengetahui pengaruh perubahan Temperature, TOP_K, Chunk Size, dan Chunk Overlap terhadap jawaban yang dihasilkan oleh sistem RAG.

- **Isi / topik PDF secara singkat:** Alih wahana data, yaitu proses mengubah informasi visual menjadi teks naratif atau deskriptif.

**Deskripsi Dokumen** : Dokumen ini merupakan file PDF dari PPT presentasi kelompok 5 kelas 5GAMD, yaitu kelompok saya, untuk mata kuliah Bahasa Indonesia. Materi yang dibahas adalah alih wahana data, yaitu proses mengubah informasi visual menjadi teks naratif atau deskriptif tanpa menghilangkan makna utamanya.

Isi presentasi mencakup beberapa materi berikut:

- Pengertian alih wahana data.
- Tahapan pengubahan informasi visual menjadi teks.
- Karakteristik infografis dan teks.
- Teknik transliterasi data.
- Tantangan dalam proses alih wahana data.

File ini digunakan sebagai dokumen sumber (knowledge source) dalam eksperimen RAG untuk menguji pengaruh perubahan parameter terhadap proses pengambilan informasi (retrieval) dan pembuatan jawaban (generation) berdasarkan materi presentasi yang diunggah.

## 2. Pertanyaan Pengujian

Dua pertanyaan berikut digunakan pada seluruh eksperimen.

### Pertanyaan 1

Apa yang dimaksud dengan alih wahana data berdasarkan materi yang telah saya unggah? Jelaskan dengan bahasa yang mudah dipahami.

### Pertanyaan 2

Informasi visual apa saja yang dapat diubah menjadi teks dalam proses alih wahana data?

## 3. Baseline Configuration

Baseline configuration adalah konfigurasi awal yang digunakan sebagai acuan sebelum saya mengubah parameter untuk setiap eksperimen.

- **Temperature:** 0.2
- **TOP_K:** 4
- **Chunk Size:** 100
- **Chunk Overlap:** 20
- **Embedding Model:** `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
- **LLM Model:** `openai/gpt-oss-120b`

Pada setiap eksperimen, saya hanya mengubah parameter yang sedang diuji, sedangkan parameter lainnya dipertahankan sesuai ketentuan. Cara ini membantu saya membandingkan hasil dengan lebih terarah.

## 4. Experiment 1 - Temperature

Pada eksperimen pertama, saya menguji Temperature dengan nilai 0.0, 0.2, dan 0.8. Parameter lainnya tetap menggunakan TOP_K = 4, CHUNK_SIZE = 100, dan CHUNK_OVERLAP = 20.

Temperature berkaitan dengan tingkat variasi dalam proses model menghasilkan jawaban. Karena itu, saya ingin melihat apakah perubahan nilai Temperature membuat susunan kalimat atau isi jawaban menjadi berbeda.

### A. Temperature = 0.0

**A.1. Actual Output**

**Pertanyaan 1:**
**Alih wahana data** adalah proses mengubah informasi visual—seperti grafik, diagram, bagan, ikon, angka, dan tata letak warna—menjadi rangkaian kalimat naratif atau deskriptif.  
Proses ini tidak sekadar “menulis ulang” angka menjadi kata; melainkan melibatkan:

1. **Membaca dan menafsirkan** setiap elemen visual secara teliti.
2. **Mengklasifikasikan** gagasan utama dan hierarki data.
3. **Merangkai ulang** informasi tersebut menjadi kalimat yang padu, jelas, dan tetap mempertahankan objektivitas serta esensi pesan asli.

Dengan cara ini, pesan yang tersampaikan melalui media visual dapat dipahami dalam bentuk teks tanpa kehilangan makna atau konteksnya.  
_(Sumber: Alih Wahana Data – kelompok 5 BINDO (5GAMD).pdf, halaman 3‑4)_

**Pertanyaan 2:**
Informasi visual yang dapat diubah menjadi teks dalam proses alih wahana data meliputi:

- Grafik (chart, diagram, bagan)
- Ikon
- Angka (data numerik)
- Tata letak warna dan elemen visual lainnya

(Sumber: _Alih Wahana Data – kelompok 5 BINDO (5GAMD).pdf_, halaman 4)

**A.2. Observation:**
Menurutku, saat pakai temperature 0.0, jawabannya kelihatan kaku banget dan bener-bener terpaku sama isi teks aslinya. Modelnya nggak berani mainin kata-kata lain, jadi hasilnya kaku tapi aman karena nggak melenceng dari dokumen.

---

### B. Temperature = 0.2

**B.1. Actual Output**
**Pertanyaan 1:**
**Alih wahana data** adalah proses mengubah informasi visual—seperti grafik, diagram, bagan, ikon, angka, dan tata letak warna—menjadi rangkaian kalimat naratif atau deskriptif.  
Proses ini tidak sekadar “menulis ulang” angka menjadi kalimat; melainkan melibatkan:

1. **Membaca dan menafsirkan** setiap elemen visual secara teliti.
2. **Mengklasifikasikan** gagasan utama dan hierarki data.
3. **Merangkai ulang** informasi tersebut dengan kaidah bahasa yang padu, tetap menjaga objektivitas dan esensi pesan asli.

Dengan cara ini, pesan yang tersampaikan dalam bentuk visual dapat dipahami lewat teks, sehingga informasi dapat diakses oleh orang yang lebih nyaman membaca narasi daripada melihat grafik. (Sumber: _Alih Wahana Data – kelompok 5 BINDO (5GAMD).pdf_, halaman 3‑4)

**Pertanyaan 2:**
Informasi visual yang dapat diubah menjadi teks dalam proses alih wahana data meliputi:

- Grafik (chart, diagram, bagan)
- Ikon
- Angka (data numerik)
- Tata letak warna dan elemen visual lainnya

(Sumber: _Alih Wahana Data – kelompok 5 BINDO (5GAMD).pdf_, halaman 4)

**B.2. Observation:**
Di angka 0.2 ini, bahasanya udah mulai agak luwes dikit tapi tetap akurat dan nggak ngawur. Makanya ini pas banget dijadiin baseline karena nggak kaku kayak 0.0 tapi juga nggak berlebihan.

---

### C. Temperature = 0.8

**C.1. Actual Output**
**Pertanyaan 1:**
**Alih wahana data** adalah proses mengubah informasi visual (seperti grafik, diagram, bagan, ikon, angka, dan tata letak warna) menjadi narasi tertulis yang jelas dan tetap mempertahankan esensi data.  
Prosesnya melibatkan:

1. **Membaca** semua elemen visual dengan teliti.
2. **Mengklasifikasikan** gagasan utama dan hubungan antar‑elemen.
3. **Menyusun** kalimat naratif yang padu, menggunakan kaidah bahasa yang baik, tanpa mengurangi objektivitas data.

Intinya, bukan sekadar menyalin angka ke kalimat, melainkan menerjemahkan makna visual menjadi teks yang dapat dipahami dengan mudah.  
_(Sumber: Alih Wahana Data – kelompok 5 BINDO, halaman 4)_

**Pertanyaan 2:**
Informasi visual yang dapat diubah menjadi teks dalam proses alih wahana data meliputi:

- **Grafik dan diagram** (mis. bar chart, pie chart, line graph)
- **Bagan dan ikon**
- **Angka** (data numerik)
- **Tata letak warna** (kontras, highlight)
- **Teks singkat** yang terintegrasi dalam visual (label, caption)

Semua unsur ini diidentifikasi, diterjemahkan, dan disusun menjadi kalimat naratif atau deskriptif, menjaga esensi data tanpa mengurangi objektivitas.  
_(Sumber: Alih Wahana Data – kelompok 5 BINDO (5GAMD).pdf, halaman 4, 3, 7, 9)_

**C.2. Observation:**
Saat nilai Temperature dinaikkan ke 0.8, respons yang dihasilkan oleh model menjadi jauh lebih ekspresif dengan variasi kosakata yang lebih kaya. Model tampak melakukan parafrase secara lebih bebas menggunakan gaya bahasanya sendiri, meskipun inti informasi yang disampaikan tetap merujuk dan bersumber secara akurat dari dokumen PDF yang sama.

### D. Kesimpulan Experiment Temperature

**1. Apa perubahan yang paling terlihat?**
Perubahan yang paling terlihat terletak pada gaya bahasa, variasi kosakata, dan tingkat kekakuan (determinisme) dari jawaban yang dihasilkan oleh LLM saat menjelaskan materi "Alih Wahana Data":

- **Pada Temperature 0.0:** Jawaban sangat kaku, deterministik, dan mekanis. LLM cenderung mengekstrak kalimat secara persis (_verbatim_) sesuai dengan teks asli di halaman 3 dan 4 dokumen, tanpa mencoba merangkai ulang dengan sinonim atau variasi gaya bahasa lain.

- **Pada Temperature 0.2:** Terlihat keseimbangan yang pas. Kalimat mengalir secara natural dan luwes saat menjelaskan proses transliterasi visual ke teks, namun strukturnya tetap sangat kuat terikat pada fakta-fakta yang ada di dokumen sumber.

- **Pada Temperature 0.8:** LLM mengambil kebebasan berkreasi yang lebih tinggi. Pilihan kosakata yang digunakan menjadi jauh lebih bervariasi (seperti penambahan frasa penjelas atau sinonim elemen visual), meskipun inti penjelasannya tetap merujuk pada dokumen yang sama.

**2. Menurut kalian nilai mana yang paling cocok untuk aplikasi RAG ini?**
Nilai **Temperature = 0.2**

**3. Kenapa?**
Dalam konteks aplikasi RAG untuk dokumen akademik atau materi presentasi (seperti materi "Alih Wahana Data"), tujuan utamanya adalah **keakuratan informasi dan kejelasan konsep**, bukan kreativitas bercerita. Nilai 0.2 memberikan titik temu terbaik: kalimatnya cukup natural dan mudah dipahami, tetapi tetap menjaga objektivitas dan kepatuhan yang tinggi terhadap isi dokumen PDF yang diunggah tanpa risiko melenceng dari materi kelompok.

---

## 5. Experiment 2 - TOP_K

Pada eksperimen kedua, saya menguji parameter TOP_K dengan nilai 1, 4 (baseline), dan 8. Parameter ini menentukan berapa banyak potongan dokumen (chunk) teratas yang ditarik dari Vector Database (Retrieval) untuk dijadikan referensi oleh LLM sebelum menjawab pertanyaan.

### A. TOP_K = 1

**A.1. Actual Output**
**Pertanyaan 1:**
Alih wahana data adalah proses mengubah informasi visual—seperti grafik, diagram, bagan, ikon, angka, dan tata letak warna—menjadi rangkaian kalimat naratif atau deskriptif.  
Proses ini tidak sekadar menyalin angka ke dalam kalimat; melainkan melibatkan analisis mendalam:

1. Membaca dan memahami tanda visual secara teliti.
2. Mengklasifikasikan gagasan utama yang terkandung.
3. Merangkai ulang informasi tersebut dengan kaidah bahasa yang padu, tetap menjaga objektivitas data.

Dengan kata lain, alih wahana data mengubah “gambar” menjadi “kata” sambil mempertahankan makna dan keakuratan data. (Sumber: Alih Wahana Data – kelompok 5 BINDO, halaman 4)

**Pertanyaan 2:**
Informasi visual yang dapat diubah menjadi teks dalam proses alih wahana data meliputi:

- grafik
- diagram
- bagan
- ikon
- angka
- tata letak warna

(Sumber: _Alih Wahana Data – kelompok 5 BINDO (5GAMD).pdf_, halaman 4)

**A.2. Sources / Similarity Score**

- **Pertanyaan 1:** Halaman 4 (Score: 0.7119)
- **Pertanyaan 2:** Halaman 4 (Score: 0.7838)

**A.3. Observation**
Karena sistem hanya menarik 1 _chunk_ dokumen teratas, informasi yang diterima oleh LLM menjadi sangat terbatas. Model tidak memiliki konteks pendukung dari halaman sebelum atau sesudahnya, sehingga cakupan jawaban menjadi kurang mendalam.

---

### B. TOP_K = 4 (Baseline)

**B.1. Actual Output**
**Pertanyaan 1:**
**Alih wahana data** adalah proses mengubah informasi visual—seperti grafik, diagram, bagan, ikon, angka, dan tata letak warna—menjadi rangkaian kalimat naratif atau deskriptif.  
Proses ini tidak sekadar “menulis ulang” angka menjadi kata; melainkan memerlukan analisis mendalam:

1. **Membaca dan mengidentifikasi** semua unsur visual (judul, ikon, grafik, warna, dll.) dan makna masing‑masingnya.
2. **Mengklasifikasikan** gagasan utama dan detail pendukung, menata hierarki informasi.
3. **Merangkai ulang** dengan kaidah bahasa yang padu, tetap menjaga objektivitas dan esensi pesan.

Tujuannya agar pesan yang tersampaikan melalui visual tetap utuh ketika diubah ke bentuk teks.  
_(Sumber: Alih Wahana Data – kelompok 5 BINDO (5GAMD).pdf, halaman 3‑4)_

**Pertanyaan 2:**
Informasi visual yang dapat diubah menjadi teks dalam proses alih wahana data meliputi:

- Grafik (diagram batang, garis, pie, dll.)
- Diagram dan bagan
- Ikon atau simbol visual
- Angka dan nilai numerik
- Tata letak warna dan skema warna
- Judul, sub‑judul, dan keterangan visual
- Elemen visual lain seperti ikon, gambar, dan layout yang menyampaikan makna (mis. pola atau tren visual)

Semua unsur ini diidentifikasi dan kemudian diterjemahkan ke dalam narasi atau deskripsi teks yang tetap mempertahankan esensi data.  
**Sumber:** _Alih Wahana Data – kelompok 5 BINDO (5GAMD).pdf_, halaman 4.

**B.2. Sources / Similarity Score**

- **Pertanyaan 1:** Halaman 4 (0.7119), Halaman 3 (0.6548), Halaman 3 (0.6178), Halaman 9 (0.6038)
- **Pertanyaan 2:** Halaman 4 (0.7838), Halaman 3 (0.7619), Halaman 7 (0.7252), Halaman 9 (0.7088)

**B.3. Observation:**
Konfigurasi `TOP_K = 4` memberikan hasil yang paling seimbang dan ideal. Sistem berhasil menarik 4 potongan teks terbaik yang saling melengkapi antar halaman (seperti memadukan halaman 3 dan 4). LLM mendapatkan porsi konteks yang cukup kaya untuk menyusun jawaban secara utuh, terstruktur, dan mendalam tanpa mengalami kelebihan muatan data ataupun kekurangan informasi referensi.

---

### C. TOP_K = 8

**C.1. Actual Output**

**Pertanyaan 1:**
**Alih wahana data** adalah proses mengubah informasi yang disajikan secara visual—seperti grafik, diagram, ikon, dan warna—menjadi teks naratif atau deskriptif yang tetap mempertahankan makna dan esensi data tersebut.  
Prosesnya meliputi:

1. **Identifikasi elemen visual** (judul, ikon, angka, warna, dll.)
2. **Klasifikasi dan hierarki informasi** (gagasan utama vs. rincian)
3. **Penyusunan kalimat naratif** yang terstruktur dan jelas
4. **Parafrase** visual menjadi kata kerja atau penjelasan
5. **Verifikasi akurasi** agar tetap objektif (Knaflic, 2015)

Tujuannya agar data visual dapat diakses, diarsipkan, dan dipahami oleh pembaca dengan latar belakang literasi berbeda (Siricharoen, 2021).  
_Source: Alih Wahana Data – kelompok 5 BINDO (5GAMD).pdf, pages 3‑4, 8‑9._

**Pertanyaan 2:**
Informasi visual yang dapat diubah menjadi teks dalam proses alih wahana data meliputi:

- Grafik (diagram, bagan, chart)
- Ikon
- Angka (data numerik)
- Tata letak warna (penekanan visual)

Semua elemen ini diidentifikasi dan kemudian diterjemahkan menjadi kalimat naratif atau deskriptif (sumber: _Alih Wahana Data – kelompok 5 BINDO (5GAMD)_, halaman 4).

**C.2. Sources / Similarity Score**

- **Pertanyaan 1:** Halaman 4 (0.7119), Halaman 3 (0.6548), Halaman 3 (0.6178), Halaman 9 (0.6038), Halaman 8 (0.5880), Halaman 8 (0.5835), Halaman 7 (0.5479), Halaman 6 (0.5100)
- **Pertanyaan 2:** Halaman 4 (0.7838), Halaman 3 (0.7619), Halaman 7 (0.7252), Halaman 9 (0.7088), Halaman 8 (0.6202), Halaman 6 (0.6012), Halaman 3 (0.5574), Halaman 8 (0.4582)

**C.3. Observation**
Ketika nilai `TOP_K` dinaikkan menjadi 8, sistem menarik terlalu banyak potongan teks sekaligus. Terlihat dari _similarity score_ bahwa dokumen pada peringkat bawah memiliki tingkat kemiripan yang sudah sangat rendah (turun hingga 0.45). Akibatnya, dokumen-dokumen tambahan ini berubah menjadi _noise_ yang mengaburkan fokus model, membuat struktur jawaban pada Pertanyaan 1 menjadi terlalu padat dan kurang terarah.

---

### Kesimpulan Experiment TOP_K

**Apakah TOP_K yang lebih besar selalu menghasilkan jawaban yang lebih baik?**
**Tidak.** Penarikan dokumen yang terlalu banyak (seperti TOP*K = 8) justru memasukkan potongan teks yang kurang relevan (\_noise*), yang dapat mengaburkan fokus LLM dalam menyusun jawaban.

**Menurut kalian, TOP_K mana yang paling cocok untuk PDF yang digunakan?**
Nilai **TOP_K = 4** (Baseline).

**Kenapa?**
Nilai 4 memberikan titik keseimbangan yang optimal. Pada TOP_K = 1, informasi terlalu sempit, sedangkan pada TOP_K = 8 terlalu banyak gangguan. Dengan TOP_K = 4, skor kemiripan dokumen masih berada di kisaran yang sangat relevan (0.60 hingga 0.78), memungkinkan model merangkum isi materi presentasi dengan akurat dan rapi.

---

## 6. Experiment 3 - Chunk Size

Eksperimen ini menguji pengaruh ukuran potongan teks (_chunk size_) terhadap hasil retrieval dan kualitas jawaban RAG. Sesuai ketentuan, parameter yang diuji adalah `CHUNK_SIZE = 50`, `CHUNK_SIZE = 100` (Baseline), dan `CHUNK_SIZE = 120` dengan nilai `CHUNK_OVERLAP` yang dibuat sama. Setiap kali mengubah ukuran chunk di `config.py`, aku melakukan proses ingestion ulang dengan langkah-langkah berikut:

1. Mematikan server (`Ctrl + C`).
2. Menghapus folder `qdrant_data/` agar database lama bersih dari sisa eksperimen sebelumnya.
3. Menjalankan server kembali dan mengunggah PDF yang sama.
4. Mencatat jumlah _chunks stored_ yang dihasilkan setelah proses ingestion.

### A. CHUNK_SIZE = 50

**A.1. Actual Output:**
**Pertanyaan 1:**
**Alih wahana data** adalah proses mengubah informasi visual—seperti grafik, diagram, bagan, ikon, angka, dan tata letak warna—menjadi rangkaian kalimat naratif atau deskriptif. Dengan kata lain, alih wahana data memindahkan “bentuk” visual menjadi “kata” sehingga orang yang membaca dapat memahami data tanpa harus melihat visual asli.

_(Sumber: Alih Wahana Data – kelompok 5 BINDO (5GAMD).pdf, halaman 4)_

**Pertanyaan 2:**
Informasi visual yang dapat diubah menjadi teks dalam proses alih wahana data meliputi:

- **Gambar** (mis. foto, ilustrasi)
- **Grafik** (diagram batang, garis, pie, dll.)
- **Ikon**
- **Angka** (data numerik yang ditampilkan)
- **Tata letak warna** (penggunaan warna untuk menekankan atau mengelompokkan data)

Semua unsur ini dapat ditransliterasi menjadi kalimat naratif atau deskriptif.  
(Sumber: _Alih Wahana Data – kelompok 5 BINDO (5GAMD)_, halaman 7)

** A.2. Chunks Stored & Retrieved:**

- _Chunks Stored:_ 33 chunks (dari 14 halaman)
- _Chunks Retrieved:_ 4 chunks (dengan `TOP_K = 4`)

**A.3. Actual Output & Score:**

- Pertanyaan 1: Rank 1 | Score: 0.6865 | Halaman: 4 (disusul halaman 9, 8, dan 3)
- Pertanyaan 2: Rank 1 | Score: 0.7433 | Halaman: 7 (disusul halaman 4, 9, dan 3)

**A.4. Observation**
Ketika `CHUNK_SIZE` diatur kecil yaitu 50, jumlah total _chunks stored_ melonjak menjadi 33 chunks. Hal ini karena teks di dalam PDF materi presentasi dipecah secara sangat agresif dan terkotak-kotak dalam ukuran kecil. Dampaknya, beberapa konteks kalimat penting menjadi terpotong di tengah jalan antar-chunk. Model kehilangan keutuhan alur paragraf, sehingga pemahaman terhadap materi "Alih Wahana Data" menjadi kurang utuh dan _similarity score_ di tingkat teratas tampak lebih rendah (0.68 dan 0.74).

### B. CHUNK_SIZE = 100 (Baseline)

**B.1. Actual Output:**
**Pertanyaan 1:**
**Alih wahana data** adalah proses mengubah informasi visual—seperti grafik, diagram, bagan, ikon, angka, dan tata letak warna—menjadi rangkaian kalimat naratif atau deskriptif.  
Proses ini tidak sekadar “menuliskan angka” saja; melainkan melibatkan:

1. **Membaca dan menafsirkan** setiap unsur visual secara teliti.
2. **Mengklasifikasikan** gagasan utama dan hierarki data.
3. **Merangkai ulang** informasi tersebut menjadi kalimat yang padu, jelas, dan tetap mempertahankan objektivitas serta esensi pesan asli.

Dengan kata lain, alih wahana data adalah konversi media informasi dari bentuk visual ke bentuk teks, sambil menjaga makna, konteks, dan pola visual yang ada.  
_(Sumber: Alih Wahana Data – kelompok 5 BINDO (5GAMD).pdf, halaman 3‑4)_

**Pertanyaan 2:**
Informasi visual yang dapat diubah menjadi teks dalam proses alih wahana data meliputi:

- Grafik (chart, diagram, bagan)
- Ikon
- Angka (data numerik)
- Tata letak warna (skema warna, highlight)

Semua elemen ini diidentifikasi, dipahami maknanya, dan kemudian diterjemahkan ke dalam rangkaian kalimat naratif atau deskriptif.  
**Sumber:** _Alih Wahana Data – kelompok 5 BINDO (5GAMD).pdf_, halaman 4.

**B.2. Chunks Stored & Retrieved:**

- _Chunks Stored:_ 18 chunks (dari 14 halaman)
- _Chunks Retrieved:_ 4 chunks (dengan `TOP_K = 4`)

**B.3. Actual Output & Score:**

- Pertanyaan 1: Rank 1 | Score: 0.7119 | Halaman: 4 (disusul halaman 3, 3, dan 9)
- Pertanyaan 2: Rank 1 | Score: 0.7838 | Halaman: 4 (disusul halaman 3, 7, dan 9)

**B.4. Observation:**
Ukuran 100 terbukti sangat pas dan ideal untuk karakteristik file PDF presentasi. Total _chunks stored_ yang dihasilkan adalah 18 chunks . Kalimat materi dapat tetap utuh berada di dalam satu potongan paragraf yang bermakna jelas tanpa ada pemotongan kata atau poin penjelasan yang terputus secara janggal. Skor kemiripannya juga jauh lebih tinggi dan stabil (mencapai 0.71 hingga 0.78), sehingga LLM mampu merangkum jawaban dengan sangat akurat dan terstruktur rapi.

### C. CHUNK_SIZE = 120

**C.1. Actual Output:**
**Pertanyaan 1:**
Alih wahana data adalah proses mengubah informasi visual—seperti grafik, diagram, ikon, angka, dan tata letak warna—menjadi rangkaian kalimat naratif atau deskriptif.  
Prosesnya tidak sekadar menyalin angka ke dalam kalimat; melainkan melibatkan:

1. **Membaca dan mengidentifikasi** semua unsur visual (judul, ikon, grafik, warna, dll.)
2. **Mengklasifikasikan** gagasan utama dan informasi pendukung menurut hierarki pentingnya
3. **Merangkai ulang** informasi tersebut menjadi kalimat yang padu, jelas, dan tetap objektif
4. **Memverifikasi** akurasi dan konsistensi istilah dengan data asli

Dengan cara ini, esensi pesan dari infografis tetap terjaga meskipun bentuknya berubah menjadi teks.  
(Sumber: Alih Wahana Data – kelompok 5 BINDO, halaman 3‑4, 8)

**Pertanyaan 2:**
Informasi visual yang dapat diubah menjadi teks dalam proses alih wahana data meliputi:

- Grafik (diagram batang, garis, pie, dll.)
- Diagram dan bagan
- Ikon atau simbol visual
- Angka dan nilai numerik
- Tata letak warna dan elemen desain visual lainnya
- Judul, keterangan, dan teks singkat yang ada di infografis

(Sumber: _Alih Wahana Data – kelompok 5 BINDO (5GAMD)_, halaman 4)

**C.2. Chunks Stored & Retrieved:**

- _Chunks Stored:_ 15 chunks (dari 14 halaman)
- _Chunks Retrieved:_ 4 chunks (dengan `TOP_K = 4`)

**C.3. Actual Output & Score:**

- Pertanyaan 1: Rank 1 | Score: 0.7119 | Halaman: 4 (disusul halaman 3, 3, dan 8)
- Pertanyaan 2: Rank 1 | Score: 0.7838 | Halaman: 4 (disusul halaman 3, 7, dan 9)

**C.4. Observation:**
Karena ukuran per potongannya diperbesar menjadi 120 karakter, jumlah total chunk yang tersimpan di dalam database menyusut menjadi hanya 15 chunks . Setiap bagian merangkum teks yang jauh lebih panjang. Meskipun skor kemiripannya mirip dengan baseline, informasi di dalam satu chunk menjadi terlalu padat, sehingga ketika ditarik oleh sistem, model membaca cakupan teks yang terlalu luas dan kurang spesifik pada poin tertentu.

### D. Kesimpulan Experiment Chunk Size

**1. Bagaimana pengaruh perubahan Chunk Size terhadap jumlah chunk yang dihasilkan?**
Semakin kecil nilai _Chunk Size_ (misal 50), jumlah _chunks stored_ akan semakin banyak (33 chunks) karena dokumen dipotong secara lebih sering . Sebaliknya, semakin besar nilainya (misal 120), jumlah total _chunks stored_ akan semakin sedikit (15 chunks) .

**2. Chunk Size mana yang paling optimal untuk dokumen ini?**
Nilai **CHUNK_SIZE = 100** (Baseline).

**3. Kenapa?**
Ukuran 100 memberikan porsi pemotongan yang paling seimbang untuk dokumen slide presentasi akademik . Ukuran 50 terlalu kecil dan merusak struktur kalimat, sedangkan ukuran 120 terlalu luas. Dengan ukuran 100, informasi terjaga utuh dalam 18 chunks dengan kualitas _similarity score_ dan susunan jawaban yang paling akurat .

## 7. Experiment 4 - Chunk Overlap

Eksperimen terakhir ini menguji pengaruh nilai irisan (_overlap_) antar-chunk terhadap kesinambungan informasi teks. Sesuai ketentuan, parameter yang diuji adalah `CHUNK_OVERLAP = 0`, `CHUNK_OVERLAP = 20` (Baseline), dan `CHUNK_OVERLAP = 40` dengan menetapkan `CHUNK_SIZE = 100` untuk seluruh percobaan ini. Sama seperti eksperimen sebelumnya, setiap kali mengubah nilai overlap di `config.py`, aku melakukan langkah-langkah: menghapus folder `qdrant_data/`, merestart aplikasi, lalu mengunggah ulang PDF untuk proses _ingestion_ agar hasilnya tidak tercampur.

### A. CHUNK_OVERLAP = 0

**A.1. Actual Output:**
**Pertanyaan 1:**
Alih wahana data adalah proses mengubah informasi visual—seperti grafik, diagram, bagan, ikon, angka, dan tata letak warna—menjadi rangkaian kalimat naratif atau deskriptif.  
Proses ini tidak sekadar menyalin angka ke dalam kalimat; melainkan melibatkan:

1. **Pembacaan visual** – mengenali semua unsur visual dan maknanya.
2. **Klasifikasi gagasan utama** – mengelompokkan informasi berdasarkan kepentingan dan hubungan antar elemen.
3. **Penyusunan kalimat** – merangkai ulang data menjadi kalimat yang jelas, terstruktur, dan tetap objektif.

Tujuannya adalah menjaga esensi pesan asli sambil mempresentasikannya dalam bentuk teks yang mudah dipahami.  
(Sumber: _Alih Wahana Data - kelompok 5 BINDO (5GAMD).pdf_, halaman 3‑4)

**Pertanyaan 2:**
Informasi visual yang dapat diubah menjadi teks dalam proses alih wahana data meliputi:

- Grafik (chart, diagram, bagan)
- Ikon
- Angka (data numerik)
- Tata letak warna dan elemen visual lainnya

(Sumber: _Alih Wahana Data – kelompok 5 BINDO (5GAMD)_, halaman 4)

**A.2. Chunks Stored & Retrieved:**

- _Chunks Stored:_ 18 chunks (dari 14 halaman)
- _Chunks Retrieved:_ 4 chunks (dengan `TOP_K = 4`)

**A.3. Actual Output & Score:**

- Pertanyaan 1: Rank 1 | Score: 0.7119 | Halaman: 4 (disusul halaman 3, 8, dan 3)
- Pertanyaan 2: Rank 1 | Score: 0.7838 | Halaman: 4 (disusul halaman 3, 7, dan 9)

**A.4. Observation:**
Saat `CHUNK_OVERLAP` diatur 0, pemotongan teks antar-chunk menjadi terisolasi sepenuhnya tanpa ada irisan kata yang berulang. Berdasarkan hasil pengujian, batas pemotongan kalimat menjadi terasa kaku. Ada risiko nyata bahwa frasa atau poin penting materi "Alih Wahana Data" yang berada persis di ujung baris terpotong secara terpisah, sehingga transisi pemahaman makna antar-halaman menjadi kurang mulus.

### B. CHUNK_OVERLAP = 20 (Baseline)

**B.1. Actual Output:**
**Pertanyaan 1:**
**Alih wahana data** adalah proses mengubah informasi visual—seperti grafik, diagram, bagan, ikon, angka, dan tata letak warna—menjadi rangkaian kalimat naratif atau deskriptif.  
Proses ini tidak sekadar “menulis ulang” angka menjadi teks; melainkan melibatkan:

1. **Membaca dan menafsirkan** setiap elemen visual secara teliti.
2. **Mengklasifikasikan** gagasan utama dan hierarki data.
3. **Merangkai ulang** informasi tersebut dengan kaidah bahasa yang padu, tetap menjaga objektivitas dan esensi pesan asli.

Dengan cara ini, pesan yang tersampaikan melalui media visual dapat dipahami dalam bentuk teks yang jelas dan terstruktur.  
_(Sumber: Alih Wahana Data – kelompok 5 BINDO (5GAMD).pdf, halaman 3‑4)_

**Pertanyaan 2:**
Informasi visual yang dapat diubah menjadi teks dalam proses alih wahana data meliputi:

- **Grafik** (mis. bar, pie, line)
- **Diagram** (mis. flowchart, diagram jaringan)
- **Bagan** (mis. tabel, diagram Venn)
- **Ikon** dan simbol visual lainnya
- **Angka** dan nilai numerik yang ditampilkan
- **Tata letak warna** (kontras, highlight)
- **Judul** dan **keterangan** (caption)
- **Teks singkat** yang sudah ada di infografis (mis. label, legend)

Semua unsur ini diidentifikasi, dicatat, dan kemudian diterjemahkan ke dalam kalimat naratif atau deskriptif tanpa mengurangi objektivitas data【Page: 4】【Page: 3】.

**B.2. Chunks Stored & Retrieved:**

- _Chunks Stored:_ 18 chunks (dari 14 halaman)
- _Chunks Retrieved:_ 4 chunks (dengan `TOP_K = 4`)

**B.3. Actual Output & Score:**

- Pertanyaan 1: Rank 1 | Score: 0.7119 | Halaman: 4 (disusul halaman 3, 3, dan 9)
- Pertanyaan 2: Rank 1 | Score: 0.7838 | Halaman: 4 (disusul halaman 3, 7, dan 9)

**B.4. Observation:**
Nilai overlap 20 terbukti bekerja secara sangat efektif sebagai "jembatan" penghubung antar-chunk. Irisan beberapa kata di akhir dan awal potongan memastikan bahwa konteks kalimat materi presentasi tetap menyambung dengan utuh tanpa membuat jumlah total chunk membengkak. Hasil jawaban yang diberikan LLM menjadi jauh lebih natural dan terstruktur rapi.

### C. CHUNK_OVERLAP = 40

**C.1. Actual Output:**
**Pertanyaan 1:**
Alih wahana data adalah proses mengubah informasi visual—seperti grafik, diagram, bagan, ikon, angka, dan tata letak warna—menjadi rangkaian kalimat naratif atau deskriptif.  
Proses ini tidak sekadar “memindahkan angka ke kalimat”; ia melibatkan:

1. Membaca tanda visual secara teliti.
2. Mengklasifikasikan gagasan utama.
3. Merangkai ulang dengan kaidah kebahasaan yang padu, tanpa mengurangi objektivitas data.

Dengan demikian, esensi pesan tetap terjaga meskipun bentuknya berubah (sumber: _Alih Wahana Data - kelompok 5 BINDO (5GAMD).pdf_, halaman 4).

**Pertanyaan 2:**
Informasi visual yang dapat diubah menjadi teks dalam proses alih wahana data meliputi:

- Grafik
- Diagram
- Bagan
- Ikon
- Angka
- Tata letak warna

(Sumber: _Alih Wahana Data – kelompok 5 BINDO (5GAMD)_, halaman 4)

**C.2. Chunks Stored & Retrieved:**

- _Chunks Stored:_ 19 chunks (dari 14 halaman)
- _Chunks Retrieved:_ 4 chunks (dengan `TOP_K = 4`)

**C.3. Actual Output & Score:**

- Pertanyaan 1: Rank 1 | Score: 0.7119 | (duplikasi chunk pada rank 1-2 dan rank 3-4)
- Pertanyaan 2: Rank 1 | Score: 0.7838 | (duplikasi chunk pada rank 1-2 dan rank 3-4)

**C.4. Observation:**
Ketika overlap dibesarkan menjadi 40, terjadi redundansi atau pengulangan data yang cukup signifikan di dalam database, yang membuat jumlah _chunks stored_ naik menjadi 19 chunks. Dampak buruknya terlihat jelas di terminal: sistem menarik potongan teks yang kembar (rank 1 & 2 memiliki skor dan halaman yang sama persis), sehingga kuota `TOP_K` terbuang sia-sia untuk data yang berulang.

### D. Kesimpulan Experiment Chunk Overlap

**1. Bagaimana pengaruh perubahan Chunk Overlap terhadap hasil Retrieval?**
Jika overlap terlalu kecil (0), transisi teks rentan terputus. Sebaliknya, jika terlalu besar (40), terjadi duplikasi data (_redundancy_) yang membuat sistem menarik _chunk_ kembar dan mengurangi variasi informasi.

**2. Chunk Overlap mana yang paling optimal?**
Nilai **CHUNK_OVERLAP = 20** (Baseline).

**3. Kenapa?**
Nilai 20 memberikan porsi irisan yang pas untuk menyambungkan konteks antar-halaman tanpa memicu duplikasi data di vector database, sehingga performa penarikan dokumen menjadi sangat efisien dan akurat.

---

## 8. Final Configuration

Setelah seluruh eksperimen, pilih konfigurasi yang menurut kalian menghasilkan hasil terbaik untuk PDF yang digunakan.

- **Temperature:** 0.2
- **TOP_K:** 4
- **Chunk Size:** 100
- **Chunk Overlap:** 20

---

**Alasan pemilihan konfigurasi:**
Alasan mengapa aku memilih kombinasi konfigurasi ini (`Temperature = 0.2`, `TOP_K = 4`, `Chunk Size = 100`, dan `Chunk Overlap = 20`) adalah karena konfigurasi ini memberikan performa yang paling seimbang dan akurat untuk jenis dokumen PDF presentasi (_slide_ materi kuliah) yang aku gunakan:

1. **Temperature = 0.2:** Nilai ini dipilih karena berada di titik tengah yang ideal. Saat diuji pada angka 0.0, respons model terlalu kaku dan mekanis. Sebaliknya, pada angka 0.8, model terlalu bebas berkreasi sehingga memunculkan risiko halusinasi. Temperature 0.2 menjaga agar jawaban tetap objektif dan sangat patuh pada fakta dokumen, namun bahasanya tetap mengalir secara natural dan enak dibaca.

2. **TOP_K = 4:** Jumlah penarikan 4 dokumen teratas terbukti paling pas. Ketika menggunakan `TOP_K = 1`, informasi yang didapat terlalu sempit tanpa konteks pendukung. Ketika dinaikkan menjadi `TOP_K = 8`, sistem justru menarik dokumen dengan skor kemiripan yang sangat rendah (hingga 0.45), yang akhirnya berubah menjadi _noise_ dan mengaburkan fokus AI. Dengan nilai 4, LLM mendapatkan porsi referensi multi-halaman yang kaya dan saling melengkapi (seperti memadukan halaman 3 dan 4) tanpa kelebihan beban data.

3. **Chunk Size = 100:** Ukuran ini sangat pas untuk memecah struktur dokumen presentasi. Jika ukuran dibuat kecil (50), kalimat terpecah terlalu agresif sehingga konteks makna paragraf rusak. Jika diperbesar (120), isi chunk menjadi terlalu luas dan kurang spesifik. Ukuran 100 menghasilkan 18 _chunks stored_ yang menjaga keutuhan kalimat secara optimal.

4. **Chunk Overlap = 20:** Nilai irisan 20 bekerja secara sempurna sebagai "jembatan" transisi antar-potongan teks. Tanpa overlap (0), batas antar kalimat rentan terputus kaku, sedangkan jika terlalu besar (40), justru memicu duplikasi data (_redundancy_) di database. Overlap 20 menjaga kesinambungan makna informasi antar halaman dengan sangat efisien.

## 9. Final Questions

### 1. Parameter mana yang paling terasa memengaruhi hasil aplikasi kalian?

Menurutku parameter yang paling berdampak langsung adalah **Chunk Size** dan **TOP_K**. _Chunk Size_ menentukan seberapa utuh informasi mentah yang bisa ditangkap oleh sistem, sedangkan _TOP_K_ menentukan seberapa banyak referensi halaman yang diizinkan masuk untuk dibaca oleh LLM.

### 2. Apakah Temperature memengaruhi Retrieval atau Generation? Jelaskan.

Temperature hanya memengaruhi proses **Generation**. Parameter ini sama sekali tidak mengubah cara sistem mencari dokumen di _vector database_ (retrieval), melainkan murni mengontrol tingkat kreativitas, variasi kosakata, dan fleksibilitas model saat merangkai kata-kata jawabannya.

### 3. Apakah TOP_K yang lebih besar selalu menghasilkan jawaban yang lebih baik?

Tidak selalu. Berdasarkan eksperimen, menaikkan `TOP_K` menjadi 8 justru memasukkan dokumen dengan skor kemiripan yang sangat rendah (hingga 0.45), yang malah berubah menjadi _noise_ dan membuat model bingung menyusun struktur jawaban.

### 4. Apa yang terjadi ketika Chunk Size dibuat lebih kecil?

Jumlah _chunks stored_ akan melonjak drastis (menjadi 33 chunks), tetapi struktur kalimat di dalam dokumen PDF materi presentasi menjadi terpotong secara terlalu agresif, sehingga AI sering kehilangan konteks utuh dari sebuah paragraf.

### 5. Setelah melakukan eksperimen, apa fungsi Chunk Overlap menurut pemahaman kalian?

Chunk Overlap berfungsi sebagai "jembatan penghubung" atau irisan kata antar potongan teks (_chunk_). Fungsinya untuk memastikan bahwa makna kalimat yang berada tepat di batas pemotongan tidak terputus, sehingga kesinambungan informasi dari satu halaman ke halaman berikutnya tetap terjaga.

### 6. Kenapa perubahan Chunk Size dan Chunk Overlap membutuhkan ingestion ulang?

Karena kedua parameter tersebut bekerja di tahap awal pengolahan data (_data preparation_). Mereka mengubah struktur fisik bagaimana file PDF dipotong-potong sebelum akhirnya diubah menjadi vektor dan disimpan ke dalam _vector database_ (Qdrant).

### 7. Kenapa perubahan Temperature tidak membutuhkan ingestion ulang?

Karena Temperature adalah parameter inferensi yang hanya dipanggil pada tahap akhir saat LLM (Groq) sedang memproses _prompt_ untuk menghasilkan teks, sehingga tidak ada hubungannya dengan isi penyimpanan di dalam database.

### 8. Menurut kalian, apakah ada satu konfigurasi RAG yang akan selalu paling bagus untuk semua jenis dokumen?

Menurutku tidak ada satu konfigurasi yang pasti benar untuk semua dokumen. Pengaturan RAG harus selalu disesuaikan dengan karakteristik fisik dokumen aslinya—misalnya, dokumen berupa novel teks panjang tentu membutuhkan strategi _chunking_ yang berbeda dibandingkan slide presentasi materi kuliah yang singkat dan berbasis poin-poin.

---

## 10. Personal Reflection

### Bagian eksperimen mana yang hasilnya paling berbeda dari dugaan kalian?

Bagian eksperimen _Chunk Overlap_ (khususnya saat dicoba di angka 40). Awalnya aku mengira semakin besar nilai overlap maka informasi akan semakin lengkap, tapi ternyata malah bikin _chunks_ jadi kembar (_redundant_) dan membuat sistem menarik data yang duplikat di terminal.

### Parameter mana yang awalnya kalian anggap tidak terlalu penting tetapi ternyata berpengaruh?

Awalnya aku kira _Chunk Overlap_ adalah parameter sepele yang bisa diabaikan atau dibiarkan nol. Ternyata setelah diuji, tanpa adanya overlap yang pas, transisi kalimat antar-halaman jadi terasa kaku dan kurang natural.

### Setelah mengerjakan tugas ini, bagaimana kalian menjelaskan hubungan antara Retrieval dan Generation pada RAG?

Keduanya saling bergantung layaknya proses "mencari referensi buku di perpustakaan lalu merangkumnya". _Retrieval_ bertugas mencari potongan informasi paling relevan dari dokumen yang diunggah, sedangkan _Generation_ bertugas membaca hasil pencarian tersebut untuk menyusun kalimat jawaban yang mudah dipahami oleh pengguna.

### Jika aplikasi ini dikembangkan lebih lanjut, parameter atau bagian apa lagi yang ingin kalian coba?

Aku penasaran pengen coba ganti model kecerdasan buatan (_model bahasa/embedding_) yang buat baca dokumennya supaya bisa lebih pintar nangkap berbagai bahasa. Selain itu, aku juga pengen coba nambahin fitur gabungan pencarian,jadi sistemnya nggak cuma nyari arti kalimatnya aja kayak sekarang, tapi juga bisa nyari berdasarkan kecocokan kata persis yang diketik (_keyword_), biar hasil pencarian datanya makin pas dan akurat.

## 11. AI Usage

**AI tools yang digunakan**
ChatGPT, Gemini API (untuk percobaan awal), dan Groq API (sebagai LLM utama).

**AI digunakan untuk membantu bagian apa?**
Membantu proses _setup_ awal repositori (_cloning_) dan sebagai teman diskusi untuk mencocokkan logika hasil evaluasi.

**Bagian eksperimen mana yang kalian lakukan dan evaluasi sendiri?**
Seluruh rangkaian teknis eksperimen, pencatatan data terminal, serta analisis hasil observasi dilakukan secara mandiri.

Jujur, untuk urusan _tools_ AI di tugas ini, perjalanan awalnya lumayan berliku. Awalnya aku coba _setup_ pakai Groq, tapi begitu instalasinya selesai dan belum sampai masukin API Key, aku tiba-tiba kepikiran pengen ganti pakai Gemini API aja karena sebelumnya aku udah sempat riset-riset tentang itu. Sayangnya, pas udah pakai Gemini, malah muncul _error_ yang udah aku coba atasi tapi tetap nggak bisa jalan. Anehnya, _error_ ini bukan karena gagal nyambung ke API Key-nya, melainkan entah ada salah di bagian mana yang aku kurang paham. Di _dashboard_ API Gemini-nya kelihatan ada _error_ pas aku lagi tes _running_ perintah `python -m uvicorn main:app`. Proses _running_-nya juga lama banget, aku sampai bingung ini _stuck_ atau emang lagi _loading_, dan aku sempat ngabisin waktu berjam-jam cuma buat nungguin itu. Akhirnya, nyerah deh dan balik lagi pakai Groq. Ternyata pakai Groq ini prosesnya jauh lebih cepat dan mulus, makanya pada akhirnya aku mutusin pakai Groq aja untuk API Key-nya.

Kalau untuk AI yang ngebantu proses pengerjaan tugas secara umum, aku pakai ChatGPT, terutama buat ngebantuin _setup_ di awal-awal. Kayak waktu harus ngambil _repository_ dari Bang Arifian, karena aku belum pernah ngelakuin itu sebelumnya, jadi aku minta tolong AI buat kasih panduan _step-by-step_-nya.

Nah, kalau untuk bagian eksperimen RAG-nya sendiri, semuanya murni aku lakuin sendiri tanpa bantuan AI. Mulai dari ngejalanin server, ngubah _config_, sampai ngevaluasi hasil observasinya, semua aku ketik berdasarkan apa yang bener-bener muncul di layarku. Jadi, setelah aku selesai nulis poin-poin menurut bahasaku sendiri, baru deh aku coba tanya ke AI untuk ngecek _cross-check_: apakah pemahamanku dan evaluasi yang udah aku tulis itu sebenarnya udah benar secara konsep atau ada yang kurang logis. Gitu sih kurang lebihnya..
