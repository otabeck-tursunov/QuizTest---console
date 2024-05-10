import random

oylangan_son = random.randint(1, 9)

son = int(input("1 va 10 oralig'ida son kiriting: "))
for i in range(3):  # (0, 1, 2)
    if son == oylangan_son:
        print("Siz o'ylangan sonni topdingiz!")
        break
    else:
        if i == 2:
            print("Urinishlar soni tugadi!")
            break
        son = int(input("Topolmadingiz, qayta kiriting: "))
