# savol1 = "Python dasturlash tildia uznlikni aniqlovchi funksiya: "
# savol2 = "Python dasturlash tildia listni tartiblovchi funksiya: "
# javob1 = input(savol1)
#
# count = 0
# if javob1.lower() == "len":
#     print("Siz to'g'ri javob berdingiz!")
#     count = count + 1
# else:
#     print("Afsuski javob noto'gri! To'g'ri javob: len")
#
# javob2 = input(savol2)
#
# if javob2.lower() == "sorted":
#     print("Siz to'g'ri javob berdingiz!")
#     count = count + 1
# else:
#     print("Afsuski javob noto'gri! To'g'ri javob: sorted")

# 1 -> Natijalar
# 2 -> Test yechish
# 0 -> Chiqish
import datetime

savollar = {}

with open('savollar.txt') as file:
    qatorlar = file.readlines()
    for qator in qatorlar:
        if qator == qatorlar[-1]:
            savollar.update({
                qator[:qator.index("////")]: qator[qator.index("////") + 4:]
            })
        else:
            savollar.update({
                qator[:qator.index("////")]: qator[qator.index("////") + 4:-1]
            })

natijalar = []

test = False
savol_qosh = False
while True:
    if test == False and savol_qosh == False:
        amal = int(input("Test yechish -> 1\n"
                         "Savol qo'shish -> 2\n"
                         "Natijalar -> 3\n"
                         "Chiqish -> 0\n\n"
                         "Bo'limni tanlang: "))
        print("-------------------------------------------------------------------")

    if amal == 1:
        test = False
        print(f"Python bo'yicha {len(savollar)} ta savol. \n")
        natija = 0
        jami = 0
        for savol, javob in savollar.items():
            jami += 1
            user_javob = input(str(jami) + "-savol.\n" + savol + ": ")
            if user_javob.lower() == javob:
                natija += 1
            print()
        print(f"--- [ Natija: {jami} ta savoldan {natija} ta topdingiz!] ---\n")
        natijalar.append(f"{natija}/{jami} - {natija / jami * 100:.2f}% [{datetime.datetime.now()}]")

        amal = int(input("Qayta yechish -> 1\n"
                         "Ortga -> 0\n\n"
                         "Bo'limni tanlang: "))
        if amal == 1:
            test = True
        print("-------------------------------------------------------------------")
    elif amal == 2:
        savol_qosh = False
        savol = input("Savolingizni kiriting: ")
        javob = input("To'g'ri javobni kiriting: ")

        savollar.update({savol: javob})
        with open("savollar.txt", 'w') as file:
            for savol, javob in savollar.items():
                file.write(savol + "////" + javob + "\n")


        print("\nSavolingiz ro'yxatga qo'shildi!\n")

        amal = int(input("Yana qo'shish -> 1\n"
                         "Ortga -> 0\n\n"
                         "Bo'limni tanlang: "))
        if amal == 1:
            amal = 2
            savol_qosh = True
        print("-------------------------------------------------------------------")


    elif amal == 3:
        print("Sizning so'nggi natijalaringiz:\n")
        for natija in natijalar:
            print(natija)
        print()
        input("Ortga -> Enter")
        print("-------------------------------------------------------------------")

    elif amal == 0:
        break
    else:
        print("Bunda bo'lim mavjud emas!")
