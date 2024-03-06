def loe_failist(fail: str) -> list:
    f = open(fail, "r", encoding="utf-8")
    jarjend = []
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend

def kirjuta_failist(fail: str, jarjend=[]):
    for i in range(7):
        jarjend.append(input(f"{i + 1}. sona: "))
    f = open(fail, "w", encoding="utf-8")
    for element in jarjend:
        f.write(element + '\n')
    f.close()

def tõlgi(sõnastik, sõna, keel1, keel2):
    if sõna in sõnastik[keel1]:
        indeks = sõnastik[keel1].index(sõna)
        return sõnastik[keel2][indeks]
    else:
        print(f"{sõna} puudub sõnastikus. Kas soovite selle lisada?")
        vastus = input("Jah (j) / Ei (e): ").lower()
        if vastus == 'j':
            lisa_sõna(sõnastik, sõna, keel1, keel2)
            return tõlgi(sõnastik, sõna, keel1, keel2)
        else:
            return "Sõna ei leitud."

def lisa_sõna(sõnastik, sõna, keel1, keel2):
    uus_sõna = input(f"Sisestage tõlge sõnale '{sõna}' {keel2}-keelde: ")
    sõnastik[keel1].append(sõna)
    sõnastik[keel2].append(uus_sõna)
    print(f"Sõna '{sõna}' lisatud sõnastikku.")

rus = loe_failist("rus.txt")
est = loe_failist("est.txt")

def est_to_rus():
    sõna = input("Введите слово на эстонском: ")
    tõlge = tõlgi({"est": est, "rus": rus}, sõna, "est", "rus")
    print(f"Перевод на русский: {tõlge}")

def rus_to_est():
    sõna = input("Введите слово на русском: ")
    tõlge = tõlgi({"est": est, "rus": rus}, sõna, "rus", "est")
    print(f"Перевод на эстонский: {tõlge}")

print("1.Перевести с эстонского на русский")
print("2.Перевести с русского на эстонский")


while True:
    valik = input("выбор (1/2): ")
    if valik == '1':
        est_to_rus()
    elif valik == '2':
        rus_to_est()





