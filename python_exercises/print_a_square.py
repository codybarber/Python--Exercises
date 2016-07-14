n = int(raw_input("Please enter a number: "))
builder = "*"
line = ''

for amount in range(0, n):
    line = line + builder

for x in range(0, n):
    print line


def square(n):
    for i in xrange(0, n):
        print '*' * n

n = int(raw_input("Enter a number: "))
square(n)
