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
    sor = int(input("Melyik sorba szeretnéd tenni? "))-1
    oszlop = int(input("Melyik oszlopba szeretnéd tenni? "))-1
    if sor >= tablameret or sor <= 0 or oszlop >= tablameret or oszlop <= 0:
        print(f"A tábla {tablameret} x {tablameret} méretű, újra!")
        print(endtag)
        continue 
    jatek[sor][oszlop] = "X"
    lepesek += 1
    egesz_sor = jatek[0]

    
    # print(f"Első sor: {egesz_sor}")
    print(endtag)
