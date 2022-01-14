#Készítette: Juhász Roland Szoft I N 2021.01.14
print('Készítette: Juhász Roland Szoft I N 2021.01.14')

from vegetableModel import VegetableModel
from typing import List

class Vegetable:
    def __init__(self):
        self.file_name = 'zoldseg.txt'
        self.vegetables: List[VegetableModel] = []
        self.lines = []
    
    def read_content(self):
        fp = open(self.file_name, 'r', encoding='utf-8')
        self.lines = fp.readlines()
        fp.close()
    
    def convert_content(self):
        for line in self.lines[1::]:
            (id, name, weight,site, price) = line.split(';')
            vegetableModel = VegetableModel(
                id, name, str(weight),site, str(price)
            )
            self.vegetables.append(vegetableModel)
    
    def print_all(self):
        for vegetable in self.vegetables:
            print(
                vegetable.name,
                vegetable.site,
                vegetable.weight
                )
    
    # A Szegeden található zöldségek össz tömegét
    def szeged_sum_wight(self):
      darab = 0
      for vegetable in self.vegetables:
        if 'Szeged' in vegetable.site:
          darab += int(vegetable.weight)
      print('Szegedi zöldségek össztömege:', darab,'kg')



    # Melyik telephelyen van értékben legtöbb zöldség
    def most_valuable_vegetables(self):
        max_value = self.vegetables[0]
        for vegetables in self.vegetables:
          if vegetables.price > str(max_value.price):
            max_value = vegetables
        print('Ezen a telephelyen van értékben a legtöbb zöldség:',max_value.site)

vegetable = Vegetable()
vegetable.read_content()
vegetable.convert_content()
vegetable.print_all()
vegetable.szeged_sum_wight()
vegetable.most_valuable_vegetables()