#crop.py
from cropModel import CropModel
from typing import List

class Crop:
    def __init__(self):
        self.file_name = 'termes.txt'
        self.crops: List[CropModel] = []

    def read_content(self):
        fp = open(self.file_name, 'r', encoding="utf-8")
        self.lines = fp.readlines() 
        fp.close()
    
    
    def convert_content(self):        
        for line in self.lines[1:]:
            (id, name, place, size, cropyield, year) = line.split(':')
            cropModel = CropModel(
                id, 
                name, 
                place, 
                int(size),
                float(cropyield.replace(',', '.') ), 
                int(year)
                )
            self.crops.append(cropModel)


    # Földterület összesen
    def total_land(self):
        osszeg = 0
        for crop in self.crops:
            osszeg += crop.size
        print('Összeg földterület:',osszeg,'hektár')

    # Hány tonna búza termés volt összesen?
    def sum_wheat(self):
        osszeg = 0
        for chop in self.crops:
            if chop.name == 'búza':
              osszeg += chop.cropyield
        print("Búza termés összesen:",osszeg,'tonna')

    # 300-nál több termés esetén név és termés legyen kiírtva
    def more_then_three_hundred(self):
        for chop in self.crops:
            if chop.cropyield > 300:
                print("300nál több termés:",chop.place,chop.name)

    # Hány területen termelnek árpát?
    def area_barley(self):
        darab = 0
        for chop in self.crops:
            if chop.name == "árpa":
                darab+= 1
        print('Ennyi helyen termetnek árpát:',darab)


    # Hány terület nagyobb mint 80 hektár?
    def area_larger_eighty(self):
        darab = 0
        for chop in self.crops:
            if chop.size > 80:
                darab += 1
        print("80nál nagyobb terület:",darab)
    

    # Milyen gabona termett a "Csendes" nevű területen?
    def which_crop_on_csendes(self):
        for chop in self.crops:
            if chop.place == 'Csendes':
                print('A csendes helyen termelt gabona:', chop.name)
    
    # Melyik területről lett a legkevesebb búzatermés?
    def which_place_wheat_min(self):
        min_chop = self.crops[0]
        for chop in self.crops:
            if chop.cropyield <  min_chop.cropyield:
                min_chop = chop
        print('Legkevesebb búzatermés innen:',min_chop.place)

crop = Crop()
crop.read_content()
crop.convert_content()
crop.total_land()
crop.sum_wheat()
crop.more_then_three_hundred()
crop.area_barley()
crop.area_larger_eighty()
crop.which_crop_on_csendes()
crop.which_place_wheat_min()