class Buah:
    def __init__(self, nama, warna, rasa):
        self._nama = nama
        self._warna = warna
        self._rasa = rasa
    
    def setNama(self, nama):
        self._nama = nama
    
    def setWarna(self, warna):
        self._warna = warna
    
    def setRasa(self, rasa):
        self._rasa = rasa
    
    def information(self):
        return f'Buah: {self._nama}, Warna: {self._warna}, Rasa: {self._rasa}'
    
class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self._vitamin = vitamin
    
    def setVitamin(self, vitamin):
        self._vitamin = vitamin
    
    def information(self):
        return f'{super().information()}, Vitamin: {self._vitamin}'
    
mangga_harum_manis = Mangga("Harum Manis", "Hijau", "Manis", "Vitamin C")
print(mangga_harum_manis.information())

mangga_harum_manis.setNama("Arumanis")
mangga_harum_manis.setWarna("Kuning")
mangga_harum_manis.setRasa("Manis")
mangga_harum_manis.setVitamin("Vitamin A")

print(mangga_harum_manis.information())

