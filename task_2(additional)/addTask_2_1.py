a = 32
b = 27

c = a <= 100 and b <= 100
print(c)
d = a * b < a ** 2 and a * b > b ** 2
print(d)
i = a * b != a ** b and a == b + 23
print(i)
f = a == str(a) and b == str(b)
print(f)

g = len(str(a)) >= 2 or len(str(d)) < 2
print(g)
h = int(str(a)[::-1]) > a or int(str(b)[::-1]) > b
print(h)
e = int(str(a + b)) > 5000 or len(str(a + b)) == 5
print(e)
j = a - b > b - a == 2 or b - 12 > a
print(j)