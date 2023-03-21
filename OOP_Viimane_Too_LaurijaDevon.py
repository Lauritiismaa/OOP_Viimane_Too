#Lauri Tiismaa, Devon Peeterson IT-21 21.03.2023


from easygui import *

class karakter:
    
    
    def __init__(self, nimi, elud, tugevus):
        self.nimi = nimi
        self.elud = elud
        self.tugevus = tugevus
        
        
    def kaotaelusi(self, dmg):
        self.elud = self.elud - dmg
        if self.elud > 0:
            print("Vastane on surnud!")
        else:
            print("Sa surid!")
            #exit()
        
        
    def lisaelusi(lisaelud):
        self.elud + (lisaelud)
        print("Teil on nüüd " + str(self.elud) + " elu")
        
    
    def andmed(self):
        print("Tegelase nimi: " + self.nimi + "/Tegelase elud: " + str(self.elud) + "/Tegelase tugevus: " + str(self.tugevus))


class vaenlane:
    
    
    def __init__(self, elud, tugevus):
        self.elud = elud
        self.tugevus = tugevus
        
        
    def kaotaelusi(self, dmg):
        while self.elud > 0:
            self.elud = self.elud - dmg
            if self.elud <= 0:
                print("Vastane kaotas, võid edasi liikuda!")

        
        def andmed(self):
            print("Vaenlase elud: " + str(self.elud) + "/Vaenlase tugevus: " + str(self.tugevus))
        
        
tegelane1 = karakter("Madis", 100, 30)
vaenlane1 = vaenlane(30, 5)
vaenlane2 = vaenlane(50, 15)


while tegelane1.elud > 0:
    
    
    nupud = ["Vasakule","Otse","Paremale"]
    vajutus = buttonbox("Olete labürindis, mis suunas soovid minna?",choices = nupud)
    
    
    if vajutus == None:
        msgbox("Vajuta mingit nuppu torbik")
    

    elif vajutus == "Vasakule":
        tegelane1.kaotaelusi(vaenlane1.tugevus)
        vaenlane1.kaotaelusi(tegelane1.tugevus)
        if tegelane1.elud > 0:
            msgbox("Vastane on surnud! Liigu edasi.")
        else:
            msgbox("Oled surnud")
            
    elif vajutus == "Otse":
        tegelane1.kaotaelusi(vaenlane2.tugevus)
        vaenlane2.kaotaelusi(tegelane1.tugevus)
        if tegelane1.elud > 0:
            msgbox("Vastane on surnud! Liigu edasi.")
        else:
            msgbox("Oled surnud")
 
    
    else:
        tegelane1.kaotaelusi(vaenlane2.tugevus)
        vaenlane2.kaotaelusi(tegelane1.tugevus)
        if tegelane1.elud > 0:
            msgbox("Vastane on surnud! Liigu edasi.")
        else:
            msgbox("Oled surnud")
    
    
    if tegelane1.elud == 5:
        break


while tegelane1.elud == 5:
    nupud = ["Vasakule","Paremale"]
    vajutus2 = buttonbox("Sein on ees, kas lähed vasakule või paremale?",choices = nupud)
    
        
    if vajutus2 == "Vasakule":
        msgbox("Kukkusid lõksu ja said surma!")
    else:
        msgbox("Jõudsid labürindi lõppu! Oled Võitnud!")
    break


    if tegelane1.elud <= 0:
        exit()

#tegelane1.andmed()
#vaenlane1.andmed()
