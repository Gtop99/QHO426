salary = float(input("Enter salary: "))
years = int(input("Enter number of years: "))


if years > 2:
    if salary < 25000:
        salary *= 1.1
    else:
        salary += 500
elif years == 1:
    salary += 200
else:
    if salary <= 18000:
        print("Ooosie! Your salary should be at least 18000.")
        salary = 18000
print(f"Your salary will now be {salary}.Keep up good work.")