ik=""
while len(ik)!=11 or ik.isdigit()!=True:
    try:
        ik=input("sisesta Isukukood")
    except ValueError :
        print("Viga andmetega")
print("isikukoodi analüüs:".center(50,"-"))
print("Esimene sümbol:")
ik_list=list(ik) #["4","7","6","1",.....]
if int(ik_list[0]) not in [1,2,3,4,5,6]:
    print(ik_list[0]," - ei oli õige!")
else:
    print(ik_list[0]," - õige arv!")
    kuu=ik_list[3]+ik_list[4]
    kuu=int(kuu)   
    print("kuu:", kuu) 
    if kuu>0 and kuu<13:
        print(ik_list[3],ik_list[4],"õiged andmed!")
        paev=int(ik_list[5]+ik_list[6])
        if int(ik_list[0])==1 or int(ik_list[0])==2:
            aasta=int("18"+ik_list[1]+ik_list[2])
        elif int(ik_list[0])==3 or int(ik_list[0])==4:
            aasta=int("19"+ik_list[1]+ik_list[2])
        elif int(ik_list[0])==5 or int(ik_list[0])==6:
            aasta=int("20"+ik_list[1]+ik_list[2])
        if kuu in [1,3,5,7,8,10,12] and paev >0 and paev<32:
                print(ik_list[5],ik_list[6],"õige paev!")
        elif kuu in ([4,6,9,11] and paev>0 and paev<31) or (kuu==2 and paev>0 and paev<29):
         print(ik_list[5],ik_list[6],"õige paev!")
        elif aasta%4==0 and kuu==2 and paev<0 and paev<30:
            print(ik_list[5],ik_list[6])
    else:
        print(ik_list[3],ik_list[4],"ei ole õiged")
Summa=0
for i in range(1,11): 
    if i<10:
        Summa+=i*int(ik_list[i-1])
    else:
        Summa+=(i-9)*int(ik_list[i-1])
print("Summa: ",Summa)
jaak=Summa//11
if jaak==10:
    Summa=0
    for i in range(3,13):
        if i<9:
            Summa+=i*int(ik_list[i-1])
        else:
            Summa+=(i-9)*int(ik_list[i-1])
    jaak=Summa//11
jaak=Summa-jaak*11
print("kontroll number:",jaak)
if jaak==int(ik_list[10]):
    print("õige isik")
else:
    print("vale isik")


#011...019 = Tartu Ülikooli Naistekliinik, Tartumaa, Tartu
#021...220 = Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla
#221...270 = Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)
#271...370 = Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla
#371...420 = Narva Haigla
#421...470 = Pärnu Haigla
#471...490 = Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla
#491...520 = Järvamaa Haigla (Paide)
#521...570 = Rakvere, Tapa haigla
#571...600 = Valga Haigla
#601...650 = Viljandi Haigla
#651...700? = Lõuna-Eesti Haigla (Võru), Põlva Haigla 






