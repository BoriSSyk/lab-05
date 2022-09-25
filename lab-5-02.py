def pointss():
    a = float(input("Введіть сторону квадрата: ")) / 2
    cord = input("Введіть координати точки через пробіл: ").split(" ")
    cord = [abs(float(cord[0])), abs(float(cord[1]))]
    if cord[0] <= a and cord[1] <= a:
        print("Так, точка належить площині квадрата!")
    else:
        print("Ні, точка не належить площині квадрата!")


pointss()
