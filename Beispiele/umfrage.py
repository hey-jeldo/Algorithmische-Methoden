umfrage = {}
umfrage_aktiv = True
while umfrage_aktiv:
    antwort = input("Nennen Sie bitte Ihr Lieblingsgericht: ")
    if umfrage.get(antwort):
        umfrage[antwort] += 1
    else:
        umfrage[antwort] = 1
    repeat = input("Soll eine weitere Person befragt werden (ja/nein)?")
    if repeat == 'nein':
        umfrage_aktiv = False
print("\n--- Umfrageergebnis ---")
for name, anzahl in umfrage.items():
    print(str(anzahl) + " Person(en) isst/essen gerne " + name + ".")