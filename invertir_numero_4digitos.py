# invertir un numero de 4 digitos

# input

A = int(input("se ingresa un numero de 4 digitos: "))

# processing

c4 = (A % 10) * 1000
pe = A//10
c3 = int((A % 100) / 10) * 100
pe = pe//10
c2 = int((A % 1000) / 100) * 10
c1 = pe // 10 

nj  = c4 + c3 + c2 + c1

# output

print("----------------------------------------")
print("----------------RESULTADO---------------")
print("----------------------------------------")
 
print(" NUMERO INNVERSO: " + str(nj))