template = """
 --- --- ---
| 1 | 2 | 3 |
 --- --- --- 
| 4 | 5 | 6 |
 --- --- ---
| 7 | 8 | 9 |
 --- --- ---
"""
galabalar = ['123', '456', '789', '147', '258', '369', '159', '357']

x_joylar = ''
o_joylar = ''

qadam = 1
tugadi = False
while qadam != 10:
    if qadam % 2 == 1:
        x = input(template + "\n(X) o'yinchi (1-9) oraliqda son kiriting: ")
        while int(x) not in range(1, 10):
            print("Noto'g'ri joy tanlandi!")
            x = input(template + "\n(X) o'yinchi qaytadan (1-9) oraliqda son kiriting: ")
        while x in x_joylar + o_joylar:
            print("Joy allaqachon belgilangan!")
            x = input(template + "\n(X) o'yinchi qaytadan (1-9) oraliqda son kiriting: ")
        x_joylar += x
        template = template.replace(x, "X")
        for galaba in galabalar: # 123, 456
            count = 0
            for i in galaba:
                if i in x_joylar:
                    count += 1
            if count == 3:
                print("\n-------------------------\n(X) o'yinchi g'alaba qozondi🎉🎉🎉!\n" + template)
                tugadi = True
                break
    if tugadi:
        break

    if qadam % 2 == 0:
        o = input(template + "\n(0) o'yinchi (1-9) oraliqda son kiriting: ")
        while int(o) not in range(1, 10):
            print("Noto'g'ri joy tanlandi!")
            o = input(template + "\n(0) o'yinchi qaytadan (1-9) oraliqda son kiriting: ")
        while o in x_joylar + o_joylar:
            print("Joy allaqachon belgilangan!")
            o = input(template + "\n(0) o'yinchi qaytadan (1-9) oraliqda son kiriting: ")
        o_joylar += o
        template = template.replace(o, "0")
        for galaba in galabalar:  # 123, 456
            count = 0
            for i in galaba:
                if i in o_joylar:
                    count += 1
            if count == 3:
                print("\n-------------------------\n(0) o'yinchi g'alaba qozondi🎉🎉🎉!\n" + template)
                tugadi = True
                break
    if tugadi:
        break
    qadam += 1

if tugadi:
    pass
else:
    print("\n--------------------------\nDurrang natija qayd etild!")


# print(x_joylar)
# print(o_joylar)
