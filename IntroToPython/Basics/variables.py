# variables: They are dynamically typed
n = 0
print('n = ', n)

n = "abc"
print('n = ', n)

# multiple assignments
n, m = 0, "def"
print('n = ', n, ", m = ", m)

# Increment
n = n + 1  # good
n += 1     # good
# n++      #bad

# None is null (absence of value)
n = 4
n = None
print("n =", n)