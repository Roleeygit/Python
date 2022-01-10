from dolgozo import Dolgozo

class Juta:
  def __init__(self):
    self.file_name = 'dolgozok.txt'
  
  def file_read(self):
    fp = open(self.file_name, 'r', encoding='utf-8')
    self.lines = fp.readlines()
    fp.close()
   

  #ezt használni kell a projektemben
  def convert_content(self):
    self.dolgozok = [] 
    for line in self.lines:
      (az,
      nev,
      anyjaneve,
      telepules,
      cim,
      fizetes,
      jutalom,
      belepes,
      szuletes,
      szulhely) = line.split(';')
      dolgozo = Dolgozo(az,nev,anyjaneve,telepules,cim, int(fizetes),int(jutalom),belepes,szuletes,szulhely)
      self.dolgozok.append(dolgozo)  #append hozzáfűzi a dolgozo objektumot a listához, így minden dolgozo bekerül a listába
    #print(self.dolgozok[0].nev)   #Kiadja a 0. sorban névő ember nevét

  #Jutalmak összege:
  def jutalmak_osszege(self):
    osszeg = 0
    for dolgozo in self.dolgozok:
      osszeg = osszeg + dolgozo.jutalom
    #print(dolgozo.jutalom)      #jutalmakat bármire át lehet írni, igy minden sorból kiirta pl. emebrek neve
    print("Jutalmak összege:", osszeg)
    
  def fizetesek_atlaga(self):
    osszeg = 0
    for dolgozo in self.dolgozok:
      osszeg = osszeg + dolgozo.fizetes
    darab = len(self.dolgozok)
    atlag = osszeg / darab
    print("Fizetések átlaga:", atlag)  



juta = Juta()
juta.file_read()
juta.convert_content()
juta.jutalmak_osszege()
juta.fizetesek_atlaga()