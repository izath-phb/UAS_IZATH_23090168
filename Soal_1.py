def tambah_data():
    mahasiswa = []
    while True:
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        mahasiswa.append({'NIM': nim, 'Nama': nama})
        
        tambah_lagi = input("Ingin tambah lagi? (YA/TIDAK): ").strip().lower()
        if tambah_lagi != 'ya':
            break
    return mahasiswa

def tampilkan_data(mahasiswa):
    print("\nData Mahasiswa:")
    for data in mahasiswa:
        print(f"NIM: {data['NIM']}, Nama: {data['Nama']}")

def main():
    print("Program Input Data Mahasiswa")
    data_mahasiswa = tambah_data()
    tampilkan_data(data_mahasiswa)
    print("Program Selesai")

if __name__ == "__main__":
    main()
