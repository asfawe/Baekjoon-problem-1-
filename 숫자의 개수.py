a = int(input())
b = int(input())
c = int(input())

sum = a * b * c
sum1 = str(sum)
s = len(sum1)
l = list(sum1)
x = 0
y = 0
z = 0
yy = 0
xx = 0
zz = 0
o = 0
oo = 0
yo = 0
younjin = 0


for i in range(s):
    if l[i].count('0'):
        x += 1
    if l[i].count('1'):
        y += 1
    if l[i].count('2'):
        z += 1
    if l[i].count('3'):
        yy += 1
    if l[i].count('4'):
        xx += 1
    if l[i].count('5'):
        zz += 1
    if l[i].count('6'):
        o += 1
    if l[i].count('7'):
        oo += 1
    if l[i].count('8'):
        yo += 1
    if l[i].count('9'):
        younjin += 1

print(x)
print(y)
print(z)
print(yy)
print(xx)
print(zz)
print(o)
print(oo)
print(yo)
print(younjin)


