from Temp.CtoFK import c_to_f,c_to_k
from Temp.FtoC import f_to_c
from Temp.KtoC import k_to_c


choice=int(input("""
1. Celsius to Fahrenheit and Kevlin
2. Fahrenheit to Celsius
3. Kelvin to Celsius
------------------------------------
Choose An Option:  """))

if choice==2:
    f=float(input("Enter temperature in Fahrenheit: "))
    print(f"{f}F = {f_to_c(f)} Celsius")

elif choice==3:
    k=float(input("Enter temperature in Kelvin: "))
    print(f"{k}K = {k_to_c(k)} Celsius")

elif choice==1:
    c=float(input("Enter temperature in Celsius: "))
    print(f"{c}C = {c_to_f(c)} Fahrenheit")
    print(f"{c}C = {c_to_k(c)} Kelvin")

else:
    print("Invalid Option")