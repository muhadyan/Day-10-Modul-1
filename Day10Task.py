class student:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

data = [
    {'nama': 'Andi', 'usia': 21},
    {'nama': 'Budi', 'usia': 22},
    {'nama': 'Caca', 'usia': 23},
    {'nama': 'Deni', 'usia': 24}
    ]

def creatObj(x):
    nama = x['nama']
    vars()[nama] = student(x['nama'], x['usia'])
    return vars()[nama]
# bisa juga
def creatObj(x):
    return student(x['nama'], x['usia'])
# bisa juga
dataNew = list(map(lambda x : student(x['nama'], x['usia']), data))

print(dataNew[0].nama)
print(dataNew[0].usia)



# untuk persegi, Luas persegi => sisi
class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi
        self.keliling = self.sisi * 4
        self.luas = self.sisi ** 2

persegiA = Persegi(4)
persegiB = Persegi(8)
persegiC = Persegi(12)

print(vars(persegiA))
print(vars(persegiB))
print(vars(persegiC))

# bikin program yg membuat angka biasa menjadi angka Romawi
class Romawi:
    def keRomawi(self, num):
        angka = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        simbol = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        angRom = ''
        i = 0
        while  num > 0:
            for a in range(int(num / angka[i])):
                angRom += simbol[i]
                num -= angka[i]
            i += 1
        return angRom


print(Romawi().keRomawi(498))