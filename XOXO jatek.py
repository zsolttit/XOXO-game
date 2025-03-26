import os 
jatek = [[1,2,3],[4,5,6,],[7,8,9]]
jatek = []

def jatekCsinal(meret):
    for i in range(meret):
        jatek.append([])
        for c in range(meret):
            # jatek[i].append(c+i)
            jatek[i].append("-")

def mutatTabla():
    # print("\n")
    # os.system('cls')
    # print(endtag)
    for i in range(len(jatek)):
        for c in range(len(jatek)):
            print(jatek[i][c], end=" ")

        print()
    print(f"\nLépések: {lepesek}")


lepesek = 0
tablameret = int(input("Mekkora táblán szeretnél játszani? "))
rossz_Szam = " Helytelen szám írd be újra!! "
endtag =f"\n{"__"*tablameret}\n"
jatekCsinal(tablameret)
jatekvege = False

while not jatekvege:
    mutatTabla()
    bek = input("Hova szeretnéd tenni? ").split("-")
    # sor = int(input("Melyik sorba szeretnéd tenni? "))-1
    # oszlop = int(input("Melyik oszlopba szeretnéd tenni? "))-1
    sor = int(bek[0])-1
    oszlop = int(bek[1])-1

    if sor < 0 or oszlop < 0 or sor >= tablameret or oszlop >= tablameret:
        print("Rossz táblaméret")
        continue
    # print("ANYÁD")
    # print(f"Sor: {sor} Oszlop: {oszlop} Tbalamerete: {tablameret}")

    if jatek[sor][oszlop] == "X":
        print("Ide már raktál X et te nyomorék")
    else:
        jatek[sor][oszlop] = "X"
        lepesek += 1
        egesz_sor = jatek[0]

    
    # print(f"Első sor: {egesz_sor}")
    