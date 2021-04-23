n = int (input ("Digite a quantidade de elementos a serem utilizados: "))
vet = [0]*n

i = 0
w = 0
while (i<n):
    vet[i] = (input ("Digite uma informação qualquer: ") )
    w = w + 1
    i = i + 1

print ("")
print("")

z = 0
print ("Quantidade de elementos inseridos: ",w)

while (z<i):
    print("",vet[z])
    z = z + 1
input()