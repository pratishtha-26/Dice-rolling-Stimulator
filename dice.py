
import random
x = "y"
while x=="y":
    num = random.randint(1,7)
    if num==1:
        print("-----------\n|         |\n|    O    |\n|         |\n-----------")
    elif num==2:
        print("-----------\n|         |\n|   O O   |\n|         |\n-----------")
    elif num==3:
        print("-----------\n|    O    |\n|    O    |\n|    O    |\n-----------")
    elif num==4:
        print("-----------\n|   O O   |\n|         |\n|   O O   |\n-----------")
    elif num==5:
        print("-----------\n|   O O   |\n|    O    |\n|   O O   |\n-----------")
    else:
        print("-----------\n|   O O   |\n|   O O   |\n|   O O   |\n-----------")
    x = input("Roll it again!! y? or n?")
