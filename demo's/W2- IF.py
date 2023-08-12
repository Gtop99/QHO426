name = input("Enter your name: ")
# len()
# name = 'abcde'
# len(name) = 5

if len(name) > 7:
    print("Your name it's very long. Please provide a nickname: ")
    name = input()
elif len(name) <= 3:
    print("You have a very short name")
elif name == "Martha":
    print("Why did you say that name!!!")

else:
    print("You have a medium name")
print(f"Welcome {name}.")

