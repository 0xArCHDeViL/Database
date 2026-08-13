# Gateway Tracker — Design Direction

## Three Initial Directions

### Theme Name: Swiss Training Ledger
Very Brief Intro: Dashboard editorial bergaya Swiss modern: grid asimetris, tipografi tegas, tinta arang, dan aksen merah sinyal. Terasa seperti buku catatan performa yang dirancang untuk dipakai setiap hari.
Probability: 0.074

### Theme Name: Quiet Progress Garden
Very Brief Intro: Nuansa mindful dan ringan dengan warna sage, krem, dan terracotta. Progress terasa seperti merawat kebiasaan, bukan mengejar angka.
Probability: 0.031

### Theme Name: Night Circuit Lab
Very Brief Intro: Workspace gelap dengan cyan dan amber yang menyala seperlunya, menggemakan panel kontrol latihan dan debugging. Enerjik, tetapi tetap fokus pada keterbacaan data.
Probability: 0.086

## Chosen Direction: Swiss Training Ledger

### Design Movement
Contemporary Swiss International Typographic Style bertemu editorial athletic field notes. Sistemnya memakai struktur dokumenter yang disiplin, tetapi diberi detail manusiawi lewat anotasi, garis ukur, dan label metadata.

### Core Principles
1. **Data dulu, dekorasi sebagai orientasi.** Setiap warna, garis, dan label membantu pengguna membaca ritme latihan atau belajar.
2. **Asimetri yang fungsional.** Sidebar tetap ringkas, area utama menjadi kanvas analitik, dan panel input harian terasa seperti lembar kerja yang terbuka.
3. **Kontras taktis.** Arang, kertas hangat, dan merah sinyal memberi hierarki tanpa mengandalkan gradient ungu, glow, atau kartu seragam.
4. **Konsistensi harian.** Microcopy dan interaksi memberi rasa checkpoint: kecil, cepat, dan dapat dipercaya.

### Color Philosophy
Kertas hangat (#F4F0E8) menjadi lingkungan yang tenang untuk rutinitas. Charcoal (#20221F) menjadi tinta utama agar data terasa permanen. Signal red (#E84C3D) hanya dipakai untuk tindakan, streak, dan titik penting; bukan sebagai dekorasi. Moss (#A8B78D) menjadi indikator habit yang hidup, sedangkan pale blue (#D9E5E8) membantu memisahkan konteks belajar dari workout. Warna dipakai sebagai sistem status, bukan ornamen.

### Layout Paradigm
Persistent left rail seperti cover notebook, dengan tanggal aktif dan mode app di atas. Konten utama memakai komposisi 7/5: kolom kiri berisi Today Log dan input progres, kolom kanan berisi Today Signal, streak, serta statistik ringkas. Di bawahnya, visualisasi melebar penuh seperti lembar laporan mingguan. Tidak semua elemen dipusatkan; beberapa panel sengaja menempel pada garis ukur dan nomor section.

### Signature Elements
1. **Section index** bernomor besar seperti `01 / TODAY`, `02 / RHYTHM`, `03 / EXPORT`.
2. **Progress strip** berupa baris kotak kecil bergaya contribution graph dengan tooltip tanggal dan total menit.
3. **Margin annotations** berupa label monospaced kecil seperti `JLPT / N3`, `AMRAP / 20:00`, dan `SYNC / LOCAL`.

### Interaction Philosophy
Input harus terasa seperti check-in, bukan form administrasi. Toggle workout memiliki state yang jelas dan langsung menampilkan field relevan. Menambah item Jepang mempertahankan nilai form sebelumnya agar entry berulang cepat. Setiap simpan memberi konfirmasi kecil yang tidak memblokir. Data tidak pernah hilang diam-diam: local journal menjadi sumber utama dan sinkronisasi GitHub selalu menampilkan status, timestamp, serta konflik.

### Animation
Gunakan entrance singkat 180–260ms dengan ease-out yang tegas. Heatmap boleh muncul dengan stagger 20ms per kolom saat pertama kali dibuka, tetapi tidak dianimasikan ulang pada setiap input. Toggle memakai transform kecil dan perubahan warna, bukan layout shift. Chart line menggambar progres secara ringan saat filter berganti. Semua motion dimatikan atau diperlambat sesuai `prefers-reduced-motion`.

### Typography System
Display: **Space Grotesk** untuk judul, angka besar, dan label section—geometris tetapi tidak generik. Body: **DM Sans** untuk teks dan input agar tetap nyaman dibaca. Metadata: **IBM Plex Mono** untuk tanggal, JLPT tag, unit menit, dan status sync. Hierarki: headline 48/52 desktop, 34/38 mobile; section 12px uppercase dengan tracking 0.18em; body 14–16px; metric 28–42px.

### Brand Essence
Gateway Tracker adalah personal operating ledger untuk orang yang ingin menggabungkan tubuh, bahasa, dan waktu luang dalam satu ritme yang dapat dilihat. Personality: **disciplined, observant, quietly intense**.

### Brand Voice
Headline terdengar ringkas, observasional, dan sedikit menantang. CTA berbentuk aksi konkret, bukan motivasi generik.

Example lines:
- “Make the day count in minutes, not intentions.”
- “Log the reps. Keep the thread.”

### Wordmark & Logo
Logo berupa simbol gerbang abstrak: dua garis vertikal charcoal yang membuka ke satu diagonal signal red, membentuk huruf G secara implisit dan menyerupai portal menuju checkpoint berikutnya. Wordmark menggunakan Space Grotesk SemiBold dengan potongan kecil pada huruf `A` di Gateway sebagai detail editorial. Ikon harus tetap terbaca tanpa teks.

### Signature Brand Color
**Signal Red `#E84C3D`** — warna yang menandai komitmen hari ini dan membuat keputusan penting terlihat tanpa membuat seluruh dashboard berisik.

## Style Decisions

- Gunakan layout sidebar + editorial dashboard; hindari hero centered dan kartu rounded seragam.
- Jangan memakai Inter atau purple gradient.
- Setiap komponen/page yang diubah wajib menyertakan komentar singkat yang mengingatkan arah Swiss Training Ledger.
- Jangan menampilkan testimoni, rating, atau review palsu.
- Workout diberi catatan keselamatan dan field scaling/modification; tracker bukan pengganti nasihat medis.
