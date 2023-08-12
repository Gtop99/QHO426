def t_area(b=1,h=1):

    area = 0.5*h*b
    return area



total = t_area() + t_area(h=5) + t_area(10,18)
print(f"Total area of 3 traingles is {total}")

height = float(input("Enter height: "))
base = float(input("Enter base: "))
t_area(height, base)
