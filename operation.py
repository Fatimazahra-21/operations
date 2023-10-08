A = float(input("entrer la valeur de A :"))
opérateur = float(input("entreropérateur :"))
B = float(input("entrer la valeur de B:"))
if opérateur == "+" :
print("A + B = ",A+B)
elif opérateur == "-" :
print("A - B = ",A-B)
elif opérateur == "*" :
print("A * B = ",A*B)
elif opérateur == "/" :
if B !=0 :
print("A / B = ",A/B)
else:
print("la division est impossible")
else:
print("opérateur est incorrect")






