
gabona = input('Gabona neve:')
gabonak = ['búza', 'árpa', 'zab', 'kukorica', 'rozs']

if gabona == '':
    exit()

if gabona in gabonak:
    print("megfelelő gabona")
else: 
    print("ismeretlen gabona")
