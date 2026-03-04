import math

a = float(input("Indtast A værdi: "))
b = float(input("Indtast B værdi: "))
c = float(input("Indtast C værdi: "))

X1 = (-b + math.sqrt(b*b - 4*a*c)) / 2*a
X2 = (-b - math.sqrt(b*b - 4*a*c)) / 2*a

print(X1)
print(X2)
