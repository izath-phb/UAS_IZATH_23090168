from Soal_3_modul import RestoranQueue

def main():
    restoran_queue = RestoranQueue()

    while True:
        print("\nMenu:")
        print("1. Tambah pesanan ke antrian (enqueue)")
        print("2. Hapus pesanan dari antrian (dequeue)")
        print("3. Tampilkan antrian saat ini")
        print("4. Keluar")

        pilihan = input("Pilih opsi (1-4): ")

        if pilihan == '1':
            pesanan = input("Masukkan nama pesanan: ")
            restoran_queue.enqueue(pesanan)
        elif pilihan == '2':
            restoran_queue.dequeue()
        elif pilihan == '3':
            restoran_queue.display_queue()
        elif pilihan == '4':
            print("Keluar dari program.")
            break
        else:
            print("Opsi tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()
