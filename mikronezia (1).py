#Juhász Roland, Szoft I N, 2021-01-12

from os import altsep, defpath
from country import Country
from typing import List 

class Mikronezia:
    # __init__ = konstruktor
    def __init__(self):
        self.countries: List[Country] = []
        self.sep = ':'
        
    def read_content(self):
        file_name = 'countries.txt'
        fp = open(file_name, 'r', encoding='utf-8')
        self.lines = fp.readlines()
        fp.close()

    def convert_content(self):
        for line in self.lines[1::]:            
            (id, name, area, population) = line.split('#')
            country = Country(id, name, int(area), int(population))
            self.countries.append(country)

    # Legnépesebb ország
    def most_populated(self):
        max_country = self.countries[0]
        for country in self.countries[1:]:
            #print(country.name) -kiiratja az összes countryt
            if country.population > max_country.population:
                max_country = country
        print(
            'Legnépesebb:',
            max_country.name,
            max_country.population
            )

    # Legkisebb területű ország
    def smallest_area(self):
        min_country = self.countries[0]
        for country in self.countries[1:]:
            if country.area < min_country.area:
                min_country = country
        print('A legkisebb méretű ország adatai:',
         min_country.id, 
         min_country.name,
         min_country.area, 
         min_country.population)

    # 99 ezernél kisebb népesség
    def less_than_ninety_nine_thousand(self):
        print('99 ezernél kisebb népesséfű országok:')        
        for country in self.countries:
            if country.population < 99000:
             print(country.name, country.population)

    # Hány 500 négyeztkilométernél nagyobb területi ország van?
    def more_than_five_hunderd_area(self):
        darab = 0
        print('500 négyzetkilóméternél nagyobb területű települések:')
        for county in self.countries:
            if county.area > 500:
                darab += 1
        print(darab)

    # Hány ország nevében szerepel a "sziget" szó?
    def island_word_in_name(self):
        darab = 0
        for country in self.countries: 
            if 'sziget 'in country.name:
                darab += 1
        print('A sziget szerepel:',darab) 

    # Az országok területe összesen
    def sum_areas(self):
        osszeg = 0
        for country in self.countries:
            osszeg += country.area 
        print('Össz terület', osszeg)

    # Az országok népességének átlaga
    def population_average(self):
        #darab,összeg (MEGSZÁMOLÁS,ÖSSZEGZÉS)
        osszeg = 0
        darab = len(self.countries)
        for country in self.countries:
            osszeg += country.population
            atlag = osszeg / darab
        print('A népességek átlaga: %.2f' % atlag)

    # Állapítsuk meg, hogy egyszavas, vagy nem, a név
    def is_one_word(self, country: Country):
        if '-' in country.name:
            return False
        else:
            return True 

    def write_a_country(self, fp, country):
        fp.write(country.id)
        fp.write(self.sep)
        fp.write(country.name)
        fp.write(self.sep)
        fp.write(str(country.area))
        fp.write(self.sep)
        fp.write(str(country.population))
        fp.write('\n')


    def write_one_word(self):
        fp = open('oneword.txt', 'w')
        for country in self.countries:
            if self.is_one_word(country):
                self.write_a_country(fp, country)
        fp.close()

#Mikronezia osztály vége: 4 feladat) példányosítás
mikro= Mikronezia()

mikro.read_content()
mikro.convert_content()
mikro.most_populated()
mikro.smallest_area()
mikro.less_than_ninety_nine_thousand()
mikro.more_than_five_hunderd_area()
mikro.island_word_in_name()
mikro.sum_areas()
mikro.population_average()
mikro.write_one_word()



#Ezzel a countyn belül az első sorban lévő country-t megnézi e, hogy több szavas-e.
#91-95 sorra vonatkozik. 
#es = mikro.is_one_word(mikro.countries[1])   
#print('res:',res)

