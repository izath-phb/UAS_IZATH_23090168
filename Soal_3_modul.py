class RestoranQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, order):
        self.queue.append(order)
        print(f"Pesanan '{order}' telah ditambahkan ke dalam antrian.")

    def dequeue(self):
        if len(self.queue) > 0:
            order = self.queue.pop(0)
            print(f"Pesanan '{order}' telah dihapus dari antrian.")
            return order
        else:
            print("Antrian kosong! Tidak ada pesanan yang dapat dihapus.")
            return None

    def display_queue(self):
        if len(self.queue) > 0:
            print("Antrian saat ini:")
            for idx, order in enumerate(self.queue, 1):
                print(f"{idx}. {order}")
        else:
            print("Antrian kosong!")
