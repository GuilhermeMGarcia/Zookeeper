balance = int (input ())

ano = 0
while balance >= 50000 and balance < 700000 :
        balance = (balance * 1.071)
        ano += 1
print(ano)
