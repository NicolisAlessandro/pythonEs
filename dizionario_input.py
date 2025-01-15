# Scrivi un programma che chieda all'utente di aggiungere una nuova coppia chiave-valore al dizionario.
persona = {"nome": "Mario"}
chiave = input("Inserisci una nuova chiave: ")
valore = input("Inserisci il valore: ")
persona[chiave] = valore
print(persona)