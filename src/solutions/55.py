count=0

for i in range(1,10000):
    n=i
    iterations=0
    pot_palin=n+int(str(n)[::-1])
    while str(pot_palin)!=str(pot_palin)[::-1] and iterations<50:
        n+=int(str(n)[::-1])
        iterations+=1
        pot_palin=n+int(str(n)[::-1])

    if iterations==50:
        count+=1

print count
