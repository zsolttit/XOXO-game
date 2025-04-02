import os 
jatek = [[1,2,3],[4,5,6,],[7,8,9]]
jatek = []

lepesek = 0
tablameret = int(input("Mekkora táblán szeretnél játszani? "))

def jatekCsinal(meret):
    for i in range(meret):
        jatek.append([])
        for c in range(meret):
            jatek[i].append("-")

def mutatTabla():
    for i in range(len(jatek)):
        for c in range(len(jatek)):
            print(jatek[i][c], end=" ")

        print()
    print(f"\nLépések: {lepesek}")

jatekosok = ["X","O"]
jelenlegi_jatekos = 0

def kovi_jatekos():
    global jelenlegi_jatekos
    jelenlegi_jatekos ^=  1

def jatekos():
    global jatekosok
    global jelenlegi_jatekos
    return jatekosok[jelenlegi_jatekos]

def checkRow(row):
    global jatek
    szuper = 0
    lastelem = ""
    for ertek in jatek[row]:
        if lastelem == ertek:
            szuper += 1
            if szuper == 5:
                return lastelem
        else:
            lastelem = ertek
            szuper = 1
        if ertek == "-":
            szuper = 0
    return False

def checkCol(col):
    global jatek
    szuper = 0
    lastelem = ""
    for sor in jatek:
        if lastelem == sor[col]:
            szuper += 1
            if szuper == 5:
                return lastelem
        else:
            lastelem = sor[col]
            szuper = 1
        if sor[col] == "-":
            szuper = 0
    return False


    # for i in range(len(jatek[row])-1):
    #     if jatek[0][i] == jatek[0][i+1]:
    #         szuper+=1
            
    #     else:
    #         szuper = 0
    # if szuper == tablameret-1:
    #     print(f"Az {row}. sor kigyűlt.")

while tablameret <5:
    tablameret = int(input(f"A tábla mérete minimum 5 legyen, kérlek válassz újra: "))

rossz_Szam = " Helytelen szám írd be újra!! "
endtag =f"\n{"__"*tablameret}\n"
jatekCsinal(tablameret)
jatekvege = False

print(f"A játék elkezdődött!")

while not jatekvege:
    mutatTabla()
    bek = input("Hova szeretnéd tenni? 'sor-oszlop' ").split("-")
    sor = int(bek[0])-1
    oszlop = int(bek[1])-1

    if sor < 0 or oszlop < 0 or sor >= tablameret or oszlop >= tablameret:
        print("Csak olyan számot adhatsz meg, ami benne van a táblában.")
        continue
    

    if jatek[sor][oszlop] != "-":
        print("Ide már raktak számot te nyomorék")
    else:
        jatek[sor][oszlop] = jatekos()
        lepesek += 1
        egesz_sor = jatek[0]
        kovi_jatekos()
    
    # print(jatek)
    # print(checkRow(sor) , " ez az")
    # print(checkCol(oszlop) , " ez az")

    if checkCol(oszlop):
        print(f"Vége a játéknak, nyertes fél: {checkCol(oszlop)}")
        jatekvege = True
        break
    elif checkRow(sor):
        jatekvege = True
        print(f"Vége a játéknak, nyertes fél: {checkRow(sor)}")
        break

    
    
    