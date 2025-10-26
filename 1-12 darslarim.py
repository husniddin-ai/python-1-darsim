# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 17:52:21 2025

@author: hp_pc
"""

#b=5
#a=10.5
#type(a)
#print(type(b))
#x, b, c = 10, 15, -20
#print(x, b, c)
#a_tomon = 15
#b_tomon = 10
#s = a_tomon*b_tomon
#p = 2*a_tomon*b_tomon
#print("To\'g\'ri n\to\'g\'rtburchakning yuzi = " ,s,'n\To\'ri to\'rtburchakning perimetri = ', p)
#'To\'g\'ri to\'rtburchakning perimetri '
#'To\'g\'ri to\'rtburchakning yuzi '

#print(help(keywords))
#ism = 'Husniddin'
#yosh = 32
#print(ism)
#print(yosh)
#a = 8 # to'g'ri to'rtburchakning tomoni
#b = 9 # to'g'ri to'rtburchakning tomoni
#p = 2*(a + b) # uchburchakning perimetri
#s = 8*9 # uchburchakning yuzi
#print('Uchburchakning perimetri p =' , p, '\nUchburchakning yuzi s = ', s)

#ism_sharif = 'Ismoilov Husniddin'
#print('Mening ism sharifim' , ' ' + ism_sharif)
#ism = 'Husniddin'
#shahar = 'Qo\'qon'
#viloyat = "Farg\'ona"
#matn = "Men yangi 📱 oldim"
#print(matn)
#ism = 'Husniddin'
#familya = "Ismoilov"
#ism_sharif = f"{ism} {familya}"
#print(f"Assalom! Mening ismim {ism}. {ism_sharif}!")
#ism ='james'
#familya = "bond"#
#ism_sharif = f"{ism} {familya}"
#ism_sharif = ism_sharif.upper()
#print(ism_sharif)
#print(ism_sharif.lower())
#print(ism_sharif.title())
#print(ism_sharif.capitalize())
#meva = '     olma      '
#print("Men " + meva + "yaxshi ko\'raman")
#print("Men " + meva.lstrip() + " yaxshi ko\'raman")
#print("Men " + meva.rstrip() + " yaxshi ko\'raman")
#print("Men " + meva.strip() + " yaxshi ko\'raman")
#ism = input("Ismingiz kim?")
#print("Assalomu alaykum, " + ism)
#ism = input("Ismingiz kim? /n>>>")
#print("Assalomu alaykum, " + ism.title())

#Sonlar bilan ishlash 21.10.2025
#a = 20
#b = 5.5
#temp = 36.6
#print(type(a))
#print(type(b))
#aholi_soni = 7_556_425_351
#print("aholi soni:", aholi_soni)
#x, y, z = 10, 5.5, -56
#c = a*b
#d = 100/2
#d = 100//2

#radius = 20
#PI =3.14159
#diametr = 2*radius
#print("Aylananing uzunligi = ", PI*diametr)

#ism = "Jobir"
#yosh = 36
#xabar = ism + ' ' + str(yosh) + ' yoshda' 
#print(xabar)

#t_yil = int(input("To\'g\'lgan yilingizni kiriting: "))
#yosh = 2025 - t_yil
#print("Siz ", yosh, "yoshda ekansiz")

#a = int("10")
#b = float("20")
#temp = str("36.6")

#Lists Ro'yxatlar

#radius = "10"
#ism = "Mahmud"
#mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati  (matnlar)
#narhlar = [12000, 18000, 10900, 22000, 25000, 36000, -25, 63.2] # Narhlar ro'yxati (sonlar)
#hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
#sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralsh ro'yxat
#ismlar = [] # bo'sh ro'yxat
#bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
#mahsulot = bozorlik.pop(3)
#print("Men " + mahsulot + " sotib oldim")
#print("Olinmagan mahsulotlar", bozorlik)

# Ro'yxat bilan ishlash. O'zgarmas ro'yxatlar (Tuples)

#cars = ['bmw', 'mersedes benz', 'volvo','general motors', 'tesla', 'audi']
#narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
#arzon = min(narhlar)
#qimmat = max(narhlar)
#jami = sum(narhlar)
#print("Eng arzon narx: ", arzon, "\nEng qimmat narx: ", qimmat, "\nJami: ", jami) 
#toys =('bus', 'car', 'bear', 'dino', 'snake', 'lizard')

# for sikli bilan tanishuv

#mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
#for mehmon in mehmonlar:
    #print('Salom', mehmon)
    #print('Xayr', mehmon)
    #print(f"Hurmatli {mehmon}, sizni 20 - dekabr kuni nahorga oshga taklif qilamiz")
    #print("Hurmat bilan, Palonchiyevlar oilasi\n")
    
#sonlar = list(range(1,11))
#for son in sonlar:
   # print(f"{son} ning kvadrati {son**2} ga teng")
#sonlar = list(range(11)) # 1 dan 10 gacha sonlar ro'yxati
#sonlar_kvadrati = [] #bo'sh ro'yxat yaratamiz
#for son in sonlar: # sonlardagi har bir son uchun
#    sonlar_kvadrati.append(son**2)  # uning kvadratini hisoblab
#print(sonlar)
#print(sonlar_kvadrati)

#dostlar = [] # bo'sh ro'yxat
#print("Beshta eng yaqin dostingiz kim?")
#for n in range(5): # n bu yerda 1 dan 4 gacha qiymat oladi
    #dostlar.append(input(f"{n+1} - dostingizning ismini kiriting: "))
#print(dostlar)

#nurlar = []
#print('Eng kuchli nurlanishlar qaysi?')
#for nur in range(5):
#    nurlar.append(input(f"{nur+1} - nurlanish turini kiriting: "))
#print(nurlar)

#nurlar = ['alfa', 'beta', 'gamma', 'netron', 'emi']
#print("Eng kuchli nurlanishlar!!!")
#for nur in nurlar:
#    print("Nur: ", nur)

# if/else shartlari va tarmoqlanish

#avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
#for avto in avtolar:  # avtolar ichidagi har avto uchun
#   if avto == 'bmw': # agar avto bmw ga teng bolsa
#        print(avto.upper())    #avto nomini hamma harflarini katta harflarda yoz
#    else : #aks holda
#        print(avto.title()) # avto nomini faqat birinchi harfini katta harfda yoz

#ism = 'Ali'
#ism.lower() == 'ali'

#ism = input("Ismingiz kim?\n>>> ") # Foydalanuvchi ismini so'rang
#if ism.lower() != 'ali': # Agar ism ali ga teng bo'lmasa 
#    print(f"Uzr, {ism.title()} biz Alini kutyapmiz." ) #
#else: 
#    print('Salom Ali')
    
#javob = float(input("12*6 nechiga teng? \n>>>"))
#if javob != 72:
#    print('Javob xato!')
#else:
#   print("Javob to\'g\'ri ")

#yosh = int(input("Yoshingiz nechida? \n>>>"))
#if yosh >= 18: # Yosh 18 dan katta yoki teng bo'lsa
#    print("Xo\'sh kelibsiz!")
#else: #Aks holda
#    print("Kirish mumkin emas!")
    
#login = input("Yangi login tanlang:")
#if len(login) <= 5:  # Login uzunligini tekshiramiz
#   print("Login 5 harfdan ko\'proq bo\'lishi shart!")

#yil = int(input("To\'g\'lgan yilingizni kiriting: \n "))
#if 2025 - yil < 18: # Foydalanuvchining yoshini hisoblaymiz
#    print(f"yoshingiz {2025 - yil} da ekan")
#    print("Kirish mumkin emas!")
#else: #Aks holda
#    print("Xo\'sh kelibsiz")

#yosh = int(input("Yoshingiz nechida? \n>>>"))
#if yosh > 65: print(" Siz COVID 19 risk guruhida ekansiz ") 

#x, y = 60, 50 # x=25, y=50
#print("x>y") if x>y else print("x<y")

# if-elif-else

#son = -72
#if son < 0:
#    print("Manfiy son")
#else:
#    print("Musbat son")

#yosh = int(input("Yoshingiz nechida?"))
#if yosh <= 4:
#    print("Sizga kirish bepul")
#elif yosh <= 12:
#    print("Sizga kirish 5000 so\'m ")
#elif yosh <= 18:
#        print("Sizga kirish 8000 so\'m ")
#else:
#    print(" Sizga kirish 10000 so\'m ")

#yosh = int(input("Yoshingiz nechida? \n "))
#if yosh <= 4:
#    narh = 0
#elif yosh <= 12:
#    narh = 5000
#elif yosh <= 18:
#    narh = 8000
#else:
#    narh = 10000
#print(f"Sizga kirish {narh} so\'m ")

#kun = input("Bugun qanday kun? \n>>> ")
#if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#    print("Bugun dam olish kuni")
#else:
#    print("Bugun ish kuni")

#kun = input("Bugun qanday kun? \n>>> ")
#harorat = float(input("Havo harorati qanday? "))
#if kun.lower() == 'yakshanba' and harorat >= 30:
#    print("Cho\'milishga kettik!")
#elif kun.lower() == 'yakshanba' and harorat < 30:
#    print("Uyda dam olamiz!")

#kun = input("Bugun qanday kun? \n>>> ")
#harorat = float(input("Havo harorati qanday? "))
#if (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat >= 30:
#    print("Cho\'milishga kettik!")
#elif (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat < 30:
#    print("Uyda dam olamiz!")

#narh = 15000 # Mijoz 15000 so'mga taom oldi
#choy = True # Mijoz choy ham oldi
#salat = False #Mijoz salat olmadi
#if choy and salat: # Agar mijoz choy ham salat ham olgan bo'lsa
#    narh = narh + 10000 # narhga 10000 so'm qo'shamiz
#elif choy or salat:  # Agar mijoz choy yoki salat ham olgan bo'lsa
#    narh = narh +5000  # narhga 5000 so'm qo'shamiz
#print(f"Jami {narh} so\'m ")  # yakuniy narhni chiqaramiz

#narh = 15000 # Mijoz 15000 so'mga taom oldi
#choy = True # Mijoz choy ham oldi
#salat = True #Mijoz salat ham oldi
#if choy and salat: # Agar mijoz choy ham salat ham olgan bo'lsa
#    narh = narh + 10000 # narhga 10000 so'm qo'shamiz
#elif choy or salat:  # Agar mijoz choy yoki salat ham olgan bo'lsa
#    narh = narh +5000  # narhga 5000 so'm qo'shamiz
#print(f"Jami {narh} so\'m ")  # yakuniy narhni chiqaramiz

#narh = 15000 # Mijoz 15000 so'mga taom oldi
#choy = True # Mijoz choy ham oldi
#salat = False #Mijoz salat olmadi
#non = True
#kompot = True
#assorti = False
## Qo'yidagi har bir shart alohida tekshiriladi va bir biriga bog'liq emas
#if choy: # agar choy olgan bo'lsa
#    print("Mijoz choy oldi")
#    narh = narh + 3000
#if salat: # agar salat olgan bo'lsa
#    print("Mijoz salat oldi")
#    narh = narh + 5000
#if non: # agar non olgan bo'lsa
#     print("Mijoz non oldi")
#     narh = narh + 2000   
#if kompot: # agar kompot olgan bo'lsa
#    print("Mijoz kompot oldi")
#    narh = narh + 5000
#if assorti: # agar assorti olgan bo'lsa
#    print("Mijoz assorti oldi")
#    narh = narh + 15000
#print(f"Jami {narh} so'm ")

#narh = 15000 # Mijoz 15000 so'mga taom oldi
#choy = 1 # Mijoz choy ham oldi
#salat = 0 #Mijoz salat olmadi
#non = 1
#kompot = 1
#assorti = 1
# Qo'yidagi har bir shart alohida tekshiriladi va bir biriga bog'liq emas
#if choy: # agar choy olgan bo'lsa
#    print("Mijoz choy oldi")
#    narh = narh + 3000
#if salat: # agar salat olgan bo'lsa
#    print("Mijoz salat oldi")
#    narh = narh + 5000
#if non: # agar non olgan bo'lsa
#     print("Mijoz non oldi")
#     narh = narh + 2000   
#if kompot: # agar kompot olgan bo'lsa
#    print("Mijoz kompot oldi")
#    narh = narh + 5000
#if assorti: # agar assorti olgan bo'lsa
#    print("Mijoz assorti oldi")
#    narh = narh + 15000
#print(f"Jami {narh} so'm ")

# in
#menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# 'manti' in menu # menu da manti bormi

#menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
#ovqat = input("Nima ovqat yeysiz? \n>>>")
#if ovqat.lower() in menu:
#    print("Buyurtma qabul qilindi.")
#else:
#    print("Afsuski bizda bunday ovqat yo\'q ")

# not in
#menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
#ovqat = input("Nima ovqat yeysiz? \n>>>")
#if ovqat.lower() not in menu:
#    print("Afsuski bizda bunday ovqat yo\'q ")
#else:
#    print("Buyurtma qabul qilindi.")

#menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
#buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']
#ovqat = input("Nima ovqat yeysiz? \n>>>")
#for taom in buyurtmalar:
#    if taom in menu:
#         print(f"Menu da {taom} bor ")
#    else:
#         print(f"Kechirasiz, menuda {taom} yo'q.")
# 12 dars
# 1-Juft sonni topish 
#son = float(input("Juft son kiriting: \t"))
#if son%2 == 0:
#  print("Rahmat!")
#else:
#   print("Bu son juft emas.") 

# Yoshga qarab chipta narxini belgilash
#yosh = int(input("Yoshingiz nechida? \t"))
#if yosh <=4 or yosh >= 60:
#   narh = 0
#elif yosh < 18:
#    narh = 10000
#else:
#    narh = 20000
#print(f"Chipta {narh} so'm")

#  sonlarni taqqoslash
#x = float(input("Birinchi sonni kiriting: "))
#y = float(input("Ikkinchi sonni kiriting: "))
#if x==y:
#    print(f"{x}={y}")
#elif x<y:
#    print(f"{x}<{y}")
#else:
#    print(f"{x}>{y}")