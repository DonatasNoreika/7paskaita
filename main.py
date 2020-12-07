class Irasas:
    def __init__(self, suma):
        self.suma = suma

class PajamuIrasas(Irasas):
    pass

class IslaiduIrasas(Irasas):
    pass

biudzetas = []
irasas1 = PajamuIrasas(2000)
irasas2 = IslaiduIrasas(20)
irasas3 = IslaiduIrasas(10)
biudzetas.append(irasas1)
biudzetas.append(irasas2)
biudzetas.append(irasas3)

for irasas in biudzetas:
    if isinstance(irasas, PajamuIrasas):
        print("Pajamos", irasas.suma)
    if type(irasas) is IslaiduIrasas:
        print("Išlaidos", irasas.suma)


#         pakeitimas
