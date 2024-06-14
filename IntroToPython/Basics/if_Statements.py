# If statements don't need parentheses
# or curly braces

n = 1
if n > 2:
    n -= 1
elif n == 2:  # there's no else if as in C#
    n *= 2
else:
    n += 2

# Parentheses for multi-line conditions.
# and == &&
# or == ||
n, m = 1, 2
if ((n > 2 and
     n != m) or n == m):
    n += 1
