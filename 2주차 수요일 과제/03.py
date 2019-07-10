a=[]
for i in range(9):
    a.append(input())
b=a[:]
sum=0

for j in range(9):
    b.pop(j)
    c=b[:]
    for y in range(8):
        c.pop(y)
        for z in range(7):
            sum = sum + int(c[z])
            if sum==100:
                c = list(map(int, c))
                print(sorted(c))
                print(sum)
                #print()
        sum=0
        c=b[:]
    b = a[:]
