from bridgeModel import  BridgeModel

class Brig:
    def read_file(self):
        fp = open('hidak.txt', 'r', encoding="utf-8")
        lines = fp.readlines()
        fp.close()

        self.bridges = []

        for line in lines[1::]:
            (id, name, place, length, year) = line.split(':')
            bridge = BridgeModel(id, name, place, int(length), int(year))
            self.bridges.append(bridge)

    # Leghosszabb híd
    def longest(self):
        max_bridge = self.bridges[0]
        #bridge-et én adom meg
        for bridge in self.bridges:
            if bridge.length > max_bridge.length:
                max_bridge = bridge
        print(
            max_bridge.name,
            max_bridge.length)    

    # A Megyeri híd szerepel a listában?
    def isHaveMegyeri(self):
        n = len(self.bridges)
        ker = 'Megyeri híd'
        i = 0
        while i<n and self.bridges[i].name != ker:
            i += 1

        if i<n:
            print('Van', ker) 
        else:
            print('Nincs',ker)       
    
    # A nem budapesti hidak nobp.txt fájlba
    def select_nobp(self):
        for bridge in self.bridges:
            if bridge.place != 'Budapest':
                self.write_bridge(bridge)
        print('Kiírva')
        

    # Híd kiírása
    def write_bridge(self, bridge):
        fp = open('nobp.txt', 'a', encoding='utf-8')
        sep = ';'
        fp.write(bridge.id)
        fp.write(sep)
        fp.write(bridge.name)
        fp.write(';')
        fp.write(bridge.place)
        fp.write(';')
        fp.write(str(bridge.length))
        fp.write('\n')
        fp.close()

brig = Brig()
#metódus meghívások
brig.read_file()
brig.longest()
brig.isHaveMegyeri()
brig.select_nobp()
