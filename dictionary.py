import json
import os

# === LOAD DATA DARI FILE JSON ===
if os.path.exists("data_nilai.json"):
    with open("data_nilai.json", "r") as file:
        data = json.load(file)
else:
    data = {}

# === FUNGSI HITUNG NILAI AKHIR ===
def hitung_akhir(tugas, uts, uas):
    return tugas*0.30 + uts*0.35 + uas*0.35

# === FUNGSI SIMPAN KE FILE ===
def simpan_data():
    with open("data_nilai.json", "w") as file:
        json.dump(data, file)

# === PROGRAM UTAMA ===
while True:
    print("\nProgram Input Nilai")
    print("============================================================")
    print("(L)ihat  (T)ambah  (U)bah  (H)apus  (C)ari  (K)eluar")
    pilih = input("Pilih Menu : ").lower()

    # TAMPILKAN DATA
    if pilih == "l":
        print("\nDaftar Nilai Mahasiswa")
        print("===========================================================================")
        print("| NO |   NIM    |     NAMA     | TUGAS |  UTS  |  UAS  |  AKHIR  |")
        print("===========================================================================")

        if not data:
            print("|                           TIDAK ADA DATA                               |")
            print("===========================================================================")
        else:
            no = 1
            for nim, nilai in data.items():
                print(
                    f"| {no:<2} | {nim:<8} | {nilai['nama']:<12} | "
                    f"{nilai['tugas']:<5} | {nilai['uts']:<5} | {nilai['uas']:<5} | {nilai['akhir']:<7.2f} |"
                )
                no += 1
            print("===========================================================================")

    # TAMBAH DATA
    elif pilih == "t":
        nim = input("Masukkan NIM   : ")
        nama = input("Masukkan Nama  : ")
        tugas = int(input("Nilai Tugas    : "))
        uts = int(input("Nilai UTS      : "))
        uas = int(input("Nilai UAS      : "))
        akhir = hitung_akhir(tugas, uts, uas)

        data[nim] = {
            "nama": nama,
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "akhir": akhir
        }
        simpan_data()
        print("Data berhasil ditambah!")

    # UBAH DATA
    elif pilih == "u":
        nim = input("Masukkan NIM yang akan diubah : ")
        if nim in data:
            print("Ubah data", data[nim]["nama"])
            data[nim]["nama"] = input("Nama baru   : ")
            data[nim]["tugas"] = float(input("Tugas baru : "))
            data[nim]["uts"] = float(input("UTS baru   : "))
            data[nim]["uas"] = float(input("UAS baru   : "))
            data[nim]["akhir"] = hitung_akhir(
                data[nim]["tugas"],
                data[nim]["uts"],
                data[nim]["uas"]
            )
            simpan_data()
            print("Data berhasil diubah!")
        else:
            print("NIM tidak ditemukan!")

    # HAPUS DATA
    elif pilih == "h":
        nim = input("Masukkan NIM yang akan dihapus : ")
        if nim in data:
            del data[nim]
            simpan_data()
            print("Data berhasil dihapus!")
        else:
            print("NIM tidak ditemukan!")

    # CARI DATA
    elif pilih == "c":
        nim = input("Masukkan NIM yang dicari : ")
        if nim in data:
            nilai = data[nim]
            print("\nData ditemukan:")
            print(f"NIM   : {nim}")
            print(f"Nama  : {nilai['nama']}")
            print(f"Tugas : {nilai['tugas']}")
            print(f"UTS   : {nilai['uts']}")
            print(f"UAS   : {nilai['uas']}")
            print(f"Akhir : {nilai['akhir']:.2f}")
        else:
            print("Data tidak ditemukan!")

    # KELUAR
    elif pilih == "k":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan menu tidak ada!")
