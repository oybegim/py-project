qiymat1 = input('''Salom. Siz python dasturiga qatnashmoqchimisiz, quyidagilardan birini tanlang: 
ha, bilmadim: ''')
if qiymat1 == "Ha":
    print("qatnashmoqchi ekansiz demak ma'lumotlarni to'ldiring")
    ism = input("ismingizni kiriting: ")
    familiya = input("familiyangizni kiriting: ")
    email = input("emailingizni kiriting: ")
    tel = input("telefon raqamingizni kiriting: ")
    qiymat2 = int(input('''Bizning darsimizda quyidagilar o'rgatiladi va quyidagilardan birini tanlang:
    1.Ma'lumotlar turi
    2.Shart operatorlari
    3.Takrorlanish operatorlari
    4.List
    5.Funksiyalar
    6.Exception
    7.OOP(class)
    8.Inheritance
    9.Tuple(Dictonaries)
    10.Time
    11.Threading'''))
    if qiymat2 == 1:
        qiymat3 = int(input('''Ma'lumotlar turi 4 xil bo'ladi:
        1.string
        2.integer
        3.float
        4.boolean  '''))
        if qiymat3 == 1:
            a = "Oybegim"
            b = "3108"
            print(a + b)
        elif qiymat3 == 2:
            birinchi = int(input("1-sonni kiriting"))
            ikkinchi = int(input("2-sonni kiriting"))
            print(birinchi-ikkinchi)
            print(birinchi+ikkinchi)
            print(birinchi/ikkinchi)
            print(birinchi*ikkinchi)
        elif qiymat3 == 3:
            birinchi2 = 123.532
            ikkinchi2 = 12.98
            print(birinchi2-ikkinchi2)
            print(birinchi2+ikkinchi2)
            print(birinchi2/ikkinchi2)
            print(birinchi2*ikkinchi2)
        elif qiymat3 == 4:
            birinchi3 = 35
            ikkinchi3 = 36.36
            print(birinchi3==ikkinchi3)
            print(birinchi3<ikkinchi3)
            print(birinchi3>ikkinchi3)
            print(birinchi3<=ikkinchi3)
            print(birinchi3>=ikkinchi3)

    elif qiymat2 == 2:
        ism2 = input("ismingizni kiriting: ")
        familiya2 = input("familiyangizni kiriting: ")
        login2 = input("login kiriting: ")
        parol2 = int(input("parol kiriting"))
        if ism2 == "Oybegim" and familiya2 == "Sultonova" and login2 == "loginso" and parol2 == 1234:
            print("siz dasturga kirdingiz")
        elif ism2 == "Oybegim" and familiya2 == "Sultonova" and login2 == "loginso" and parol2 != 1234:    
            print("parol xato")
        elif ism2 == "Oybegim" and familiya2 == "Sultonova" and login2 != "loginso" and parol2 == 1234:
            print("login xato")
        elif ism2 == "Oybegim" and familiya2 != "Sultonova" and login2 == "loginso" and parol2 == 1234:
            print("familiya xato")
        elif ism2 != "Oybegim" and familiya2 == "Sultonova" and login2 == "loginso" and parol2 == 1234: 
            print("ism xato")   
        if ism2 == "Oybegim" and familiya2 == "Sultonova" and login2 != "loginso" and parol2 != 1234:
            print("login va parol xato")
        elif ism2 == "Oybegim" and familiya2 != "Sultonova" and login2 != "loginso" and parol2 == 1234:
            print("familiya va login xato")
        if ism2 != "Oybegim" and familiya2 != "Sultonova" and login2 == "loginso" and parol2 == 1234:
            print("ism va familiya xato")
        else:
            print("siz dasturga kira olmadingiz")
    
    elif qiymat2 == 3:
        qiymat4= int(input('''takrorlanish operatorlari:
        1.while
        2.for'''))
        if qiymat4 == 1:
            f = 0
            while f < 10:
                f += 1
                print(f)
        elif qiymat4 == 2:
            for x in range(0, 10, 1):
                print(x)
    elif qiymat2 == 4:
        qiymat5 = [1, 2, "tekst", 2.4, [True, 4]]
        print(qiymat5[4][0])
    elif qiymat2 == 5:
        birinchi4 = int(input("1-sonni kiriting: "))
        ikkinchi4 = int(input("2-sonni kiriting: "))
        def sanash(birinchi4, ikkinchi4):
            while birinchi4 < ikkinchi4:
                birinchi4 += 1
                print(birinchi4)
        sanash(birinchi4, ikkinchi4)
    elif qiymat2 == 6:
        try:
            int("salom")
        except ValueError:
            print("xatolik")
    elif qiymat2 == 7:
        class Odam:
            def __init__(self, ismi, familiyasi, yoshi):
                self.ismi = ismi 
                self.familiyasi = familiyasi
                self.yoshi = yoshi
        o1 = Odam("Meronshoh", "Lazizbekov", "20 yoshda")
        print(o1.ismi, o1.familiyasi, o1.yoshi)
    elif qiymat2 == 8:
        class Phone:
            def __init__(self, nomi, xotirasi):
                self.nomi = nomi
                self.xotirasi = xotirasi
            def __str__(self):
                return f"{self.nomi} {self.xotira}"
        class Iphone(Phone):
            def __init__(self, nomi, xotirasi, rangi):
                super().__init__(nomi, xotirasi)
                self.rangi=rangi
            def phone1(self):
                print(self.nomi, self.xotirasi, self.rangi)
        p1 = Iphone("Iphone5S", "32GB", "oq")
        print(p1.phone1())
    elif qiymat2 == 9:
        lugat ={
            "Odam1": {
                "ismi": ["Dilshod"],
                "familiyasi": ["Azizbekov"],
                "yoshi": [20]},
            "Odam2": {
                "ismi1": ["Dilshoda"],
                "familiyasi1": ["Azizbekova"],
                "yoshi1": [18]}
        }
        print(lugat["Odam1"])
        print(lugat["Odam2"])
    elif qiymat2 == 10:
        print("4 sekund kuting")
        import time
        h = 0
        while h < 4:
            h += 1
            time.sleep(1)
            print(h)
    elif qiymat2 == 11:
        import threading
        import time

        def py1():
            for x in range(0, 2):
                time.sleep(0.2)
                print("salom")
        def py2():
            for x in range(0, 2):
                time.sleep(0.2)
                print("hello")
        t1 = threading.Thread(target=py1)
        t2 = threading.Thread(target=py2)

        t1.start()
        t2.start()
elif qiymat1 == "bilmadim":
    print("kuratorlarimizdan ma'lumot olishingiz mumkin")
