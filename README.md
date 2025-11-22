rogram Daftar Nilai Mahasiswa (Python + JSON)

Program ini digunakan untuk mengelola data nilai mahasiswa dengan fitur input, lihat, ubah, hapus, dan cari.
Seluruh data disimpan dalam file JSON (data_nilai.json) sehingga akan tetap tersimpan meskipun program ditutup.

Fitur Program
✔ Lihat Data

Menampilkan seluruh daftar nilai mahasiswa dalam bentuk tabel:

NIM

Nama

Nilai Tugas

Nilai UTS

Nilai UAS

Nilai Akhir (dihitung otomatis)

✔ Tambah Data

Menambahkan data mahasiswa baru, meliputi:

NIM

Nama

Nilai Tugas, UTS, UAS

Nilai Akhir dihitung menggunakan rumus:

nilai_akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

✔ Ubah Data

Mengubah data mahasiswa berdasarkan NIM:

Nama

Nilai Tugas

Nilai UTS

Nilai UAS
Setelah diubah, nilai akhir dihitung ulang.

✔ Hapus Data

Menghapus data mahasiswa berdasarkan NIM.

✔ Cari Data

Mencari dan menampilkan data mahasiswa berdasarkan NIM.

✔ Keluar

Menutup program.

Struktur Data JSON

Data disimpan dalam file data_nilai.json dengan format:

{
  "NIM12345": {
    "nama": "Budi",
    "tugas": 80,
    "uts": 85,
    "uas": 90,
    "akhir": 86.75
  }
}

Cara Menjalankan Program

Pastikan Python sudah terinstall

Simpan kode program dengan nama apa saja 

jalankan program

File data_nilai.json akan otomatis dibuat setelah Anda menambah data.

| Menu  | Fungsi                             |
| ----- | ---------------------------------- |
| L | Menampilkan daftar nilai mahasiswa |
| T | Menambah data baru                 |
| U | Mengubah data berdasarkan NIM      |
| H | Menghapus data berdasarkan NIM     |
| C | Mencari data berdasarkan NIM       |
| K | Keluar dari program                |


