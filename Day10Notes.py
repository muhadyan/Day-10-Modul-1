'''
# Class = cetakan object
class Mobil:
    warna= 'merah'
    tahun= 2010

# create object mobil1

mobil1 = Mobil()
print(mobil1)
print(mobil1.warna)
print(mobil1.tahun)

mobil2 = Mobil()
print(mobil2.warna)     # hasilnya sama dengan yg 'mobil1' karna cetakannya sama
print(mobil2.tahun)


# Class dengan atribut
class MobilCustom():
    def __init__(self, warna, tahun, model):
        self.color = warna
        self.year = tahun
        self.model = model
    # method
    def jadul(self):
        if self.year < 2010:
            return True
        else:
            return False
    def tes(self):
        return (self.color, self.year, self.model, self.jadul())

mobilC1 = MobilCustom('pink', 2018, ['A', 'B'])     # kalo di cetakannya ada 3 atribut, maka masukinnya harus 3 juga
mobilC2 = MobilCustom('blue', 2009, ['A', 'B'])

print(mobilC1.year)
# bisa juga
print(getattr(mobilC1, 'year'))

# manggil method
print(mobilC2.jadul())
print(mobilC1.tes())

# ngecek ada atribut yg dimaksud apa engga
print(hasattr(mobilC1, 'color'))



# Bikin cetakan lain yg mirip
class Mobil:
    def __init__(self, warna, seat):
        self.warna = warna
        self.seat = seat

class Car(Mobil):       # disebut inheritance
    pass
# bisa juga
class Car(Mobil):
    def __init__(self, warna, seat):
        Mobil.__init__(self, warna, seat)
# bisa juga
class Car(Mobil):
    def __init__(self, warna, seat):
        super().__init__(warna, seat)

mobil1 = Mobil('pink', 4)
car1 = Car('black', 8)
print(mobil1.warna, mobil1.seat)
print(car1.warna, car1.seat)


# Bikin cetakan lain yg mirip tapi ditambahin atributnya
class Mobil:
    def __init__(self, warna, seat):
        self.warna = warna
        self.seat = seat

class Car(Mobil):
    def __init__(self, warna, seat, soundSys):
        super().__init__(warna, seat)
        self.soundSys = soundSys
# bisa juga
class Car(Mobil):
    gps = True
    def __init__(self, soundSys):
        self.soundSys = soundSys

mobil1 = Mobil('pink', 4)
car1 = Car('black', 8, 'simbada')
print(mobil1.warna, mobil1.seat)
print(car1.warna, car1.seat, car1.soundSys)


# buat ngeliat atribut nya apa aja
from pprint import pprint
pprint(vars(car1))
# bisa juga
print(vars(car1))


# buat nambahin atribut dari Object yg udah dibuat
mobil1.velg = '23 inch'
print(vars(mobil1))
# bisa juga
setattr(mobil1, 'velg', '23 inch')
print(vars(mobil1))


# buat hapus atribut objek
delattr(mobil1, 'warna')
print(vars(mobil1))



class Z:
    nama = 'Z'
    usia = 21

objZ = Z()

# buat hapus atribut kelas
del Z.nama
print(objZ.usia)



# vars mengambil nama menjadi variabel
nama = 'ultraman'
vars()[nama] = 12345
print(ultraman)
'''
