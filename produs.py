from errorHandling import *
class produs:
    def __init__(self, nume, pret, pret_open, pret_close):
        self.nume = nume
        try:
            self.lastPret = float(pret)
        except:
            self.lastPret = 0
        self.listaPret = []
#        self.listaPret.append(float(self.lastPret))
        self.tendinta = 0
        self.tendintaActuala = 0
        self.MAXNR = 99999
        try:
            self.pret_initial = pret
            self.pret_max = pret
            self.pret_min = pret
        except:
            self.pret_initial = 0
            self.pret_max = 0
            self.pret_min = 999999999     
            
    def afisareProdus(self):
        print("Produsul " + str(self.nume) + " are pretul " + str(self.lastPret) + " trend " + str(self.tendinta) + ".")
        afisare = " "
        for pret in self.listaPret:
            afisare = afisare + " " + str(pret)
        print(afisare)
            
    def modifPret(self, pret,test):

        if test:
#            print("pret : " + str(pret))
            try:
                pretActual = float(pret)
#                print("pret actual : " + str(pretActual))
                if pretActual > float(self.lastPret):
                    if self.tendintaActuala < 0:
                        self.tendintaActuala = 0
                    self.tendinta += 1
                    self.tendintaActuala += 1
                    if pretActual/100 + pretActual > self.lastPret:
                        self.tendinta += 1
                        self.tendintaActuala += 1
                        if self.tendinta > 3:
                            self.tendintaActuala = 0
                            print("Pretul " + self.nume + " a crescut. Pret vechi " + str(self.lastPret) +
                            " pret nou " + str(pret) + " tendinta " + str(self.tendinta))
                    if self.tendintaActuala > 3:
                        print("!!!Pretul " + self.nume + " a crescut. Pret vechi " + str(self.lastPret) +
                              " pret nou " + str(pret) + " tendinta " + str(self.tendinta) +
                              " tendinta actuala : " + str(self.tendintaActuala))
                elif pretActual < self.lastPret and self.lastPret > 0:
                    if self.tendinta > 3:
                        self.tendintaActuala = 0
                    self.tendinta -= 1
                    self.tendintaActuala -= 1
                    if pretActual < self.lastPret - self.lastPret/100:
                        self.tendinta -= 1
                        self.tendintaActuala -= 1
                    if self.tendinta < -3:
                        self.tendintaActuala = 0
                        print("Pretul " + self.nume + " a scazut. Pret vechi " + str(self.lastPret) +
                              " pret nou " + str(pret) + " tendinta " + str(self.tendinta))
                    if self.tendintaActuala < - 3:
                        print("!!!Pretul " + self.nume + " a scazut. Pret vechi " + str(self.lastPret) +
                              " pret nou " + str(pret) + " tendinta " + str(self.tendinta) +
                              " tendinta actuala : " + str(self.tendintaActuala))
            except:
                data = "eroare pret " + self.nume
                scrieEroare("ErrorLog.txt", data)
        try:
            if self.lastPret != float(pret):
                self.lastPret = float(pret)
                self.listaPret.append(float(self.lastPret))
        except:
            self.lastPret = 0
            self.listaPret.append(float(self.lastPret))

    def cautare_produs(self, nume, listaProduse, pret):
    #    print("cautare_produs")
        for produs in listaProduse:
        #    print(f' produs 1 {prod.nume} == produs 2 {produs.nume}')
            if nume == produs.nume:
                produs.modifPret(pret, True)
                return True
        return False