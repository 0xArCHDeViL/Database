import re
import os

css_front = """<style>
.frontcard{font-family:-apple-system,'Hiragino Sans','Yu Gothic',sans-serif;
  background:#ffffff !important;color:#18181b !important;
  padding:26px 20px;border-radius:12px;text-align:center;
  border:1px solid #e4e4e7}
.front-num{font-size:11px;color:#a1a1aa !important;font-weight:700;
  letter-spacing:1.5px;text-transform:uppercase;margin-bottom:12px}
.front-main{font-size:30px;font-weight:700;color:#18181b !important;
  line-height:1.5;letter-spacing:0.3px}
.front-hint{margin-top:16px;font-size:10.5px;text-transform:uppercase;
  letter-spacing:1.8px;color:#a1a1aa !important;font-weight:700}
</style>"""

css_back = """<style>
.bp{font-family:-apple-system,'Hiragino Sans','Yu Gothic',sans-serif;
  background:#ffffff !important;color:#18181b !important;
  border-radius:12px;overflow:hidden;border:1px solid #e4e4e7}
.bp-head{padding:14px 18px;background:#18181b !important}
.bp-head-num{font-size:11px;font-weight:700;letter-spacing:1.5px;
  color:#a1a1aa !important;text-transform:uppercase}
.bp-head-rumus{font-size:17px;font-weight:700;color:#ffffff !important;
  margin-top:2px}
.bp-body{padding:16px 18px}
.bp-section{margin-bottom:14px}
.bp-section:last-child{margin-bottom:0}
.bp-k{font-size:10px;font-weight:700;letter-spacing:1.2px;
  text-transform:uppercase;color:#a1a1aa !important;margin-bottom:5px;
  display:flex;align-items:center;gap:5px}
.bp-k::before{content:'';width:3px;height:11px;background:#3b82f6;
  border-radius:2px;display:inline-block}
.bp-target{font-size:14.5px;color:#3f3f46 !important;line-height:1.55}
.bp-target b{color:#18181b !important}
.bp-contoh{background:#fafafa !important;border-radius:8px;padding:4px 12px}
.bp-contoh-item{padding:8px 0;border-bottom:1px solid #ececec}
.bp-contoh-item:last-child{border-bottom:none}
.bp-contoh-jp{font-size:15px;color:#18181b !important;font-weight:500}
.bp-contoh-id{font-size:12.5px;color:#71717a !important;margin-top:1px}
.bp-tips{font-size:13px;color:#3f3f46 !important;line-height:1.65;
  background:#eff6ff !important;border-radius:8px;padding:11px 13px}
.bp-tips b{color:#1d4ed8 !important;font-weight:700}
.bp-warn{font-size:13px;color:#3f3f46 !important;line-height:1.65;
  background:#fef2f2 !important;border-left:3px solid #ef4444;
  border-radius:6px;padding:10px 12px;margin-top:9px}
.bp-warn b{color:#b91c1c !important;font-weight:700}
</style>"""

def get_ai_data():
    return {
        "1": {
            "01": {"tips": "Pola ini ibarat 'sama dengan' (=) dalam matematika. Ingat, partikel は dibaca 'wa'.", "target_summary": "Menjelaskan identitas subjek (KB1) dengan kata benda (KB2)."},
            "02": {"tips": "Jangan pakai pola ini untuk ragam tulisan resmi (gunakan ではありません).", "target_summary": "Menyatakan bentuk penyangkalan dari pola sebelumnya (bukan ~)."},
            "03": {"tips": "Partikel か itu sama seperti tanda tanya (?). Cukup tambahkan di akhir kalimat.", "target_summary": "Menandai sebuah kalimat sebagai kalimat tanya (Apakah ~?)."},
            "04": {"tips": "Anggap も seperti kata 'juga' atau 'too'. Fungsinya menggantikan partikel は jika predikatnya sama.", "target_summary": "Menyatakan kesamaan atau tambahan informasi (juga ~)."},
            "05": {"tips": "Bedakan dengan partikel で. に dipakai khusus untuk kata kerja keberadaan/menetap seperti すんでいます.", "target_summary": "Menyatakan tempat menetap atau tempat tinggal."},
            "06": {"tips": "Partikel と bisa diartikan 'bersama' atau 'dan'. Kalau sendirian, pakai 一人で (tanpa と).", "target_summary": "Menyatakan dengan siapa kita tinggal bersama."},
            "07": {"tips": "Tidak perlu pakai kata sambung 'atau'. Cukup jejerkan dua kalimat tanya.", "target_summary": "Menanyakan pilihan alternatif di antara dua opsi (~ atau ~?)."},
            "08": {"tips": "Pola ini bentuk lampau dari きます (datang) karena perbuatannya sudah selesai.", "target_summary": "Menyatakan asal usul kedatangan atau kampung halaman."},
            "09": {"tips": "Hati-hati dengan umur 20 tahun. Bukan にじゅっさい, tapi はたち.", "target_summary": "Menyebutkan usia seseorang dalam hitungan tahun."},
            "10": {"tips": "Awalan お membuat kalimat terdengar lebih sopan untuk menanyakan nama lawan bicara.", "target_summary": "Menanyakan nama seseorang dengan sopan."}
        },
        "2": {
            "11": {"tips": "Pola の selalu diterjemahkan dari belakang ke depan (KB2 milik KB1).", "target_summary": "Menyatakan kepemilikan atau hubungan antara dua kata benda."},
            "12": {"tips": "Pola ini berdiri sendiri tanpa diikuti kata benda. Gunakan untuk menunjuk benda secara umum.", "target_summary": "Kata tunjuk benda (Ini/Itu/Itu jauh) yang berfungsi sebagai subjek."},
            "13": {"tips": "Ingat! Jangan pernah memisahkan kata tunjuk ini dari kata benda yang diikutinya.", "target_summary": "Kata tunjuk benda yang harus langsung diikuti oleh kata benda."},
            "14": {"tips": "Hanya digunakan jika jumlah pilihan lebih dari dua benda.", "target_summary": "Menanyakan benda mana yang dimaksud dari banyak pilihan."},
            "15": {"tips": "Sama seperti どれ, tetapi wajib langsung ditempelkan dengan kata benda.", "target_summary": "Menanyakan benda/orang mana yang dimaksud dengan menempel pada kata benda."},
            "16": {"tips": "Partikel で di sini berarti 'menggunakan' atau 'dalam bahasa'.", "target_summary": "Menanyakan istilah atau terjemahan suatu benda dalam bahasa asing."},
            "17": {"tips": "Hati-hati dengan bacaan tidak beraturan: 一人 (ひとり) dan 二人 (ふたり).", "target_summary": "Menyatakan jumlah orang."},
            "18": {"tips": "Kanji sama dengan satuan orang, tapi dibaca じん dan fungsinya berbeda total.", "target_summary": "Menyatakan kewarganegaraan atau asal negara seseorang."}
        },
        "3": {
            "19": {"tips": "Meskipun 'suka' adalah kata kerja dalam bahasa Indonesia, 好き adalah kata sifat dalam bahasa Jepang, jadi pakai partikel が.", "target_summary": "Menyatakan hal atau benda yang disukai."},
            "20": {"tips": "Untuk bentuk lampau, gunakan 好きじゃありませんでした (tidak suka di masa lalu).", "target_summary": "Menyatakan hal atau benda yang tidak disukai."},
            "21": {"tips": "Cara andalan orang Jepang untuk menolak tawaran atau ajakan tanpa menyakiti hati.", "target_summary": "Menyatakan ketidaksukaan dengan sangat halus dan menggantung."},
            "22": {"tips": "Lebih halus dari 好きじゃない tapi lebih tegas dari ちょっと…. Biasanya dipakai untuk makanan atau kemampuan.", "target_summary": "Menyatakan kelemahan atau ketidaksukaan terhadap sesuatu."},
            "23": {"tips": "Hanya bisa digunakan untuk menghubungkan sesama kata benda, tidak bisa untuk kata kerja/sifat.", "target_summary": "Menghubungkan dua kata benda (dan/dengan)."},
            "24": {"tips": "Partikel を dibaca 'o'. Fungsinya seperti lem yang menempelkan objek dengan kata kerja.", "target_summary": "Menyatakan objek dari suatu aktivitas/kata kerja."},
            "25": {"tips": "Ubah akhiran ます menjadi ません untuk membentuk kalimat negatif formal.", "target_summary": "Menyatakan bentuk negatif atau penyangkalan dari suatu kata kerja."},
            "26": {"tips": "Dipakai dalam percakapan santai dengan teman. Jangan gunakan pada atasan atau orang asing.", "target_summary": "Bentuk penyangkalan kata kerja yang lebih kasual/santai."},
            "27": {"tips": "Kata あまり (jarang/tidak terlalu) WAJIB selalu diikuti oleh bentuk negatif (ません/ない).", "target_summary": "Menyatakan frekuensi yang rendah atau 'jarang/tidak begitu'."},
            "28": {"tips": "Kata よく (sering) selalu diletakkan sebelum kata kerja positif.", "target_summary": "Menyatakan frekuensi yang tinggi atau kebiasaan 'sering'."},
            "29": {"tips": "Kombinasi pamungkas untuk menyangkal secara total tanpa pengecualian.", "target_summary": "Menyatakan penyangkalan total terhadap semua hal (apapun tidak)."},
            "30": {"tips": "Intonasi menurun (nada rendah) berarti paham. Jika intonasi naik, berarti bertanya (benarkah?).", "target_summary": "Merespons dan menunjukkan pemahaman atas informasi baru."},
            "31": {"tips": "Fungsinya mirip dengan 'ya kan?' dalam bahasa Indonesia, mencari kesepahaman.", "target_summary": "Meminta persetujuan atau simpati dari lawan bicara di akhir kalimat."},
            "32": {"tips": "Fungsinya mirip dengan 'lho' dalam bahasa Indonesia, memberi tahu informasi baru.", "target_summary": "Menegaskan informasi atau memberi tahu hal baru yang belum diketahui lawan bicara."},
            "33": {"tips": "Tidak ada aturan pasti, tapi kata benda asli Jepang pakai お dan serapan China pakai ご.", "target_summary": "Awalan yang ditambahkan pada kata benda untuk membuatnya terdengar lebih halus dan sopan."}
        },
        "4": {
            "34": {"tips": "Ingat! あります untuk benda mati/tumbuhan. います untuk manusia/hewan.", "target_summary": "Menyatakan keberadaan benda/makhluk hidup."},
            "35": {"tips": "Bentuk penyangkalan sopan dari あります/います. Partikel berubah dari が menjadi は.", "target_summary": "Bentuk sopan dari penyangkalan keberadaan sesuatu (tidak ada)."},
            "36": {"tips": "Hanya gunakan untuk percakapan dengan teman atau junior. Jangan dipakai ke atasan.", "target_summary": "Bentuk kasual dari penyangkalan keberadaan sesuatu."},
            "37": {"tips": "Urutan pola ini fokus untuk menjawab pertanyaan 'di situ ada apa/siapa?'", "target_summary": "Menyebutkan apa/siapa yang ada di suatu tempat."},
            "38": {"tips": "Urutan pola ini kebalikan dari yang sebelumnya, fokus untuk menjawab pertanyaan 'X ada di mana?'", "target_summary": "Menyebutkan lokasi keberadaan suatu benda/orang."},
            "39": {"tips": "Ingat! Jangan pernah pakai pola ini kalau yang menerima adalah kamu sendiri.", "target_summary": "Menyatakan perbuatan memberi ke orang lain (bukan ke diri saya)."},
            "40": {"tips": "Pola ini KHUSUS dipakai kalau ada orang lain yang memberikan sesuatu KEPADA SAYA.", "target_summary": "Menyatakan ada orang lain yang memberi kepada saya."},
            "41": {"tips": "Pola ini kebalikan dari あげます/くれます, fokusnya pada si penerima, bukan pemberi.", "target_summary": "Menyatakan perbuatan menerima sesuatu dari seseorang."},
            "42": {"tips": "Kata tunjuk tempat. Konsepnya sama dengan これ/それ/あれ (dekat pembicara/pendengar/jauh dari keduanya).", "target_summary": "Kata tunjuk untuk menyatakan lokasi tempat."},
            "43": {"tips": "Paling sering dipakai saat memesan makanan/minuman di restoran atau berbelanja.", "target_summary": "Meminta atau memesan sesuatu dengan sopan (tolong~)."},
            "44": {"tips": "Satuan つ (ひとつ, ふたつ) aman dipakai untuk berbagai macam benda, utamanya makanan.", "target_summary": "Memesan suatu barang dengan menyebutkan jumlah/satuannya."},
            "45": {"tips": "Bisa diartikan 'Saya pilih/pesan ~'. Ini bukan pola niat/ingin (nanti dibahas di bab lain).", "target_summary": "Menyatakan pilihan spesifik atau pesanan (Saya pesan/pilih ~)."},
            "46": {"tips": "Ketiganya selalu diikuti bentuk positif kata kerja. Urutan frekuensi: いつも > よく > ときどき.", "target_summary": "Menyatakan seberapa sering suatu kegiatan dilakukan."},
            "47": {"tips": "Penting! しか harus selalu dipasangkan dengan bentuk negatif (-ません/ない). だけ bisa dipakai di kalimat positif.", "target_summary": "Menyatakan pembatasan (hanya/cuma)."},
            "48": {"tips": "Partikel や menandakan bahwa masih ada benda lain selain yang disebutkan (dll).", "target_summary": "Menyebutkan contoh beberapa benda dari suatu himpunan (X, Y, dan lain-lain)."}
        },
        "5": {
            "49": {"tips": "Ini adalah bentuk dasar (positif/sekarang). Kata sifat -na membutuhkan partikel 'na' jika langsung disambung kata benda, tapi jika berada di akhir (predikat), 'na'-nya hilang.", "target_summary": "Menjelaskan sifat suatu kata benda dengan bentuk positif."},
            "50": {"tips": "Pengecualian: kata sifat いい (bagus) bentuk negatifnya bukan いくない melainkan よくない.", "target_summary": "Menyatakan bentuk penyangkalan (negatif) dari kata sifat -i."},
            "51": {"tips": "Bentuk penyangkalan kata sifat -na sama persis dengan cara membuat bentuk negatif kata benda.", "target_summary": "Menyatakan bentuk penyangkalan (negatif) dari kata sifat -na."},
            "52": {"tips": "Bagian ini digunakan untuk menanyakan pendapat tentang suatu hal.", "target_summary": "Menanyakan pendapat atau keadaan mengenai suatu topik/hal (bagaimana?)."},
            "53": {"tips": "Perhatikan bahwa kata sifat -na WAJIB pakai な (contoh: 静かな 町) sedangkan kata sifat -i langsung gabung (contoh: 高い 車).", "target_summary": "Menyisipkan kata sifat langsung di depan kata benda (KB yang ~)."},
            "54": {"tips": "Topik utama di depan pakai は, bagian/fitur yang dijelaskan sifatnya pakai が.", "target_summary": "Menjelaskan sifat bagian tertentu dari suatu subjek besar."},
            "55": {"tips": "Jangan pakai pola ini untuk nanya rupa wajah/tubuh, gunakan untuk nanya sifat atau karakteristik utama seseorang.", "target_summary": "Menanyakan karakteristik atau ciri khas seseorang."},
            "56": {"tips": "Pola ini pasif: proses perubahan terjadi dengan sendirinya tanpa intervensi disengaja.", "target_summary": "Menyatakan perubahan suatu kondisi/keadaan menjadi suatu sifat."},
            "57": {"tips": "Konsepnya sama dengan pola sebelumnya, tapi diterapkan pada kata benda.", "target_summary": "Menyatakan perubahan menjadi suatu profesi/kata benda lain."},
            "58": {"tips": "Pola ini aktif (kausatif): perubahan terjadi karena campur tangan atau disengaja oleh seseorang.", "target_summary": "Menyatakan tindakan sengaja untuk membuat sesuatu menjadi suatu sifat."},
            "59": {"tips": "Digunakan untuk menggabungkan dua hal yang berlawanan dalam satu kalimat yang sama.", "target_summary": "Partikel penghubung kalimat kontras (~ tapi ~)."},
            "60": {"tips": "Lebih umum dipakai dalam obrolan santai atau lisan dibandingkan format tulisan yang menggunakan しかし.", "target_summary": "Kata penghubung untuk mengawali kalimat baru yang bertentangan dengan kalimat sebelumnya."},
            "61": {"tips": "Semua kata keterangan ini harus diletakkan tepat di depan kata sifat yang dijelaskan intensitasnya.", "target_summary": "Kata keterangan untuk menyatakan berbagai tingkat atau level suatu sifat."},
            "62": {"tips": "Kata yang ada partikel より-nya adalah pihak yang KALAH (daripada), pihak のほうが adalah yang MENANG (lebih).", "target_summary": "Membandingkan tingkat sifat antara dua hal."},
            "63": {"tips": "Kata tanya untuk membandingkan dua hal (hanya dua, jika lebih dari dua pakai どれ).", "target_summary": "Menanyakan pilihan/perbandingan di antara dua benda."}
        },
        "6": {
            "64": {"tips": "Bedakan dengan partikel に. Partikel で digunakan jika ada suatu AKTIVITAS/TINDAKAN yang dilakukan di tempat tersebut.", "target_summary": "Menyatakan tempat di mana suatu kegiatan/aktivitas berlangsung."},
            "65": {"tips": "Partikel に untuk waktu yang pasti, ごろ digunakan saat menunjuk waktu yang belum pasti/perkiraan (sekitar).", "target_summary": "Menyatakan keterangan waktu kapan suatu kegiatan dilakukan."},
            "66": {"tips": "Sangat berguna untuk menanyakan jadwal rutinitas atau acara.", "target_summary": "Menanyakan waktu spesifik (jam berapa) terkait suatu hal."},
            "67": {"tips": "Pola ini berguna untuk mencocokkan jadwal dan membuat kesepakatan waktu yang pas dengan lawan bicara.", "target_summary": "Menawarkan pilihan waktu atau tempat yang pas/cocok bagi lawan bicara."},
            "68": {"tips": "Kedua partikel ini bisa dipakai untuk waktu (Jam 9 sampai Jam 5) atau lokasi (Jakarta sampai Bandung).", "target_summary": "Menyatakan titik awal (dari) dan titik akhir (sampai)."},
            "69": {"tips": "Selalu sebutkan alasannya terlebih dahulu, lalu diakhiri partikel から, barulah sebutkan akibatnya.", "target_summary": "Menyatakan sebab/alasan terjadinya sesuatu."},
            "70": {"tips": "Partikel に (target) dan へ (arah) bisa saling bertukar fungsi di sini tanpa masalah berarti.", "target_summary": "Menyatakan perpindahan ke suatu tujuan tempat."},
            "71": {"tips": "Pengecualian penting: Jika 'jalan kaki', tidak pakai partikel で, tapi pakai kata 歩いて (aruite).", "target_summary": "Menyatakan alat transportasi/kendaraan yang dipakai untuk menuju suatu tempat."},
            "72": {"tips": "Ini adalah penggabungan kata benda acara dengan kata kerja perpindahan.", "target_summary": "Menyatakan pergi/datang/pulang dengan tujuan menghadiri acara/kegiatan."},
            "73": {"tips": "Tiga kata keterangan ini sering dipakai dalam obrolan lisan untuk mendesak atau memperkirakan waktu mepet.", "target_summary": "Keterangan waktu untuk mendesak atau menunjukkan kejadian yang akan segera tiba."},
            "74": {"tips": "Ingat tabel ini: positif lampau pakai でした, negatif lampau pakai じゃなかった です.", "target_summary": "Mengubah kata benda ke bentuk waktu lampau."},
            "75": {"tips": "Ingat tabel ini: positif lampau kata kerja pakai ~ました, negatif lampau pakai ~ません でした.", "target_summary": "Mengubah kata kerja ke bentuk waktu lampau."},
            "76": {"tips": "Sudah dan belum adalah paket lengkap. 'Belum' adalah いいえ、まだです.", "target_summary": "Menyatakan bahwa suatu perbuatan sudah selesai dilakukan."},
            "77": {"tips": "Penting! Buang huruf 'い' terakhir pada kata sifat lalu tempelkan 'かった' atau 'くなかった'. Jangan tambahkan kata でした (Salah: さむいでした).", "target_summary": "Mengubah kata sifat -i ke bentuk waktu lampau."},
            "78": {"tips": "Kata sifat -na aturannya sama persis dengan aturan pengubahan kata benda ke bentuk lampau.", "target_summary": "Mengubah kata sifat -na ke bentuk waktu lampau."},
            "79": {"tips": "Selalu sebutkan 'Benda Patokannya' lebih dulu (KB1), lalu diikuti partikel の, baru sebut posisi (atas/bawah/samping).", "target_summary": "Menyebutkan posisi benda secara detail di dalam ruang/tempat."},
            "80": {"tips": "Namun, でも lebih kasual dan sering dipakai dalam percakapan lisan dibandingkan しかし yang bersifat tulisan formal.", "target_summary": "Kata sambung formal untuk kontras kalimat (tetapi/namun)."}
        },
        "7": {
            "81": {"tips": "Pola paling penting di Bab 7. Menambahkan ください setelah kata kerja yang diubah jadi bentuk ~te.", "target_summary": "Meminta seseorang untuk melakukan sesuatu dengan sopan (tolong~)."},
            "82": {"tips": "Sama seperti ください, tapi sedikit lebih formal dan sering digunakan dalam urusan bisnis/tulis.", "target_summary": "Meminta sesuatu dengan lebih formal (mohon~)."},
            "83": {"tips": "Mengubah kata kerja jadi kata keterangan yang menjelaskan BAGAIMANA suatu aksi dilakukan.", "target_summary": "Menjelaskan cara suatu kegiatan dilakukan (dengan cara~)."},
            "84": {"tips": "Ingat konsep memberi (あげます) di Bab 4. Sekarang yang diberikan adalah AKSI, bukan cuma benda.", "target_summary": "Melakukan suatu perbuatan untuk orang lain (saya me~kan untuk~)."},
            "85": {"tips": "Ingat konsep くれます di Bab 4. Digunakan saat orang lain berbuat baik untuk diri KITA.", "target_summary": "Orang lain melakukan sesuatu kebaikan untuk saya."},
            "86": {"tips": "Pola ini menitikberatkan pada SAYA (sebagai penerima bantuan), meskipun orang lain yang melakukannya.", "target_summary": "Saya menerima manfaat dari tindakan orang lain (di~kan oleh~)."},
            "87": {"tips": "Bentuk ~te + mo ini adalah cara utama untuk menyatakan pengandaian konsesif (meskipun/walaupun) dalam Bahasa Jepang.", "target_summary": "Menyatakan kondisi berlawanan dengan harapan (meskipun melakukan ~, tetap ~)."},
            "88": {"tips": "Biasanya diucapkan dengan nada bertanya jika meminta izin. Kalau nada datar, berarti memberi izin.", "target_summary": "Meminta atau memberikan izin (bolehkah ~? / boleh ~)."},
            "92": {"tips": "Larangan yang cukup kuat. Dalam obrolan santai, いけません sering diganti dengan だめです.", "target_summary": "Menyatakan larangan keras (tidak boleh ~)."},
            "93": {"tips": "Mirip dengan kata 'try' dalam bahasa Inggris, melakukan suatu aksi untuk melihat hasilnya.", "target_summary": "Menyatakan tindakan percobaan (mencoba melakukan~)."},
            "89": {"tips": "Memastikan urutan. Aksi pertama SELESAI dulu (てから), barulah aksi kedua dilakukan.", "target_summary": "Menyatakan urutan aksi yang dilakukan berturut-turut (setelah melakukan ~)."},
            "90": {"tips": "Perbedaan makna rutinitas vs sedang berlangsung murni bergantung pada konteks kalimat (misal ada keterangan waktu 'setiap hari' vs 'sekarang').", "target_summary": "Menyatakan rutinitas/kebiasaan, ATAU menyatakan sedang berlangsung SEKARANG."},
            "91": {"tips": "Ini adalah penggabungan pola yang sama dengan pola 90, beda makna berdasar konteks.", "target_summary": "Menyatakan rutinitas/kebiasaan, ATAU menyatakan sedang berlangsung SEKARANG."},
            "94": {"tips": "Kata まだ (masih) yang diikuti kalimat POSITIF berarti suatu aktivitas sedang dan masih berlanjut.", "target_summary": "Menyatakan suatu perbuatan/keadaan masih berlangsung (masih melakukan~)."},
            "95": {"tips": "Kata まだ (belum) yang diikuti kalimat NEGATIF berarti suatu aktivitas belum terjadi sampai saat ini.", "target_summary": "Menyatakan suatu perbuatan/keadaan belum terjadi sampai saat ini (belum melakukan~)."},
            "96": {"tips": "Jangan pakai partikel と untuk menyambung sifat! Kalau sifat -i, wajib ubah い jadi くて.", "target_summary": "Menyambung dua kata sifat -i dalam satu kalimat (~ dan ~)."},
            "97": {"tips": "Ini versi kata sifat -na. Buang huruf 'na' dan ganti dengan 'de' untuk menyambungnya.", "target_summary": "Menyambung dua kata sifat -na (atau dengan hal lain) dalam satu kalimat."},
            "98": {"tips": "Sama seperti pola 87 (kata kerja), pola ini menyatakan 'meskipun' tapi untuk kata sifat.", "target_summary": "Menyatakan konsesif untuk kata sifat (meskipun sifatnya ~, tetap ~)."},
            "99": {"tips": "Ini adalah gabungan dari bentuk negatif (くない/じゃない) dengan bentuk konsesif (ても/でも).", "target_summary": "Menyatakan konsesif dari kondisi negatif (meskipun tidak ~, tetap ~)."},
            "100": {"tips": "Kata benda pakai aturan yang sama persis dengan kata sifat -na untuk bentuk sambung/konsesif.", "target_summary": "Menyatakan konsesif untuk kata benda (meskipun KB~/meskipun bukan KB~)."},
            "101": {"tips": "Pola ini sering dipakai saat meminta (dengan bentuk kudasai) untuk melakukan sesuatu sesuai sifat tertentu.", "target_summary": "Melakukan sesuatu DENGAN suatu sifat/cara."},
            "102": {"tips": "Dipakai di awal kalimat kedua untuk menyambung cerita. Beda dengan てから yang menyambung anak kalimat dalam satu kalimat utuh.", "target_summary": "Menyambung urutan kejadian (kemudian/setelah itu)."},
            "103": {"tips": "Sangat berguna saat mendeskripsikan berbagai kelebihan atau ciri khas suatu benda/tempat beruntun.", "target_summary": "Menambahkan informasi tambahan untuk memperkuat pernyataan (selain itu/dan lagi)."}
        },
        "8": {
            "104": {"tips": "Cara buat bentuk た sama persis dengan bentuk て, bedanya huruf e diganti a. (contoh: 食べて -> 食べた)", "target_summary": "Menyatakan kata kerja masa lampau dalam bentuk kasual/biasa."},
            "105": {"tips": "Selalu gunakan bentuk た sebelum ことがあります. Ini dipakai untuk menceritakan pengalaman hidup.", "target_summary": "Menyatakan pengalaman (pernah melakukan sesuatu)."},
            "106": {"tips": "Pola ini urutannya terbalik dari てから. Polanya: [Aksi Pertama]た あと、[Aksi Kedua].", "target_summary": "Menyatakan urutan aksi (setelah melakukan suatu hal)."},
            "107": {"tips": "Bisa diterjemahkan 'baru saja'. Menunjukkan aksi lampau yang masih sangat segar.", "target_summary": "Menyatakan suatu perbuatan yang baru saja terjadi."},
            "108": {"tips": "Meskipun maknanya menyarankan untuk hal di masa depan, tata bahasanya menggunakan bentuk lampau (た).", "target_summary": "Memberikan saran yang kuat kepada lawan bicara (sebaiknya)."},
            "109": {"tips": "Cara baca kondisional. 'Kalau A terjadi, maka B dilakukan'.", "target_summary": "Menyatakan syarat atau pengandaian (kalau/jika melakukan~)."},
            "110": {"tips": "Selalu diakhiri dengan します/しました. Tidak menceritakan kejadian secara berurutan, melainkan menyebutkan contoh aktivitas saja.", "target_summary": "Menyebutkan perwakilan atau contoh beberapa aktivitas yang dilakukan."},
            "111": {"tips": "Kata kerja bentuk asal ini wajib dihafal karena jadi dasar buat banyak tata bahasa lanjutan.", "target_summary": "Bentuk asli kata kerja tanpa konjugasi sopan (bentuk kamus/kasual)."},
            "112": {"tips": "Fungsi こと adalah mengubah predikat/kata kerja 'melakukan sesuatu' menjadi sebuah subjek layaknya kata benda.", "target_summary": "Membendakan kata kerja untuk mendeskripsikan kegiatan sebagai suatu hobi."},
            "113": {"tips": "Berbeda dengan bentuk た yang artinya 'pernah'. Bentuk kamus ini artinya kadang-kadang terjadi di saat ini.", "target_summary": "Menyatakan kejadian atau kebiasaan yang kadang-kadang terjadi."},
            "114": {"tips": "Mirip dengan bahasa Inggris 'can do'. Mengubah kata kerja jadi benda lalu ditambah 'bisa'.", "target_summary": "Menyatakan kesanggupan atau kemampuan melakukan suatu tindakan."},
            "115": {"tips": "Selalu gunakan bentuk kamus (bentuk asal) di depan kata まえに meskipun konteksnya lampau.", "target_summary": "Menyatakan tindakan yang dilakukan sebelum tindakan lainnya."},
            "116": {"tips": "Digunakan untuk menerangkan situasi terjadinya suatu perbuatan.", "target_summary": "Menyatakan keterangan waktu/suasana di mana aksi lain terjadi (pada saat)."},
            "117": {"tips": "Sama dengan こと, の mengubah kalimat kerja jadi subjek. Sering diikuti oleh kata sifat suka/benci (好き/嫌い).", "target_summary": "Menjadikan aktivitas sebagai topik utama pembicaraan."},
            "118": {"tips": "Ingat! Kata kerja yang menerangkan harus selalu ada di depan kata benda yang diterangkan (berkebalikan dengan bahasa Indonesia).", "target_summary": "Kata kerja bentuk kamus yang langsung menjelaskan suatu benda spesifik."},
            "119": {"tips": "Kondisional sebab-akibat. Jika A dilakukan, maka B PASTI terjadi (misal: menekan tombol maka lampu menyala).", "target_summary": "Menyatakan sebuah kejadian yang menjadi akibat mutlak/pasti dari suatu aksi."},
            "120": {"tips": "Dipakai untuk menanyakan niat/rencana lawan bicara atas situasi yang baru saja terjadi.", "target_summary": "Menanyakan solusi, rencana, atau tindakan berikutnya."},
            "121": {"tips": "Bisa dijawab dengan menyebutkan kategori spesifik atau memberikan sebuah contoh benda.", "target_summary": "Menanyakan jenis, macam, atau klasifikasi spesifik dari sebuah kata benda."},
            "122": {"tips": "Sangat penting: kata-kata keterangan tingkat ekstrem ini (ぜんぜん, ほとんど, いちども) WAJIB ditutup dengan kalimat negatif.", "target_summary": "Menyatakan frekuensi sangat jarang atau pengalaman nol mutlak."},
            "123": {"tips": "Gunakan partikel で setelah angka jumlah orang (misal 3人で) untuk menerangkan kondisi jumlah pesertanya.", "target_summary": "Menerangkan bersama berapa orang suatu aktivitas dilakukan."}
        },
        "9": {
            "124": {"tips": "Ini rumus memotong kata kerja (Stem/Akar). Buang bagian -ます, lalu sisa kata tersebut ditambahkan partikel に yang berfungsi sebagai 'untuk'.", "target_summary": "Menggabungkan akar kata kerja (Stem) dengan kata kerja perpindahan (pergi untuk~)."},
            "125": {"tips": "Sangat natural digunakan dalam bahasa sehari-hari. Kalau ditolak pun terdengar lebih halus.", "target_summary": "Mengajak orang lain melakukan sesuatu secara sopan dan tidak memaksa (maukah?)."},
            "126": {"tips": "Sifatnya lebih mendorong atau memutuskan. Jangan pakai kepada atasan karena bisa terdengar seperti perintah.", "target_summary": "Mengajak atau menyimpulkan suatu tindakan bersama (mari/ayo)."},
            "127": {"tips": "Hati-hati dengan bedanya dari ましょう. Pola dengan か ini dipakai untuk menawarkan jasa atau bantuan.", "target_summary": "Menawarkan bantuan secara inisiatif dari pihak pembicara (maukah saya~?)."},
            "128": {"tips": "Aktivitas kedua (setelah ながら) biasanya adalah kegiatan utamanya. Sifatnya dikerjakan di waktu yang bersamaan.", "target_summary": "Melakukan dua kegiatan sekaligus dalam waktu bersamaan (sambil)."},
            "129": {"tips": "Perubahan ini menjadikan kata kerja memiliki sifat seperti kata benda. Sering dipakai untuk minta tolong diajarkan.", "target_summary": "Menyatakan sebuah metode, teknik, atau cara melakukan sesuatu."},
            "130": {"tips": "Perintah dari atas ke bawah. Sering ditemui pada soal ujian bahasa Jepang atau teguran orang tua ke anak.", "target_summary": "Memberikan perintah tegas namun mendidik dari pihak yang superior."},
            "131": {"tips": "Setelah diubah dengan pola ini, kata tersebut secara gramatikal berubah total menjadi kata sifat -i.", "target_summary": "Menyatakan suatu perbuatan sangat gampang atau mudah dilakukan."},
            "132": {"tips": "Sama seperti やすい, ini juga bertindak sebagai kata sifat -i utuh.", "target_summary": "Menyatakan suatu perbuatan memiliki kendala atau sulit dilakukan."},
            "133": {"tips": "Hanya boleh dipakai saat menginginkan suatu OBJEK (barang). Jangan dipakai untuk menyatakan keinginan berbuat sesuatu.", "target_summary": "Menyatakan keinginan untuk memiliki suatu benda materi/abstrak."},
            "134": {"tips": "Perubahannya mirip sekali dengan bentuk negatif kata sifat -i (buang い jadi くない).", "target_summary": "Menyatakan rasa tidak ingin memiliki atau membutuhkan suatu benda."},
            "135": {"tips": "Hanya boleh dipakai bersama dengan AKAR KATA KERJA (Stem). Hati-hati dengan partikel yang mendahuluinya.", "target_summary": "Menyatakan hasrat atau niat untuk melakukan suatu aksi (ingin~)."},
            "136": {"tips": "Bentuk penyangkalan dari たい. Bisa dibilang ini merupakan peleburan dari kalimat negatif + keinginan.", "target_summary": "Menyatakan penolakan atas niat atau aksi (tidak ingin~)."},
            "137": {"tips": "Beda dengan pola あります untuk benda pasif. Di sini あります diartikan 'diadakan' atau 'dilangsungkan'.", "target_summary": "Menyatakan keberadaan/terselenggaranya suatu acara di suatu lokasi."},
            "138": {"tips": "Cara alami untuk menunjukkan penekanan atau intonasi tanya yang lembut dalam dialog antarteman.", "target_summary": "Mengubah kalimat pernyataan menjadi kalimat interogatif bernada kasual/akrab."},
            "139": {"tips": "Urutan formalitas kata 'tapi': が (formal) > でも (netral) > けど/けれど/けれども (kasual-sopan).", "target_summary": "Penghubung untuk mengontraskan antar dua frasa/kalimat secara luwes."},
            "140": {"tips": "Kata pembuka klasik yang sangat sering terdengar di akhir rapat atau saat memutuskan beralih tindakan.", "target_summary": "Mengawali langkah, tindakan, atau kesimpulan baru dari perbincangan sebelumnya."}
        },
        "10": {
            "141": {"tips": "Ini adalah bentuk penyangkalan non-sopan. Grup I: ganti vokal terakhir ke u menjadi a (contoh: 飲む->飲まない).", "target_summary": "Menyatakan bentuk penyangkalan kata kerja dalam bentuk kasual/biasa."},
            "142": {"tips": "Larangan yang lebih halus dari pola てはいけません. Sering diucapkan oleh atasan ke bawahan.", "target_summary": "Meminta atau memohon dengan sopan agar seseorang JANGAN melakukan sesuatu."},
            "143": {"tips": "Tentu saja boleh kalau tidak dilakukan. Sering diucapkan untuk meringankan beban lawan bicara.", "target_summary": "Menyatakan keleluasaan bahwa suatu perbuatan TIDAK PERLU dilakukan."},
            "144": {"tips": "Keharusan paling dasar. Menjadi rutinitas jika sering terjadi. Secara harfiah berarti 'kalau tidak ..., maka jadi buruk'.", "target_summary": "Menyatakan kewajiban atau keharusan melakukan sesuatu."},
            "145": {"tips": "Levelnya sedikit lebih ringan dibanding なければなりません, sering dipakai dalam pergaulan sehari-hari.", "target_summary": "Bentuk lain untuk menyatakan kewajiban/keharusan (harus~)."},
            "146": {"tips": "Sangat kasual. Sering diucapkan pada diri sendiri ketika menyadari suatu kewajiban.", "target_summary": "Cara singkat dan santai (kasual) untuk mengingatkan diri sendiri akan kewajiban."},
            "147": {"tips": "Berbeda dengan なければなりません yang wajib dilakukan karena rutinitas, pola ini dipakai sebagai saran wajib/terbaik dari si pembicara.", "target_summary": "Memberikan instruksi kuat (harus~) dari sudut pandang logika pembicara."},
            "148": {"tips": "Cara lain memotong kalimat なければならない. Nuansanya mendesak.", "target_summary": "Bentuk kasual dari keharusan/kewajiban yang sering diucapkan spontan."},
            "149": {"tips": "Partikel に berarti naik (masuk ke dalam kendaraan). Partikel を berarti turun (keluar dari kendaraan).", "target_summary": "Menyatakan aktivitas menaiki atau menuruni sebuah kendaraan/transportasi."},
            "150": {"tips": "Bisa untuk waktu (jam/hari/bulan) dan juga biaya (jumlah uang). Tidak perlu partikel penghubung.", "target_summary": "Menyatakan biaya (uang) atau waktu yang diperlukan untuk mencapai suatu tujuan."},
            "151": {"tips": "Tabel konjugasi ini WAJIB dihafal luar kepala, karena dipakai di semua bab di bahasa Jepang level atas (N4-N1).", "target_summary": "Rangkuman semua bentuk kalimat non-sopan (biasa/futsuukei) dari segala jenis kata."},
            "152": {"tips": "Subjek dalam anak kalimat bentuk f ini seringkali ditandai partikel が (bukan は) saat menjelaskan kata benda.", "target_summary": "Menggunakan Bentuk Biasa (f) untuk menjelaskan suatu kata benda secara rinci."},
            "153": {"tips": "Hanya boleh diisi dengan bentuk Biasa di depan partikel と. Ini adalah opini sepihak dari diri sendiri.", "target_summary": "Menyatakan opini/pendapat pribadi mengenai suatu hal (saya pikir/rasa~)."},
            "154": {"tips": "Hanya mengulangi kata yang diucapkan persis. Kalau dalam bahasa Indonesia sama seperti tanda kutip langsung/tidak langsung.", "target_summary": "Mengutip perkataan/pernyataan dari pihak lain (berkata bahwa~)."},
            "155": {"tips": "Cocok dipakai saat bergosip atau membicarakan kabar yang didapat dari pihak ketiga.", "target_summary": "Menyampaikan informasi yang bersumber dari desas-desus atau orang lain (saya dengar~)."},
            "156": {"tips": "Sebuah kata penghubung (konjungsi) yang diletakkan di awal kalimat berikutnya.", "target_summary": "Menghubungkan dua kalimat dengan unsur sebab dan akibat (karena itu/jadi)."},
            "157": {"tips": "Kata tanya apa saja (siapa/kapan/di mana/apa) bisa digabungkan dengan でも untuk arti semesta.", "target_summary": "Mengubah kata tanya menjadi frasa universal/keseluruhan (apapun/kapanpun)."},
            "158": {"tips": "Bedakan dengan でも, kata tanya yang memakai か artinya hal yang merujuk belum/tidak diketahui persis bentuknya.", "target_summary": "Mengubah kata tanya menjadi frasa ketidakpastian spesifik (sesuatu/seseorang)."},
            "159": {"tips": "Selalu gunakan Bentuk Biasa sebelum partikel か yang menjadi inti penanda pertanyaannya.", "target_summary": "Menyematkan pertanyaan tak langsung ke dalam kalimat (apakah kamu tahu~?)."},
            "160": {"tips": "Berlaku untuk kondisi pilihan biner ya atau tidak. Selalu diakhiri ekspresi tidak tahu/belum diputuskan.", "target_summary": "Menyatakan ketidaktahuan akan dua kemungkinan berlawanan (apakah~ atau tidak)."},
            "161": {"tips": "Fungsinya seperti highlight atau penebalan pada bagian spesifik di kalimat.", "target_summary": "Menempelkan partikel は di atas partikel lain untuk memberikan kontras topik yang dibicarakan."}
        }
    }

def process_example_line(line):
    # This logic aims to PERFECTLY extract JP and ID translations, handling missing parentheses
    # and preventing ID leaks into JP boxes.

    line = line.strip()

    # 1. Match typical `A: (JP) (ID)` or just `(JP) (ID)`
    match = re.search(r'^(.*?)\s*[\(（]([^)）]+)[\)）]$', line)

    if match:
        jp_part = match.group(1).strip()
        id_part = match.group(2).strip()
        return jp_part, id_part
    else:
        # 2. No parenthesis found. We need to check if there's a hidden Indonesian translation
        # that wasn't wrapped in parentheses, OR if it's purely a Japanese string.
        # But looking at the markdown, if there's no parenthesis, the translation is missing.
        # However, earlier bugs showed "A: あれ は 何 です か。(Itu" and "yang jauh) apa?"
        # which means my previous regex `r'^(.*?)\((.*?)\)$'` failed when the translation ITSELF contained a parenthesis like `(yang jauh)`.

        # Let's fix nested parenthesis by doing a smart rsplit.
        if line.endswith(')') or line.endswith('）'):
            # Find the FIRST opening parenthesis after Japanese text.
            # Usually Japanese text doesn't contain ascii '(' unless it's a translation start.
            open_idx = line.find('(')
            if open_idx != -1:
                jp_part = line[:open_idx].strip()
                id_part = line[open_idx+1:-1].strip()
                return jp_part, id_part

        return line, ""

def parse_examples(examples_text):
    raw_examples = [x.strip() for x in examples_text.split('\n') if x.strip()]
    examples_html = ""
    count = 0

    for line in raw_examples:
        line = re.sub(r'^- ', '', line).strip()
        if not line: continue

        # Remove trailing italic notes like `*(contoh personal...)*`
        line = re.sub(r'\*.*?\*$', '', line).strip()

        jp, id_ = process_example_line(line)

        # Format speaker tags
        jp = re.sub(r'^(A|B|C|学生|先生)：', r'<b>\1:</b> ', jp)

        examples_html += f'<div class="bp-contoh-item"><div class="bp-contoh-jp">{jp}</div><div class="bp-contoh-id">{id_}</div></div>'
        count += 1
        if count >= 4:
            break
    return examples_html

def parse_md(filepath, bab_num):
    ai_data = get_ai_data()
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    patterns = re.split(r'### 【(\d+)】', content)[1:]
    cards = []

    for i in range(0, len(patterns), 2):
        num = patterns[i].strip()
        body = patterns[i+1]

        title_match = re.match(r'(.+)', body.strip())
        title = title_match.group(1).strip() if title_match else ""

        # Use AI data
        ai_info = ai_data.get(str(bab_num), {}).get(num, {"tips": "Pelajari struktur kalimat ini agar bisa dipakai dalam percakapan sehari-hari.", "target_summary": ""})
        target = ai_info["target_summary"]
        if not target:
             target_match = re.search(r'🎯 \*\*Target:\*\*(.*?)(?=\n🛠️|\n📝|\n💡|\n>|\n---|$)', body, re.DOTALL)
             target = target_match.group(1).strip() if target_match else ""
             target_sentences = re.split(r'(?<=[.!?])\s+', target)
             target = " ".join(target_sentences[:1]).strip()

        target = re.sub(r'"([^"]+)"', r'<b>"\1"</b>', target)

        rumus_match = re.search(r'🛠️ \*\*Rumus Hack:\*\*(.*?)(?=\n|$)', body)
        rumus = rumus_match.group(1).strip() if rumus_match else title

        warn_text = " ".join([line.strip()[1:].strip() for line in body.split('\n') if line.strip().startswith('>')])
        warn_text = re.sub(r'^\*\*(.*?)\*\* ', r'<b>\1</b> ', warn_text)

        tips = ai_info["tips"]
        warn_box = ""
        if "Bedain" in warn_text or "Hati-hati" in warn_text or "Awas" in warn_text or "Catatan" in warn_text or "Ingat" in warn_text or "Pengecualian" in warn_text or "Koreksi" in warn_text or "Validasi" in warn_text:
             warn_text = re.sub(r'^(Bedain.*?:|Hati-hati.*?:|Awas.*?:|Catatan.*?:|Ingat.*?:|Pengecualian.*?:|Koreksi.*?:|✅\s*Validasi.*?:)\s*', '', warn_text)
             warn_box = f'<div class="bp-warn"><b>Awas:</b> {warn_text.strip()}</div>'
        elif warn_text:
             warn_box = f'<div class="bp-warn"><b>Catatan:</b> {warn_text}</div>'

        examples_text = ""
        contoh_basic = re.search(r'(?:📝 \*\*Contoh Basic:\*\*|\*\*Contoh asli[^\n]*)(.*?)(?=\n💡|\n>|\n---|$)', body, re.DOTALL)
        if contoh_basic: examples_text += contoh_basic.group(1) + "\n"

        contoh_lateral = re.search(r'💡 \*\*Contoh Lateral.*?:(.*?)(?=\n>|\n---|$)', body, re.DOTALL)
        if contoh_lateral: examples_text += contoh_lateral.group(1)

        examples_html = parse_examples(examples_text)

        front_font_style = ""
        if len(rumus) > 25:
             front_font_style = ' style="font-size:24px;"'

        # Deck mapping fix (e.g. Bab 10 instead of Bab 010)
        deck_name = f"Bab {bab_num}::Bunpou" if bab_num >= 10 else f"Bab 0{bab_num}::Bunpou"

        front_html = f'{css_front}<div class="frontcard"><div class="front-num">Pola {num} &middot; Bab {bab_num}</div><div class="front-main"{front_font_style}>{rumus}</div><div class="front-hint">Bunpou &middot; Fungsi &amp; cara pakainya?</div></div>'

        back_html = f'{css_back}<div class="bp"><div class="bp-head"><div class="bp-head-num">Pola {num} &middot; Bab {bab_num}</div><div class="bp-head-rumus">{title}</div></div><div class="bp-body"><div class="bp-section"><div class="bp-k">Fungsi</div><div class="bp-target">{target}</div></div>'

        if examples_html:
            back_html += f'<div class="bp-section"><div class="bp-k">Contoh</div><div class="bp-contoh">{examples_html}</div></div>'

        back_html += f'<div class="bp-section"><div class="bp-k">Tips Cepat Hapal</div><div class="bp-tips">{tips}{warn_box}</div></div></div></div>'

        front_html = front_html.replace('\n', '')
        back_html = back_html.replace('\n', '')

        cards.append(f'Basic\t{deck_name}\t{front_html}\t{back_html}\tBunpou')

    return cards

def write_deck(cards, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("#separator:tab\n")
        f.write("#html:true\n")
        f.write("#notetype column:1\n")
        f.write("#deck column:2\n")
        f.write("#tags column:5\n")
        for card in cards:
            f.write(card + "\n")

babs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for bab in babs:
    input_path = f"BAB_{bab:02d}/bunpou.md" if bab < 10 else f"BAB_{bab}/bunpou.md"
    os.makedirs(f"BAB_{bab}", exist_ok=True)
    output_path = f"BAB_{bab}/BAB_{bab}_bunpou.txt"
    if os.path.exists(input_path):
        cards = parse_md(input_path, bab)
        write_deck(cards, output_path)
        print(f"Generated {output_path} with {len(cards)} cards.")
