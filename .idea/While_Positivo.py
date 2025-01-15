#Scrivi un programma che chieda all'utente di inserire un numero positivo e continui a chiedere finché non lo fa. 

numero = -1
while numero < 0:
    numero = int(input("Inserisci un numero positivo: "))
print("Hai inserito:", numero)