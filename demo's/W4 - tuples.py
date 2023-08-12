# Declare a tuple
x = ("Valentin", 27 , True)
y = tuple(["Garry", 23, False])
# Print Tuples
print(x)
print(y)
print(x[2])
print(y[1])
# or
print(y[0:2])
# Cannot change individual items (imutability)
 # x[1] += 1
# Concatonate Tuples
z = x + y
print(z)
print(x)
print(y)

# Use min and max on tuples
t = (74, 35, 1, 83, 65, 62)
print(max(t))
print(min(t))

# Fixing errors on tuples
print(x)
l1 = list(x)
l1[2] = False
x = tuple(l1)
print(x)
