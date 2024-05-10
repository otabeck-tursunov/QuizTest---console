# Tic Tac Toe
template = """
 ____ ____ ____
|  1 |  2 |  3 |
 ____ ____ ____
|  4 |  5 |  6 |
 ____ ____ ____
|  7 |  8 |  9 |
 ---- ---- ----
"""
galabalar = ['123', '456', '789', '147', '258', '369', '159', '357']

indekslar = {
    "1": template.index("1"),
    "2": template.index("2"),
    "3": template.index("3"),
    "4": template.index("4"),
    "5": template.index("5"),
    "6": template.index("6"),
    "7": template.index("7"),
    "8": template.index("8"),
    "9": template.index("9"),
}
x_list = ''
o_list = ''

toxta = False
galaba = False
for i in range(1, 10):
    if i % 2 == 1:
        x = input(template + "\n(X) o'yinchi (1-9) oraqlig'ida joy tanlang: ")
        for j in range(3):
            if x not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print("Noto'g'ri kiritish!")
                x = input(template + "\n(X) o'yinchi (1-9) oraqlig'ida joy tanlang: ")
        if x not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Dastur to'xtadi!")
            toxta = True

        x_list += x
        template = template.replace(f" {x}", "❎")
        x_list = ''.join(sorted(x_list))
        for g in galabalar:
            count = 0
            for k in g:
                if g in x_list:
                    count += 1
            if count == 3:
                print("\n---------------------------------------------------\n(X) lar g'alaba qozondi🎉🎉🎉!\n" + template)
                galaba = True
                break
        if galaba:
            break

    if toxta:
        break
    if i % 2 == 0:
        o = input(template + "\n(O) o'yinchi (1-9) oraqlig'ida joy tanlang: ")
        for j in range(3):
            if o not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print("Noto'g'ri kiritish!")
                o = input(template + "\n(0) o'yinchi (1-9) oraqlig'ida joy tanlang: ")
        if o not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Dastur to'xtadi!")
            toxta = True
        o_list += o
        template = template.replace(f" {o}", "0️⃣")

        o_list = ''.join(sorted(o_list))
        for g in galabalar:
            count = 0
            for k in g:
                if g in o_list:
                    count += 1
            if count == 3:
                print("\n---------------------------------------------------\n(0) lar g'alaba qozondi🎉🎉🎉!\n" + template)
                galaba = True
                break
        if galaba:
            break
        if toxta:
            break
if toxta:
    print("\n-----------------------------------------\nO'yin qoidalari buzildi")
elif galaba == False:
    print("\n---------------------------------------------------\nDurrang!" + template)

# x = input(template + "\nX o'yinchi (1-9) oraqlig'ida joy tanlang: ")
