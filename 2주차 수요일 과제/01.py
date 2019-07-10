a=['apple', 'apps', 'ape']
b=[]
c=[]
d=[]
for i in range(len(a)):
    b.append(len(a[i]))

for j in range(min(b)):
    for y in range(len(a)):
        c.append(a[y][j])
    if len(list(set(c)))==1:
        d.append(c[0])
    del c[:]

print(''.join(d))