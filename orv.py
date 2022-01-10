from paciens import Paciens

class Orv:
    def beolvas(self):
        fajlnev = 'paciens.txt'
        fajlmod = 'r'
        fp = open(fajlnev, fajlmod, encoding="utf-8")
        sorok = fp.readlines()
        fp.close()
        self.paciensek = []
        for sor in sorok[1::]: #Az első sortol olvassa (0.at hagyja ki)
            (nev, tunet, kezeles, ido, ar) = sor.split(':')
            paciens = Paciens(nev, tunet, kezeles, ido, ar)
            self.paciensek.append(paciens)

            
            
    
    def moxavalKezeltek(self):
        for paciens in self.paciensek:
            print(paciens.nev)

    def bevetel(self):
        osszeg = 0
        for paciens in self.paciensek:
            osszeg = osszeg + int(paciens.ar)
        print('Összeg:', osszeg)

    def tizezernelNagyobbBevetel(self):
        for paciens in self.paciensek:
            if int(paciens.ar) > 10000:
                print(paciens.nev, 
                      paciens.tunet,
                      paciens.kezeles,
                      paciens.idopont,
                      paciens.ar)



 
orv = Orv()
orv.beolvas()
orv.moxavalKezeltek()
orv.bevetel()
orv.tizezernelNagyobbBevetel()


