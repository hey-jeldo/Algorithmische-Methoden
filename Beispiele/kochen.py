def kochen(gericht, **zutaten):
    zutaten['Gericht'] = gericht
    return zutaten
x = kochen('pizza', Mehl='300 Gramm', Olivenöl='50 ml', Tomaten='4 Stück')
print(x)