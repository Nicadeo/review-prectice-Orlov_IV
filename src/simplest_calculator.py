#простейший калькулятор
a=float(input("Введите первое число: "))
b=float(input("Введите второе число: "))
result=(0) 
operation=input("Выберите операцию (+, -, *, /): ")
arr = ["+","-","/","*"] #что бы выдавало
if operation == "+":
    result = a+b
if operation == "-":
    result = a*b
if operation == "*":
    result = a*b
if operation == "/":
    result = a/b
if operation not in arr: #только для того что бы выдавало один вариант
    print("Неверная операция!")
if operation in arr: #иначе выдаёт два ответа сразу
    print("Результат:", result)
