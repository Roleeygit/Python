
def check_crop_name(name):
    nevek =  ["búza","kukorica","zab","rozs"]
    if name in nevek: 
        return True
    else:
        return False

gabona_nev = ''
while gabona_nev != 'end':
    gabona_nev = input('Gabona nev:')
    if gabona_nev != 'end':
        if check_crop_name(gabona_nev):
            print("Megfelelő")
        else: 
            print("Nem felel meg")





