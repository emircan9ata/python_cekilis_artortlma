import random


x=int(input("lütfen ilk sınav notunuzu giriniz:"))

y=int(input("Lütfen ikinci sınav notunuzu giriniz:"))

sonuc=int()

def ortalama():
    if x and y :
       
        sonuc=(x+y)/2
        
        if sonuc<50:
            print(f"ortalamanız 50 den küçüktür üzgünüm dersten kaldınız. Ortalamanız: {sonuc}")
            return

        elif sonuc >=50:    
            print(f"tebrikler 50 ve üstü oratalamaya sahipsin dersten geçtin. Ortalamanız: {sonuc}")
        return
        


ortalama()























