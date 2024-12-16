#Scrivi un programma che inserito un numero mi dica se è positivo, negativo o è uguale a 0;

num = int(input("Inserisci un numero: "))

if num > 0:
    print("Il numero è positivo:")
elif num < 0:
    print("Il numero è negativo")
else:
    print("il numero è 0")
