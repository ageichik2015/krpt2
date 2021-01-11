with open('vernam.txt') as f1:
    x = f1.read()
with open('key.txt') as f2:
    y = f2.read()

x = format(int(x), 'b')
y = format(int(y), 'b')

while (len(x)<len(y)):
    x = "0" + x

while (len(x)>len(y)):
    y = "0" + y

print("Иходный файл:", x)
print("Ключ:", y)

i = 0
z = ""
while (i<len(x)):
    if (x[i] == y[i]):
        z = z + "0"
        i = i + 1
    else:
        z = z + "1"
        i = i + 1

print("Результат:", z)

z = int(z, 2)

k = open('rezult.txt','w') 
k.write(str(z))
k.close()

