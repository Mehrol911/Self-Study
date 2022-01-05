#MEKHROL BAZAROV
while True:  
    print("\nMAIN MENU - MEKHROL BAZAROV - INHA")  
    print("1. Salom beradigan dastur")  
    print("2. 3 ta raqan yig'indisi")  
    print("3. Olmalar")
    print("4. Oldingi va keyingi raqam")
    print("5. 2 ta raqam kiritish, misol berish")
    print("---------------------------------------------")
    print("6. O'rtacha raqam qaytaradigan dastur")
    print("7. Yoshni kiritadigan dastur")
    print("8. Oy nomi va kunlar")
    print("9. Kabisa yili")
    print("10. O`xshash sonlar")
    Tanlov = int(input("Dasturni tanlang 1-10: "))  
    if Tanlov == 1:
        #Salom beradigan dastur
        ism = input("Ismingizni kiriting: ")
        print("Assalomu alaykum, " + ism + "!")
    elif Tanlov == 2:
        #3 ta raqam yig'indisi
        raqam1 = int(input("Birinchi sonni kiriting: "))
        raqam2 = int(input("Ikkinchi sonni kiriting: "))
        raqam3 = int(input("Uchinchi sonni kiriting: "))
        yigindi = raqam1 + raqam2 + raqam3
        print(f"Kiritilgan sonlar yig'indisi: {yigindi} ga teng")
    elif Tanlov == 3:
        #Olmalar
        import math
        oquvchilar_soni = 6
        olma_soni = 50
        har_bir_oquvchi = math.floor(olma_soni / oquvchilar_soni)
        qoldi = olma_soni % oquvchilar_soni
        print(f"O'quvchilar soni: {oquvchilar_soni} ta.")
        print(f"Olma soni: {olma_soni} ta." )
        print(f"Har bir o'quvchiga {har_bir_oquvchi} tadan olma tegadi.")
        print(f"Savatchada {qoldi} ta olma qoladi")
    elif Tanlov == 4:
        #Oldingi va keyingi raqam
        Raqam = int(input("Raqamni kiriting: "))
        print(f"{Raqam} raqami uchun bitta oldingi raqam {Raqam-1}")
        print(f"{Raqam} raqami uchun bitta keyingi raqam {Raqam+1}")
    elif Tanlov == 5:
        #2 ta raqam kiritish, misol berish
        raqam1 = int(input("Birinchi sonni kiriting: "))
        raqam2 = int(input("Ikkinchi sonni kiriting: "))

        qoshish = int(input(f"{raqam1} + {raqam2} = "))
        javob_user = (qoshish)
        print(f"Sizning javob: {javob_user}, To'g'ri javob: {raqam1+raqam2}")


        ayirish = int(input(f"{raqam1} - {raqam2} = "))
        javob_user = (ayirish)
        print(f"Sizning javob: {javob_user}, To'g'ri javob: {raqam1-raqam2}")

        kopaytirish = int(input(f"{raqam1} * {raqam2} = "))
        javob_user = (kopaytirish)
        print(f"Sizning javob: {javob_user}, To'g'ri javob: {raqam1*raqam2}")

        bolish = int(input(f"{raqam1} / {raqam2} = "))
        javob_user = (bolish)
        print(f"Sizning javob: {javob_user}, To'g'ri javob: {raqam1/raqam2}")
        
    elif Tanlov == 6:
        #O'rtacha raqam qaytaradigan dastur
        raqam1 = int(input("Birinchi sonni kiriting: "))
        raqam2 = int(input("Ikkinchi sonni kiriting: "))
        raqam3 = int(input("Uchinchi sonni kiriting: "))
        if raqam1>raqam2:
             if raqam1<raqam3:
              median = raqam1
             elif raqam2>raqam3:
                median = raqam2
             else:
                median = raqam3
        else:
            if raqam1>raqam3:
                median = raqam1
            elif raqam2<raqam3:
                median = raqam2
            else:
                median = raqam3
        print(f"O'rtacha raqam: {median}")
    elif Tanlov == 7:
        #Yoshni kiritadigan dastur
        yosh = int(input("Yoshingizni kiriting: "))
        if yosh > 0 and yosh <= 18:
            print("Siz o'qishingiz kerak.")
        elif yosh > 18 and yosh <= 50:
            print("Siz ishlashingiz kerak.")
        elif yosh > 50 and yosh <= 59:
            print("Siz tez orada nafaqaga chiqasiz.") 
        elif yosh > 59 and yosh <= 150:
            print("Siz pensionerga o'xshaysiz.")
        else:
            print("Nimadir noto'g'ri ketib qoldi.")
    elif Tanlov == 8:
        #Oy nomi va kunlar
            oy_nomi = {
            1:'Yanvar',
            2:'Fevral',
            3:'Mart',
            4:'Aprel',
            5:'May',
            6:'Iyun',
            7:'Iyul',
            8:'Avgust',
            9:'Sentabr',
            10:'Oktabr',
            11:'Noyabr',
            12:'Dekabr'}
            Kunlar_soni = {
            oy_nomi[1]: 31,
            oy_nomi[2]: 28 or 29,
            31:'Mart',
            30:'Aprel',
            31:'May',
            30:'Iyun',
            31:'Iyul',
            31:'Avgust',
            30:'Sentabr',
            31:'Oktabr',
            30:'Noyabr',
            31:'Dekabr'}

            n = int(input('Oyning raqamini kiriting: '))
            print("Oy nomi: " + oy_nomi[n])
            print("Kunlar Soni: " + f"{Kunlar_soni}")
    elif Tanlov == 9:
        # Kabisa yili
        yil = int(input("Yilni kiriting: "))
        if (yil % 400 == 0) and (yil % 100 == 0):
            print("{0} - yil kabisa yilidir.".format(yil))
        elif (yil % 4 ==0) and (yil % 100 != 0):
            print("{0} - yil kabisa yilidir.".format(yil))
        else:
            print("{0} - yil kabisa yili emas.".format(yil))
    elif Tanlov == 10:
        #O`xshash sonlar
        raqam1 = int(input("Birinchi sonni kiriting: "))
        raqam2 = int(input("Ikkinchi sonni kiriting: "))
        raqam3 = int(input("Uchinchi sonni kiriting: "))
        if raqam1 == raqam2 == raqam3:
            print("Kiritilgan raqamlar orasida bir xil raqamlar soni 3")         
        elif raqam1 != raqam2 and raqam2 != raqam3 and raqam1 !=raqam3:
                 print("Kiritilgan raqamlar orasida bir xil raqamlar yo'q ")      
        else: 
             print("Kiritilgan raqamlar orasida bir xil ra5qamlar soni 2")           
        break
    else:
        print("Xato tanlov!")