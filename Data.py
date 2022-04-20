import csv

def mostrar(self):
      with open('listasenadores.csv', newline='') as File:  
      reader = csv.reader(File)
      for row in reader:
          print(row)
    
