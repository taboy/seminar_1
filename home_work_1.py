#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
a=int(input("write a number"))
if a >0 and a<6:
    print(f"{a} this day is weekday")
elif a==6 or a==7:
    print(f"{a} this day is weekend")
else:print("please write week days")
