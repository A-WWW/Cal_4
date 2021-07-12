while True:
    try:
        Arg_1 = int(input("введите число 1 "))
    except ValueError:
        print("введите коректные данные")
        continue
    break
while True:
    try:
        Arg_2 = int(input("введите число 2 "))
    except ValueError:
        print("введите коректные данные")
        continue
    break
while True:
     Oper = input("введите оператор действия ")
     if Oper == "+":
          break
     elif Oper == "-":
          break
     elif Oper == "*":
          break
     elif Oper == "/":
          break
     print("введите коректный оператор")
     continue
try:
    if Oper == "+":
        print(Arg_1 + Arg_2)
    elif Oper == "-":
        print(Arg_1 + Arg_2)
    elif Oper == "*":
        print(Arg_1 * Arg_2)
    elif Oper == "/":
        print(Arg_1 / Arg_2)
except ZeroDivisionError:
    print("нет деления на 0")