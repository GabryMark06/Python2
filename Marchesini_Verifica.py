#Senza uso di risorse
class Articolo: 
  def __init__(self, codice, fornitore, marca,prezzo, quantita):
    self.codice=codice
    self.fornitore=fornitore
    self.marca=marca
    self.prezzo=prezzo
    self.quantita=quantita

  def scheda_articolo(self):
    s=f"Codice: {self.codice}\nFornitore: {self.fornitore}\nMarca: {self.marca}\nPrezzo: {self.prezzo}\nQuantita: {self.quantita}"
    return s

  def modifica_scheda(self):
    print("Seleziona l' attributo da modificare")
    print("Cosa vuoi modificare?")
    print("1. Fornitore")
    print("2. Marca")
    print("3. Prezzo")
    print("4. Quantità")
    print("5. Nulla")
    scelta=int(input())
    if scelta==1:
      self.fornitore=input("Inserisci il nuovo fornitore: ")
    elif scelta==2:
      self.marca=input("Inserisci la nuovo marca: ")
    elif scelta==3:
      self.prezzo=float(input("Inserisci il nuovo prezzo: "))
    elif scelta==4:
      self.quantita=int(input("Inserisci la nuova quantita: "))
    elif scelta==5:
      print("Modifica nulla")
    else:
      print("Scelta non valida")
    #9:27 Invernizzi

class Televisore(Articolo):
    def __init__(self, codice, fornitore,marca,prezzo,quantita,pollici,tipo):
      super().__init__(codice, fornitore, marca,prezzo, quantita)
      self.pollici=pollici
      self.tipo=tipo

    def scheda_articolo(self):
      s=super().scheda_articolo()+f"\nPollici: {self.pollici}\nTipo: {self.tipo}"
      return s

class Frigorifero(Articolo):
  def __init__(self, codice, fornitore, marca, prezzo, quantita,dimensioni,modello):
    super().__init__(codice, fornitore, marca,prezzo, quantita)
    self.dimensioni=dimensioni
    self.modello=modello

  def scheda_articolo(self):
    s=super().scheda_articolo()+f"Dimensioni: {self.dimensioni}\nModello: {self.modello}"
    return s
  
class Ordine():
  def __init__(self,codice,data, piva,indirizzo):
    self.codice=codice
    self.data=data
    self.piva=piva
    self.indirizzo=indirizzo
    self.listaArticoli=[]

  def aggiungi_articolo(self,articolo):
    if articolo in self.listaArticoli:
      print(f"Articolo {articolo.codice} già presente")
    else:
      if isinstance(articolo,Televisore):
        tipo_articolo="televisore"
        self.listaArticoli.append(articolo)
        print(f"{tipo_articolo} è stata aggiunto all' ordine {self.codice} del giorno {self.data}")
      elif isinstance(articolo,Frigorifero):
        tipo_articolo="frigorifero"
        self.listaArticoli.append(articolo)
        print(f"{tipo_articolo} è stata aggiunto all' ordine {self.codice} del giorno {self.data}")
    

  def rimuovi_articolo(self,articolo):
    if articolo in self.listaArticoli:
      self.listaArticoli.remove(articolo)
      print(f"Articolo {articolo.codice} è stato rimosso")
    else:
      print(f"Articolo {articolo.codice} non presente")


  def importo_ordine(self):
    totArt=len(self.listaArticoli)
    totPrezzo=0
    for i in range(totArt):
      totPrezzo+=self.listaArticoli[i].prezzo*self.listaArticoli[i].quantita
    print(f"Importo ordine con codice {self.codice} contenente {totArt} = {totPrezzo}")

  def dettaglio_ordine(self):
    totArt=len(self.listaArticoli)
    sommaT=0
    sommaF=0
    for i in range(totArt):
      if isinstance(self.listaArticoli[i],Televisore):
        print("Articolo: Televisore")
        print(self.listaArticoli[i].scheda_articolo())
        print()
        sommaT+=self.listaArticoli[i].prezzo*self.listaArticoli[i].quantita
      elif isinstance(self.listaArticoli[i],Frigorifero):
        print("Articolo: Frigorifero")
        print(self.listaArticoli[i].scheda_articolo())
        print()
        sommaF+=self.listaArticoli[i].prezzo*self.listaArticoli[i].quantita
    return([sommaT,sommaF,sommaT+sommaF])
  
class Ordini():
  def __init__(self,nome_negozio,codice_negozio):
    self.nome_negozio=nome_negozio
    self.codice_negozio=codice_negozio
    self.listaOrdini=[]

  def aggiungi_ordine(self,ordine):
    if ordine in self.listaOrdini:
      print(f"Articolo {ordine.codice} già presente")
    else:
        self.listaOrdini.append(ordine)
        print(f"Ordine {ordine.codice} aggiunto")

  def rimuovi_ordine(self,ordine):
    if ordine in self.listaOrdini:
      self.listaOrdini.remove(ordine)
      print(f"Ordine {ordine.codice} rimosso")
    else:
      print(f"Ordine {ordine.codice} non presente")

  def totale_ordini(self):
    totOrd=len(self.listaOrdini)
    totT=0
    totF=0
    tot=0
    for i in range(totOrd):
      print(f"Ordine {self.listaOrdini[i].codice} del giorno {self.listaOrdini[i].data}")
      print()
      importi=self.listaOrdini[i].dettaglio_ordine()
      totT+=importi[0]
      totF+=importi[1]
      tot+=importi[2]
      print()
    return ([totT,totF,tot])


t1 = Televisore(1,"Fornitore 1","Sony",700,10,40,"Schermo piatto")
print(t1.scheda_articolo())
print()

t1.modifica_scheda()
print(t1.scheda_articolo())
print()
#controllato alle 09:43

t2 = Televisore(2,"Fornitore 2","Samsung",1000,5,80,"Schermo curvo")
f1 = Frigorifero(3,"Fornitore 3","Bosch",750,12,'790x2000x600','Ultra')
f2 = Frigorifero(4,"Fornitore 4","Ariston",550,10,'590x1600x500','Medium')

ordine1=Ordine(1,"24/02/2022",'213143','Via della consegna 1')
ordine1.aggiungi_articolo(t1)
ordine1.aggiungi_articolo(t2)
ordine1.aggiungi_articolo(f1)
ordine1.aggiungi_articolo(f2)
print()

ordine1.rimuovi_articolo(f2)
ordine1.rimuovi_articolo(f2)
print()

ordine1.importo_ordine()
print()

importi=ordine1.dettaglio_ordine()
print("--------------------------")
print(f"\nImporto televisori= {importi[0]}")
print(f"\nImporto frigoriferi= {importi[1]}")
print(f"\nImporto totale= {importi[2]}")
print()
#Controllato alle 10:14

ordini_negozio=Ordini("Megastore vendita ",1)
ordini_negozio.aggiungi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)
print()

ordini_negozio.aggiungi_ordine(ordine1)
print()

t3 = Televisore(5,"Fornitore 5","LG",600,4,70,"Schermo curvo")
f3 = Frigorifero(6,"Fornitore 6","Bosch",450,10,'490x1000x400','Small')
ordine2=Ordine(2,"25/02/2022",'213113','Via della consegna 2')
ordine2.aggiungi_articolo(t3)
ordine2.aggiungi_articolo(f3)
print()

ordini_negozio.aggiungi_ordine(ordine2)
print()

importiTotali=ordini_negozio.totale_ordini()
print("--------------------------")
print(f"\nImporto totale televisori= {importiTotali[0]}")
print(f"\nImporto totale frigoriferi= {importiTotali[1]}")
print(f"\nImporto totale tutti gli ordini= {importiTotali[2]}")
print()
