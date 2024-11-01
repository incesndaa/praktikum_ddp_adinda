jumlah = 0
output = ""

for i in range(1, 20, 2):  
    jumlah += i
    output += str(i)  
    if i < 19:  
        output += " + "

print(output + " = " + str(jumlah))
