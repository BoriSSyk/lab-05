import math
x = int(input("Введіть x: "))
if x >= 5.1:
    y = math.log2(3*x)-7*math.sqrt(x)
    print(y)
elif -0.7 < x < 5.1:
    y = math.exp(x)+2*math.pow(x, 3)
    print(y)
elif x <= -0.7:
    y = math.exp(x)+math.sin(x+math.pi/4)
    print(y)
