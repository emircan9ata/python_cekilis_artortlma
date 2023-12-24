import random

users = ["ahmet", "mehmet", "buse", "kerem","ali"]
oduller = ["tatil", "araba", "yemek"]
cekilisler = {}

def cekilis_yap():
    #  Her öğrenciye verilen hak sayısı
    hak_sayisi = 1 
   

    while users and oduller:
        secilen_user = random.choice(users)
        secilen_odul = random.choice(oduller)

        if secilen_user not in cekilisler and secilen_odul not in cekilisler.values():
            cekilisler[secilen_user] = secilen_odul
            hak_sayisi += 1
            print(f"{hak_sayisi-1}. çekilişte {secilen_user} adlı yarışmacımız:  {secilen_odul} ödülünü kazandı.")
            users.remove(secilen_user)
            

            if hak_sayisi > len(oduller):
                break

     

cekilis_yap()














